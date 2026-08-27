import os
import chromadb
import cohere
import streamlit as st

COHERE_API_KEY = "Gy4O1VXLDp21bOpHPPXzfgyFY4BS7MR6BlyZU3ng"
co = cohere.Client(COHERE_API_KEY)

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(
    name="neurology_clinical_cases"
)

if collection.count() == 0:
  default_cases = [
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
              "A 45-year-old woman with a history of recurrent headaches"
              " presents with a 3-day history of progressive severe headache,"
              " confusion, and new-onset focal seizures. Magnetic resonance"
              " venography (MRV) demonstrates thrombosis of the superior sagittal"
              " sinus. She is currently stable without intracranial hemorrhage on"
              " CT."
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

  docs = [
      f"Patient Presentation: {c['presentation']}. Findings: {c['findings']}"
      for c in default_cases
  ]
  metas = [
      {"case_id": c["case_id"], "gold_standard_action": c["gold_standard_action"]}
      for c in default_cases
  ]
  ids = [c["case_id"] for c in default_cases]

  res = co.embed(
      texts=docs, model="embed-english-v3.0", input_type="search_document"
  )
  collection.add(
      documents=docs, embeddings=res.embeddings, metadatas=metas, ids=ids
  )

st.set_page_config(
    page_title="NeuroClinical RAG Assistant", page_icon="🧠", layout="wide"
)

st.title("🧠 NeuroClinical RAG Assistant")
st.markdown(
    "Artificial Intelligence System for Clinical Reasoning and Neurological"
    " Cases"
)

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
          model="embed-english-v3.0",
          input_type="search_query",
      )
      query_embedding = response.embeddings

      results = collection.query(query_embeddings=query_embedding, n_results=1)

      if (
          results
          and results.get("documents")
          and len(results["documents"]) > 0
          and len(results["documents"][0]) > 0
      ):
        matched_doc = results["documents"][0][0]
        metadata = results["metadatas"][0][0]

        st.success("Analysis completed successfully!")

        col1, col2 = st.columns(2)

        with col1:
          st.subheader("🔍 Most Similar Case in Database")
          st.info(f"**Case ID:** {metadata['case_id']}")
          st.write(matched_doc)

        with col2:
          st.subheader("💡 Gold Standard Action")
          st.success(metadata["gold_standard_action"])
      else:
        st.warning("No similar case found in the database.")