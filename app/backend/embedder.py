from sentence_transformers import SentenceTransformer
from typing import List

class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        return self.model.encode(texts, convert_to_numpy=True).tolist()

    def embed_text(self, text: str) -> List[float]:
        return self.embed_texts([text])[0]
    

#optional for testing
if __name__ == "__main__":
    e = Embedder()
    vec = e.embed_text("How do I remove the cover?")
    print(f"Vector dims: {len(vec)}")
    print(vec[:5])  # preview