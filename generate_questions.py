"""
Generate new high-quality ARRT Radiography questions.
Target: ~500 questions across Patient Care, Safety, Image Production.
Difficulty: Exam-weighted (mostly 3-4).
Correct answer always listed as first option; positions randomized at end.
"""

import json
import random

# Format: (stem, [correct, wrong1, wrong2, wrong3], explanation, subcategory, difficulty, tags)
# Correct answer is ALWAYS the first option — positions randomized later.

PATIENT_CARE = [
    # ── Patient Interactions and Communication ──────────────────────────────
    ("A patient is hard of hearing and misses breathing instructions during a chest radiograph. What is the BEST corrective action?",
     ["Use visual signals and written instructions","Speak louder into both ears","Proceed with the exam and repeat if needed","Ask a family member to translate from outside the room"],
     "Written cues and hand signals bridge communication barriers without compromising privacy or clinical accuracy.",
     "Patient Interactions and Management", 3, ["communication","chest"]),

    ("A patient with dementia becomes agitated during positioning for a hip radiograph. Which action is MOST appropriate?",
     ["Speak calmly, simplify instructions, and use gentle reassurance","Restrain the patient with tape to prevent motion","Increase exposure factors to compensate for motion","Proceed quickly without explanation to reduce stress"],
     "A calm, simplified approach respects dignity and reduces agitation; physical restraints require physician orders.",
     "Patient Interactions and Management", 3, ["communication","positioning"]),

    ("Before a contrast-enhanced CT, the patient asks why blood work was ordered. The BEST response is:",
     ["Kidney function must be confirmed before IV contrast because contrast can worsen existing kidney disease","The doctor ordered it as part of the routine protocol","It checks for allergies to contrast media","It confirms you are not pregnant"],
     "Serum creatinine and eGFR assess renal function, which directly affects contrast media clearance and nephrotoxicity risk.",
     "Patient Interactions and Management", 3, ["contrast","patient education"]),

    ("A radiographer is asked to perform an examination on an unconscious trauma patient with no documented consent. Which principle applies?",
     ["Implied consent allows the examination to proceed in an emergency","Informed consent must be obtained from the nearest relative before any imaging","The examination must be postponed until consent can be obtained","Only the radiologist may authorize imaging in this situation"],
     "In life-threatening emergencies, implied consent assumes a reasonable person would consent to necessary treatment.",
     "Patient Interactions and Management", 4, ["consent","trauma"]),

    ("A patient refuses a recommended radiograph. The radiographer should FIRST:",
     ["Explain the clinical reason for the examination and document the refusal","Proceed with the examination since it was physician-ordered","Convince the patient by explaining possible consequences in detail","Notify the physician and cancel the order without documenting"],
     "Competent patients have the right to refuse; the radiographer should explain, document the refusal, and notify the ordering provider.",
     "Patient Interactions and Management", 3, ["consent","ethics"]),

    ("Which statement BEST reflects the radiographer's role regarding patient confidentiality?",
     ["Patient information must not be shared with anyone not directly involved in the patient's care","Imaging findings may be discussed with other patients if names are withheld","Family members may always receive information about a patient's condition","Confidentiality applies only to written records, not verbal discussions"],
     "HIPAA mandates that protected health information is shared only with those directly involved in care.",
     "Patient Interactions and Management", 2, ["HIPAA","ethics"]),

    ("A patient expresses fear about radiation exposure before a chest X-ray. The radiographer's BEST response is:",
     ["Explain that the dose is very low and comparable to natural background radiation","Tell the patient not to worry because X-rays are perfectly safe","Offer to skip the exam to alleviate the patient's concern","Explain that the benefits of diagnosis outweigh any concerns about radiation"],
     "Providing factual, reassuring information about dose context addresses the fear without minimizing it or dismissing the exam.",
     "Patient Interactions and Management", 2, ["communication","radiation safety"]),

    ("During positioning, a patient tells the radiographer they are in pain. The MOST appropriate action is:",
     ["Adjust positioning to minimize discomfort and notify the radiologist if needed","Complete the examination quickly to reduce exposure to discomfort","Administer pain medication from the department's supply","Ask the patient to tolerate the discomfort until the exam is complete"],
     "Patient comfort is a priority; modification of positioning and escalation to appropriate staff is the correct response.",
     "Patient Interactions and Management", 3, ["patient care","positioning"]),

    ("A non-English-speaking patient is scheduled for an upper GI series. What is the MOST appropriate approach?",
     ["Arrange for a qualified medical interpreter","Use a bilingual family member who happens to be present","Use simple English and gestures alone","Postpone the exam until a translator is found"],
     "Qualified medical interpreters ensure accurate communication of clinical information; using family members risks inaccuracies and privacy issues.",
     "Patient Interactions and Management", 3, ["communication","GI"]),

    ("What is the radiographer's responsibility when a physician's order appears clinically inconsistent with the patient's complaint?",
     ["Clarify the order with the ordering physician before proceeding","Proceed with the ordered exam without question","Substitute a more appropriate examination based on clinical judgment","Refuse the examination and document the inconsistency"],
     "Clarifying ambiguous or inconsistent orders protects the patient and is within the radiographer's professional responsibility.",
     "Patient Interactions and Management", 4, ["ethics","clinical judgment"]),

    # ── Infection Control ───────────────────────────────────────────────────
    ("A patient is on airborne precautions. Which PPE is REQUIRED before entering the room for a portable chest X-ray?",
     ["N95 respirator","Surgical mask, gown, and gloves","Gloves and gown only","No PPE is needed if the exposure is brief"],
     "Airborne precautions require an N95 or higher respirator to protect against small-particle aerosols.",
     "Infection Control", 3, ["infection control","portable","PPE"]),

    ("After imaging a patient on contact precautions, which step should the radiographer take with the image receptor?",
     ["Disinfect the receptor with an EPA-approved disinfectant before returning it to the department","Return the receptor directly to the department for routine cleaning","Place the receptor in a biohazard bag without cleaning","Discard the receptor after single patient use"],
     "Equipment that contacts or enters a contact-precaution patient's environment must be decontaminated before reuse.",
     "Infection Control", 3, ["infection control","contact precautions"]),

    ("Standard precautions apply to:",
     ["All patients regardless of diagnosis","Only patients with confirmed infectious diseases","Only patients with visible blood or body fluid exposure","Only immunocompromised patients"],
     "Standard precautions treat all blood and body fluids as potentially infectious for all patients, not just those with known infections.",
     "Infection Control", 2, ["infection control","standard precautions"]),

    ("A radiographer sustains a needlestick injury during an IV contrast injection. The FIRST action should be:",
     ["Wash the site thoroughly with soap and water and report to occupational health","Apply an antiseptic and continue with the examination","Report to the charge nurse at the end of the shift","Apply pressure and cover with a bandage before continuing work"],
     "Immediate thorough washing reduces pathogen load; prompt reporting initiates post-exposure protocol within recommended timeframes.",
     "Infection Control", 3, ["infection control","needlestick"]),

    ("A patient with active tuberculosis requires a portable chest X-ray. Which room precaution is MOST critical?",
     ["Negative pressure (airborne isolation) room","Standard precautions with a surgical mask","Contact precautions with gown and gloves","Droplet precautions with a surgical mask"],
     "Active TB is transmitted via airborne droplet nuclei; negative-pressure isolation rooms prevent spread.",
     "Infection Control", 4, ["infection control","TB","airborne"]),

    ("Hand hygiene should be performed:",
     ["Before and after each patient contact","Only when hands are visibly soiled","Only after removing gloves","Once per patient care session"],
     "WHO and CDC guidelines mandate hand hygiene before and after every patient contact to prevent healthcare-associated infections.",
     "Infection Control", 2, ["infection control","hand hygiene"]),

    ("Which disinfectant level is required for semi-critical radiographic equipment that contacts mucous membranes?",
     ["High-level disinfection","Low-level disinfection","Intermediate-level disinfection","Sterilization is required for all equipment"],
     "Semi-critical items contacting mucous membranes require high-level disinfection to destroy all microorganisms except high concentrations of bacterial spores.",
     "Infection Control", 4, ["infection control","disinfection"]),

    ("Proper donning order of PPE is:",
     ["Gown, mask/respirator, eye protection, gloves","Gloves, gown, mask, eye protection","Mask, gown, gloves, eye protection","Gown, gloves, mask, eye protection"],
     "Gown first protects clothing; mask and eye protection protect mucous membranes; gloves last protect hands and complete the barrier.",
     "Infection Control", 3, ["infection control","PPE"]),

    # ── Medical Emergencies ─────────────────────────────────────────────────
    ("A patient undergoing IV contrast injection develops urticaria, mild nausea, and rhinorrhea. This represents:",
     ["A mild contrast reaction requiring observation and possible antihistamine","A severe anaphylactic reaction requiring epinephrine immediately","A vasovagal reaction requiring Trendelenburg positioning","A normal physiological response to contrast media"],
     "Urticaria, nausea, and rhinorrhea indicate a mild allergic-type reaction; monitoring and possible antihistamine are appropriate first steps.",
     "Medical Emergencies", 3, ["contrast reaction","emergency"]),

    ("A patient develops bronchospasm and laryngeal edema after IV contrast. The PRIORITY medication is:",
     ["Epinephrine 1:1000 (0.3 mL IM)","Diphenhydramine (Benadryl) IV","Methylprednisolone (Solu-Medrol) IV","Oxygen via nasal cannula"],
     "Bronchospasm and laryngeal edema indicate anaphylaxis; epinephrine is the first-line drug for anaphylaxis and must be given immediately.",
     "Medical Emergencies", 4, ["contrast reaction","anaphylaxis","emergency"]),

    ("A patient loses consciousness during fluoroscopy. After activating the emergency response system, what should the radiographer do NEXT?",
     ["Begin a pulse check and initiate CPR if no pulse is found","Administer oxygen immediately via non-rebreather mask","Lower the fluoroscopic table to a flat position","Move the patient to a gurney for transport to the ER"],
     "After calling for help, assessment of circulation (pulse check) and initiation of CPR if absent is the next priority per BLS guidelines.",
     "Medical Emergencies", 4, ["emergency","CPR","loss of consciousness"]),

    ("A patient on the radiographic table reports feeling lightheaded and diaphoretic while standing for an upright chest X-ray. This presentation MOST suggests:",
     ["Vasovagal syncope","Severe contrast reaction","Pulmonary embolism","Hypoglycemia"],
     "Lightheadedness and diaphoresis (sweating) in an upright patient are classic vasovagal symptoms caused by sudden drop in blood pressure and heart rate.",
     "Medical Emergencies", 3, ["syncope","emergency"]),

    ("During a barium enema, a patient suddenly complains of sharp abdominal pain and develops rigidity. The radiographer should IMMEDIATELY:",
     ["Stop the infusion, notify the radiologist, and prepare for possible bowel perforation protocol","Slow the barium flow and reassure the patient","Complete the examination quickly before symptoms worsen","Administer an antispasmodic medication"],
     "Sharp pain and abdominal rigidity suggest possible bowel perforation; stopping the procedure and alerting the radiologist is critical.",
     "Medical Emergencies", 4, ["barium","GI","emergency"]),

    ("Which vital sign finding in a post-procedure patient requires IMMEDIATE escalation?",
     ["Blood pressure of 80/50 mmHg with altered mental status","Heart rate of 95 bpm with normal mentation","Respiratory rate of 18 breaths/min","Oxygen saturation of 96% on room air"],
     "Hypotension (BP 80/50) with altered mental status indicates hemodynamic instability and possible shock, requiring immediate intervention.",
     "Medical Emergencies", 4, ["vital signs","emergency","shock"]),

    ("What is the normal adult respiratory rate?",
     ["12–20 breaths per minute","6–10 breaths per minute","22–28 breaths per minute","30–40 breaths per minute"],
     "The normal adult respiratory rate is 12–20 breaths per minute; rates outside this range indicate respiratory distress.",
     "Medical Emergencies", 2, ["vital signs"]),

    ("A diabetic patient becomes confused and diaphoretic during an exam. Which action is MOST appropriate?",
     ["Check blood glucose if possible and notify the nurse; provide oral glucose if patient is alert","Administer insulin per standing order","Position supine and monitor without intervention","Proceed quickly and send the patient back to the ward"],
     "Confusion and diaphoresis in a diabetic patient suggest hypoglycemia; glucose assessment and nursing notification are the appropriate first steps.",
     "Medical Emergencies", 3, ["emergency","diabetic","hypoglycemia"]),

    ("A patient's radial pulse is 52 bpm and irregular. The radiographer should:",
     ["Document the finding and notify the referring team before proceeding","Proceed with the examination as this is within acceptable limits","Ask the patient to perform a Valsalva maneuver","Administer oxygen and continue the examination"],
     "Bradycardia below 60 bpm and an irregular pulse should be documented and reported to the ordering team, who will determine if imaging should proceed.",
     "Medical Emergencies", 3, ["vital signs","cardiac"]),

    # ── Patient Transfer and Mobility ───────────────────────────────────────
    ("When transferring a patient from a wheelchair to the radiographic table, the wheelchair should be positioned:",
     ["At a 45-degree angle to the table on the patient's stronger side","Parallel to the table on either side","Perpendicular to the table at the foot end","At a 90-degree angle to the table on the patient's weaker side"],
     "A 45-degree angle minimizes the transfer distance; placing it on the stronger side allows the patient to use their stronger extremities for support.",
     "Patient Transfer and Positioning", 3, ["transfer","wheelchair"]),

    ("A patient is on a backboard with a cervical collar following trauma. The MOST appropriate action before repositioning is:",
     ["Obtain radiologist or physician approval before moving the patient","Remove the collar to allow better neck positioning","Transfer the patient to the radiographic table alone if help is unavailable","Perform only AP projections to avoid repositioning"],
     "Trauma patients with spinal precautions must not be moved without physician clearance to avoid worsening potential spinal injuries.",
     "Patient Transfer and Positioning", 4, ["trauma","spinal","transfer"]),

    ("Body mechanics principles that reduce back injury during patient transfer include:",
     ["Keeping the load close to the body and bending the knees","Bending at the waist to reach the patient","Twisting the torso while lifting","Using arm strength rather than leg muscles"],
     "Correct body mechanics require a wide base of support, knee flexion, and keeping the load close to prevent musculoskeletal injury.",
     "Patient Transfer and Positioning", 2, ["body mechanics","transfer"]),

    ("How many staff members are recommended at minimum to log-roll a trauma patient to evaluate the spine?",
     ["Three (one for head/neck, two for body)","One experienced radiographer","Two (one for head, one for body)","Four to ensure complete safety"],
     "Log-rolling a trauma patient safely requires at least three people: one to maintain cervical alignment and two for the body.",
     "Patient Transfer and Positioning", 3, ["trauma","transfer","spinal"]),

    ("A patient's drainage tube is inadvertently pulled during transfer. The radiographer should:",
     ["Clamp the tube, notify the nurse immediately, and document the incident","Reinsert the tube using aseptic technique","Ignore the displacement if the patient is not in distress","Apply pressure and continue with the examination"],
     "A dislodged drainage tube is a clinical complication; clamping prevents fluid loss and immediate nursing notification is required.",
     "Patient Transfer and Positioning", 4, ["patient care","tubes","emergency"]),

    # ── Contrast Media ──────────────────────────────────────────────────────
    ("Which patient history finding is MOST significant before administering iodinated IV contrast?",
     ["Renal insufficiency (eGFR < 45 mL/min/1.73m²)","History of seasonal allergies","Previous antibiotic use","Mild lactose intolerance"],
     "Renal insufficiency significantly increases the risk of contrast-induced nephropathy; an eGFR below 45 warrants risk-benefit discussion.",
     "Contrast Media", 4, ["contrast","renal"]),

    ("Metformin should be withheld after iodinated contrast administration because:",
     ["It can accumulate and cause lactic acidosis if renal function is temporarily impaired","It reacts chemically with iodine to cause hypoglycemia","It accelerates contrast excretion leading to osmotic diuresis","It increases the risk of a delayed allergic reaction"],
     "Contrast can transiently impair renal function; metformin accumulation in this setting increases lactic acidosis risk.",
     "Contrast Media", 4, ["contrast","pharmacology","metformin"]),

    ("Which type of iodinated contrast agent has the LOWEST risk of adverse reactions?",
     ["Non-ionic, low-osmolality agents","Ionic, high-osmolality agents","Ionic, low-osmolality agents","Non-ionic, high-osmolality agents"],
     "Non-ionic, low-osmolality contrast agents have a significantly lower rate of adverse reactions compared to ionic, high-osmolality agents.",
     "Contrast Media", 3, ["contrast","pharmacology"]),

    ("A patient has a documented prior anaphylactic reaction to iodinated contrast. If contrast is still required, the physician will MOST likely order:",
     ["A premedication protocol (e.g., corticosteroids and antihistamines)","A lower volume of the same contrast agent","Barium sulfate as an alternative","A skin test before administration"],
     "Premedication with corticosteroids and antihistamines reduces the risk of repeat allergic reactions in sensitized patients.",
     "Contrast Media", 4, ["contrast","allergy","premedication"]),

    ("During IV contrast injection, the patient reports sharp pain and the injection site becomes swollen. The MOST likely cause is:",
     ["Extravasation of contrast into soft tissue","Normal pressure sensation from rapid injection","An allergic reaction to the contrast agent","Vasovagal response to the injection"],
     "Swelling and pain at the injection site during contrast injection indicate extravasation (infiltration into surrounding tissue).",
     "Contrast Media", 3, ["contrast","extravasation","IV"]),

    ("Barium sulfate is contraindicated in suspected bowel perforation because:",
     ["Barium entering the peritoneum causes severe peritonitis","Barium reacts with gastric acid to form toxic compounds","Barium is absorbed and causes nephrotoxicity","Barium inhibits peristalsis and worsens obstruction"],
     "Barium in the peritoneal cavity causes a severe inflammatory reaction (barium peritonitis), which has high mortality.",
     "Contrast Media", 4, ["contrast","barium","GI"]),

    ("The MOST common route of gadolinium contrast administration for MRI is:",
     ["Intravenous injection","Oral ingestion","Intra-articular injection","Intrathecal injection"],
     "Gadolinium-based contrast agents for MRI are most commonly administered intravenously to enhance vascular and tissue detail.",
     "Contrast Media", 2, ["contrast","MRI","gadolinium"]),

    ("Which lab value is MOST important to assess before administering gadolinium-based contrast?",
     ["Glomerular filtration rate (GFR)","Serum glucose","Prothrombin time (PT)","Serum potassium"],
     "Nephrogenic systemic fibrosis (NSF) risk from gadolinium is highest in patients with severe renal impairment; GFR screening is essential.",
     "Contrast Media", 4, ["contrast","MRI","renal","gadolinium"]),

    # ── Pharmacology and Vital Signs ────────────────────────────────────────
    ("The normal range for adult systolic blood pressure is:",
     ["90–120 mmHg","60–80 mmHg","130–150 mmHg","150–180 mmHg"],
     "Normal adult systolic blood pressure is 90–120 mmHg; hypertension is defined as consistently above 130 mmHg.",
     "Vital Signs and Monitoring", 2, ["vital signs","blood pressure"]),

    ("Which oxygen delivery device provides the HIGHEST concentration of oxygen?",
     ["Non-rebreather mask","Simple face mask","Nasal cannula","Venturi mask"],
     "A non-rebreather mask with a one-way valve and reservoir bag delivers 60–90% oxygen at 10–15 L/min.",
     "Medical Emergencies", 3, ["oxygen","emergency"]),

    ("Atropine is used in a radiography emergency setting primarily to treat:",
     ["Severe bradycardia","Anaphylaxis","Severe hypotension","Seizures"],
     "Atropine is an anticholinergic agent that increases heart rate and is used to treat symptomatic bradycardia.",
     "Medical Emergencies", 4, ["pharmacology","emergency","cardiac"]),

    ("Which medication is a bronchodilator used to treat bronchospasm during a contrast reaction?",
     ["Albuterol (salbutamol)","Epinephrine","Diphenhydramine","Methylprednisolone"],
     "Albuterol is a beta-2 agonist bronchodilator administered via inhaler or nebulizer for bronchospasm.",
     "Medical Emergencies", 3, ["pharmacology","contrast reaction","bronchospasm"]),

    ("Normal adult pulse oximetry (SpO₂) is:",
     ["95–100%","85–94%","75–84%","Below 75%"],
     "Normal SpO₂ is 95–100%; below 90% indicates hypoxemia requiring intervention.",
     "Vital Signs and Monitoring", 2, ["vital signs","oxygen saturation"]),

    ("A patient is being monitored with an ECG during fluoroscopy. Flat-line (asystole) is noted. The radiographer should FIRST:",
     ["Check that the leads are properly attached before assuming cardiac arrest","Begin chest compressions immediately","Call a code immediately without further assessment","Administer oxygen and reassess in 30 seconds"],
     "ECG artifacts from lead displacement are common; checking lead attachment before declaring cardiac arrest prevents unnecessary interventions.",
     "Medical Emergencies", 4, ["ECG","cardiac","emergency"]),

    ("IV access for contrast media is MOST commonly established in which vessel?",
     ["Antecubital vein","Femoral vein","Jugular vein","Subclavian vein"],
     "The antecubital vein is large, accessible, and tolerates the flow rates needed for contrast injection.",
     "Contrast Media", 2, ["IV access","contrast"]),

    ("When documenting a contrast reaction, the radiographer MUST record:",
     ["Time, symptoms, vital signs, interventions, and patient response","Only the type of reaction and medication given","Patient name and date of exam only","A verbal report to the radiologist is sufficient"],
     "Thorough documentation including timeline, clinical findings, interventions, and response is both a legal requirement and clinical necessity.",
     "Medical Emergencies", 3, ["documentation","contrast reaction"]),

    ("A patient's Glasgow Coma Scale (GCS) score is 8. This indicates:",
     ["Severe impairment requiring airway management consideration","Mild confusion but intact protective reflexes","Normal neurological status","Moderate impairment with reliable verbal response"],
     "A GCS of 8 or below indicates severe neurological impairment; airway protection is a priority.",
     "Medical Emergencies", 4, ["neuro","emergency","GCS"]),
]


SAFETY = [
    # ── Radiation Protection Principles ────────────────────────────────────
    ("The annual occupational whole-body effective dose limit in the United States is:",
     ["50 mSv (5 rem)","100 mSv (10 rem)","25 mSv (2.5 rem)","150 mSv (15 rem)"],
     "The NRC and NCRP set the annual occupational whole-body effective dose limit at 50 mSv (5 rem).",
     "Radiation Protection", 2, ["dose limits","occupational"]),

    ("The annual occupational dose limit for the lens of the eye is:",
     ["150 mSv (15 rem)","50 mSv (5 rem)","500 mSv (50 rem)","15 mSv (1.5 rem)"],
     "The lens of the eye has a dose limit of 150 mSv/year due to its radiosensitivity and risk for cataract formation.",
     "Radiation Protection", 3, ["dose limits","lens","occupational"]),

    ("What is the recommended gestational dose limit for occupationally exposed pregnant workers?",
     ["5 mSv (0.5 rem) for the entire pregnancy","50 mSv (5 rem) per trimester","1 mSv (0.1 rem) per month","No additional limit beyond standard annual limit"],
     "NCRP recommends an embryo/fetus dose equivalent limit of 5 mSv for the entire pregnancy once declared.",
     "Radiation Protection", 3, ["dose limits","pregnancy","occupational"]),

    ("The ALARA principle requires that radiation exposure be:",
     ["As low as reasonably achievable while obtaining diagnostic quality images","As low as possible regardless of image quality","Eliminated completely for all patients","Limited to the minimum annual dose without exceptions"],
     "ALARA balances minimizing exposure against obtaining diagnostic-quality images necessary for patient care.",
     "Radiation Protection", 2, ["ALARA","radiation protection"]),

    ("Which of the following BEST describes the cardinal principles of radiation protection?",
     ["Time, distance, and shielding","Filtration, collimation, and shielding","kVp, mAs, and distance","Dose, rate, and duration"],
     "The three cardinal principles of radiation protection are time (minimize), distance (maximize), and shielding (use appropriate barriers).",
     "Radiation Protection", 2, ["cardinal principles","radiation protection"]),

    ("Doubling the distance from a radiation source reduces the exposure rate by a factor of:",
     ["4 (inverse square law)","2 (linear relationship)","8 (cube law)","1.5 (proportional reduction)"],
     "The inverse square law states that intensity is inversely proportional to the square of the distance; doubling distance reduces exposure to 1/4.",
     "Radiation Protection", 3, ["inverse square law","distance"]),

    ("Inherent filtration in an x-ray tube is PRIMARILY provided by:",
     ["The glass envelope and oil surrounding the tube","Added aluminum sheets at the port","The lead housing","The collimator blades"],
     "Inherent filtration comes from the glass envelope, insulating oil, and tube window, and is typically 0.5–1 mm Al equivalent.",
     "Radiation Protection", 3, ["filtration","inherent","x-ray tube"]),

    ("Added filtration in a diagnostic x-ray unit is PRIMARILY used to:",
     ["Remove low-energy photons that contribute to patient dose without aiding the image","Increase beam intensity for better penetration","Reduce the overall kVp required","Eliminate scatter radiation from the beam"],
     "Added filtration (typically aluminum) hardens the beam by removing low-energy photons that only contribute to dose without producing useful image information.",
     "Radiation Protection", 3, ["filtration","added","beam quality"]),

    ("A lead apron used for patient or personnel protection should have a lead equivalence of at least:",
     ["0.25 mm Pb (0.5 mm Pb for fluoroscopy)","0.05 mm Pb","1.0 mm Pb","0.10 mm Pb"],
     "NCRP recommends at least 0.25 mm Pb for diagnostic radiography; fluoroscopy aprons require 0.5 mm Pb due to longer exposure times.",
     "Radiation Protection", 3, ["shielding","lead apron"]),

    ("Gonadal shielding should be used when the gonads are within how many centimeters of the primary beam?",
     ["5 cm","2 cm","10 cm","15 cm"],
     "NCRP recommends gonadal shielding when the gonads are within 5 cm of the collimated field.",
     "Radiation Protection", 3, ["gonadal shielding","radiation protection"]),

    ("Contact shielding (gonad shield) is MOST effective for:",
     ["Male patients in whom the gonads are superficial","Female patients in whom the gonads are deep in the pelvis","Pediatric patients receiving chest radiographs","All patients equally regardless of gender"],
     "Male gonads are superficial and easily shielded; female gonads are within the pelvis and contact shielding may obscure anatomy.",
     "Radiation Protection", 3, ["gonadal shielding","gender"]),

    ("Which personnel monitoring device provides the MOST accurate cumulative dose record?",
     ["Optically stimulated luminescence (OSL) dosimeter","Film badge","Pocket ionization chamber","Geiger-Müller counter"],
     "OSL dosimeters have high sensitivity, wide dynamic range, and are re-readable, making them the most accurate personnel monitoring option.",
     "Radiation Protection", 4, ["dosimetry","OSL","personnel monitoring"]),

    ("A radiographer's monthly dosimeter reading exceeds the expected range. The FIRST action should be:",
     ["Investigate potential causes of high exposure and report to radiation safety officer","Discard the dosimeter and replace it","Assume the dosimeter is malfunctioning and continue working","Reduce personal workload for the remainder of the year"],
     "An unexpectedly high reading must be investigated to determine if it reflects actual exposure or equipment malfunction; the RSO must be notified.",
     "Radiation Protection", 3, ["dosimetry","personnel monitoring"]),

    ("Which type of radiation interaction produces the most scatter in diagnostic radiography?",
     ["Compton scatter","Photoelectric effect","Coherent (classical) scatter","Pair production"],
     "Compton scatter predominates at diagnostic energies above 30 keV and is the primary source of scatter radiation affecting image quality.",
     "Radiation Physics", 3, ["Compton scatter","scatter","interaction"]),

    ("The half-value layer (HVL) of a beam is the material thickness needed to reduce beam intensity by:",
     ["50%","25%","75%","10%"],
     "The HVL is defined as the thickness of a specified material that reduces beam intensity to one-half (50%) of its original value.",
     "Radiation Physics", 2, ["HVL","beam quality"]),

    ("Beam restriction (collimation) reduces patient dose primarily by:",
     ["Limiting the volume of tissue irradiated","Reducing the kVp applied to the patient","Increasing the filtration of low-energy photons","Reducing the mAs used during exposure"],
     "Collimation restricts the beam to the area of interest, reducing the volume of tissue receiving radiation and lowering scatter.",
     "Radiation Protection", 2, ["collimation","beam restriction","dose reduction"]),

    # ── Radiation Biology ───────────────────────────────────────────────────
    ("Which cells in the body are considered MOST radiosensitive?",
     ["Lymphocytes","Nerve cells","Muscle cells","Mature red blood cells"],
     "Lymphocytes (and other rapidly dividing cells) are the most radiosensitive; neurons and muscle cells are among the least sensitive.",
     "Radiation Biology", 3, ["radiosensitivity","biology"]),

    ("The law of Bergonié and Tribondeau states that cells are MORE radiosensitive when they are:",
     ["Actively dividing with a long mitotic future and undifferentiated","Mature and highly specialized","Non-dividing with stable DNA","Large in size and metabolically active"],
     "Bergonié and Tribondeau found that radiosensitivity increases with high mitotic rate, long mitotic future, and low differentiation.",
     "Radiation Biology", 3, ["radiosensitivity","Bergonié and Tribondeau"]),

    ("Stochastic effects of radiation are BEST described as:",
     ["All-or-none responses with no threshold dose","Effects with a dose threshold below which they do not occur","Deterministic effects that worsen with increasing dose","Effects limited to the gonads"],
     "Stochastic effects (cancer, genetic effects) have no dose threshold; probability increases with dose, but severity does not.",
     "Radiation Biology", 4, ["stochastic effects","radiation biology"]),

    ("Radiation-induced cataract formation is classified as a:",
     ["Deterministic (tissue reaction) effect","Stochastic somatic effect","Stochastic genetic effect","Acute somatic effect"],
     "Cataracts occur above a threshold dose and worsen with increasing dose, classifying them as deterministic tissue reactions.",
     "Radiation Biology", 4, ["cataract","deterministic","radiation biology"]),

    ("Which tissue is MOST susceptible to radiation-induced cancer?",
     ["Bone marrow (leukemia)","Mature brain tissue","Skeletal muscle","Liver"],
     "Bone marrow is highly radiosensitive; radiation-induced leukemia has one of the shortest latency periods of all radiation-induced cancers.",
     "Radiation Biology", 3, ["cancer risk","bone marrow","radiation biology"]),

    ("The term 'relative biological effectiveness' (RBE) compares the biological damage of a given radiation type relative to:",
     ["250 kVp x-rays","Alpha particles","Neutrons","Gamma rays from cobalt-60"],
     "RBE is defined relative to 250 kVp x-rays (the standard reference radiation).",
     "Radiation Biology", 4, ["RBE","radiation biology"]),

    ("Which type of radiation has the HIGHEST relative biological effectiveness (RBE)?",
     ["Alpha particles","X-rays","Beta particles","Gamma rays"],
     "Alpha particles have an RBE of 20 due to their high linear energy transfer (LET) and dense ionization track.",
     "Radiation Biology", 3, ["RBE","alpha","radiation biology"]),

    ("The latent period in radiation carcinogenesis refers to:",
     ["The time between exposure and appearance of the cancer","The dose required to cause cancer","The period of maximum radiosensitivity","The time for DNA repair after irradiation"],
     "The latent period is the time between radiation exposure and clinical manifestation of cancer; it varies by cancer type.",
     "Radiation Biology", 3, ["latent period","carcinogenesis","radiation biology"]),

    ("Free radicals produced by indirect radiation action PRIMARILY damage which cellular structure?",
     ["DNA","Cell membrane","Mitochondria","Ribosomes"],
     "Radiolysis of water creates reactive free radicals (OH•) that cause DNA strand breaks via indirect action, the dominant mechanism in cells.",
     "Radiation Biology", 4, ["free radicals","indirect action","DNA"]),

    ("Which type of ionizing radiation can penetrate skin but is stopped by several millimeters of aluminum?",
     ["Beta particles","Alpha particles","X-rays","Gamma rays"],
     "Beta particles can penetrate skin but are stopped by a few millimeters of material; alpha particles cannot penetrate skin.",
     "Radiation Biology", 3, ["beta","penetration","radiation physics"]),

    ("The whole-body dose that would be lethal to 50% of an exposed population within 30 days (LD 50/30) for humans is approximately:",
     ["3–4 Gy (300–400 rad)","0.5–1 Gy (50–100 rad)","8–10 Gy (800–1000 rad)","20–30 Gy (2000–3000 rad)"],
     "The human LD 50/30 is approximately 3–4 Gy; above this dose, without medical support, half the exposed population will die within 30 days.",
     "Radiation Biology", 4, ["LD 50/30","acute radiation syndrome"]),

    ("Acute radiation syndrome (ARS) develops after a whole-body dose GREATER than approximately:",
     ["1 Gy (100 rad)","0.1 Gy (10 rad)","5 Gy (500 rad)","10 Gy (1000 rad)"],
     "ARS requires a whole-body absorbed dose of at least 1 Gy; below this threshold, acute systemic effects are not observed.",
     "Radiation Biology", 3, ["ARS","acute radiation syndrome","threshold"]),

    # ── Radiation Physics ───────────────────────────────────────────────────
    ("X-rays are produced in an x-ray tube PRIMARILY by:",
     ["Bremsstrahlung and characteristic radiation","Compton scatter within the tube","Pair production at the anode","Coherent scattering from the focal spot"],
     "X-rays are produced by bremsstrahlung (braking radiation) when electrons decelerate in the tungsten target, and by characteristic radiation when inner-shell electrons are ejected.",
     "Radiation Physics", 3, ["x-ray production","bremsstrahlung","characteristic radiation"]),

    ("The primary controller of x-ray beam QUALITY (penetrating power) is:",
     ["Kilovoltage peak (kVp)","Milliamperage (mA)","Exposure time (s)","Source-to-image distance (SID)"],
     "kVp determines the maximum energy of the x-ray beam and therefore its penetrating ability (beam quality).",
     "Radiation Physics", 2, ["kVp","beam quality"]),

    ("The primary controller of x-ray beam QUANTITY (number of photons) is:",
     ["Milliampere-seconds (mAs)","Kilovoltage peak (kVp)","Inherent filtration","Focal spot size"],
     "mAs (tube current × time) determines the number of electrons striking the anode and thus the number of x-ray photons produced.",
     "Radiation Physics", 2, ["mAs","beam quantity"]),

    ("Which x-ray interaction is RESPONSIBLE for the photoelectric effect?",
     ["A photon is completely absorbed and ejects an inner-shell electron","A photon loses part of its energy and changes direction","A photon passes through matter without interaction","A photon creates an electron-positron pair"],
     "The photoelectric effect involves total absorption of the photon and ejection of an inner-shell (photoelectron); it predominates at lower kVp.",
     "Radiation Physics", 3, ["photoelectric effect","interaction"]),

    ("Characteristic radiation is produced when:",
     ["An outer-shell electron fills an inner-shell vacancy, releasing the energy difference as a photon","A high-speed electron decelerates near a nucleus","A photon is absorbed by the patient","Pair production occurs at the anode"],
     "When an electron vacancy in an inner shell is filled by an outer-shell electron, the energy difference is emitted as characteristic x-radiation.",
     "Radiation Physics", 3, ["characteristic radiation","x-ray production"]),

    ("The anode heel effect results in higher x-ray intensity on the:",
     ["Cathode side of the beam","Anode side of the beam","Center of the beam","Lateral edges only"],
     "The anode heel effect causes the beam to be more intense on the cathode side because photons directed toward the anode must exit through more target material.",
     "Radiation Physics", 3, ["anode heel effect","x-ray tube"]),

    ("Which anode material is MOST commonly used in x-ray tubes because of its high atomic number and high melting point?",
     ["Tungsten","Copper","Molybdenum","Lead"],
     "Tungsten (W, Z=74) has a high atomic number for efficient x-ray production and a high melting point (3422°C) for heat tolerance.",
     "Radiation Physics", 2, ["tungsten","anode","x-ray tube"]),

    ("Rectification in an x-ray generator converts:",
     ["Alternating current to direct current","Direct current to alternating current","Low voltage to high voltage","High voltage to low voltage"],
     "Rectifiers convert the alternating current (AC) from the transformer to direct current (DC) so electrons flow only in one direction (cathode to anode).",
     "Radiation Physics", 3, ["rectification","generator"]),

    ("A three-phase, 12-pulse generator produces a more consistent x-ray output than single-phase because it:",
     ["Maintains voltage closer to peak with less ripple","Delivers higher kVp with lower mAs","Uses three separate x-ray tubes","Reduces filtration requirements"],
     "Three-phase, 12-pulse generators have very low voltage ripple (<1%), producing a nearly constant potential and more efficient x-ray output.",
     "Radiation Physics", 4, ["generator","three-phase","voltage ripple"]),

    ("The quantity of radiation measured in air, expressed as charge produced per unit mass, is:",
     ["Exposure (measured in coulombs/kg or roentgens)","Absorbed dose (measured in gray)","Effective dose (measured in sievert)","Equivalent dose (measured in sievert)"],
     "Exposure quantifies ionization in air; absorbed dose measures energy deposited in tissue; effective and equivalent doses account for biological effectiveness.",
     "Radiation Physics", 3, ["units","exposure","dosimetry"]),

    ("The unit of absorbed dose in the SI system is the:",
     ["Gray (Gy)","Sievert (Sv)","Roentgen (R)","Rem"],
     "The gray (Gy) is the SI unit of absorbed dose; 1 Gy = 1 J/kg of energy deposited in tissue.",
     "Radiation Physics", 2, ["gray","absorbed dose","SI units"]),

    ("Effective dose accounts for:",
     ["Both radiation type and tissue radiosensitivity weighting factors","Only the absorbed dose in a specific tissue","The charge produced per unit mass of air","The dose delivered per unit time"],
     "Effective dose (Sv) multiplies absorbed dose by radiation weighting factor (Wr) and tissue weighting factor (Wt) to represent stochastic risk.",
     "Radiation Physics", 4, ["effective dose","weighting factors"]),

    # ── Fluoroscopy Safety ──────────────────────────────────────────────────
    ("During fluoroscopy, the patient's entrance skin dose rate should NOT exceed:",
     ["88 mGy/min (10 R/min) for standard mode","500 mGy/min","200 mGy/min","10 mGy/min"],
     "FDA regulations limit fluoroscopic entrance skin dose to 88 mGy/min (10 R/min) for standard mode and 176 mGy/min for high-dose mode.",
     "Fluoroscopy Safety", 3, ["fluoroscopy","dose limit","entrance skin dose"]),

    ("Which factor MOST effectively reduces patient dose during fluoroscopy?",
     ["Minimizing fluoroscopy time using intermittent activation","Increasing kVp to maximum","Using the highest magnification mode available","Positioning the image intensifier far from the patient"],
     "Fluoroscopy time is the primary determinant of dose; intermittent activation and limiting total time are the most effective dose reduction strategies.",
     "Fluoroscopy Safety", 3, ["fluoroscopy","dose reduction"]),

    ("Last image hold (LIH) in fluoroscopy reduces dose by:",
     ["Displaying the last acquired image without continuous radiation","Storing images for review after the procedure","Reducing the kVp during low-dose sequences","Automatically collimating the beam to the smallest field"],
     "LIH displays the last fluoroscopic frame without additional radiation, allowing review of anatomy and reducing unnecessary exposure.",
     "Fluoroscopy Safety", 3, ["fluoroscopy","last image hold","dose reduction"]),

    ("In fluoroscopy, placing the image intensifier (or flat-panel detector) CLOSER to the patient:",
     ["Reduces patient dose and magnification","Increases patient dose","Has no effect on dose","Reduces spatial resolution"],
     "Minimizing the air gap between the patient and detector reduces dose by increasing the fraction of transmitted photons captured.",
     "Fluoroscopy Safety", 3, ["fluoroscopy","geometry","dose"]),

    ("The 5-minute audible alarm in fluoroscopy equipment serves to:",
     ["Remind operators of cumulative fluoroscopy time to prompt dose monitoring","Indicate that the tube is overheating","Signal that the exposure limit has been reached","Warn that the image intensifier needs replacement"],
     "The 5-minute alarm alerts the operator to total beam-on time, prompting dose awareness and encouraging necessary imaging efficiency.",
     "Fluoroscopy Safety", 2, ["fluoroscopy","5-minute alarm"]),

    # ── Shielding and Equipment ─────────────────────────────────────────────
    ("Primary protective barriers are designed to attenuate:",
     ["The useful (primary) x-ray beam","Scatter and leakage radiation only","Neutron radiation in interventional rooms","Only secondary radiation from scattered photons"],
     "Primary barriers face the useful beam and must attenuate it to safe levels; secondary barriers handle scatter and leakage.",
     "Structural Shielding", 3, ["shielding","primary barrier"]),

    ("Lead glass viewing windows in radiographic control areas must provide radiation protection equivalent to:",
     ["The adjacent primary or secondary barrier","At least 2 mm Pb","Standard glass of equal thickness","The lead apron worn by the radiographer"],
     "The viewing window must meet the same shielding requirements as the barrier in which it is located.",
     "Structural Shielding", 3, ["shielding","control area","viewing window"]),

    ("The radiographer should stand at least how far from the patient during a mobile radiograph if no protective shielding is available?",
     ["6 feet (1.8 m)","3 feet (0.9 m)","10 feet (3 m)","2 feet (0.6 m)"],
     "At 6 feet from the patient, scatter radiation is reduced significantly due to the inverse square law; NCRP recommends this minimum distance.",
     "Radiation Protection", 3, ["mobile radiography","distance","scatter"]),

    ("Which factor causes the GREATEST increase in scatter radiation reaching the image receptor?",
     ["Large field size","High kVp","Long SID","Thick added filtration"],
     "A larger field irradiates more tissue volume, producing significantly more scatter radiation that degrades image quality.",
     "Radiation Physics", 3, ["scatter","field size"]),

    ("Radiation leakage from an x-ray tube housing must NOT exceed:",
     ["1 mGy/hr at 1 meter from the source","10 mGy/hr at 1 meter","0.1 mGy/hr at 0.5 meter","5 mGy/hr at 1 meter"],
     "Federal regulations require x-ray tube housing to limit leakage radiation to no more than 1 mGy/hr (100 mR/hr) measured at 1 meter.",
     "Radiation Protection", 3, ["leakage radiation","tube housing","regulations"]),
]


IMAGE_PRODUCTION = [
    # ── Exposure Factors ────────────────────────────────────────────────────
    ("Increasing kVp while maintaining radiographic density requires:",
     ["Reducing mAs (15% rule)","Increasing mAs proportionally","Doubling the SID","Adding filtration"],
     "The 15% rule: increasing kVp by 15% approximately doubles the effect on density, so mAs must be halved to maintain density.",
     "Exposure Factors", 3, ["kVp","mAs","15% rule"]),

    ("Which exposure change will DOUBLE the radiographic density?",
     ["Doubling the mAs","Increasing kVp by 15%","Halving the SID","Doubling the SID"],
     "Doubling mAs directly doubles the number of photons and therefore the radiographic density on the image.",
     "Exposure Factors", 2, ["mAs","density"]),

    ("A radiograph is underexposed. Which adjustment will MOST increase density without changing contrast?",
     ["Increase mAs","Increase kVp","Decrease SID","Decrease filtration"],
     "Increasing mAs increases photon quantity (density) without significantly altering the beam energy spectrum (contrast).",
     "Exposure Factors", 3, ["mAs","density","contrast"]),

    ("What happens to radiographic contrast when kVp is increased significantly?",
     ["Contrast decreases (longer scale, more gray tones)","Contrast increases (shorter scale, more black and white)","Contrast is unaffected","Contrast only changes if mAs is also altered"],
     "Higher kVp produces more Compton interactions relative to photoelectric, reducing subject contrast and creating a longer gray scale.",
     "Exposure Factors", 3, ["kVp","contrast","scale of contrast"]),

    ("The 'direct square law' for mAs states that when SID changes, mAs must be adjusted proportionally to:",
     ["The square of the SID ratio","The SID ratio","The inverse of the SID","The cube root of the SID ratio"],
     "Direct square law: new mAs = old mAs × (new SID)² / (old SID)². This compensates for the inverse square law effect on intensity.",
     "Exposure Factors", 4, ["direct square law","SID","mAs"]),

    ("A radiograph exposed at 100 cm SID with 20 mAs needs to be repeated at 180 cm SID. The new mAs should be approximately:",
     ["64.8 mAs","7.8 mAs","20 mAs","40 mAs"],
     "New mAs = 20 × (180²/100²) = 20 × 3.24 = 64.8 mAs. The direct square law compensates for decreased intensity at longer SID.",
     "Exposure Factors", 4, ["direct square law","SID","mAs","calculation"]),

    ("Which factor, when increased, will MOST reduce patient dose without significantly degrading image quality?",
     ["kVp (with reciprocal mAs decrease)","mAs (with reciprocal kVp decrease)","Collimation (beam restriction)","Grid ratio"],
     "Increasing kVp with a reciprocal mAs reduction maintains density while reducing patient dose, as fewer low-energy photons are absorbed.",
     "Exposure Factors", 4, ["dose reduction","kVp","mAs","optimization"]),

    ("When using automatic exposure control (AEC), which factor does the radiographer STILL control?",
     ["kVp and backup time","mAs","Exposure time","Number of photons reaching the detector"],
     "With AEC, the system controls mAs to achieve optimal detector exposure; the radiographer sets kVp, backup time, and chooses ionization chambers.",
     "Exposure Factors", 3, ["AEC","automatic exposure control"]),

    ("What is the purpose of the backup timer in AEC systems?",
     ["To terminate the exposure if the AEC fails to reach the preset dose","To set the maximum allowable kVp","To control the density of the image","To limit the minimum exposure time"],
     "The backup timer prevents excessive patient dose if the AEC malfunctions; it must be set to no more than 6× the expected exposure time.",
     "Exposure Factors", 3, ["AEC","backup timer"]),

    ("Which combination of factors BEST characterizes a high-contrast (short-scale) radiograph?",
     ["Low kVp, high mAs, no grid","High kVp, low mAs, grid","Low kVp, low mAs, long SID","High kVp, high mAs, short SID"],
     "Low kVp maximizes photoelectric interactions, producing greater subject contrast (short gray scale with stark black and white differences).",
     "Exposure Factors", 3, ["contrast","kVp","short scale"]),

    ("The optimal kVp range for an AP chest radiograph using a grid is:",
     ["110–125 kVp","60–70 kVp","80–90 kVp","140–150 kVp"],
     "High kVp (110–125) is used for chest radiography to penetrate the mediastinum and lung fields while achieving appropriate gray scale.",
     "Exposure Factors", 3, ["kVp","chest","exposure"]),

    ("The relationship between mA and exposure time in determining mAs is:",
     ["Reciprocal (mA × s = constant mAs)","Additive","Logarithmic","Inversely proportional to kVp"],
     "mAs = mA × time; mA and time are reciprocally related — doubling mA while halving time produces the same mAs.",
     "Exposure Factors", 2, ["mA","mAs","reciprocity"]),

    # ── Image Quality ───────────────────────────────────────────────────────
    ("Spatial resolution in digital radiography is MOST directly determined by:",
     ["Detector element (del) size","kVp","mAs","Grid ratio"],
     "Pixel/del size determines the smallest detail that can be resolved; smaller del size = higher spatial resolution.",
     "Image Quality", 3, ["spatial resolution","del size","digital radiography"]),

    ("Quantum mottle (noise) on a digital radiograph is MOST reduced by:",
     ["Increasing mAs","Increasing kVp","Decreasing SID","Using a higher-ratio grid"],
     "Quantum mottle results from too few photons; increasing mAs increases photon quantity and reduces statistical noise.",
     "Image Quality", 3, ["quantum mottle","noise","mAs"]),

    ("In digital radiography, the exposure indicator (EI) value increases when:",
     ["The detector receives more radiation","The detector receives less radiation","kVp is decreased","The collimation is reduced"],
     "Higher radiation exposure to the digital detector produces a higher exposure indicator value; low EI signals underexposure.",
     "Image Quality", 3, ["exposure indicator","digital","EI"]),

    ("The modulation transfer function (MTF) is a measure of a system's ability to:",
     ["Faithfully reproduce object detail at various spatial frequencies","Reduce quantum noise","Measure radiation dose to the patient","Suppress scatter radiation"],
     "MTF quantifies how well a system reproduces spatial detail across a range of frequencies; higher MTF = better detail reproduction.",
     "Image Quality", 4, ["MTF","spatial resolution","image quality"]),

    ("Detective quantum efficiency (DQE) measures:",
     ["How efficiently a detector converts x-ray signal to image information relative to ideal","Patient dose relative to image quality","Scatter fraction reaching the detector","Spatial resolution at the Nyquist frequency"],
     "DQE describes the fraction of the x-ray signal effectively used by the detector; higher DQE = better image quality at a given dose.",
     "Image Quality", 4, ["DQE","detector efficiency","image quality"]),

    ("Size distortion (magnification) increases when:",
     ["Object-to-image distance (OID) increases or SID decreases","OID decreases and SID increases","SID and OID both increase proportionally","kVp is decreased"],
     "Magnification = SID/SOD; increasing OID (moving object away from detector) or decreasing SID increases magnification.",
     "Image Quality", 3, ["magnification","distortion","OID","SID"]),

    ("Shape distortion occurs due to:",
     ["Misalignment of the central ray, object, or image receptor","Excessive patient dose","Grid cutoff from improper centering","Using too short an SID"],
     "Shape distortion results from angling the central ray, tilting the object, or tilting the receptor — any of which prevents true representation of object shape.",
     "Image Quality", 3, ["shape distortion","central ray","alignment"]),

    ("The penumbra (geometric unsharpness) is MINIMIZED by:",
     ["Using a small focal spot and long SID with short OID","Using a large focal spot and short SID","Increasing mAs","Using high kVp"],
     "Small focal spot + long SID + short OID reduces penumbra; these geometric factors minimize the shadow edge that creates unsharpness.",
     "Image Quality", 3, ["penumbra","focal spot","unsharpness"]),

    ("A grid is used primarily to improve radiographic:",
     ["Contrast by reducing scatter reaching the detector","Density by increasing photon quantity","Spatial resolution by reducing penumbra","Patient dose by filtering low-energy photons"],
     "Grids absorb scatter radiation before it reaches the detector, improving subject contrast.",
     "Image Quality", 2, ["grid","contrast","scatter"]),

    ("Grid cutoff results in:",
     ["Non-uniform density loss across the image","Increased contrast throughout","Uniform density increase","Improved resolution at the edges"],
     "Grid cutoff occurs when primary beam photons are absorbed by grid strips (e.g., off-center, angled beam), producing dark bands or non-uniform density loss.",
     "Image Quality", 3, ["grid","grid cutoff","density"]),

    ("Increasing grid ratio:",
     ["Improves contrast but requires increased exposure","Reduces patient dose","Improves spatial resolution","Decreases the Bucky factor"],
     "Higher grid ratios improve scatter cleanup (contrast) but absorb more primary radiation, requiring increased mAs (higher Bucky factor).",
     "Image Quality", 3, ["grid ratio","contrast","Bucky factor"]),

    ("Focused grids must be used at their rated focal distance because:",
     ["Off-distance use causes grid cutoff at the image periphery","They are more expensive than parallel grids","They provide better scatter reduction at all distances","The grid strips face different directions"],
     "Focused grids have angled strips converging at the rated focal distance; use outside this range causes peripheral cutoff.",
     "Image Quality", 3, ["focused grid","focal distance","cutoff"]),

    ("An upside-down focused grid causes:",
     ["Severe grid cutoff at the image periphery","Uniform grid cutoff across the entire image","Improved contrast in the center only","No significant image change"],
     "An inverted focused grid has strips angling away from the beam at the edges, causing severe peripheral cutoff.",
     "Image Quality", 4, ["focused grid","inverted","cutoff"]),

    ("Dynamic range in digital imaging refers to:",
     ["The range of exposure values a detector can record while maintaining diagnostic quality","The maximum achievable spatial resolution","The speed class of the imaging system","The time required to process an image"],
     "Dynamic range is the ratio of the maximum to minimum signal levels the detector can accurately record; digital systems have wide dynamic range.",
     "Image Quality", 3, ["dynamic range","digital imaging"]),

    # ── Digital Imaging Systems ─────────────────────────────────────────────
    ("In computed radiography (CR), the latent image is stored on:",
     ["A photostimulable phosphor plate (PSP/IP)","A cesium iodide flat-panel detector","A silver halide film","A charge-coupled device (CCD)"],
     "CR uses photostimulable phosphor (usually barium fluorohalide) imaging plates that store latent image energy for later laser readout.",
     "Digital Imaging", 2, ["CR","computed radiography","PSP"]),

    ("In direct digital radiography (DR), x-rays are converted directly to an electrical signal using:",
     ["Amorphous selenium","Cesium iodide with a-Si TFT (indirect)","A photostimulable phosphor","A CCD camera"],
     "Direct conversion DR (e.g., amorphous selenium) directly converts x-rays to electrical charge without an intermediate light step.",
     "Digital Imaging", 4, ["DR","direct digital","amorphous selenium"]),

    ("The key advantage of indirect flat-panel detectors over direct flat-panel detectors is:",
     ["Higher detective quantum efficiency (DQE) at lower dose levels","Direct electrical conversion without light","Better spatial resolution","Lower cost and simpler construction"],
     "Indirect detectors (CsI + a-Si) have higher DQE due to CsI's efficient x-ray-to-light conversion, allowing good image quality at lower doses.",
     "Digital Imaging", 4, ["DR","indirect","DQE","CsI"]),

    ("Post-processing in digital radiography can compensate for:",
     ["Minor exposure errors but cannot fully replace proper technique","Severely underexposed images without increasing noise","Patient motion artifacts","Grid cutoff artifacts"],
     "Digital processing can adjust display brightness and contrast but cannot add signal information absent due to severe underexposure; noise will be amplified.",
     "Digital Imaging", 3, ["post-processing","digital","exposure latitude"]),

    ("Erasure of a CR imaging plate before use is performed to:",
     ["Remove any residual background radiation signal","Increase the sensitivity of the phosphor","Reduce the quantum noise","Calibrate the plate for specific body part thickness"],
     "Residual signal from background or prior exposures on the PSP must be erased with bright light before each use to prevent ghosting artifacts.",
     "Digital Imaging", 3, ["CR","erasure","PSP","artifact"]),

    ("Digital image matrix size and pixel depth PRIMARILY determine:",
     ["Spatial resolution and contrast resolution respectively","Radiation dose to the patient","The speed of image processing","The exposure latitude of the system"],
     "Matrix size (rows × columns of pixels) determines spatial resolution; bit depth determines the number of gray shades (contrast resolution).",
     "Digital Imaging", 3, ["matrix","pixel depth","spatial resolution","contrast resolution"]),

    ("Which artifact in digital radiography appears as a grid-like pattern over the image?",
     ["Moiré artifact","Ghosting artifact","Quantum mottle","Dead pixel artifact"],
     "Moiré pattern occurs when the digital sampling frequency of the CR scanner interacts with the grid frequency, creating a wavering interference pattern.",
     "Digital Imaging", 4, ["Moiré","artifact","CR","grid"]),

    ("In PACS (Picture Archiving and Communication System), DICOM is:",
     ["The standard format for medical image storage and transmission","A type of image compression algorithm","A radiation dose monitoring software","An image post-processing filter"],
     "DICOM (Digital Imaging and Communications in Medicine) is the universal standard for medical imaging data, enabling interoperability between systems.",
     "Digital Imaging", 2, ["PACS","DICOM","digital"]),

    ("The Nyquist frequency determines:",
     ["The maximum spatial frequency that can be accurately sampled by the digital system","The minimum dose required for adequate image quality","The number of gray shades in the image","The speed of image reconstruction"],
     "The Nyquist theorem states the sampling rate must be at least twice the highest spatial frequency to avoid aliasing artifacts.",
     "Digital Imaging", 4, ["Nyquist","spatial frequency","aliasing"]),

    # ── Grids and Scatter ────────────────────────────────────────────────────
    ("A grid is generally recommended when the body part thickness exceeds:",
     ["10 cm","5 cm","15 cm","20 cm"],
     "Grids are recommended when part thickness exceeds approximately 10 cm, as scatter becomes significant enough to degrade contrast.",
     "Image Quality", 2, ["grid","scatter","part thickness"]),

    ("The Bucky factor (grid conversion factor) represents:",
     ["The ratio of mAs needed with a grid to mAs needed without a grid","The ratio of scatter to primary radiation","The number of grid lines per cm","The efficiency of scatter cleanup"],
     "The Bucky factor quantifies the increase in mAs required to compensate for primary radiation absorbed by the grid.",
     "Image Quality", 3, ["Bucky factor","grid","mAs"]),

    ("Which grid type allows the x-ray tube to be used at any tube-to-grid distance without cutoff?",
     ["Parallel (linear) grid","Focused grid","Crossed grid","Rhombic grid"],
     "Parallel grids have straight (non-angled) strips and can be used at any SID, though they cause some peripheral cutoff with large fields.",
     "Image Quality", 3, ["parallel grid","focused grid","distance"]),

    ("Air gap technique reduces scatter by:",
     ["Increasing OID so that scatter photons miss the image receptor","Using a grid to absorb scatter","Reducing the field size to limit scatter production","Increasing kVp to reduce scatter interactions"],
     "Increasing OID creates an air gap; scatter photons traveling at oblique angles miss the detector, improving contrast without a grid.",
     "Image Quality", 4, ["air gap","scatter","OID"]),

    # ── Quality Control ──────────────────────────────────────────────────────
    ("The sensitometric strip (sensitometry) in film-based QC measures:",
     ["The relationship between exposure and optical density (H&D curve)","Spatial resolution of the imaging system","Radiation dose to the patient","Grid alignment and cutoff"],
     "Sensitometry creates an H&D (Hurter & Driffield) curve showing how a film/system responds to varying exposure levels.",
     "Quality Control", 3, ["sensitometry","QC","H&D curve"]),

    ("A densitometer is used in radiographic quality control to measure:",
     ["Optical density of a processed film or digital output","kVp accuracy","Timer accuracy","Grid ratio"],
     "A densitometer measures the degree of light transmission through a processed film, expressed as optical density.",
     "Quality Control", 2, ["densitometry","optical density","QC"]),

    ("Acceptance testing of a new radiographic unit should be performed:",
     ["Before clinical use is begun","After 30 days of clinical use","Only if problems are reported by clinical staff","Once per year by the state inspector"],
     "Acceptance testing establishes baseline performance data and confirms the unit meets specifications before clinical use.",
     "Quality Control", 2, ["acceptance testing","QC"]),

    ("Which QC test verifies that the collimator light field and x-ray field are aligned?",
     ["Field size/beam alignment test","Half-value layer measurement","Focal spot size test","mAs linearity test"],
     "Field size accuracy testing uses a test template to ensure the light field matches the x-ray beam within ±2% of SID.",
     "Quality Control", 3, ["QC","collimator","field alignment"]),

    ("kVp accuracy should be tested at minimum:",
     ["Annually and after repairs","Daily","Monthly","Only at acceptance"],
     "kVp accuracy should be evaluated annually and following any repairs or adjustments that may affect beam quality.",
     "Quality Control", 3, ["QC","kVp accuracy"]),

    ("Reproducibility testing for x-ray output evaluates:",
     ["Consistency of exposure with repeated identical settings","Maximum achievable output at peak kVp","Tube heat capacity and cooling rate","Focal spot size at various kVp levels"],
     "Reproducibility testing verifies the unit produces consistent radiation output when the same exposure factors are repeated.",
     "Quality Control", 3, ["QC","reproducibility","output"]),

    ("In digital radiography QC, the 'flat field' image is used to evaluate:",
     ["Detector uniformity and artifact identification","Spatial resolution","Noise characteristics at low exposure","Patient dose estimation"],
     "Flat field images expose the detector uniformly to reveal non-uniformities, dead pixels, and artifacts across the detector surface.",
     "Quality Control", 4, ["QC","flat field","digital","uniformity"]),

    ("The test tool used to measure spatial resolution in radiography is the:",
     ["Line pair test pattern (resolution test chart)","Penetrameter","Dosimetry phantom","Step wedge"],
     "Line pair per mm (lp/mm) test patterns assess the system's ability to resolve fine detail at various spatial frequencies.",
     "Quality Control", 3, ["QC","spatial resolution","line pair"]),

    ("Collimator shutters that do not close properly present a risk of:",
     ["Unnecessary patient and staff radiation exposure","Poor image contrast","Geometric distortion","Grid cutoff artifacts"],
     "Faulty collimator shutters that do not fully close expose patients and staff to radiation outside the intended field, increasing dose unnecessarily.",
     "Quality Control", 3, ["QC","collimator","radiation protection"]),
]


def build_questions():
    """Assign IDs, randomize option order, assign balanced difficulties."""
    rng = random.Random(99)
    all_q = []
    counters = {"PC": 200, "SF": 200, "IP": 200}  # Start IDs after existing questions

    for source, cat, prefix in [
        (PATIENT_CARE, "Patient Care", "PC"),
        (SAFETY, "Safety", "SF"),
        (IMAGE_PRODUCTION, "Image Production", "IP"),
    ]:
        for i, (stem, opts_list, exp, sub, diff, tags) in enumerate(source):
            # Shuffle option positions (correct is always first in source list)
            positions = ['A', 'B', 'C', 'D']
            shuffled = positions[:]
            rng.shuffle(shuffled)
            mapping = {positions[j]: shuffled[j] for j in range(4)}

            new_opts = {}
            for j, old_letter in enumerate(positions):
                new_opts[shuffled[j]] = opts_list[j]

            correct_ans = [mapping['A']]  # Correct was always index 0

            counters[prefix] += 1
            q_id = f"{prefix}-NEW-{counters[prefix]:03d}"

            all_q.append({
                "id": q_id,
                "cat": cat,
                "sub": sub,
                "diff": diff,
                "type": "single",
                "stem": stem,
                "opts": new_opts,
                "ans": correct_ans,
                "exp": exp,
                "tags": tags,
            })

    return all_q


if __name__ == "__main__":
    new_questions = build_questions()

    # Verify answer distribution
    from collections import Counter
    dist = Counter()
    for q in new_questions:
        dist[q['ans'][0]] += 1

    print(f"Generated {len(new_questions)} new questions")
    print("Answer distribution:")
    for letter in ['A', 'B', 'C', 'D']:
        pct = dist[letter] / len(new_questions) * 100
        print(f"  {letter}: {dist[letter]} ({pct:.1f}%)")

    # Category breakdown
    cats = Counter(q['cat'] for q in new_questions)
    print("Category breakdown:")
    for cat, count in cats.items():
        print(f"  {cat}: {count}")

    # Difficulty breakdown
    diffs = Counter(q['diff'] for q in new_questions)
    print("Difficulty distribution:")
    for d in sorted(diffs.keys()):
        pct = diffs[d] / len(new_questions) * 100
        print(f"  Level {d}: {diffs[d]} ({pct:.1f}%)")

    # Save
    with open('questions_new.json', 'w') as f:
        json.dump(new_questions, f, separators=(',', ':'), indent=None)

    print(f"\nSaved to questions_new.json ({len(open('questions_new.json').read()) // 1024} KB)")
