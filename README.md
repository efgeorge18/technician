# technician
upload repair manuals and ask it questions


# 🔧 Technician Assistant Chatbot

This project is a local prototype of an intelligent assistant that helps technicians troubleshoot and repair a car by querying PDF manuals. It uses open-source embeddings, a FAISS vector store, and a Streamlit-based chat UI.

---

## Quickstart

### 1. Install dependencies

```pip install -r requirements.txt```

---

### 2. 📄 Drop in Your Manual

Place a PDF (e.g., a repair manual) into the `app/pdfs/` directory.

Example:

`app/pdfs/MyRepairManual.pdf`

---

### 3. Build the Vector Store

Run the build script to:
- Extract and chunk text from the PDF
- Generate embeddings
- Store everything in `app/data/`

```bash
PYTHONPATH=. python scripts/build_index.py
```

---

### 4. Run the app

```sh run.sh```