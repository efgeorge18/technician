
import base64
import streamlit as st
from app.backend.vector_store import FaissVectorStore
from app.backend.embedder import Embedder
from app.backend.retriever import Retriever
from app.backend.page_images import render_page_image_base64
from pathlib import Path



# Load once at startup
@st.cache_resource
def load_services():
    store = FaissVectorStore.load("app/data/bmw_e46")
    embedder = Embedder()
    retriever = Retriever(store, embedder)
    return retriever

retriever = load_services()

st.title("🔧 Technician Assistant")
st.markdown("Ask a question about the repair manual.")

# Chat input
user_query = st.text_input("What are you trying to fix or understand?", "")

if user_query:
    with st.spinner("Searching the manual..."):
        results = retriever.query(user_query)
        summary = retriever.summarize_answer(user_query, results)

    st.subheader("📋 Suggested Guidance")
    st.markdown(summary)

    st.subheader("📑 Source Passages")
    for res in results:
        st.markdown(f"**Page {res['page']} - {res['source']}**")
        st.markdown(res["text"])

        try:
            pdf_path = Path("app/pdfs") / res["source"]
            img_b64 = render_page_image_base64(str(pdf_path), res["page"])
            st.image(f"data:image/png;base64,{img_b64}", use_container_width=True)
        except Exception as e:
            st.warning(f"Image unavailable for page {res['page']} ({e})")

        st.markdown("---")