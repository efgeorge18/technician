import pymupdf
from pathlib import Path
from typing import List, Dict

def extract_chunks_from_pdf(pdf_path: str) -> List[Dict]:
    doc = pymupdf.open(pdf_path)
    chunks = []

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        text = page.get_text()
        if text.strip():
            # Break the page into smaller chunks by double line breaks
            for chunk in text.split("\n\n"):
                chunk = chunk.strip()
                if chunk:
                    chunks.append({
                        "text": chunk,
                        "page": page_number,
                        "source": Path(pdf_path).name
                    })

    return chunks