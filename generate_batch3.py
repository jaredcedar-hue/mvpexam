"""
Batch 3: ~60 Procedures + ~60 Patient Care questions.
Correct answer always first in list; positions randomized at end.
"""
import json, random
from collections import Counter

PROCEDURES = [
    # ── Chest & Thorax ──────────────────────────────────────────────────────
    ("For a PA chest radiograph, the patient should be instructed to suspend respiration at:",
     ["Full inspiration (second deep breath)","Normal expiration","Full expiration","Any point during normal breathing"],
     "Full inspiration depresses the diaphragm, expands lung fields, and separates thoracic structures for maximum diagnostic information.",
     "Thoracic Imaging", 2, ["chest","inspiration","breathing"]),

    ("Which projection of the chest is ordered to rule out a small pneumothorax not visible on the PA projection?",
     ["PA chest on expiration","Lateral decubitus","AP lordotic","Lateral chest"],
     "On expiration the lungs are smaller, making a small pneumothorax relatively larger and easier to detect against the lung margin.",
     "Thoracic Imaging", 3, ["pneumothorax","expiration","chest"]),

    ("The AP lordotic projection of the chest demonstrates the:",
     ["Lung apices free of clavicular superimposition","Right middle lobe and lingula","Costophrenic angles","Retrocardiac area"],
     "The AP lordotic projection angles the beam or tilts the patient to project the clavicles above the lung apices, showing the apices clearly.",
     "Thoracic Imaging", 3, ["lordotic","apices","chest"]),

    ("For a lateral chest radiograph, the patient's arms should be:",
     ["Raised above the head to avoid superimposition over the lungs","Crossed over the abdomen","Extended forward at shoulder height","Placed on the hips"],
     "Raising the arms removes soft tissue and muscle from the chest field, preventing superimposition over posterior lung tissue.",
     "Thoracic Imaging", 2, ["lateral chest","arm position"]),

    ("On a PA chest radiograph, the carina should be visualized at approximately the level of:",
     ["T4–T5 (sternal angle of Louis)","T1–T2","T8–T9","L1"],
     "The carina (tracheal bifurcation) lies at the level of T4–T5, corresponding to the sternal angle, a key landmark on chest radiographs.",
     "Thoracic Imaging", 3, ["carina","chest","anatomy","T4"]),

    ("The lateral decubitus chest projection is performed with the patient lying on their side and the beam directed:",
     ["Horizontal (cross-table)","Vertical (overhead)","Angled 15° cephalad","Angled 15° caudad"],
     "A horizontal beam is essential for the decubitus projection; it demonstrates air-fluid levels and free pleural fluid pooling dependently.",
     "Thoracic Imaging", 3, ["decubitus","horizontal beam","pleural effusion"]),

    ("Which ribs are best demonstrated on an AP projection taken on expiration?",
     ["Posterior ribs below the diaphragm (axillary ribs)","Anterior ribs above the diaphragm","Costovertebral joints","Floating ribs (11th and 12th)"],
     "Ribs below the diaphragm (8–12) are demonstrated on expiration, which elevates the diaphragm and moves those ribs into view.",
     "Thoracic Imaging", 3, ["ribs","expiration","below diaphragm"]),

    ("For the sternum in the RAO position, the patient is rotated approximately:",
     ["15–20° RAO","45° RAO","30° RAO","60° RAO"],
     "The RAO (15–20°) superimposes the sternum over the cardiac shadow, which acts as a uniform background to improve contrast.",
     "Thoracic Imaging", 3, ["sternum","RAO","positioning"]),

    # ── Abdomen & GI ─────────────────────────────────────────────────────────
    ("For a KUB (kidneys, ureters, bladder) radiograph, the CR is directed to:",
     ["Iliac crest level at midsagittal plane","2 inches above the umbilicus","Symphysis pubis","L3 level"],
     "The CR for a KUB is centered at the iliac crest to include the kidneys superiorly and bladder inferiorly on the same image.",
     "Abdominal Imaging", 2, ["KUB","abdomen","CR","centering"]),

    ("A left lateral decubitus abdomen projection is used primarily to demonstrate:",
     ["Free intraperitoneal air collecting under the right hemidiaphragm","Ascites collecting on the left","Bowel obstruction","Retroperitoneal masses"],
     "In left lateral decubitus (right side up), free air rises to the highest point — the right side — where it is visible between liver and diaphragm.",
     "Abdominal Imaging", 3, ["free air","decubitus","abdomen"]),

    ("For an upper GI series using barium, the patient should be NPO (nothing by mouth) for at least:",
     ["6–8 hours before the examination","2 hours before","12 hours before","24 hours before"],
     "A 6–8 hour fast ensures the stomach is empty of food, which would interfere with mucosal coating and visualization.",
     "GI Procedures", 2, ["upper GI","NPO","barium","preparation"]),

    ("The Trendelenburg position is used during a barium enema to:",
     ["Fill the sigmoid and descending colon by allowing barium to flow cephalad","Drain the colon more rapidly","Demonstrate the rectal ampulla","Reduce the risk of aspiration"],
     "Tilting the table head-down helps barium flow from the rectum into the sigmoid and descending colon.",
     "GI Procedures", 3, ["barium enema","Trendelenburg","positioning"]),

    ("Which radiographic projection of the abdomen is performed with the patient supine and the CR directed vertically?",
     ["AP supine (KUB)","Left lateral decubitus","Erect abdomen","Dorsal decubitus"],
     "The standard AP supine abdomen (KUB) uses a vertical beam with the patient supine; other abdominal projections use various positions and beam angles.",
     "Abdominal Imaging", 2, ["AP","supine","KUB"]),

    ("During a small bowel series, the terminal ileum is best visualized when:",
     ["Barium reaches the ileocecal valve (approximately 30–120 min post-ingestion)","Immediately after barium ingestion","After 24 hours","During the double-contrast phase"],
     "Small bowel transit time to the terminal ileum varies; fluoroscopic monitoring tracks barium until it reaches the ileocecal valve.",
     "GI Procedures", 3, ["small bowel","terminal ileum","barium","GI"]),

    ("Double-contrast barium enema achieves mucosal detail by using:",
     ["Barium to coat the mucosa and air to distend the colon","Two different concentrations of barium","Barium and water-soluble contrast together","Barium and CO₂ infused together at high pressure"],
     "Double-contrast technique coats the mucosal surface with high-density barium, then distends the lumen with air to demonstrate fine mucosal detail.",
     "GI Procedures", 3, ["double contrast","barium enema","mucosal detail"]),

    ("Prior to an intravenous urogram (IVU/IVP), a scout (preliminary) radiograph is taken to:",
     ["Assess bowel preparation and identify calcifications before contrast","Confirm the patient is not pregnant","Measure the kidneys","Verify the contrast dose"],
     "The scout KUB reveals pre-existing calcifications, organ size, bowel gas patterns, and confirms positioning before contrast is given.",
     "Urinary Procedures", 3, ["IVP","scout","KUB","urogram"]),

    ("In an IVU, the best time to image the ureters is:",
     ["Compression or prone positioning 5–10 minutes post-injection","Immediately after injection","At 60 minutes post-injection","After the patient voids"],
     "Ureteral compression or prone positioning impedes ureteral drainage, allowing contrast to fill and distend the ureters for best visualization.",
     "Urinary Procedures", 3, ["IVP","ureters","compression","timing"]),

    ("A post-void (post-micturition) radiograph in an IVU is obtained to evaluate:",
     ["Bladder emptying and residual contrast","Ureteral peristalsis","Cortical thickness of the kidneys","The renal pelvis"],
     "Post-void imaging shows how completely the bladder empties and reveals bladder wall abnormalities or residual urine.",
     "Urinary Procedures", 3, ["IVP","post-void","bladder"]),

    # ── Upper Extremity ──────────────────────────────────────────────────────
    ("For a PA wrist projection, the CR is directed to:",
     ["The midcarpal area (proximal row of carpals)","The distal radioulnar joint","The metacarpophalangeal joints","The ulnar styloid"],
     "The CR centers to the midcarpal region to include the proximal and distal carpal rows, distal radius/ulna, and proximal metacarpals.",
     "Upper Extremity", 2, ["wrist","PA","CR","carpals"]),

    ("The scaphoid bone of the wrist is BEST demonstrated in which projection?",
     ["PA with ulnar deviation (scaphoid projection)","PA wrist","Lateral wrist","PA with radial deviation"],
     "Ulnar deviation reduces overlap of the scaphoid with adjacent bones and opens the scapholunate joint space for best visualization.",
     "Upper Extremity", 3, ["scaphoid","ulnar deviation","wrist"]),

    ("For an AP elbow projection, the patient's elbow must be:",
     ["Fully extended with no rotation","Flexed 90°","Slightly flexed (15°)","Pronated"],
     "A fully extended elbow in true AP position places the elbow joint parallel to the image receptor for accurate joint space demonstration.",
     "Upper Extremity", 2, ["elbow","AP","extension"]),

    ("Which special projection of the elbow is used to demonstrate the olecranon process in profile?",
     ["Lateral (mediolateral) elbow projection","AP elbow","Axial (Jones) projection","Oblique elbow"],
     "The true lateral elbow best demonstrates the olecranon process in profile along with the radial head, capitellum, and trochlea.",
     "Upper Extremity", 2, ["elbow","olecranon","lateral"]),

    ("The Norgaard (ball-catcher) projection is used to demonstrate early erosive changes in:",
     ["Rheumatoid arthritis of the hands","Osteoarthritis of the thumb","Carpal tunnel syndrome","De Quervain tenosynovitis"],
     "The Norgaard position (bilateral AP oblique hands in slight supination) reveals early periarticular erosions characteristic of rheumatoid arthritis.",
     "Upper Extremity", 4, ["Norgaard","hands","rheumatoid arthritis"]),

    ("For a PA projection of the hand, the CR is directed to:",
     ["Third metacarpophalangeal (MCP) joint","The wrist","The proximal phalanges","The midpoint of the palm"],
     "Centering to the 3rd MCP joint includes all metacarpals and phalanges; the wrist is typically at the top of the field.",
     "Upper Extremity", 2, ["hand","PA","CR","MCP"]),

    ("The Clements-Nakayama projection is a specialized view of the:",
     ["Shoulder (inferosuperior axial)","Scaphoid","Acromioclavicular joint","Coracoid process"],
     "The Clements-Nakayama method is an inferosuperior axial shoulder projection used when the patient cannot fully abduct the arm for the standard axillary projection.",
     "Upper Extremity", 4, ["shoulder","Clements-Nakayama","axial"]),

    ("For an AP shoulder radiograph, external rotation of the humerus demonstrates:",
     ["The greater tubercle in profile on the lateral aspect","The lesser tubercle in profile","The bicipital groove","The glenoid in profile"],
     "External rotation profiles the greater tubercle laterally; internal rotation profiles the lesser tubercle medially.",
     "Upper Extremity", 3, ["shoulder","AP","external rotation","greater tubercle"]),

    # ── Lower Extremity ──────────────────────────────────────────────────────
    ("For an AP knee projection, the CR should be angled:",
     ["5–7° cephalad to the joint space","0° (perpendicular)","5–7° caudad","10–15° cephalad"],
     "A 5–7° cephalad angle directs the beam parallel to the tibial plateau, opening the knee joint space for accurate demonstration.",
     "Lower Extremity", 3, ["knee","AP","CR angle","cephalad"]),

    ("The tunnel (intercondylar fossa) projection of the knee requires the patient to be:",
     ["Prone with the knee flexed 40–50°","Supine with the knee fully extended","Supine with the knee flexed 90°","Weight-bearing in full extension"],
     "The tunnel (Camp-Coventry or Holmblad) projection with ~40–50° flexion projects the beam through the intercondylar fossa, demonstrating loose bodies and fossa pathology.",
     "Lower Extremity", 3, ["knee","tunnel","intercondylar","fossa"]),

    ("The weight-bearing AP and lateral projections of the ankle are used to evaluate:",
     ["Joint alignment and true joint space narrowing under stress","Fractures of the fibula","Soft tissue swelling","Bony detail of the talus"],
     "Weight-bearing views apply physiological load, revealing true joint space narrowing and alignment that non–weight-bearing views may miss.",
     "Lower Extremity", 3, ["ankle","weight-bearing","alignment"]),

    ("For a lateral ankle projection, the patient is positioned with the ankle in:",
     ["True lateral (mediolateral) with leg internally rotated","External rotation","Plantar flexion","Dorsiflexion"],
     "True lateral ankle requires internal rotation so the malleoli are superimposed; the medial malleolus will be slightly anterior.",
     "Lower Extremity", 2, ["ankle","lateral","mediolateral"]),

    ("The Salter-Harris classification applies to fractures involving the:",
     ["Physis (growth plate) in pediatric patients","Femoral neck in adults","Tibial plateau in adults","Calcaneus in any age group"],
     "Salter-Harris types I–V classify physeal (growth plate) fractures in children; accurate classification guides treatment and prognosis.",
     "Lower Extremity", 4, ["Salter-Harris","growth plate","physis","pediatric"]),

    ("The axial (plantodorsal) projection of the calcaneus uses a CR angle of:",
     ["40° cephalad to the plantar surface","0° perpendicular","20° caudad","90° to the plantar surface"],
     "A 40° cephalad angle (from the plantar surface) directs the beam through the calcaneus to demonstrate the sustentaculum tali and body.",
     "Lower Extremity", 3, ["calcaneus","axial","CR angle"]),

    ("For a lateral hip projection (cross-table), the unaffected leg is:",
     ["Flexed and elevated out of the beam path","Extended alongside the affected leg","Internally rotated","Crossed over the affected leg"],
     "Elevating and flexing the unaffected hip removes it from the collimated field, allowing the beam to pass unobstructed to the affected hip.",
     "Lower Extremity", 3, ["hip","cross-table lateral","positioning"]),

    ("The frog-leg lateral projection of the hip places the thigh in:",
     ["Abduction and external rotation (like a frog's leg)","Adduction and internal rotation","Full extension with no rotation","Flexion with internal rotation"],
     "Frog-leg lateral abducts and externally rotates the thigh, placing the femoral neck in profile perpendicular to the receptor.",
     "Lower Extremity", 2, ["hip","frog-leg","lateral"]),

    # ── Spine ─────────────────────────────────────────────────────────────────
    ("For an AP lumbar spine, the CR is directed to:",
     ["L3 (approximately 2 inches above the iliac crest at midsagittal plane)","Iliac crest level","L5–S1 junction","Umbilicus"],
     "L3 is the mid-lumbar level; centering here with appropriate field size includes L1–S1 on most adults.",
     "Spinal Imaging", 2, ["lumbar spine","AP","L3","CR"]),

    ("The L5–S1 lumbosacral junction is best demonstrated on:",
     ["Lateral lumbar spine projection","AP lumbar spine","45° oblique lumbar spine","AP axial lumbar spine"],
     "The lateral projection demonstrates the L5–S1 disk space in profile; the AP view shows it obliquely and it may be partially obscured by the pelvis.",
     "Spinal Imaging", 3, ["L5-S1","lateral","lumbar spine"]),

    ("For an AP open-mouth (odontoid) projection, the patient's mouth must be open so that the:",
     ["Upper and lower teeth are superimposed over the C1–C2 region on the same horizontal plane","The mandible clears the C3 vertebra","The soft palate is at the level of C1","The teeth are not in the field"],
     "The open-mouth position superimposes the upper and lower teeth at the level of C1–C2, allowing the dens (odontoid process) to be seen through the oral cavity.",
     "Spinal Imaging", 3, ["odontoid","open-mouth","C1-C2"]),

    ("The swimmer's (Twining) lateral projection is used to demonstrate the cervicothoracic junction because:",
     ["Standard lateral cannot penetrate the shoulder density at C7–T1","The AP projection distorts this region","Oblique projections are contraindicated here","Standard lateral shows the facets better"],
     "The shoulder mass prevents adequate penetration on standard lateral; the swimmer's projection lifts one arm to clear the shoulders and allows visualization of C7–T1.",
     "Spinal Imaging", 3, ["swimmer's","cervicothoracic","C7-T1","Twining"]),

    ("Lateral flexion and extension projections of the cervical spine are used to evaluate:",
     ["Ligamentous instability and range of motion","Foraminal stenosis","Fracture line visibility","Vertebral body height"],
     "Dynamic flexion/extension lateral views demonstrate abnormal motion between vertebrae, indicating ligamentous laxity or instability.",
     "Spinal Imaging", 3, ["cervical spine","flexion","extension","instability"]),

    ("For an AP sacrum projection, the CR is angled:",
     ["15° cephalad","5° caudad","0° (perpendicular)","30° cephalad"],
     "A 15° cephalad angle compensates for the sacrum's posterior inclination, projecting it without foreshortening onto the receptor.",
     "Spinal Imaging", 3, ["sacrum","AP","CR angle","cephalad"]),

    ("For an AP coccyx projection, the CR is angled:",
     ["10° caudad","15° cephalad","0°","20° caudad"],
     "A 10° caudad angle aligns the beam with the coccyx's anterior curve to avoid foreshortening.",
     "Spinal Imaging", 3, ["coccyx","AP","CR angle","caudad"]),

    # ── Skull & Facial Bones ─────────────────────────────────────────────────
    ("The Caldwell projection of the skull/sinuses places the OML at:",
     ["15° caudad to the image receptor","Perpendicular to the receptor","30° to the receptor","45° to the receptor"],
     "The Caldwell method tilts the OML 15° caudad, projecting the petrous ridges into the lower third of the orbits to demonstrate the frontal sinuses and orbital rims.",
     "Skull and Facial Bones", 3, ["Caldwell","skull","OML","sinuses"]),

    ("The submentovertex (SMV) projection of the skull demonstrates:",
     ["The base of the skull and the sphenoid sinuses","The vertex of the skull","The sella turcica","The frontal bone"],
     "The SMV (base view) directs the beam from below the chin vertically through the skull base, demonstrating the foramina and sphenoid sinuses.",
     "Skull and Facial Bones", 3, ["SMV","skull base","submentovertex"]),

    ("Which projection is used to demonstrate the nasal bones in profile?",
     ["Lateral nasal bones projection","Waters projection","PA Caldwell","Submentovertex"],
     "The lateral projection shows nasal bone fractures in profile; both lateral views should be obtained for complete evaluation.",
     "Skull and Facial Bones", 2, ["nasal bones","lateral","fracture"]),

    ("The Towne projection (AP axial) is used to demonstrate the:",
     ["Occipital bone, foramen magnum, and dorsum sellae","Frontal sinuses","Maxillary sinuses","Mandibular condyles"],
     "The Towne (AP axial) with 30° caudad OML or 37° caudad IOML angle projects the occiput, foramen magnum, and posterior cranial fossa.",
     "Skull and Facial Bones", 3, ["Towne","occipital","AP axial","skull"]),

    ("To demonstrate the mandible, which projection best shows the body?",
     ["PA projection of the mandible (axiolateral oblique)","AP Towne projection","Waters projection","Lateral skull"],
     "The axiolateral oblique of the mandible rotates the mandibular body of interest into profile free of superimposition.",
     "Skull and Facial Bones", 3, ["mandible","axiolateral oblique","positioning"]),

    # ── Special / Trauma ─────────────────────────────────────────────────────
    ("For a trauma patient with a suspected cervical spine injury, the FIRST cervical spine radiograph obtained is usually:",
     ["Cross-table lateral cervical spine (C1–C7 must be visible)","AP open-mouth odontoid","AP cervical spine","Oblique cervical spine"],
     "The cross-table lateral must include all seven cervical vertebrae; it identifies major instability before the patient is moved for additional views.",
     "Trauma Radiography", 3, ["cervical spine","trauma","cross-table lateral"]),

    ("A 'trauma series' of the shoulder typically includes:",
     ["AP with internal/external rotation and lateral scapular Y or axillary view","AP only","Bilateral AP for comparison","AP and Waters projection"],
     "The trauma shoulder series includes true AP views with rotation to profile the tuberosities and a Y or axillary view to assess glenohumeral alignment.",
     "Trauma Radiography", 3, ["shoulder","trauma","series"]),

    ("For a patient who cannot stand or sit for an upright chest radiograph, the best alternative to detect a pneumothorax is:",
     ["Lateral decubitus chest (affected side up)","AP supine chest","Expiration AP supine","Prone chest"],
     "With the affected side up, free pleural air rises laterally and is visible between the chest wall and lung; horizontal beam is required.",
     "Trauma Radiography", 3, ["pneumothorax","decubitus","trauma"]),

    ("The Judet oblique projections are used to evaluate the:",
     ["Acetabulum (anterior and posterior columns)","Sacroiliac joints","Femoral head","Iliac wings"],
     "Judet views (45° anterior and posterior obliques) profile the ilioischial and iliopubic columns and acetabular walls for fracture assessment.",
     "Trauma Radiography", 4, ["Judet","acetabulum","trauma","oblique"]),

    ("When performing a portable AP chest on a mechanically ventilated ICU patient, the most important positioning goal is:",
     ["True AP without rotation, with the entire thorax on the receptor","The patient seated at 90°","Including the entire abdomen","Ensuring full inspiration via ventilator cycle"],
     "True AP positioning minimizes apparent heart size distortion and allows accurate interval comparison; rotation causes pseudo-widening of mediastinum.",
     "Trauma Radiography", 4, ["portable","chest","ICU","AP","rotation"]),

    ("Which radiographic sign on a supine abdomen suggests small bowel obstruction?",
     ["Stepladder pattern of dilated small bowel loops with air-fluid levels","Pneumoperitoneum under the diaphragm","Ground-glass opacity in the flanks","Sentinel loop in the left upper quadrant only"],
     "Small bowel obstruction produces a stepladder pattern of dilated loops (>3 cm) with air-fluid levels at different heights within the same loop.",
     "Abdominal Imaging", 4, ["small bowel obstruction","stepladder","abdomen"]),
]


PATIENT_CARE_B3 = [
    ("A patient tells you they are taking warfarin (Coumadin) before a contrast injection. Why is this clinically relevant?",
     ["Warfarin increases bleeding risk at the venipuncture site and may affect contrast excretion","Warfarin reacts with iodinated contrast causing clot formation","Warfarin is contraindicated with all radiographic procedures","Warfarin must be discontinued 48 hours before any radiograph"],
     "Warfarin is an anticoagulant; venipuncture and arterial access carry higher bleeding risk, and the care team should be informed.",
     "Contrast Media", 3, ["warfarin","contrast","anticoagulant"]),

    ("A patient on a gurney arrives in the imaging department with no identification band. The BEST action is:",
     ["Use two identifiers (ask the patient to state name and DOB) and apply an ID band before imaging","Proceed with imaging if the requisition matches the department record","Ask the transporter to confirm the patient's name","Postpone the examination until a band is applied by nursing staff"],
     "Two-patient identification methods are required before any procedure; imaging without confirmed identity risks wrong-patient errors.",
     "Patient Interactions and Management", 3, ["patient identification","safety"]),

    ("Which solution is MOST appropriate for routine skin antisepsis before venipuncture?",
     ["70% isopropyl alcohol swab","Betadine (povidone-iodine) only","Chlorhexidine gluconate solution","Sterile saline"],
     "70% isopropyl alcohol is the standard antiseptic for routine venipuncture; iodine-based solutions are used for larger procedures.",
     "Infection Control", 2, ["venipuncture","antisepsis","skin prep"]),

    ("A patient on airborne isolation requires an urgent portable chest X-ray. The radiographer should:",
     ["Don an N95 respirator before entering, image the patient, and clean equipment before leaving","Wear a surgical mask only","Ask a nurse to bring the patient to a standard room","Defer the examination until isolation is lifted"],
     "Active airborne precautions require N95 respirator use; equipment must be decontaminated before leaving the isolation environment.",
     "Infection Control", 3, ["airborne","N95","portable","isolation"]),

    ("A pediatric patient is uncooperative during positioning. The MOST appropriate first action is:",
     ["Speak calmly to the child, explain the procedure in simple terms, and allow a parent to stay","Restrain the child immediately to prevent motion","Complete the exam as quickly as possible regardless of position","Request sedation before attempting any radiograph"],
     "Child-friendly communication and parental presence reduce anxiety; restraints and sedation are last resorts.",
     "Patient Interactions and Management", 3, ["pediatric","communication","uncooperative"]),

    ("When assisting an elderly patient with osteoporosis to the radiographic table, the radiographer should:",
     ["Use assistive devices and a minimum of two people to avoid falls and fractures","Move quickly to reduce the patient's discomfort during transfer","Allow the patient to transfer independently to maintain dignity","Have the patient hop up unassisted while the radiographer positions equipment"],
     "Osteoporotic bones fracture easily; careful, assisted transfers with adequate staffing are essential for safety.",
     "Patient Transfer and Positioning", 3, ["osteoporosis","elderly","transfer","fall prevention"]),

    ("Which of the following is the CORRECT sharps disposal method after venipuncture?",
     ["Immediately place the uncapped needle in a rigid sharps container","Recap the needle using a two-hand technique and dispose in a sharps container","Place the needle in a biohazard bag before disposal","Bend the needle to prevent reuse then dispose in regular waste"],
     "Needles must be disposed immediately uncapped in an approved sharps container; recapping with two hands risks needlestick injury.",
     "Infection Control", 2, ["sharps disposal","needlestick","safety"]),

    ("Which of the following actions BEST protects a patient's modesty during radiographic positioning?",
     ["Draping exposed areas not needed for the examination and explaining each step beforehand","Completing positioning as quickly as possible","Performing the examination with the door open for supervision","Asking a chaperone only for opposite-gender patients"],
     "Draping and communication protect dignity and reduce anxiety; modesty should be preserved for all patients regardless of the clinician's gender.",
     "Patient Interactions and Management", 2, ["modesty","patient dignity","positioning"]),

    ("When calculating the mAs for a portable chest X-ray, the radiographer should consider that most mobile units operate at:",
     ["Lower maximum mA than fixed units, requiring longer exposure times","Higher kVp than fixed units","The same output as ceiling-mounted units","Fixed mAs of 2.5 regardless of patient size"],
     "Mobile units have lower tube current capacity than fixed installations; the radiographer must compensate with longer time or adjusted technique.",
     "Exposure Factors", 3, ["portable","mAs","mobile unit"]),

    ("A patient has an above-the-elbow amputation on the right side. Where should the IV contrast be administered?",
     ["Left antecubital vein","Right forearm (distal to amputation)","Right internal jugular (radiographer places IV)","Either site is acceptable"],
     "The left antecubital vein is the preferred peripheral access site; the right is unavailable due to the amputation.",
     "Contrast Media", 3, ["IV access","amputation","contrast"]),

    ("A patient arrives in the department with a Jackson-Pratt (JP) drain. During positioning, the radiographer should:",
     ["Ensure the bulb remains compressed and the drain is secured to prevent dislodgement","Remove the drain before imaging for an unobstructed view","Clamp the drain during the exposure","Leave the drain management to nursing staff and not interact with it"],
     "JP drains require the bulb to remain compressed for suction; dislodgement or unclamping during positioning can compromise wound healing.",
     "Patient Transfer and Positioning", 3, ["drain","JP drain","patient care"]),

    ("A patient states they are 8 weeks pregnant. A lumbar spine radiograph has been ordered. The radiographer should:",
     ["Notify the radiologist and ordering physician before proceeding","Proceed with the examination using gonadal shielding","Cancel the exam and document without notifying anyone","Substitute an MRI automatically"],
     "Any pregnant patient requiring ionizing radiation to the abdomen/pelvis must be evaluated by the radiologist and ordering physician before imaging.",
     "Radiation Protection", 3, ["pregnancy","lumbar spine","radiation protection"]),

    ("When performing CPR on an adult, the correct compression-to-ventilation ratio is:",
     ["30 compressions to 2 breaths","15 compressions to 2 breaths","5 compressions to 1 breath","Continuous compressions with no ventilation"],
     "Current AHA BLS guidelines recommend 30:2 compression-to-ventilation ratio for adult CPR by single or two-rescuer teams.",
     "Medical Emergencies", 2, ["CPR","BLS","compressions"]),

    ("A patient with an IV line in the antecubital fossa needs an AP elbow radiograph. The radiographer should:",
     ["Position around the IV line carefully and notify the nurse if the line must be moved","Remove the IV line before imaging","Image through the IV line without repositioning","Request a different projection to avoid the IV site entirely"],
     "The radiographer should work around existing IV lines; any necessary repositioning of IV equipment must involve the nurse.",
     "Patient Transfer and Positioning", 3, ["IV line","elbow","positioning"]),

    ("Which ethical principle is violated when a radiographer performs an examination on a patient who has clearly refused it?",
     ["Autonomy (patient's right to self-determination)","Beneficence","Justice","Nonmaleficence"],
     "Autonomy grants competent patients the right to refuse treatment; proceeding against their expressed wishes violates this fundamental right.",
     "Patient Interactions and Management", 3, ["autonomy","ethics","refusal"]),

    ("A patient's blood pressure drops from 130/80 to 90/60 mmHg 10 minutes after contrast injection. The FIRST action is:",
     ["Place the patient supine, administer oxygen, notify the radiologist, and prepare to treat anaphylaxis","Continue the examination and recheck in 5 minutes","Administer oral fluids","Ask the patient to sit up slowly"],
     "A drop in BP with possible anaphylaxis requires immediate supine positioning, oxygen, notification, and preparation for epinephrine.",
     "Medical Emergencies", 4, ["contrast reaction","hypotension","anaphylaxis"]),

    ("The purpose of a two-patient identifier check (name + DOB) is to:",
     ["Prevent wrong-patient and wrong-procedure errors","Verify insurance eligibility","Confirm the radiograph is billable","Establish the patient's preferred name"],
     "The Joint Commission requires at least two patient identifiers before any procedure to prevent wrong-patient events.",
     "Patient Interactions and Management", 2, ["patient identification","safety","two identifier"]),

    ("A patient who is deaf communicates primarily in American Sign Language (ASL). The BEST approach for obtaining informed consent is:",
     ["Arrange for a qualified ASL interpreter","Write all instructions on paper","Use diagrams only","Have a family member interpret if they know some signs"],
     "A qualified medical ASL interpreter ensures accurate communication; family members may lack medical vocabulary and may breach confidentiality.",
     "Patient Interactions and Management", 3, ["ASL","deaf","interpreter","communication"]),

    ("When a radiographer discovers that the wrong patient received a radiograph, the FIRST step is:",
     ["Notify the radiologist and ordering physician immediately and complete an incident report","Repeat the correct examination first, then report the error","Document the error in the patient's chart without notifying the physician","Reassign the images to the correct patient in PACS"],
     "Patient safety events require immediate disclosure to the clinical team and formal incident reporting; correcting records comes after notification.",
     "Patient Interactions and Management", 4, ["wrong patient","incident report","safety"]),

    ("Which type of isolation precaution requires placement of the patient in a positive-pressure room?",
     ["Protective (reverse) isolation for immunocompromised patients","Airborne isolation for TB","Droplet isolation for influenza","Contact isolation for MRSA"],
     "Reverse (protective) isolation uses positive-pressure rooms to prevent environmental microorganisms from entering and infecting immunocompromised patients.",
     "Infection Control", 4, ["reverse isolation","positive pressure","immunocompromised"]),

    ("The MOST effective method of preventing healthcare-associated infections is:",
     ["Proper hand hygiene before and after patient contact","Wearing gloves for all patient contact","Routine use of N95 masks","Daily environmental disinfection of all patient areas"],
     "Hand hygiene is consistently the single most effective intervention for preventing transmission of healthcare-associated pathogens.",
     "Infection Control", 2, ["hand hygiene","HAI","infection prevention"]),

    ("A patient's nasogastric (NG) tube needs to be checked for proper placement. Which imaging modality is used?",
     ["Chest radiograph to confirm tip position at the gastroesophageal junction or below","Fluoroscopy of the abdomen only","CT of the abdomen","Ultrasound of the esophagus"],
     "Chest X-ray is the standard method to confirm NG tube placement; the tip should be below the diaphragm in the stomach.",
     "Patient Transfer and Positioning", 3, ["NG tube","nasogastric","chest radiograph","placement"]),

    ("When a radiographer needs to move a comatose patient's head for a skull radiograph, which precaution is MOST important?",
     ["Maintaining cervical spine alignment during all movements until cleared by physician","Using a pillow to support the head only","Extending the neck to optimize the Towne projection","Moving the head only after removing monitoring leads"],
     "Comatose patients may have undetected cervical injuries; spinal precautions must be maintained until cleared by the trauma team.",
     "Patient Transfer and Positioning", 4, ["comatose","cervical spine","skull","spinal precautions"]),

    ("What is the purpose of an incident report after a patient fall in the imaging department?",
     ["To document the event for quality improvement and potential liability review","To prove the radiographer was not at fault","To notify the patient's insurance company","To request disciplinary action"],
     "Incident reports are quality and risk management tools; they document events accurately for investigation, trend analysis, and prevention.",
     "Patient Interactions and Management", 3, ["incident report","fall","quality improvement"]),

    ("A patient complains of burning pain and swelling at the IV site during contrast injection. The injection should be:",
     ["Stopped immediately; assess for extravasation","Slowed to a lower flow rate and continued","Switched to the opposite arm while injection continues","Completed and then evaluated post-procedure"],
     "Burning and swelling indicate contrast extravasation; continuing the injection worsens tissue injury and can cause compartment syndrome.",
     "Contrast Media", 3, ["extravasation","contrast","IV","injection"]),
]


def build_batch3():
    rng = random.Random(55)
    all_q = []
    counters = {"PROC": 500, "PC": 500}

    for source, cat, sub_default, prefix in [
        (PROCEDURES, "Procedures", "Procedures", "PROC"),
        (PATIENT_CARE_B3, "Patient Care", "Patient Care", "PC"),
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
    batch3 = build_batch3()

    dist = Counter(q['ans'][0] for q in batch3)
    cats = Counter(q['cat'] for q in batch3)
    diffs = Counter(q['diff'] for q in batch3)
    print(f"Batch 3: {len(batch3)} questions")
    print("Answer dist:", {l: f"{dist[l]} ({dist[l]/len(batch3)*100:.1f}%)" for l in 'ABCD'})
    print("Categories:", dict(cats))
    print("Difficulty:", {k: diffs[k] for k in sorted(diffs)})

    # Load existing and merge
    with open('questions.json') as f:
        existing = json.load(f)

    combined = existing + batch3

    # Final stats
    final_cats = Counter(q['cat'] for q in combined)
    final_dist = Counter(q['ans'][0] for q in combined)
    print(f"\nCombined total: {len(combined)}")
    print("Final categories:")
    for cat in sorted(final_cats):
        print(f"  {cat}: {final_cats[cat]}")
    print("Final answer distribution:")
    for l in 'ABCD':
        print(f"  {l}: {final_dist[l]} ({final_dist[l]/len(combined)*100:.1f}%)")

    with open('questions.json', 'w') as f:
        json.dump(combined, f, separators=(',', ':'))
    print(f"\nSaved questions.json ({len(open('questions.json').read())//1024} KB)")
