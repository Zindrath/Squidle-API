# --- Setup ---
from sqapi.api import SQAPI
import requests
import csv

# Variables
host = "https://squidle.org"
api_key = "your_api_key_here"  # Get this from your Squidle+ account

# Connect to Squidle+
api = SQAPI(host=host, api_key=api_key, verbosity=1)

# Filter by label scheme ID
label_scheme_id = 54 # Catami 1.4 extended label scheme ID
label_scheme_name = "Catami 1.4 (extended)" # Catami 1.4 extended label scheme name

# Filter for public annotation sets with label_scheme_id = 54 that are complete
annotation_set_response = api.get("/api/annotation_set") \
              .filter("is_public", "eq", True) \
              .filter("label_scheme_id", "eq", label_scheme_id) \
              .filter("is_final", "eq", True) \
              .execute().json()

# Get the data from the response
annotation_set_data = annotation_set_response.get("objects", [])

# Print the number of annotation sets found
print(f"Found {len(annotation_set_data)} annotation sets that match the filters.")

# Get the anntotations for each annotation set
page_size = 100
all_annotations = []

for aset in annotation_set_data:
    aset_id = aset["id"]
    aset_name = aset['name']
    print(f"→ Fetching annotations for set {aset_id} {aset_name}…")

    page = 1
    
    while True:
        try:
            # Fetch annotations for a specific set and page
            annotation_response = api.get(f"/api/annotation?page={page}&page_size={page_size}").filter("annotation_set_id", "eq", aset_id).execute().json() 
            data = annotation_response.get('objects', [])
            #print(json.dumps(all_annotations, indent=4))

            if page >= annotation_response.get('total_pages', 1):
                break
            #print(annotation_response.get('total_pages', 1))

            all_annotations.extend(data)
            page += 1  # Move to the next page

            #print(page)
        except Exception as e:
            print(f"Failed to fetch annotations: {e}")
            break
        
        
# Write annotations to CSV
csv_file_path = 'Annotations_From_API.csv'
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["id","lineage","label", "point_x", "point_y"])

    # Write each annotation's data
    for annotation in all_annotations:
        writer.writerow([
            annotation.get('point', {}).get('media_id', 'N/A'),
            annotation.get('label', {}).get('lineage_names', 'N/A'),
            annotation.get('label', {}).get('name', 'N/A'),
            annotation.get('point', {}).get('x', 'N/A'),
            annotation.get('point', {}).get('y', 'N/A'),
        ])

print("All pages fetched and saved to CSV.")

# Get all media for all annotation sets
page_size = 100
all_media = []

for aset in annotation_set_data:
    aset_id = aset["id"]
    aset_name = aset['name']
    print(f"→ Fetching media for set {aset_id} {aset_name}…")

    # Loop through pages to get all media items
    page = 1

    # put it in a loop to get all media items
    while True:
            try:
                # Fetch annotations for a specific set and page
                media_query = api.get(f"/api/annotation_set/{aset_id}/media?page={page}&page_size={page_size}").execute().json() 
                media_data = media_query.get('objects', [])

                if page >= media_query.get('total_pages', 1):
                    break

                all_media.extend(media_data)
                page += 1  # Move to the next page

                #print(page)
            except Exception as e:
                print(f"Failed to fetch media: {e}")
                break

    # Count the media items
    print(f"Found {len(all_media)} media items.")
    
# Save media to folder
media_folder = "Images"

for media in all_media:
    media_id = media.get('id', 'N/A')
    media_path = media.get('path_best', 'N/A')

    if media_path != 'N/A':
        # Download and save the media file
        response = requests.get(media_path)
        if response.status_code == 200:
            with open(f"{media_folder}/{media_id}.jpg", "wb") as img_file:
                img_file.write(response.content)
        else:
            print(f"Failed to download {media_path}")