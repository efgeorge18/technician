import faiss
import json
import numpy as np
from typing import List, Dict
from pathlib import Path

class FaissVectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.metadata_store: List[Dict] = []

    def add(self, embeddings: List[List[float]], metadata: List[Dict]):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.metadata_store.extend(metadata)

    def search(self, query_embedding: List[float], k: int = 5) -> List[Dict]:
        query_vec = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vec, k)
        return [self.metadata_store[i] for i in indices[0] if i < len(self.metadata_store)]

    def save(self, base_path: str):
        base = Path(base_path)
        base.parent.mkdir(parents=True, exist_ok=True)

        faiss.write_index(self.index, str(base.with_suffix(".index.faiss")))

        with open(base.with_suffix(".metadata.json"), "w") as f:
            json.dump(self.metadata_store, f)

    @classmethod
    def load(cls, base_path: str):
        base = Path(base_path)
        index = faiss.read_index(str(base.with_suffix(".index.faiss")))

        with open(base.with_suffix(".metadata.json"), "r") as f:
            metadata = json.load(f)

        store = cls(index.d)
        store.index = index
        store.metadata_store = metadata
        return store

def get_vector_store(store_type: str = "faiss", dim: int = 384):
    if store_type == "faiss":
        return FaissVectorStore(dim)
    raise ValueError(f"Unknown vector store: {store_type}")