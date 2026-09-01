
import os
 
import chromadb
import cohere
import streamlit as st
 

SIMILARITY_THRESHOLD = 0.5
EMBED_MODEL = "embed-english-v3.0"
 
 
@st.cache_resource
def get_cohere_client():
    """Return a Cohere client, or None if no API key is configured."""
    api_key = os.environ.get("COHERE_API_KEY")
    if not api_key:
        return None
    return cohere.Client(api_key)
 
 
@st.cache_resource
def get_collection(_co):
    """Return the Chroma collection, seeding it on first run."""
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(
        name="neurology_clinical_cases",
        metadata={"hnsw:space": "cosine"},
    )
 
    if collection.count() == 0:
        docs = [
            f"Patient Presentation: {c['presentation']} Findings: {c['findings']}"
            for c in REFERENCE_CASES
        ]
        metas = [
            {
                "case_id": c["case_id"],
                "gold_standard_action": c["gold_standard_action"],
            }
            for c in REFERENCE_CASES
        ]
        ids = [c["case_id"] for c in REFERENCE_CASES]
 
        # Documents and queries use different input_type values. Cohere's v3
        # embeddings are asymmetric: indexing with "search_document" and
        # querying with "search_query" produces meaningfully better retrieval
        # than using the same type for both.
        res = _co.embed(
            texts=docs, model=EMBED_MODEL, input_type="search_document"
        )
        collection.add(
            documents=docs, embeddings=res.embeddings, metadatas=metas, ids=ids
        )
 
    return collection
 
 

 
REFERENCE_CASES = [
    {
        "case_id": "NEURO-001",
        "presentation": (
            "A 64-year-old right-handed man presents with acute onset of"
            " right-sided weakness, expressive aphasia, and a right visual field"
            " defect starting 90 minutes prior to arrival. National Institutes of"
            " Health Stroke Scale (NIHSS) score is 14. Blood pressure is 165/95"
            " mmHg. Non-contrast head CT shows no acute hemorrhage."
        ),
        "findings": "Acute ischemic stroke involving the left MCA territory.",
        "gold_standard_action": (
            "Administer IV alteplase (tPA) immediately if within the 4.5-hour"
            " window, evaluate for mechanical thrombectomy via CTA/CTP, and"
            " monitor blood pressure strictly below 185/110 mmHg."
        ),
    },
    {
        "case_id": "NEURO-002",
        "presentation": (
            "A 45-year-old woman with a history of recurrent headaches presents"
            " with a 3-day history of progressive severe headache, confusion, and"
            " new-onset focal seizures. Magnetic resonance venography (MRV)"
            " demonstrates thrombosis of the superior sagittal sinus. She is"
            " currently stable without intracranial hemorrhage on CT."
        ),
        "findings": (
            "Superior sagittal sinus thrombosis with secondary venous"
            " infarction/seizures."
        ),
        "gold_standard_action": (
            "Initiate prompt anticoagulation with low-molecular-weight heparin"
            " (LMWH) or unfractionated heparin (UFH) regardless of minor"
            " hemorrhagic venous infarction, manage seizures with anti-seizure"
            " medications, and monitor intracranial pressure."
        ),
    },
]
 
 

 
st.set_page_config(
    page_title="NeuroClinical RAG Assistant", page_icon="🧠", layout="wide"
)
 
st.title("🧠 NeuroClinical RAG Assistant")
st.markdown(
    "Semantic retrieval over a curated knowledge base of neurological reference"
    " cases."
)
st.caption(
    "Educational prototype built to explore retrieval quality on clinical text."
    " Not a clinical decision support tool and not for use in patient care."
)
 
co = get_cohere_client()
 
if co is None:
    st.error(
        "No Cohere API key found. Set the COHERE_API_KEY environment variable"
        " and restart the app."
    )
    st.stop()
 
collection = get_collection(co)
 
query_text = st.text_area(
    "Enter or paste the neurological clinical case presentation:",
    placeholder=(
        "E.g., A 64-year-old man presents with acute right-sided weakness..."
    ),
    height=120,
)
 
if st.button("Analyze Clinical Case", type="primary"):
    if not query_text.strip():
        st.warning("Please enter a clinical case before performing the search.")
    else:
        with st.spinner("Searching the medical knowledge base..."):
            response = co.embed(
                texts=[query_text],
                model=EMBED_MODEL,
                input_type="search_query",
            )
            results = collection.query(
                query_embeddings=response.embeddings, n_results=1
            )
 
        documents = (results.get("documents") or [[]])[0]
 
        if not documents:
            st.warning("The knowledge base is empty.")
        else:
            distance = results["distances"][0][0]
 
            # Nearest-neighbour search always returns something. Without this
            # check the app confidently shows a stroke protocol for any input,
            # including text that has nothing to do with neurology.
            if distance > SIMILARITY_THRESHOLD:
                st.warning(
                    "No sufficiently similar case found in the knowledge base."
                    f" (closest distance: {distance:.3f})"
                )
                st.caption(
                    "The knowledge base currently holds"
                    f" {collection.count()} reference cases, so most"
                    " presentations will fall outside it."
                )
            else:
                metadata = results["metadatas"][0][0]
                st.success(
                    f"Closest match found (distance: {distance:.3f})"
                )
 
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("🔍 Most Similar Case in Database")
                    st.info(f"**Case ID:** {metadata['case_id']}")
                    st.write(documents[0])
                with col2:
                    st.subheader("💡 Documented Gold Standard Action")
                    st.success(metadata["gold_standard_action"])
                    st.caption(
                        "Retrieved from the reference case above — not generated,"
                        " and not a recommendation for any real patient."
                    )
 