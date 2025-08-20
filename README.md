# Squidle+ API Extended Example

This repository provides an updated working example of interfacing with the **Squidle+ API** to retrieve both image annotations and associated media. It demonstrates filtering by label schemes, downloading annotations in bulk, and saving both annotations and images locally.

---

## 🔧 What It Does

- Connects to the Squidle+ API using an API key  
- Filters annotation sets by a chosen **label scheme** (e.g., Catami 1.4 extended)  
- Retrieves all annotations from matching public and finalised sets, handling pagination  
- Saves annotations to a CSV file (including media ID, lineage, label, and point coordinates)  
- Fetches all associated media for each annotation set  
- Downloads media images and stores them in a local folder  

---

## 🚀 Quick Start

### 1. Install Requirements

```bash
pip install sqapi requests
```

### 2. Set Your API Key

Replace `"your_api_key_here"` with your personal Squidle+ token.

### 3. Choose Your Label Scheme

The script defaults to **Catami 1.4 (extended)** (ID: 54).  
You can change this by updating `label_scheme_id` and `label_scheme_name` in the script.

### 4. Run the Script

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
- Match annotaions to respective images using the shared image IDs

---

## 🛠️ Future Work

Potential improvements include:
- Code to match labels to their broader class in Catami 1.4 scheme
- Support for multiple label schemes in a single run  
- More robust error handling and logging  
- Option to download annotations and media selectively
