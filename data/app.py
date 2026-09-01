import os
import chromadb
import cohere
from dotenv import load_dotenv
import streamlit as st

# Ngarko konfigurimet
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
  st.error("Mungon COHERE_API_KEY te skedari .env!")
  st.stop()

co = cohere.Client(COHERE_API_KEY)
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="neurology_clinical_cases"
)

# Konfigurimi ifaqes në Streamlit
st.set_page_config(
    page_title="NeuroClinical RAG Assistant", page_icon="🧠", layout="wide"
)

st.title("🧠 NeuroClinical RAG Assistant")
st.markdown(
    "Sistem i Inteligjencës Artificiale për Arsyetim Klinik dhe Raste"
    " Neurologjike (Përdor Cohere Embeddings & ChromaDB)."
)

# Fusha e kërkimit për mjekun ose përdoruesin
query_text = st.text_area(
    "Shkruani ose ngjisni prezantimin e rastit klinik neurologjik:",
    placeholder=(
        "P.sh. A 64-year-old man presents with acute right-sided weakness..."
    ),
    height=120,
)

if st.button("Analizo Rastin Klinik", type="primary"):
  if not query_text.strip():
    st.warning("Ju lutem shkruani një rast klinik para se të bëni kërkimin.")
  else:
    with st.spinner("Duke kërkuar në bazën e njohurive mjekësore..."):
      # 1. Gjenero embedding për pyetjen e përdoruesit duke përdorur Cohere
      response = co.embed(
          texts=[query_text],
          model="embed-english-v3.0",
          input_type="search_query",
      )
      query_embedding = response.embeddings

      # 2. Bëj kërkimin semantik në ChromaDB
      results = collection.query(
          query_embeddings=query_embedding,
          n_results=1,  # Marrim rastin më të ngjashëm
      )

      if results["documents"] and len(results["documents"][0]) > 0:
        matched_doc = results["documents"][0][0]
        metadata = results["metadatas"][0][0]

        st.success("Analiza u krye me sukses!")

        col1, col2 = st.columns(2)

        with col1:
          st.subheader("🔍 Rasti më i Ngjashëm në Databazë")
          st.info(f"**Case ID:** {metadata['case_id']}")
          st.write(matched_doc)

        with col2:
          st.subheader("💡 Udhëzimi i Standardit të Artë (Gold Standard)")
          st.success(metadata["gold_standard_action"])
      else:
        st.warning(
            "Nuk u gjet asnjë rast i ngjashëm në bazën e të dhënave."
        )