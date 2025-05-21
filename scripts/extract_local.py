# extract_text.py

import fitz  # PyMuPDF
import sys
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage : python extract_text.py <chemin_du_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not os.path.exists(pdf_path):
        print(f"❌ Fichier introuvable : {pdf_path}")
        sys.exit(1)

    print(f"📄 Lecture du fichier : {pdf_path}")
    text = extract_text_from_pdf(pdf_path)

    os.makedirs("data", exist_ok=True)
    output_path = "data/rgpd_text.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Texte extrait → {output_path}")
