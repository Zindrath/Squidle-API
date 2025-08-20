#!/usr/bin/env python3
"""
Map CATAMI 1.4 (extended) labels to broader classes using lineage.

Usage:
  python catami_broad_mapper.py \
      --input Annotations_From_API.csv \
      --output Annotations_With_Broad.csv \
      --levels 1
"""

import argparse
import csv
import json
from typing import List

def parse_args():
    p = argparse.ArgumentParser(
        description="Add a 'broad_class' column by moving up N levels from the lineage leaf."
    )
    p.add_argument("--input", "-i", required=True, help="Input CSV (e.g., Annotations_From_API.csv)")
    p.add_argument("--output", "-o", required=True, help="Output CSV to write with 'broad_class' column")
    p.add_argument("--levels", "-l", type=int, default=1,
                   help="How many levels to move up from the leaf (default: 1 = immediate parent)")
    return p.parse_args()

def parse_lineage(lineage_str) -> List[str]:
    """Parse lineage string into a list of levels (handles JSON and common delimiters)."""
    if not lineage_str:
        return []
    lineage_str = str(lineage_str).strip()

    # Try JSON list first
    try:
        parsed = json.loads(lineage_str)
        if isinstance(parsed, list):
            return [x.strip() for x in parsed if isinstance(x, str) and x.strip()]
    except Exception:
        pass

    # Try common delimiters
    for delim in ["|", ">", ",", ";", "/"]:
        if delim in lineage_str:
            parts = [p.strip() for p in lineage_str.split(delim)]
            return [p for p in parts if p]

    # Fallback: single token lineage
    return [lineage_str]

def get_broad_class(lineage: List[str], parent_levels: int) -> str:
    """Return lineage element moved up 'parent_levels' from the leaf, clamped to root."""
    if not lineage:
        return ""
    idx = max(0, len(lineage) - 1 - parent_levels)
    return lineage[idx]

def sniff_lineage_column(header: List[str]) -> str:
    """Find a reasonable lineage column name from the header."""
    lowered = [h.lower() for h in header]
    for cand in ["lineage", "lineage_names", "label_lineage", "lineagepath"]:
        if cand in lowered:
            return header[lowered.index(cand)]
    # Default to 'lineage' if nothing matches (will just produce empty)
    return "lineage"

def main():
    args = parse_args()

    with open(args.input, newline="", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        rows = list(reader)
        if not rows:
            # Still write an empty file with header if possible
            fieldnames = (reader.fieldnames or []) + (["broad_class"] if "broad_class" not in (reader.fieldnames or []) else [])
            with open(args.output, "w", newline="", encoding="utf-8") as f_out:
                csv.DictWriter(f_out, fieldnames=fieldnames).writeheader()
            print(f"Input appears empty. Wrote header-only CSV to {args.output}.")
            return

        lineage_col = sniff_lineage_column(reader.fieldnames)

    # Prepare output
    fieldnames = list(rows[0].keys())
    if "broad_class" not in fieldnames:
        fieldnames.append("broad_class")

    with open(args.output, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            lineage = parse_lineage(row.get(lineage_col, ""))
            row["broad_class"] = get_broad_class(lineage, parent_levels=max(0, args.levels))
            writer.writerow(row)

    print(f"✅ Done. Saved mapped CSV to {args.output} (levels up: {args.levels})")

if __name__ == "__main__":
    main()
