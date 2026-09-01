import json
import os
import chromadb
import cohere
from dotenv import load_dotenv

# Ngarko çelësin e Cohere
load_dotenv()
COHERE_API_KEY = "BQAcTIZE2why75ZSNBKLaQQdrBnxPBhKNRzQeYzr"
co = cohere.Client(COHERE_API_KEY)

# 1. Krijo klientin persistent të ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(
    name="neurology_clinical_cases"
)

# 2. Lexo rastet klinike nga skedari JSON
json_path = "data/complex_cases.json"
if not os.path.exists(json_path):
  print(f"Gabim: Nuk u gjet skedari {json_path}!")
  exit()

with open(json_path, "r", encoding="utf-8") as f:
  cases = json.load(f)

# 3. Përgatit të dhënat për embedding
documents = []
metadatas = []
ids = []

for case in cases:
  case_id = case["case_id"]
  # Teksti që do të bëhet embedding (prezantimi klinik)
  clinical_text = f"Patient Presentation: {case['presentation']}. Findings: {case['findings']}"

  documents.append(clinical_text)
  metadatas.append(
      {
          "case_id": case_id,
          "gold_standard_action": case["gold_standard_action"],
      }
  )
  ids.append(case_id)

# 4. Gjenero embedding duke përdorur Cohere
print("Duke gjeneruar embeddings me Cohere...")
response = co.embed(
    texts=documents, model="embed-english-v3.0", input_type="search_document"
)
embeddings = response.embeddings

# 5. Shto rastet te ChromaDB
collection.add(
    documents=documents, embeddings=embeddings, metadatas=metadatas, ids=ids
)

print(
    f"U shtuan me sukses {len(cases)} raste klinike te ChromaDB në dosjen"
    " './chroma_db'!"
)