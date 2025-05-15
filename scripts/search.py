query = "Quels sont les droits des personnes selon le RGPD ?"
query_vector = model.encode(query)

results = qdrant.search(
    collection_name="rgpd_docs",
    query_vector=query_vector,
    limit=3
)

for result in results:
    print("Score:", result.score)
    print("Texte:", result.payload["text"])
    print("Source:", result.payload["source"])
    print("------")
