"""Batch 2: Additional ARRT questions to reach ~500 total new questions."""

import json, random
from collections import Counter

PATIENT_CARE_B2 = [
    ("A patient scheduled for an IVP reports a shellfish allergy. What is the MOST important action?",
     ["Report the allergy to the radiologist before administering contrast","Proceed since shellfish and iodine allergies are unrelated","Substitute barium sulfate for the iodinated contrast","Cancel the examination without contacting the physician"],
     "Although the link between shellfish and iodine allergy is disputed, any prior allergy should be reported to the radiologist for risk assessment and premedication decision.",
     "Contrast Media", 3, ["contrast","allergy","shellfish"]),

    ("Which position is used to evaluate air-fluid levels in the paranasal sinuses?",
     ["Erect (upright)","Supine","Prone","Trendelenburg"],
     "Air-fluid levels only form under gravity and are only visible on upright projections; supine positions cause fluid to pool and levels disappear.",
     "Positioning", 2, ["sinuses","air-fluid level","positioning"]),

    ("A patient's catheter drainage bag is above the level of the bladder during transport. This is problematic because:",
     ["Urine may flow back into the bladder causing infection","The bag may overflow during imaging","Catheter output cannot be measured","The catheter may become kinked"],
     "Gravity drainage is essential; if the bag rises above bladder level, urine refluxes into the bladder, introducing bacteria.",
     "Patient Transfer and Positioning", 3, ["catheter","infection control"]),

    ("When obtaining informed consent, the radiographer's role is to:",
     ["Confirm the patient has signed the consent form and understands the procedure","Explain the detailed risks and benefits of the examination","Obtain the signature if the physician has not done so","Verify the patient's insurance information"],
     "Informed consent is the physician's responsibility; the radiographer confirms consent is documented and the patient's questions have been addressed.",
     "Patient Interactions and Management", 3, ["consent","ethics"]),

    ("Trendelenburg positioning (head lower than feet) is indicated for:",
     ["Hypotensive shock to improve venous return","Respiratory distress requiring lung expansion","Post-procedure nausea to prevent aspiration","Lumbar spine pain during imaging"],
     "Trendelenburg position promotes venous return to the heart, used in hypotension; it is contraindicated in head injury or respiratory distress.",
     "Medical Emergencies", 3, ["Trendelenburg","shock","positioning"]),

    ("Which contrast medium is used for myelography?",
     ["Water-soluble non-ionic iodinated contrast","Barium sulfate","Oil-based iodinated contrast (e.g., Pantopaque)","Gadolinium-based contrast"],
     "Modern myelography uses water-soluble, non-ionic, low-osmolality intrathecal contrast agents that are safe to inject into the subarachnoid space.",
     "Contrast Media", 4, ["myelography","contrast","intrathecal"]),

    ("Which precaution type is used for patients with meningococcal meningitis?",
     ["Droplet precautions","Airborne precautions","Contact precautions","Standard precautions only"],
     "N. meningitidis is transmitted by respiratory droplets; droplet precautions (surgical mask within 6 feet) are required.",
     "Infection Control", 3, ["infection control","droplet","meningitis"]),

    ("A patient with a latex allergy is scheduled for fluoroscopy. The radiographer should:",
     ["Use latex-free gloves and alert all staff involved","Use double gloves to protect the patient","Substitute vinyl gloves for the radiographer only","Document the allergy but proceed with standard equipment"],
     "Latex allergy can cause anaphylaxis; all latex products in the procedure room must be replaced with latex-free alternatives.",
     "Patient Interactions and Management", 3, ["latex allergy","patient safety"]),

    ("What is the FIRST priority when a patient is found unresponsive?",
     ["Ensure scene safety and check responsiveness","Begin chest compressions immediately","Establish IV access","Administer oxygen via non-rebreather mask"],
     "Scene safety and confirming unresponsiveness (tap shoulders, call out) come before any intervention per BLS protocol.",
     "Medical Emergencies", 3, ["emergency","BLS","unresponsive"]),

    ("A patient's systolic blood pressure is 185 mmHg before a contrast study. The radiographer should:",
     ["Notify the radiologist before administering contrast","Proceed since hypertension does not affect contrast safety","Administer antihypertensive medication per protocol","Cancel the examination"],
     "Severely elevated blood pressure increases the risk of contrast-related complications; the radiologist should be notified before proceeding.",
     "Vital Signs and Monitoring", 3, ["blood pressure","contrast","hypertension"]),

    ("Which approach BEST minimizes radiation dose to pediatric patients?",
     ["Optimize technique for smaller body habitus and eliminate unnecessary repeats","Use adult protocols at reduced mAs","Use high kVp and low mAs for all projections","Always use a grid to improve contrast"],
     "Pediatric patients require customized technique (smaller field, lower dose) and meticulous positioning to avoid repeats.",
     "Patient Interactions and Management", 3, ["pediatric","dose reduction","technique"]),

    ("A combative patient needs a portable chest X-ray. Who should restrain the patient during the exposure?",
     ["A nurse or family member using appropriate shielding","The radiographer while wearing a lead apron","Another radiographer positioned outside the beam","No one; proceed with the patient unrestrained"],
     "Non-radiology personnel (nurse, family) who must be in the room during exposure should be shielded; radiographers must not remain in the beam.",
     "Radiation Protection", 3, ["radiation protection","portable","restraint"]),

    ("Which position is used to demonstrate free air under the diaphragm?",
     ["Erect PA chest or left lateral decubitus abdomen","Supine AP abdomen","Prone abdomen","Right lateral decubitus abdomen"],
     "Free intraperitoneal air rises; an upright chest or left lateral decubitus (right side up) allows air to collect under the diaphragm or liver.",
     "Positioning", 3, ["free air","diaphragm","decubitus","positioning"]),

    ("What does 'scope of practice' mean for a radiographer?",
     ["The legal and professional limits of what a radiographer may perform","The number of patients a radiographer can see per day","The equipment a radiographer is permitted to purchase","The geographic area in which a radiographer may work"],
     "Scope of practice defines the procedures, actions, and processes that a radiographer is legally permitted to perform based on education and licensure.",
     "Patient Interactions and Management", 2, ["scope of practice","ethics"]),

    ("Which patient condition requires special attention to gonadal shielding during lumbar spine radiography?",
     ["A woman of reproductive age undergoing an AP lumbar spine","An elderly male with known prostate cancer","A teenage boy with scoliosis requiring spine survey","Any patient over 50 years old"],
     "Women of reproductive age have radiosensitive ovaries near the lumbar spine field; contact shielding is important though it may not fully shield ovaries.",
     "Radiation Protection", 3, ["gonadal shielding","lumbar spine","reproductive"]),

    ("When a patient is positioned for an AP pelvis, the correct tube centering point is:",
     ["2 inches (5 cm) superior to the symphysis pubis","At the level of the iliac crest","At the level of the ASIS","At the level of the greater trochanter"],
     "The AP pelvis CR is directed to midpoint of the pelvis, approximately 2 inches (5 cm) above the symphysis pubis at midsagittal plane.",
     "Positioning", 2, ["pelvis","positioning","CR"]),

    ("The most common side effect of oral barium sulfate is:",
     ["Constipation","Diarrhea","Nausea and vomiting","Abdominal cramping"],
     "Barium sulfate draws water from the colon, commonly causing constipation; patients should be instructed to increase fluid and fiber intake.",
     "Contrast Media", 2, ["barium","GI","side effects"]),

    ("After administering IV contrast, the patient should be observed for a minimum of:",
     ["30 minutes for delayed reactions","5 minutes","1 hour","2 hours only for high-risk patients"],
     "Most adverse contrast reactions occur within 30 minutes; patients should be observed for this period following IV contrast administration.",
     "Contrast Media", 3, ["contrast","observation","reaction"]),

    ("Which term describes the ethical principle of 'doing good' for the patient?",
     ["Beneficence","Nonmaleficence","Autonomy","Justice"],
     "Beneficence means acting in the patient's best interest; nonmaleficence means 'do no harm'; autonomy respects patient decisions; justice ensures fair treatment.",
     "Patient Interactions and Management", 2, ["ethics","beneficence"]),

    ("A suicidal patient expresses intent to harm themselves while in the imaging department. The radiographer should:",
     ["Stay with the patient, activate emergency response, and notify the charge nurse immediately","Complete the imaging examination quickly and document the statement afterward","Ask the patient not to discuss personal issues during the examination","Refer the patient back to their ward without further action"],
     "Patient safety is the priority; the radiographer must not leave the patient alone and must immediately involve clinical staff.",
     "Patient Interactions and Management", 4, ["mental health","patient safety","emergency"]),

    ("The role of the radiographer during a code blue is PRIMARILY to:",
     ["Assist as trained while notifying the code team and supporting clinical staff","Lead resuscitation efforts until the physician arrives","Continue imaging other patients to clear the department","Document the event without participating"],
     "Radiographers support the code team using their BLS training while alerting the appropriate clinical responders.",
     "Medical Emergencies", 3, ["code blue","BLS","emergency"]),

    ("A patient reports worsening shortness of breath after a thoracentesis. The MOST likely complication is:",
     ["Pneumothorax","Hemorrhage into the pleural space","Infection at the puncture site","Vasovagal reaction"],
     "Pneumothorax is a common complication of thoracentesis; sudden dyspnea after the procedure warrants immediate chest imaging.",
     "Medical Emergencies", 4, ["thoracentesis","pneumothorax","emergency"]),

    ("During a barium swallow, an adult patient begins to aspirate barium. The radiographer should FIRST:",
     ["Stop the infusion and alert the radiologist immediately","Continue the examination at a lower flow rate","Ask the patient to cough to clear the airway","Position the patient prone to drain the airway"],
     "Barium aspiration is a serious complication; stopping the study and immediate radiologist notification allows clinical assessment.",
     "Medical Emergencies", 4, ["barium","aspiration","GI","emergency"]),

    ("Which professional organization issues voluntary national certification for radiographers in the United States?",
     ["ARRT (American Registry of Radiologic Technologists)","ASRT (American Society of Radiologic Technologists)","ACR (American College of Radiology)","JRCERT (Joint Review Committee on Education in Radiologic Technology)"],
     "The ARRT administers national certification examinations and maintains credentialing standards for radiographers.",
     "Patient Interactions and Management", 2, ["ARRT","certification","professional"]),

    ("A patient's oxygen saturation drops from 98% to 88% during a procedure. The FIRST action is:",
     ["Apply supplemental oxygen and notify the nurse or physician","Continue the procedure and recheck in 5 minutes","Increase the room's ventilation","Document the finding and reassess at the end of the procedure"],
     "SpO₂ of 88% indicates significant hypoxemia; supplemental oxygen and immediate clinical notification are required.",
     "Vital Signs and Monitoring", 3, ["oxygen saturation","hypoxemia","emergency"]),

    ("What is the MOST important consideration before performing a portable radiograph in the ICU?",
     ["Verifying IV lines, tubes, and monitoring equipment are not displaced during imaging","Ensuring the room temperature is appropriate","Confirming the patient's insurance authorization","Checking that the portable unit battery is fully charged"],
     "Critically ill ICU patients have multiple lines and tubes; accidental displacement during positioning can be life-threatening.",
     "Patient Transfer and Positioning", 4, ["ICU","portable","patient safety"]),
]


SAFETY_B2 = [
    ("Which radiation weighting factor (Wr) is assigned to x-rays and gamma rays?",
     ["1","2","10","20"],
     "X-rays and gamma rays have a radiation weighting factor of 1; alpha particles have Wr=20, protons Wr=2, neutrons Wr=2–20.",
     "Radiation Physics", 2, ["weighting factor","Wr","x-rays"]),

    ("The tissue with the HIGHEST tissue weighting factor (Wt) for effective dose calculation is:",
     ["Bone marrow (red)","Lung","Skin","Bone surface"],
     "Red bone marrow has a tissue weighting factor of 0.12, one of the highest, reflecting its high radiosensitivity.",
     "Radiation Physics", 4, ["tissue weighting factor","Wt","effective dose"]),

    ("Coherent (Rayleigh) scatter occurs primarily at:",
     ["Very low photon energies (<10 keV)","Diagnostic imaging energies (60–120 kVp)","High energies above 1 MeV","Mammography energies (15–30 kVp)"],
     "Coherent scatter occurs at very low photon energies; the photon interacts with the whole atom and is redirected without energy loss.",
     "Radiation Physics", 4, ["coherent scatter","Rayleigh","interaction"]),

    ("Pair production occurs when:",
     ["A photon with energy >1.022 MeV interacts near a nucleus","A photon ejects an inner-shell electron","A photon loses energy and changes direction","A photon is completely absorbed by an outer-shell electron"],
     "Pair production requires >1.022 MeV (the rest mass energy of two electrons); it produces an electron-positron pair and does not occur at diagnostic energies.",
     "Radiation Physics", 4, ["pair production","threshold","interaction"]),

    ("The energy of characteristic radiation from a tungsten anode depends on:",
     ["The binding energy of the electron shells of tungsten","The applied kVp","The mAs setting","The filtration in the beam"],
     "Characteristic radiation energy is determined by the difference in binding energies between shells of the target material (tungsten), not the applied kVp.",
     "Radiation Physics", 4, ["characteristic radiation","binding energy","tungsten"]),

    ("What happens to beam intensity when SID is increased from 100 cm to 200 cm?",
     ["Intensity decreases to 1/4 of original","Intensity decreases to 1/2 of original","Intensity doubles","Intensity decreases to 1/8 of original"],
     "By the inverse square law: (100/200)² = 1/4. Doubling SID reduces intensity to one-quarter.",
     "Radiation Physics", 2, ["inverse square law","intensity","SID"]),

    ("Which type of personnel dosimeter measures dose using thermoluminescent crystals?",
     ["TLD (thermoluminescent dosimeter)","OSL (optically stimulated luminescence) dosimeter","Film badge","Pocket ionization chamber"],
     "TLDs use crystals (e.g., lithium fluoride) that store energy from radiation; heating releases the stored energy as light, which is measured.",
     "Radiation Protection", 3, ["TLD","dosimetry","personnel monitoring"]),

    ("The critical organ for radiation-induced leukemia is the:",
     ["Red bone marrow","Thyroid gland","Gonads","Skin"],
     "Red bone marrow contains the hematopoietic stem cells whose damage leads to radiation-induced leukemia.",
     "Radiation Biology", 3, ["leukemia","bone marrow","radiation biology"]),

    ("Genetic effects of radiation are those that:",
     ["Affect future generations through gonadal irradiation","Occur only in the irradiated individual","Are immediately apparent after high doses","Cause chromosomal abnormalities only in somatic cells"],
     "Genetic (hereditary) effects result from radiation-induced mutations in germ cells (sperm or ova) that may be passed to offspring.",
     "Radiation Biology", 3, ["genetic effects","hereditary","radiation biology"]),

    ("The most radiosensitive phase of the cell cycle is:",
     ["Late G2 and mitosis (M phase)","S phase (DNA synthesis)","G1 phase","G0 (resting phase)"],
     "Cells in late G2 and mitosis have condensed chromosomes and no ability to repair radiation damage before division, making them most radiosensitive.",
     "Radiation Biology", 4, ["cell cycle","radiosensitivity","mitosis"]),

    ("Which of the following is a deterministic (non-stochastic) effect of radiation?",
     ["Radiation-induced skin erythema (reddening)","Radiation-induced leukemia","Genetic mutation in future generations","Radiation-induced thyroid cancer"],
     "Skin erythema occurs above a threshold dose and severity increases with dose — classic deterministic effect. Cancers and genetic effects are stochastic.",
     "Radiation Biology", 3, ["deterministic","erythema","threshold"]),

    ("The process by which cells repair sublethal radiation damage between fractionated doses is called:",
     ["Repair of sublethal damage (SLD repair)","Repopulation","Redistribution","Reoxygenation"],
     "The '4 Rs of radiobiology' include repair of SLD, repopulation, redistribution in cell cycle, and reoxygenation — all relevant in fractionated therapy.",
     "Radiation Biology", 4, ["4 Rs","radiobiology","repair"]),

    ("Radiation-induced hypothyroidism most commonly results from:",
     ["External beam radiation to the neck/head region","Occupational exposure to x-rays","Ingestion of radioactive iodine in contaminated water","Scatter from abdominal CT scans"],
     "Thyroid gland irradiation from external beam radiation (e.g., for Hodgkin's lymphoma) can cause hypothyroidism; it is also dose-related.",
     "Radiation Biology", 4, ["thyroid","hypothyroidism","radiation biology"]),

    ("The MOST effective time to shield the embryo/fetus from radiation effects is:",
     ["Throughout the entire pregnancy, especially the first trimester","Only in the third trimester when the fetus is largest","Before the pregnancy is confirmed","Only during fluoroscopic procedures"],
     "The first trimester is the most critical period of organogenesis; however, radiation protection should be maintained throughout pregnancy.",
     "Radiation Protection", 3, ["pregnancy","embryo","first trimester"]),

    ("Lead apparel (aprons) should be inspected fluoroscopically for cracks at least:",
     ["Annually","Monthly","Weekly","Only when damage is suspected"],
     "Lead aprons should be inspected for cracks and holes at least annually by fluoroscopy or radiography to ensure shielding integrity.",
     "Radiation Protection", 2, ["lead apron","inspection","QC"]),

    ("The NCRP recommends that personnel dosimeters be worn at:",
     ["Collar level outside the lead apron during fluoroscopy","Waist level under the apron","The dominant hand","Chest level under clothing"],
     "The collar dosimeter outside the apron at neck level provides the best estimate of effective dose; a second badge under the apron may be used for more accurate whole-body estimation.",
     "Radiation Protection", 3, ["dosimeter","placement","fluoroscopy"]),

    ("The annual effective dose limit for members of the general public from occupational sources is:",
     ["1 mSv (0.1 rem)","5 mSv (0.5 rem)","50 mSv (5 rem)","0.1 mSv (0.01 rem)"],
     "NCRP recommends the annual dose limit for the public from occupational sources (e.g., radiation workers' neighbors) is 1 mSv.",
     "Radiation Protection", 3, ["dose limit","public","occupational"]),

    ("A cumulative lifetime dose limit recommendation for occupationally exposed workers is:",
     ["10 mSv × age (in years)","50 mSv per year without limit","500 mSv total career dose","100 mSv total career dose"],
     "NCRP recommends a cumulative lifetime limit of 10 mSv × age in years to limit long-term stochastic risk.",
     "Radiation Protection", 4, ["lifetime dose","cumulative","occupational"]),

    ("Thermoluminescent dosimeters (TLDs) have advantages over film badges because they:",
     ["Are reusable, have wider dynamic range, and are not affected by heat or humidity","Provide real-time dose readout","Are less expensive to manufacture","Require no processing equipment"],
     "TLDs are reusable, provide better sensitivity and dynamic range, and are not affected by humidity or temperature that can fog film badges.",
     "Radiation Protection", 3, ["TLD","film badge","dosimetry"]),

    ("Which principle guides the design of radiation shielding for occupied areas?",
     ["ALARA combined with occupancy and workload factors","Maximum dose to the wall at any position","Minimum shielding required by building codes","Equal shielding for all walls regardless of direction"],
     "Shielding design uses workload, use factor, occupancy factor, and ALARA to determine the minimum shielding needed to protect occupants.",
     "Structural Shielding", 4, ["shielding design","occupancy factor","ALARA"]),

    ("During a mobile radiograph, the radiographer should direct the beam:",
     ["Away from occupied areas and personnel","Toward the ceiling to reduce floor scatter","At right angles to the nearest wall","Downward at all times to reduce scatter"],
     "The primary beam should be directed away from staff and occupied areas; personnel should stand at 90° to the beam and at maximum distance.",
     "Radiation Protection", 3, ["mobile radiography","beam direction","protection"]),

    ("Photostimulable phosphor plates used in CR should be protected from:",
     ["Background radiation and light exposure before processing","Excessive mAs during exposure","High humidity during imaging","Temperature fluctuations during storage"],
     "PSP plates are sensitive to background radiation and ambient light; accidental exposure causes fogging that degrades image quality.",
     "Digital Imaging", 3, ["CR","PSP","storage","artifact"]),

    ("The effective dose from a posteroanterior (PA) chest X-ray is approximately:",
     ["0.02 mSv (2 mrem)","2 mSv (200 mrem)","0.2 mSv (20 mrem)","20 mSv (2000 mrem)"],
     "A PA chest X-ray delivers approximately 0.02 mSv (20 µSv), comparable to about 2.4 days of background radiation.",
     "Radiation Protection", 3, ["effective dose","chest","dose estimation"]),

    ("Which factor most significantly increases the amount of scatter radiation produced?",
     ["Increasing the field size","Increasing the SID","Decreasing kVp below 60","Using a high-ratio grid"],
     "Larger field sizes irradiate more tissue, producing more Compton scatter interactions that degrade image quality.",
     "Radiation Physics", 3, ["scatter","field size","Compton"]),

    ("Radiation-induced cataracts have a threshold dose of approximately:",
     ["0.5–2 Gy (50–200 rad) for chronic exposure","0.05 Gy","10 Gy","50 Gy"],
     "The ICRP updated the threshold for radiation-induced cataracts to approximately 0.5 Gy for acute exposure and 0.5–2 Gy for chronic exposure.",
     "Radiation Biology", 4, ["cataract","threshold","lens"]),
]


IMAGE_PRODUCTION_B2 = [
    ("A radiograph appears too dark (overexposed) with acceptable contrast. The MOST appropriate correction is:",
     ["Decrease mAs","Decrease kVp","Increase SID","Use a lower-ratio grid"],
     "Overexposure is best corrected by reducing mAs, which reduces photon quantity without altering beam quality (contrast).",
     "Exposure Factors", 2, ["overexposure","mAs","density"]),

    ("A radiograph appears too light (underexposed) with low contrast. The MOST appropriate correction is:",
     ["Increase kVp and mAs together","Increase mAs only","Increase kVp only","Decrease SID"],
     "Insufficient density and low contrast together suggest both photon quantity and quality need improvement; increasing both kVp and mAs addresses this.",
     "Exposure Factors", 3, ["underexposure","density","contrast"]),

    ("The standard SID for most tabletop radiographic procedures is:",
     ["100 cm (40 inches)","150 cm (60 inches)","180 cm (72 inches)","75 cm (30 inches)"],
     "The standard SID for tabletop radiography is 100 cm (40 inches), balancing magnification and beam intensity.",
     "Exposure Factors", 2, ["SID","standard distance"]),

    ("Standard SID for upright chest radiography is:",
     ["180 cm (72 inches)","100 cm (40 inches)","150 cm (60 inches)","120 cm (48 inches)"],
     "Upright chest radiography uses 180 cm (72-inch) SID to reduce magnification of the heart and mediastinum.",
     "Exposure Factors", 2, ["SID","chest","upright"]),

    ("Recorded detail (sharpness) is MOST affected by which factor?",
     ["Focal spot size","kVp","mAs","Grid ratio"],
     "Focal spot size determines geometric unsharpness (penumbra); a smaller focal spot produces sharper recorded detail.",
     "Image Quality", 3, ["recorded detail","focal spot","sharpness"]),

    ("An x-ray image shows elongation of a structure. This indicates:",
     ["The central ray was angled away from the part or the part was tilted toward the tube","The OID was excessive","The SID was too short","The focal spot was too large"],
     "Elongation distortion occurs when the central ray is angled away from the object (CR angled toward foot) or the object is tilted toward the tube.",
     "Image Quality", 3, ["elongation","distortion","central ray"]),

    ("Foreshortening of a structure on a radiograph is caused by:",
     ["Excessive part-to-receptor angulation or CR angled toward the part","Using too long an SID","Excessive OID","Using too small a focal spot"],
     "Foreshortening occurs when the part is tilted away from the receptor or the CR is angled toward the part, compressing the image.",
     "Image Quality", 3, ["foreshortening","distortion","CR"]),

    ("Which term describes the range of exposures over which a film or digital detector produces a diagnostic image?",
     ["Exposure latitude","Dynamic range","Optical density","Sensitometric range"],
     "Exposure latitude defines the range of acceptable exposure values; digital systems have much wider latitude than film.",
     "Image Quality", 3, ["exposure latitude","digital","film"]),

    ("Motion unsharpness is BEST reduced by:",
     ["Minimizing exposure time and using proper immobilization","Increasing mAs to permit shorter time","Using a large focal spot","Decreasing SID"],
     "Short exposure time freezes motion; immobilization prevents motion. These two strategies together minimize motion unsharpness.",
     "Image Quality", 3, ["motion","unsharpness","exposure time"]),

    ("Which radiographic artifact appears as a crescent-shaped mark on film caused by bending the film prior to exposure?",
     ["Crinkle (crescent) artifact","Pi line artifact","Moiré pattern","Quantum mottle"],
     "Crinkle artifacts (also called crescent or half-moon artifacts) result from rough handling and bending of film before or after processing.",
     "Image Quality", 3, ["artifact","crinkle","film"]),

    ("The sensitometric step on the H&D curve where maximum contrast is achieved is called the:",
     ["Shoulder and straight-line portion","Toe","Base plus fog level","Speed point"],
     "Maximum contrast is achieved in the straight-line (linear) portion of the H&D curve; the toe and shoulder are regions of reduced contrast.",
     "Quality Control", 4, ["H&D curve","sensitometry","contrast"]),

    ("In digital radiography, increased image noise is MOST associated with:",
     ["Insufficient radiation reaching the detector (low mAs)","Excessive radiation reaching the detector","High kVp with low mAs","Using a high-ratio grid"],
     "Digital noise (quantum mottle) results from insufficient photon count; the detector doesn't receive enough signal to accurately reproduce anatomy.",
     "Image Quality", 3, ["noise","quantum mottle","digital"]),

    ("What does a high spatial frequency in an MTF test pattern represent?",
     ["Fine detail (small structures close together)","Large structures far apart","Low-contrast objects","High-density materials"],
     "High spatial frequency means many line pairs per millimeter; the ability to resolve high frequencies indicates the system can depict fine detail.",
     "Image Quality", 4, ["MTF","spatial frequency","resolution"]),

    ("The heel effect of the x-ray beam is utilized clinically by:",
     ["Placing the thicker part of the anatomy toward the cathode end","Placing the thicker part toward the anode end","Centering the anatomy in the middle of the beam","Rotating the tube to equalize beam intensity"],
     "The cathode side of the beam is more intense; placing the thicker anatomy cathode-side (e.g., femur toward cathode for femur radiograph) provides more uniform exposure.",
     "Exposure Factors", 3, ["heel effect","cathode","anode","positioning"]),

    ("Which factor does NOT affect magnification of the radiographic image?",
     ["mAs","SID","OID","Focal spot size"],
     "Magnification = SID/SOD; only geometry (SID, OID) affects magnification. mAs affects density and focal spot affects sharpness, not magnification.",
     "Image Quality", 3, ["magnification","SID","OID"]),

    ("Spatial resolution is expressed in units of:",
     ["Line pairs per millimeter (lp/mm)","Gray levels","Lumens per square centimeter","Hounsfield units"],
     "Spatial resolution describes the ability to resolve fine detail and is measured in line pairs per millimeter (lp/mm).",
     "Image Quality", 2, ["spatial resolution","lp/mm"]),

    ("Which detector type provides the HIGHEST spatial resolution in digital radiography?",
     ["Computed radiography (CR) with fine-grained phosphor plates","Large-area flat-panel detector (FPD)","Image intensifier-based system","Indirect FPD with CsI"],
     "CR with fine-grained phosphor and small laser scanning spot can achieve high spatial resolution; however, modern direct FPDs with small del size now rival CR resolution.",
     "Digital Imaging", 4, ["spatial resolution","CR","digital"]),

    ("In CR, quantum noise is MOST reduced by:",
     ["Increasing mAs to improve the signal-to-noise ratio","Using a finer laser scanning spot","Using a high-frequency grid","Decreasing the phosphor plate thickness"],
     "Higher mAs increases the number of photons reaching the PSP, improving SNR and reducing quantum (statistical) noise.",
     "Digital Imaging", 3, ["CR","noise","mAs"]),

    ("Windowing (window width and window level) in digital radiography affects:",
     ["The display contrast and brightness of the image","The spatial resolution of the image","The radiation dose to the patient","The amount of scatter in the image"],
     "Window width controls display contrast (gray scale) and window level controls display brightness; neither affects the underlying acquired data.",
     "Digital Imaging", 2, ["windowing","window width","window level","contrast"]),

    ("The term 'histogram analysis' in digital radiography refers to:",
     ["The distribution of pixel values in a digital image used to optimize display","Measurement of optical density on film","The frequency of patient repeats","The distribution of radiation dose across the detector"],
     "The histogram shows pixel value distribution; software uses it to auto-adjust window width/level and identify over- or underexposure.",
     "Digital Imaging", 3, ["histogram","digital","display"]),

    ("An artifact appearing as a grid-like pattern when a stationary grid is used with CR is caused by:",
     ["Aliasing between grid frequency and CR scanner sampling frequency (Moiré effect)","Grid cutoff from incorrect tube alignment","Overexposure of the PSP plate","Insufficient grid ratio"],
     "Moiré artifacts occur in CR when the grid line frequency and laser scan frequency alias; using an oscillating Bucky or removing the grid prevents this.",
     "Digital Imaging", 4, ["Moiré","CR","grid","artifact"]),

    ("The most important method for reducing repeat radiographs in a digital department is:",
     ["Proper positioning and optimal technique selection before exposure","Post-processing adjustments after exposure","Using the highest possible mAs","Repeating all questionable images for quality assurance"],
     "Good positioning and appropriate technique selection before exposure minimize the need for repeats; digital processing cannot compensate for poor positioning.",
     "Quality Control", 3, ["repeat rate","positioning","technique"]),

    ("Which quality control test evaluates whether the x-ray tube produces consistent output for repeated identical exposures?",
     ["Reproducibility test","Linearity test","HVL measurement","kVp accuracy test"],
     "Reproducibility tests confirm that the same settings produce consistent output (<5% variation) across multiple exposures.",
     "Quality Control", 3, ["reproducibility","QC","output"]),

    ("mAs linearity testing verifies that:",
     ["Changing mAs in direct proportion produces a proportional change in radiation output","kVp and mAs are inversely related","Exposure time and kVp are linearly related","The AEC terminates exposure at the correct dose"],
     "Linearity testing ensures that doubling mAs doubles output (within ±10%), confirming the generator produces predictable, calibrated output.",
     "Quality Control", 3, ["mAs linearity","QC","output"]),

    ("A radiograph of the lumbar spine appears with a large area of unexposed (white) film on the left side. The MOST likely cause is:",
     ["The patient or part was not centered to the field","The grid was off-center causing cutoff","Overexposure on the right side","A faulty collimator shutter on the left"],
     "Non-centered patient positioning relative to the collimated field leaves unexposed film on one side, appearing white on the processed image.",
     "Image Quality", 3, ["centering","positioning","artifact"]),

    ("Bit depth in a digital imaging system determines:",
     ["The number of gray levels that can be displayed (contrast resolution)","The matrix size (spatial resolution)","The radiation dose required","The image acquisition speed"],
     "Bit depth (e.g., 12-bit = 4096 gray levels) determines contrast resolution — the ability to distinguish subtle density differences.",
     "Digital Imaging", 3, ["bit depth","contrast resolution","gray levels"]),

    ("Which x-ray projection demonstrates the carpal tunnel?",
     ["Tangential (inferosuperior) carpal tunnel projection","PA wrist projection","Lateral wrist projection","Oblique wrist projection"],
     "The tangential carpal tunnel (Gaynor-Hart) projection directs the beam through the carpal tunnel to demonstrate bony walls and the carpal bones.",
     "Positioning", 3, ["carpal tunnel","wrist","positioning"]),

    ("For an AP knee, the standard SID and CR placement is:",
     ["100 cm SID, CR to the knee joint (1 cm below patellar apex)","180 cm SID, CR to mid-patella","100 cm SID, CR to mid-patella","100 cm SID, CR to the tibial tuberosity"],
     "AP knee: 100 cm SID with CR directed to the knee joint at 1 cm below the patellar apex, angled 5–7° cephalad.",
     "Positioning", 3, ["knee","AP","SID","CR"]),

    ("Which projection of the chest is BEST for demonstrating the left lateral lung and pleural effusion on the left?",
     ["Left lateral projection","PA projection","Right lateral projection","AP projection"],
     "In a left lateral projection, the left lung is closest to the receptor, reducing magnification and providing the best detail of left-sided pathology.",
     "Positioning", 3, ["chest","lateral","pleural effusion"]),

    ("Which projection BEST demonstrates the zygapophyseal (facet) joints of the lumbar spine?",
     ["45-degree oblique lumbar spine projection","Lateral lumbar spine projection","AP lumbar spine projection","Lateral flexion/extension projection"],
     "Oblique lumbar spine projections at 45 degrees place the zygapophyseal joints perpendicular to the beam, clearly demonstrating them.",
     "Positioning", 3, ["lumbar spine","oblique","facet joints"]),

    ("The AP axial projection of the pelvis with 15–20° cephalad tube angle is used to demonstrate:",
     ["The pubic rami (inlet pelvis/AP axial outlet)","The sacroiliac joints","The femoral neck without overlap","The acetabular columns"],
     "The AP axial outlet (Taylor method) angled cephalad demonstrates the superior and inferior pubic rami free of superimposition.",
     "Positioning", 3, ["pelvis","pubic rami","AP axial","positioning"]),

    ("A Waters projection (PA axial) of the paranasal sinuses is used primarily to demonstrate:",
     ["The maxillary sinuses","The frontal sinuses","The ethmoid sinuses","The sphenoid sinus"],
     "The Waters projection angles the OML 37° from perpendicular, projecting the petrous ridges below the maxillary sinus floors for optimal maxillary sinus demonstration.",
     "Positioning", 2, ["Waters","sinus","maxillary","positioning"]),
]


def build_batch2():
    rng = random.Random(77)
    all_q = []
    counters = {"PC": 350, "SF": 350, "IP": 350}

    for source, cat, prefix in [
        (PATIENT_CARE_B2, "Patient Care", "PC"),
        (SAFETY_B2, "Safety", "SF"),
        (IMAGE_PRODUCTION_B2, "Image Production", "IP"),
    ]:
        for stem, opts_list, exp, sub, diff, tags in source:
            positions = ['A', 'B', 'C', 'D']
            shuffled = positions[:]
            rng.shuffle(shuffled)
            mapping = {positions[j]: shuffled[j] for j in range(4)}
            new_opts = {shuffled[j]: opts_list[j] for j in range(4)}
            correct_ans = [mapping['A']]

            counters[prefix] += 1
            q_id = f"{prefix}-NEW-{counters[prefix]:03d}"

            all_q.append({
                "id": q_id, "cat": cat, "sub": sub, "diff": diff,
                "type": "single", "stem": stem, "opts": new_opts,
                "ans": correct_ans, "exp": exp, "tags": tags,
            })

    return all_q


if __name__ == "__main__":
    batch2 = build_batch2()

    dist = Counter(q['ans'][0] for q in batch2)
    print(f"Batch 2: {len(batch2)} questions")
    print("Answer distribution:")
    for l in ['A','B','C','D']:
        print(f"  {l}: {dist[l]} ({dist[l]/len(batch2)*100:.1f}%)")

    cats = Counter(q['cat'] for q in batch2)
    print("Categories:", dict(cats))

    diffs = Counter(q['diff'] for q in batch2)
    print("Difficulty:", {k: diffs[k] for k in sorted(diffs)})

    # Merge with batch 1
    with open('questions_new.json') as f:
        batch1 = json.load(f)

    all_new = batch1 + batch2
    print(f"\nTotal new questions: {len(all_new)}")

    # Merge with existing cleaned bank
    with open('questions_cleaned.json') as f:
        existing = json.load(f)

    combined = existing + all_new
    print(f"Combined with existing: {len(combined)} total questions")

    # Final distribution check
    final_dist = Counter(q['ans'][0] for q in combined)
    print("\nFinal answer distribution:")
    for l in ['A','B','C','D']:
        print(f"  {l}: {final_dist[l]} ({final_dist[l]/len(combined)*100:.1f}%)")

    final_cats = Counter(q['cat'] for q in combined)
    print("Final categories:", dict(final_cats))

    # Save combined
    with open('questions.json', 'w') as f:
        json.dump(combined, f, separators=(',', ':'))
    print(f"\nSaved to questions.json ({len(open('questions.json').read()) // 1024} KB)")
