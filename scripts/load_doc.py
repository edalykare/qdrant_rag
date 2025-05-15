from pymongo import MongoClient

client = MongoClient("mongodb://admin:pass123@15.237.211.7:27017/")
db = client["ma_base"]
collection = db["documents"]

# Exemple de lecture
docs = []
for doc in collection.find():
    texte = doc.get("texte")  # ou "contenu", "body", etc.
    source = doc.get("source", "inconnu")
    if texte:
        docs.append({"text": texte, "source": source})
