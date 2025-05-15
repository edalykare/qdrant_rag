from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

qdrant = QdrantClient(host="localhost", port=6333)

# Création de la collection
qdrant.recreate_collection(
    collection_name="rgpd_docs",
    vectors_config=VectorParams(
        size=embeddings[0].shape[0],
        distance=Distance.COSINE
    )
)

# Préparation des points
points = []
for i, chunk in enumerate(chunks):
    points.append(PointStruct(
        id=i,
        vector=embeddings[i],
        payload={
            "text": chunk["text"],
            "source": chunk["source"]
        }
    ))

qdrant.upsert(collection_name="rgpd_docs", points=points)
