import pymupdf
import base64
from pathlib import Path

def render_page_image_base64(pdf_path: str, page_number: int, zoom: float = 2.0) -> str:
    pdf_path = Path(pdf_path)
    doc = pymupdf.open(str(pdf_path))
    page = doc.load_page(page_number)
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    image_bytes = pix.tobytes("png")
    return base64.b64encode(image_bytes).decode("utf-8")