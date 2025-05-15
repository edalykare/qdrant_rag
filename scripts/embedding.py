from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  # rapide, efficace

texts = [chunk["text"] for chunk in chunks]
embeddings = model.encode(texts, show_progress_bar=True)
