from pathlib import Path
from app.backend.pdf_loader import extract_chunks_from_pdf

def test_pdf_extraction():
    pdf_path = Path(__file__).resolve().parent.parent / "app" / "pdfs" / "BMW-3-Series-E46-1997-2006-Workshop-Manual.pdf"
    assert pdf_path.exists(), f"PDF not found at {pdf_path}"

    chunks = extract_chunks_from_pdf(str(pdf_path))
    assert len(chunks) > 0, "No chunks extracted from the PDF"