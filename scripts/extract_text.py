# extract_text.py

import fitz  # PyMuPDF
from pymongo import MongoClient
import gridfs
import os
from io import BytesIO

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "rag_rgpd"
COLLECTION_NAME = "pdfs"

def extract_text_from_pdf_bytes(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def save_text_to_file(filename, text):
    os.makedirs("data", exist_ok=True)
    with open(f"data/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    # Connexion MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    fs = gridfs.GridFS(db)

    # Récupération de tous les fichiers PDF
    pdf_files = fs.find()
    for file in pdf_files:
        print(f"🗂️ Traitement du fichier : {file.filename}")
        pdf_bytes = file.read()
        text = extract_text_from_pdf_bytes(pdf_bytes)
        base_filename = os.path.splitext(file.filename)[0]
        save_text_to_file(base_filename, text)
        print(f"✅ Texte extrait → data/{base_filename}.txt")
