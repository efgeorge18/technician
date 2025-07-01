from app.backend.vector_store import get_vector_store
from app.backend.embedder import Embedder
from app.backend.pdf_loader import extract_chunks_from_pdf

chunks = extract_chunks_from_pdf("app/pdfs/BMW-3-Series-E46-1997-2006-Workshop-Manual.pdf")
texts = [chunk["text"] for chunk in chunks]
embedder = Embedder()
embeddings = embedder.embed_texts(texts)

store = get_vector_store(dim=len(embeddings[0]))
store.add(embeddings, chunks)

query = "how do I remove the fuse box cover"
query_embedding = embedder.embed_texts([query])[0]
results = store.search(query_embedding)

for r in results:
    print(f"[Page {r['page']}] {r['text'][:100]}...")