NeuroClinical RAG Assistant

Semantic retrieval over a curated knowledge base of neurological reference cases.

Enter a free-text clinical presentation; the system finds the most semantically similar reference case and surfaces the documented gold-standard action for it.

Educational prototype. Built to explore retrieval quality on clinical text. Not a clinical decision support tool, not validated, and not for use in patient care.

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/0e2f841f-d819-44b6-ab33-071b234002f8" />


---How it works---
free-text case
      ↓
Cohere embed-english-v3.0          (input_type="search_query")
      ↓
ChromaDB nearest-neighbour search  (cosine distance)
      ↓
distance threshold                 ← rejects weak matches
      ↓
reference case + documented gold-standard action

The returned action is retrieved, never generated. It comes verbatim from the matched reference case's metadata. In a clinical context this distinction matters: there is no model free-associating a treatment plan.
Two things worth knowing

Vector search always returns something. A nearest-neighbour query hands back the closest vector whether or not it is genuinely relevant — there is no built-in concept of "nothing here matches." The first working version of this app would confidently return a stroke thrombolysis protocol for input that had nothing to do with neurology. A system that cannot say I don't know is worse than no system at all when the subject is medicine.

SIMILARITY_THRESHOLD in app.py is the fix: matches beyond that cosine distance are rejected and reported as such. The value is a starting point and should be tuned against a real evaluation set rather than trusted as given.

Cohere v3 embeddings are asymmetric. Documents are indexed with input_type="search_document" and queries embedded with input_type="search_query". Using the same type for both measurably degrades retrieval — an easy detail to miss, with a real effect on results.


---Running locally----
pip install -r requirements.txt
export COHERE_API_KEY="your-key-here"
streamlit run app.py



---Reference cases----

The knowledge base holds fifteen curated neurological reference cases,
each with a presentation, findings, and a documented gold-standard action:

| Case | Condition |
|---|---|
| NEURO-001 | Acute ischaemic stroke, left MCA territory |
| NEURO-002 | Cerebral venous sinus thrombosis |
| NEURO-003 | Aneurysmal subarachnoid haemorrhage |
| NEURO-004 | Acute bacterial meningitis |
| NEURO-005 | Convulsive status epilepticus |
| NEURO-006 | Guillain-Barré syndrome |
| NEURO-007 | Myasthenic crisis |
| NEURO-008 | Giant cell arteritis |
| NEURO-009 | Metastatic spinal cord compression |
| NEURO-010 | Transient ischaemic attack |
| NEURO-011 | Wernicke encephalopathy |
| NEURO-012 | Intracerebral haemorrhage on anticoagulation |
| NEURO-013 | Optic neuritis |
| NEURO-014 | Idiopathic intracranial hypertension |
| NEURO-015 | Herpes simplex encephalitis |

Several were chosen because the correct action is counter-intuitive —
anticoagulating a patient who already has a haemorrhagic venous infarct,
giving thiamine before glucose, starting steroids before the biopsy.
Those are the cases where retrieval earns its keep.

