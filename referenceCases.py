
REFERENCE_CASES = [
    {
        "case_id": "NEURO-001",
        "presentation": (
            "A 64-year-old right-handed man presents with acute onset of"
            " right-sided weakness, expressive aphasia, and a right visual"
            " field defect starting 90 minutes prior to arrival. NIHSS is 14."
            " Blood pressure is 165/95 mmHg. Non-contrast head CT shows no"
            " acute haemorrhage."
        ),
        "findings": "Acute ischaemic stroke in the left middle cerebral artery territory.",
        "gold_standard_action": (
            "Administer IV alteplase (tPA) if within the 4.5-hour window and no"
            " contraindications, evaluate for mechanical thrombectomy with"
            " CTA/CT perfusion, and keep blood pressure below 185/110 mmHg"
            " before and during thrombolysis."
        ),
    },
    {
        "case_id": "NEURO-002",
        "presentation": (
            "A 45-year-old woman with a history of recurrent headaches presents"
            " with three days of progressive severe headache, confusion, and"
            " new-onset focal seizures. MR venography demonstrates thrombosis of"
            " the superior sagittal sinus. CT shows a small haemorrhagic venous"
            " infarct."
        ),
        "findings": "Cerebral venous sinus thrombosis with secondary haemorrhagic venous infarction and seizures.",
        "gold_standard_action": (
            "Start anticoagulation with low-molecular-weight heparin despite the"
            " haemorrhagic infarct — the haemorrhage is a consequence of the"
            " thrombosis, not a contraindication. Treat seizures with"
            " anti-seizure medication and monitor intracranial pressure."
        ),
    },
    {
        "case_id": "NEURO-003",
        "presentation": (
            "A 52-year-old woman describes a sudden, severe headache that"
            " reached maximum intensity within seconds while she was lifting a"
            " box, six hours ago. She vomited twice. Neck stiffness is present."
            " She is alert with no focal deficit."
        ),
        "findings": "Suspected aneurysmal subarachnoid haemorrhage; thunderclap headache with meningism.",
        "gold_standard_action": (
            "Obtain an urgent non-contrast head CT — sensitivity approaches 100%"
            " within the first six hours. If the CT is negative and suspicion"
            " remains, perform a lumbar puncture looking for xanthochromia."
            " Once confirmed, start nimodipine, control blood pressure, and"
            " refer urgently to neurosurgery for aneurysm securing."
        ),
    },
    {
        "case_id": "NEURO-004",
        "presentation": (
            "A 23-year-old student is brought in with fever of 39.4°C, severe"
            " headache, photophobia, and neck stiffness that began this morning."
            " He is drowsy and disoriented. A non-blanching petechial rash is"
            " visible on the trunk."
        ),
        "findings": "Acute bacterial meningitis, likely meningococcal given the petechial rash.",
        "gold_standard_action": (
            "Give empirical IV antibiotics immediately — do not delay for CT or"
            " lumbar puncture. Ceftriaxone plus vancomycin, with ampicillin"
            " added if over 50 or immunocompromised to cover Listeria."
            " Dexamethasone should be given with or just before the first"
            " antibiotic dose. Take blood cultures, then perform LP once safe."
        ),
    },
    {
        "case_id": "NEURO-005",
        "presentation": (
            "A 34-year-old man with known epilepsy has been convulsing"
            " continuously for eight minutes. He has not regained consciousness"
            " between events. Oxygen saturation is 89%."
        ),
        "findings": "Convulsive status epilepticus.",
        "gold_standard_action": (
            "Secure the airway and give oxygen. Administer a benzodiazepine"
            " first line — IV lorazepam, or IM midazolam if no access. If"
            " seizures persist after two doses, move to a second-line agent:"
            " IV levetiracetam, valproate, or fosphenytoin. Check glucose,"
            " electrolytes and toxicology, and prepare for intubation and"
            " anaesthetic infusion if refractory."
        ),
    },
    {
        "case_id": "NEURO-006",
        "presentation": (
            "A 41-year-old man reports symmetric weakness that began in both"
            " feet five days ago and has ascended to the thighs. Deep tendon"
            " reflexes are absent throughout. He had a diarrhoeal illness three"
            " weeks ago. Forced vital capacity is falling on serial testing."
        ),
        "findings": "Guillain-Barré syndrome — acute inflammatory demyelinating polyradiculoneuropathy.",
        "gold_standard_action": (
            "Admit and monitor forced vital capacity and bulbar function"
            " closely; respiratory failure is the main cause of death. Treat"
            " with IV immunoglobulin or plasma exchange — the two are"
            " equivalent. Corticosteroids are not effective in GBS and should"
            " not be given. Provide VTE prophylaxis and autonomic monitoring."
        ),
    },
    {
        "case_id": "NEURO-007",
        "presentation": (
            "A 58-year-old woman with myasthenia gravis presents with"
            " worsening dyspnoea, weak cough, and difficulty swallowing over"
            " two days following a respiratory infection. She cannot count"
            " past 12 in a single breath."
        ),
        "findings": "Myasthenic crisis with impending respiratory failure.",
        "gold_standard_action": (
            "Prioritise the airway — assess with serial vital capacity and"
            " negative inspiratory force rather than oxygen saturation, which"
            " falls late. Treat with IV immunoglobulin or plasma exchange, and"
            " start or increase corticosteroids with awareness of transient"
            " worsening. Identify and treat the precipitant, and avoid drugs"
            " that impair neuromuscular transmission such as aminoglycosides,"
            " fluoroquinolones and magnesium."
        ),
    },
    {
        "case_id": "NEURO-008",
        "presentation": (
            "A 74-year-old woman describes a new right-sided temporal headache"
            " for three weeks, pain in the jaw when chewing, and scalp"
            " tenderness when brushing her hair. This morning she had ten"
            " minutes of blurred vision in the right eye. ESR is 88 mm/h."
        ),
        "findings": "Giant cell (temporal) arteritis with impending visual loss.",
        "gold_standard_action": (
            "Start high-dose corticosteroids immediately — do not wait for the"
            " temporal artery biopsy. Visual loss in giant cell arteritis is"
            " sudden and irreversible, and steroid treatment does not"
            " meaningfully alter biopsy findings within the first one to two"
            " weeks. Arrange biopsy or vascular ultrasound promptly and refer"
            " to ophthalmology and rheumatology."
        ),
    },
    {
        "case_id": "NEURO-009",
        "presentation": (
            "A 67-year-old man with known prostate cancer reports mid-thoracic"
            " back pain for two weeks, worse at night and when lying flat. Over"
            " the past 24 hours he has developed leg weakness, a sensory level"
            " at the umbilicus, and difficulty passing urine."
        ),
        "findings": "Metastatic spinal cord compression at the thoracic level.",
        "gold_standard_action": (
            "Give high-dose dexamethasone immediately and arrange urgent MRI of"
            " the whole spine, not only the symptomatic level, since deposits"
            " are often multiple. Refer the same day to oncology and spinal"
            " surgery for decompression or radiotherapy. Neurological outcome"
            " depends almost entirely on function at the time of treatment."
        ),
    },
    {
        "case_id": "NEURO-010",
        "presentation": (
            "A 69-year-old hypertensive man had 25 minutes of right arm"
            " weakness and slurred speech that resolved completely two hours"
            " ago. Neurological examination is now normal. He is in sinus"
            " rhythm."
        ),
        "findings": "Transient ischaemic attack — high early risk of completed stroke.",
        "gold_standard_action": (
            "Treat as an emergency, not a resolved event; the risk of stroke is"
            " highest in the first 48 hours. Arrange urgent brain and carotid"
            " imaging, ECG and prolonged rhythm monitoring for atrial"
            " fibrillation. Start dual antiplatelet therapy for 21 days"
            " followed by single agent in high-risk TIA, and treat blood"
            " pressure, lipids and diabetes. Refer for carotid endarterectomy"
            " if stenosis is significant and symptomatic."
        ),
    },
    {
        "case_id": "NEURO-011",
        "presentation": (
            "A 49-year-old man with chronic alcohol use is brought in confused."
            " He has horizontal nystagmus, bilateral lateral rectus palsy, and"
            " a broad unsteady gait. Capillary glucose is 3.1 mmol/L."
        ),
        "findings": "Wernicke encephalopathy — the classic triad of confusion, ophthalmoplegia and ataxia.",
        "gold_standard_action": (
            "Give high-dose parenteral thiamine BEFORE any glucose. Giving"
            " glucose first consumes the remaining thiamine and can precipitate"
            " or worsen the encephalopathy. Continue thiamine for several days,"
            " correct magnesium, and treat the underlying alcohol withdrawal."
        ),
    },
    {
        "case_id": "NEURO-012",
        "presentation": (
            "A 71-year-old woman on warfarin for atrial fibrillation presents"
            " with sudden headache, vomiting and left hemiparesis. Blood"
            " pressure is 210/115 mmHg. CT shows a 3 cm right basal ganglia"
            " haemorrhage. INR is 3.4."
        ),
        "findings": "Spontaneous intracerebral haemorrhage with anticoagulation.",
        "gold_standard_action": (
            "Reverse anticoagulation urgently with prothrombin complex"
            " concentrate and vitamin K — reversal speed drives outcome. Lower"
            " systolic blood pressure toward 140 mmHg in a controlled fashion."
            " Discuss with neurosurgery, particularly for cerebellar or large"
            " lobar haemorrhage with deterioration. Do not give antiplatelets"
            " or heparin acutely."
        ),
    },
    {
        "case_id": "NEURO-013",
        "presentation": (
            "A 28-year-old woman reports blurred vision and pain on eye"
            " movement in the left eye over four days. Visual acuity is reduced"
            " and colour vision is desaturated. There is a relative afferent"
            " pupillary defect on the left. The optic disc looks normal."
        ),
        "findings": "Retrobulbar optic neuritis, a common first presentation of multiple sclerosis.",
        "gold_standard_action": (
            "Arrange MRI of brain and orbits with contrast to look for"
            " demyelinating lesions and assess risk of conversion to multiple"
            " sclerosis. High-dose IV methylprednisolone speeds recovery but"
            " does not change final visual outcome, so it is optional and"
            " guided by severity. Oral prednisolone at standard dose alone"
            " should be avoided — it increases recurrence risk. Refer to"
            " neurology for disease-modifying therapy if MRI is suggestive."
        ),
    },
    {
        "case_id": "NEURO-014",
        "presentation": (
            "A 27-year-old woman with a BMI of 36 reports daily headache worse"
            " on lying down and on straining, with brief episodes of visual"
            " greying on standing. Fundoscopy shows bilateral papilloedema."
            " Imaging is normal and CSF opening pressure is 32 cmH2O with"
            " normal constituents."
        ),
        "findings": "Idiopathic intracranial hypertension.",
        "gold_standard_action": (
            "Confirm normal neuroimaging including venography to exclude venous"
            " sinus thrombosis before making the diagnosis. Start acetazolamide"
            " and arrange supervised weight reduction, which is disease"
            " modifying. Monitor visual fields serially, since vision — not"
            " headache — determines urgency. Consider CSF diversion or optic"
            " nerve sheath fenestration for rapidly progressive visual loss."
        ),
    },
    {
        "case_id": "NEURO-015",
        "presentation": (
            "A 55-year-old man has had fever, headache and progressive"
            " confusion over three days, with two focal seizures involving the"
            " right arm. MRI shows asymmetric high signal in the left temporal"
            " lobe and insula. CSF shows lymphocytic pleocytosis."
        ),
        "findings": "Herpes simplex virus encephalitis with temporal lobe involvement.",
        "gold_standard_action": (
            "Start IV aciclovir empirically as soon as the diagnosis is"
            " suspected — do not wait for CSF PCR, since delay of even hours"
            " worsens outcome and untreated mortality approaches 70%. Continue"
            " treatment for 14 to 21 days, treat seizures, and cover bacterial"
            " meningitis until excluded."
        ),
    },
]