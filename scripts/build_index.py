from app.backend.embedder import Embedder
from app.backend.pdf_loader import extract_chunks_from_pdf
from app.backend.vector_store import get_vector_store

pdf_path = "app/pdfs/BMW-3-Series-E46-1997-2006-Workshop-Manual.pdf"
chunks = extract_chunks_from_pdf(pdf_path)
texts = [c["text"] for c in chunks]

embedder = Embedder()
embeddings = embedder.embed_texts(texts)

store = get_vector_store(dim=len(embeddings[0]))
store.add(embeddings, chunks)
store.save("app/data/bmw_e46")

print("✅ Index built and saved to app/data/")