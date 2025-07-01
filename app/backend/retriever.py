from typing import List, Dict
from app.backend.vector_store import FaissVectorStore
from app.backend.embedder import Embedder

class Retriever:
    def __init__(self, store: FaissVectorStore, embedder: Embedder):
        self.store = store
        self.embedder = embedder

    def query(self, question: str, k: int = 5) -> List[Dict]:
        query_embedding = self.embedder.embed_text(question)
        results = self.store.search(query_embedding, k)

        formatted = [
            {
                "page": r.get("page"),
                "source": r.get("source"),
                "text": r.get("text").strip()
            }
            for r in results
        ]

        return formatted

    def summarize_answer(self, question: str, contexts: List[Dict]) -> str:
        # Start with a simple heuristic approach (you can later add an LLM call here)
        context_snippets = "\n\n".join(f"[Page {c['page']}] {c['text']}" for c in contexts)
        response = f"Based on the manual, here's what I found:\n\n{context_snippets}"
        return response