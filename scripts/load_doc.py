from pymongo import MongoClient

client = MongoClient("$$$$")
db = client["ma_base"]
collection = db["documents"]

# Exemple de lecture
docs = []
for doc in collection.find():
    texte = doc.get("texte")  # ou "contenu", "body", etc.
    source = doc.get("source", "inconnu")
    if texte:
        docs.append({"text": texte, "source": source})
