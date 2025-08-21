# Squidle+ API Extended Example

This repository provides an updated working example of interfacing with the **Squidle+ API** to retrieve both image annotations and associated media. It demonstrates filtering by label schemes, downloading annotations in bulk, and saving both annotations and images locally.

---

## 🔧 What It Does

- Connects to the Squidle+ API using an API key  
- Filters annotation sets by a chosen **label scheme** (e.g., CATAMI 1.4 extended)  
- Retrieves all annotations from matching public and finalised sets, handling pagination  
- Saves annotations to a CSV file (including media ID, lineage, label, and point coordinates)  
- Fetches all associated media for each annotation set  
- Downloads media images and stores them in a local folder

---

## 🚀 Quick Start

### 1) Install Requirements

```bash
pip install sqapi requests
```

### 2) Set Your API Key

Replace `your_api_key_here` in the script with your personal Squidle+ token.

### 3) Choose Your Label Scheme

The script defaults to **CATAMI 1.4 (extended)** (ID: 54).  
You can change this by updating `label_scheme_id` and `label_scheme_name` in the script.

### 4) Run the Script

```bash
python Squidle_API_Extended.py
```

- Annotations will be saved to `Annotations_From_API.csv`  
- Media files will be downloaded into the `Images/` directory

---

## ⚠️ Notes

- Only public and finalised annotation sets are retrieved  
- Label scheme ID must be set manually in the script  
- API calls are paginated and handled automatically  
- Image downloads require an active internet connection

---

## 🛠️ Optional: Map to Higher-Order CATAMI Labels

For users who want to group fine-grained CATAMI 1.4 (extended) labels into broader classes, an **optional** helper script is included: `Map_Catami_Labels.py`.  
It reads your exported annotations CSV and adds a `broad_class` column by moving up _N_ levels in the lineage from the leaf.

### Install

No extra install required beyond Python’s standard library (`argparse`, `csv`, `json`).

### Usage

**Terminal:**
```bash
python Map_Catami_Labels.py --input Annotations_From_API.csv --output Annotations_With_Broad.csv --levels 1
```

### What `--levels` Means

- `--levels 1` → immediate parent of the leaf label  
- `--levels 2` → two levels up from the leaf, etc.  
- If you request more levels than exist, it clamps to the root (e.g., **Biota**).

**Example**

Lineage: `Biota > Biotic substrate > Seagrasses > Posidonia`  
- Leaf label: `Posidonia`  
- `--levels 1` → `Seagrasses`  
- `--levels 2` → `Biotic substrate`  
- `--levels 10` → `Biota` (clamped)

---

## 📧 Contact

If you have ideas, suggestions, or would like to collaborate, feel free to reach out:  
**jean.terblans@gmail.com**
