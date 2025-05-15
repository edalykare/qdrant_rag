from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

chunks = []
for doc in docs:
    parts = splitter.split_text(doc["text"])
    for part in parts:
        chunks.append({
            "text": part,
            "source": doc["source"]
        })
