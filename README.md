# Squidle+ API Minimal Example

This repository provides a minimal working example of interfacing with the outdated **Squidle+ API** to retrieve image annotations using Python. It demonstrates querying a public dataset, handling pagination, and printing labelled data.

---

## 🔧 What It Does

- Connects to the Squidle+ API using an API key  
- Retrieves annotations for a chosen dataset  
- Handles paginated responses  
- Outputs raw label data

---

## 🚀 Quick Start

### 1. Install Requirements

```bash
pip install sqapi
```

### 2. Set Your API Key

Replace `"Your API Key Here"` with your personal Squidle+ token.

### 3. Choose Your Dataset

Download the dataset media file from the Squidle platform and update the annotation set ID in the notebook to match.

### 4. Run the Notebook

Open and execute `Squidle_API_Example.ipynb` in Jupyter or VS Code.

---

## ⚠️ Notes

- Only annotation download is demonstrated  
- Annotation set ID must be specified manually  
- Dataset selection and media downloads still require use of the Squidle+ website

---

## 🛠️ Future Work

There is significant work needed to bring this API integration up to modern, professional standards. I'm currently working on:

- Filtering across label schemes to download multiple sets of images and annotations
- Moving entirely to API-based workflows without relying on the website

If you have ideas, suggestions, or would like to collaborate, feel free to contact me at:  
📧 **[jean.terblans@gmail.com]**

---

## 📚 Resources

- [Squidle+ GitHub (Archived)](https://github.com/developmentseed/squidle)  
- [Squidle+ API Docs (if available)](https://squidle.org/api/docs/)  
- [Squidle_ML_Algorithm by leoguen](https://github.com/leoguen/Squidle_ML_Algorithm)
