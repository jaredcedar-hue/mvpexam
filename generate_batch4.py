"""
Batch 4: ~50 Procedures questions targeting ARRT blueprint gaps.
Subcategory targets:
  Extremity (42.4% of Procedures) — need most questions here
  Thorax/Abdomen (30.3%)
  Head/Spine/Pelvis (27.3%)
Correct answer always first; positions randomized at end.
"""
import json, random
from collections import Counter

PROCEDURES_B4 = [
    # ══ EXTREMITY — Upper (target ~20 questions) ═══════════════════════════

    ("Which projection of the thumb is obtained with the hand in the true lateral position?",
     ["Mediolateral thumb — hand flat on the receptor in lateral position","AP thumb","PA thumb","Oblique thumb with 45° rotation"],
     "With the hand in true lateral, the thumb naturally lies in a mediolateral (true lateral) projection, profiling the phalanges and interphalangeal joints.",
     "Extremity Procedures", 3, ["thumb","lateral","upper extremity"]),

    ("For a PA projection of the fingers, the CR is directed to:",
     ["The proximal interphalangeal (PIP) joint of the finger of interest","The distal phalanx","The metacarpophalangeal (MCP) joint","The midshaft of the middle phalanx"],
     "Centering to the PIP joint of the affected finger includes all three phalanges and both interphalangeal joints on the image.",
     "Extremity Procedures", 2, ["fingers","PA","CR","PIP"]),

    ("Which wrist projection demonstrates the pisiform free of superimposition?",
     ["45° semisupinated (medial) oblique","PA wrist","Lateral wrist","PA with ulnar deviation"],
     "The 45° semisupinated oblique rotates the pisiform free of the triquetrum and adjacent carpals, showing it in profile.",
     "Extremity Procedures", 3, ["wrist","pisiform","oblique","carpal"]),

    ("The carpal bridge (tangential) projection of the wrist is used to demonstrate:",
     ["Dorsal surface of the carpals and dorsal chip fractures","The carpal tunnel","The scaphoid waist","The distal radioulnar joint"],
     "The carpal bridge projection directs the beam tangentially over the dorsal wrist to demonstrate foreign bodies or chip fractures on the dorsal carpal surface.",
     "Extremity Procedures", 4, ["wrist","carpal bridge","tangential","dorsal"]),

    ("For a lateral forearm radiograph, which anatomical landmark confirms true lateral positioning?",
     ["The radial head is superimposed over the ulna at the elbow","The radius and ulna are parallel with no overlap","The olecranon is seen in profile","The styloid processes are superimposed"],
     "On a true lateral forearm, the distal radius and ulna are slightly superimposed at the wrist; at the elbow the radial head overlaps the coronoid process — not completely superimposed on ulna.",
     "Extremity Procedures", 3, ["forearm","lateral","positioning","radius","ulna"]),

    ("The Jones method (acute flexion) of the elbow is used when:",
     ["The patient cannot fully extend the elbow due to injury or pain","Demonstrating the radial head in profile","Evaluating the olecranon fossa","Showing the capitellum without superimposition"],
     "The Jones (acute flexion) method obtains an AP-equivalent view of the distal humerus when the patient cannot extend the elbow.",
     "Extremity Procedures", 3, ["elbow","Jones","acute flexion","trauma"]),

    ("The radial head–capitellum projection (lateral with 45° cephalad angle) is used to demonstrate:",
     ["The radial head free of ulnar superimposition","The olecranon in profile","The coronoid process","The medial epicondyle"],
     "A 45° cephalad angulation on the lateral elbow projects the radial head anterior to the coronoid, allowing unobstructed visualization.",
     "Extremity Procedures", 4, ["elbow","radial head","capitellum","lateral"]),

    ("For an AP shoulder with neutral rotation, which structure is best demonstrated?",
     ["Greater and lesser tubercles in partial profile","Greater tubercle fully in profile","Lesser tubercle fully in profile","Glenoid in true profile"],
     "Neutral rotation places the tubercles partially in profile; external rotation fully profiles the greater tubercle, internal rotation the lesser.",
     "Extremity Procedures", 3, ["shoulder","AP","neutral rotation","tubercle"]),

    ("The Grashey method (true AP glenoid) requires the patient to be rotated:",
     ["35–45° toward the affected side (posterior oblique)","45° away from the affected side","15° toward the affected side","No rotation — true AP"],
     "Rotating the patient 35–45° toward the affected shoulder brings the glenoid perpendicular to the beam, demonstrating the glenohumeral joint space.",
     "Extremity Procedures", 3, ["shoulder","Grashey","glenoid","oblique"]),

    ("The scapular Y projection (lateral scapula) is used primarily to evaluate:",
     ["Humeral head position relative to the glenoid (dislocation)","Acromioclavicular joint separation","Glenoid rim fractures","Coracoid process fractures"],
     "The Y view shows the glenoid at the center of the Y; a dislocated humeral head is displaced anterior (subcoracoid) or posterior.",
     "Extremity Procedures", 3, ["shoulder","scapular Y","dislocation","lateral"]),

    ("Which projection of the clavicle is taken with a 15–30° cephalad CR angle?",
     ["AP axial clavicle (to project it above the ribs)","PA clavicle","Tangential clavicle","Lateral clavicle"],
     "A cephalad angle projects the clavicle superiorly, free of rib and scapular superimposition, for better visualization.",
     "Extremity Procedures", 3, ["clavicle","AP axial","cephalad","positioning"]),

    ("The acromioclavicular (AC) joints are best evaluated with:",
     ["Bilateral weight-bearing AP projections with and without weights","Unilateral AP with internal rotation","Scapular Y projection","AP axial clavicle"],
     "Bilateral weight-bearing AC views with and without 5–10 lb weights compare joint width and detect ligamentous disruption causing joint widening.",
     "Extremity Procedures", 3, ["acromioclavicular","AC joint","weight-bearing","bilateral"]),

    # ══ EXTREMITY — Lower (target ~20 questions) ═══════════════════════════

    ("For an AP foot projection, the CR is directed:",
     ["10° posteriorly (toward the heel) to the base of the 3rd metatarsal","Perpendicular to the receptor","15° anteriorly (toward the toes)","20° medially"],
     "A 10° posterior angle aligns the beam with the metatarsal shafts, reducing foreshortening and showing the tarsometatarsal joints.",
     "Extremity Procedures", 3, ["foot","AP","CR angle","metatarsal"]),

    ("Which foot projection best demonstrates the intermetatarsal joint spaces?",
     ["45° medial oblique foot","AP foot","Lateral foot","45° lateral oblique foot"],
     "The 45° medial oblique opens the 3rd–5th metatarsal interspaces and demonstrates the cuboid, lateral cuneiforms, and lateral tarsometatarsal joints.",
     "Extremity Procedures", 3, ["foot","oblique","metatarsal","joint spaces"]),

    ("For a lateral foot projection, which surface of the foot rests on the image receptor?",
     ["Medial surface (mediolateral projection)","Lateral surface (lateromedial projection)","Plantar surface","Dorsal surface"],
     "The mediolateral projection places the medial foot on the detector; it best demonstrates the longitudinal arch and lateral foot bones.",
     "Extremity Procedures", 2, ["foot","lateral","mediolateral","positioning"]),

    ("The sesamoid bones of the foot are best demonstrated using which projection?",
     ["Tangential (Lewis or Holly method) — beam directed along the metatarsal shafts","AP foot","Lateral foot","Medial oblique foot"],
     "The tangential sesamoid projection directs the beam tangentially along the first metatarsal to profile the sesamoids beneath the first MTP joint.",
     "Extremity Procedures", 3, ["sesamoid","foot","tangential","Lewis"]),

    ("For an AP mortise projection of the ankle, the foot is rotated:",
     ["15–20° internally to place the intermalleolar line parallel to the receptor","15–20° externally","No rotation — true AP","45° internally"],
     "The 15–20° internal rotation brings both malleoli equidistant from the receptor, opening the entire mortise (tibiotalar) joint space.",
     "Extremity Procedures", 3, ["ankle","mortise","AP","internal rotation"]),

    ("The calcaneal axial (plantodorsal) projection requires the patient to:",
     ["Dorsiflex the foot (pull toes toward shin) so the plantar surface is nearly vertical","Plantar flex maximally","Lie prone with the foot hanging off the table","Rotate the ankle 45° internally"],
     "Dorsiflexion positions the plantar surface close to perpendicular, allowing the 40° cephalad beam to pass through the calcaneal body and sustentaculum.",
     "Extremity Procedures", 3, ["calcaneus","axial","dorsiflexion","plantodorsal"]),

    ("Which projection of the knee best demonstrates the proximal tibiofibular articulation?",
     ["45° internal rotation oblique (AP oblique)","AP knee","Lateral knee","Tunnel (intercondylar) projection"],
     "A 45° internal rotation AP oblique profiles the proximal tibiofibular joint space, which is otherwise obscured on routine AP and lateral views.",
     "Extremity Procedures", 3, ["knee","tibiofibular","oblique","internal rotation"]),

    ("The Merchant (axial) projection of the knee is used to evaluate:",
     ["Patellofemoral joint alignment and patellar subluxation","Intercondylar fossa pathology","Tibial plateau fractures","Collateral ligament integrity"],
     "The Merchant view directs the beam caudally through both knees in flexion (~45°), demonstrating the patellofemoral joint and trochlear groove bilaterally.",
     "Extremity Procedures", 3, ["knee","Merchant","patellofemoral","axial"]),

    ("For a lateral knee projection, the knee is flexed approximately:",
     ["20–30°","90°","5–10°","45°"],
     "A 20–30° flexion relaxes the posterior capsule, opens the joint space, and places the femoral condyles in the best lateral position.",
     "Extremity Procedures", 3, ["knee","lateral","flexion"]),

    ("The AP hip projection in the trauma setting with a suspected fracture should be performed:",
     ["Without moving the injured extremity from its presenting position","With 15° internal rotation of the foot","Only in the frog-leg position","With the leg in traction"],
     "The limb should be imaged in the position it presents; manipulation before fracture confirmation risks displacing an unstable fracture.",
     "Extremity Procedures", 4, ["hip","trauma","AP","fracture"]),

    ("Which landmark is used to center the CR for an AP femur (distal third)?",
     ["Midpoint between the ASIS and the knee joint (for mid-femur) or 2 inches above the knee for distal femur","Greater trochanter","Midpoint of the patellar ligament","The knee joint itself"],
     "For distal femur the CR is centered about 2 inches above the knee joint; for mid-femur it is centered at the midshaft between ASIS and knee.",
     "Extremity Procedures", 3, ["femur","AP","CR","distal"]),

    # ══ THORAX & ABDOMEN (target ~15 questions) ════════════════════════════

    ("For an AP portable chest on a supine patient, which finding appears artificially enlarged compared to an upright PA?",
     ["The cardiac silhouette (due to shorter SID and AP direction)","The lung fields","The costophrenic angles","The trachea"],
     "AP portable technique magnifies the heart due to shorter SID and anterior-to-posterior beam direction; the heart lies anteriorly and is farther from the receptor.",
     "Thoracic Imaging", 3, ["portable","chest","cardiac magnification","AP"]),

    ("The right posterior oblique (RPO) projection of the chest demonstrates the:",
     ["Left lung and left-sided heart border","Right lung","Right posterior ribs","Aortic arch in profile"],
     "In RPO the left side is closer to the receptor; the left lung, left heart border, and descending aorta are best demonstrated.",
     "Thoracic Imaging", 3, ["chest","RPO","oblique","left lung"]),

    ("For a lateral decubitus abdominal projection, which side is placed down to demonstrate free peritoneal air?",
     ["Left side down (left lateral decubitus) — air rises to right side above the liver","Right side down","Either side — the position does not matter","The affected side down"],
     "Left lateral decubitus raises the right side; free air collects above the liver, providing an air–liver interface that is easier to detect than an air–spleen interface.",
     "Abdominal Imaging", 3, ["abdomen","decubitus","free air","peritoneal"]),

    ("For an esophagram, which patient position best demonstrates esophageal varices?",
     ["Prone RAO with full barium swallow","Erect PA","Lateral recumbent","Left lateral decubitus"],
     "Prone RAO increases intraesophageal pressure, distending the esophagus and making varices visible as serpiginous filling defects.",
     "GI Procedures", 4, ["esophagram","varices","RAO","prone"]),

    ("During a barium enema, the hepatic and splenic flexures are best demonstrated with which patient positions?",
     ["RPO for hepatic flexure; LPO for splenic flexure","LPO for hepatic flexure; RPO for splenic flexure","Prone for both flexures","Supine AP for both flexures"],
     "RPO raises the right side, opening the hepatic flexure; LPO raises the left side, opening the splenic flexure.",
     "GI Procedures", 4, ["barium enema","hepatic flexure","splenic flexure","oblique"]),

    ("Which abdominal radiograph projection best demonstrates the retroperitoneal space?",
     ["Lateral (cross-table or horizontal beam lateral)","AP supine","Erect AP","Left lateral decubitus"],
     "The lateral projection of the abdomen profiles the retroperitoneal structures (kidneys, psoas margins, lumbar spine) free of anterior abdominal content.",
     "Abdominal Imaging", 3, ["abdomen","lateral","retroperitoneal"]),

    ("For an intravenous urogram (IVU), the timing of the nephrogram phase is:",
     ["30–90 seconds post-injection (immediate filling of renal parenchyma)","5 minutes post-injection","15 minutes post-injection","After patient voids"],
     "The nephrogram phase occurs immediately as contrast fills the renal tubules, producing a homogeneous dense blush of the parenchyma.",
     "Urinary Procedures", 3, ["IVP","nephrogram","timing","contrast"]),

    ("A voiding cystourethrogram (VCUG) is performed to evaluate:",
     ["Vesicoureteral reflux and urethral anatomy during voiding","Renal cortical thickness","Ureteral peristalsis","Bladder wall calcification"],
     "VCUG instills contrast into the bladder via catheter; fluoroscopy during voiding demonstrates reflux into the ureters and urethral anatomy.",
     "Urinary Procedures", 3, ["VCUG","cystourethrogram","reflux","bladder"]),

    ("Which breathing instructions are given during an AP thoracic spine radiograph?",
     ["Suspend respiration on expiration OR use a breathing technique (slow, shallow breathing during exposure)","Full inspiration, breath-hold","Normal tidal breathing only","Deep inspiration followed by slow expiration during exposure"],
     "Expiration depresses the sternum and reduces thoracic kyphosis; alternatively, a breathing technique blurs overlying ribs and vasculature to improve vertebral detail.",
     "Thoracic Imaging", 3, ["thoracic spine","breathing","AP","technique"]),

    ("The standard AP abdomen projection should include which anatomical boundaries?",
     ["Superior: diaphragm; inferior: pubic symphysis (or ischial tuberosities)","Superior: clavicles; inferior: greater trochanters","Superior: xiphoid; inferior: ASIS","Superior: T10; inferior: coccyx"],
     "A complete KUB must include the diaphragm (for kidney tops) and the pubic symphysis (for bladder), both essential for urinary tract evaluation.",
     "Abdominal Imaging", 2, ["abdomen","KUB","field coverage","boundaries"]),

    # ══ HEAD / SPINE / PELVIS ═══════════════════════════════════════════════

    ("The PA Caldwell projection of the paranasal sinuses places the petrous ridges:",
     ["In the lower third of the orbits","At the orbital rims","Below the orbital floor","Superimposed on the maxillary sinuses"],
     "The 15° caudad OML angle in the Caldwell method projects the petrous ridges into the lower third of the orbits, demonstrating the frontal and anterior ethmoid sinuses.",
     "Skull and Facial Bones", 3, ["Caldwell","sinuses","petrous ridges","orbits"]),

    ("For an AP axial (Towne) projection, the CR is angled:",
     ["30° caudad to the OML (or 37° caudad to the IOML)","15° cephalad","20° caudad to the IOML","Perpendicular to the OML"],
     "The Towne method uses 30° caudad relative to the OML; if the chin is tucked and IOML is used, 37° caudad achieves the same geometry.",
     "Skull and Facial Bones", 3, ["Towne","AP axial","OML","caudad"]),

    ("The zygomatic arch is best demonstrated on which projection?",
     ["Submentovertex (SMV) or modified SMV (tangential)","Waters projection","PA Caldwell","Lateral skull"],
     "The SMV and tangential zygomatic arch projections direct the beam along the arch to profile it without superimposition from the skull base.",
     "Skull and Facial Bones", 3, ["zygomatic arch","SMV","tangential","positioning"]),

    ("For oblique cervical spine projections, which structures are best demonstrated?",
     ["Intervertebral foramina (the side farthest from the receptor on RPO/LPO)","Spinous processes","Vertebral body heights","Zygapophyseal joints"],
     "On cervical obliques, the intervertebral foramina closest to the tube (far side from receptor) are opened toward the beam and best demonstrated.",
     "Spinal Imaging", 3, ["cervical spine","oblique","intervertebral foramina","RPO","LPO"]),

    ("For an AP axial sacroiliac (SI) joint projection, the CR is angled:",
     ["30–35° cephalad to the SI joints","15° cephalad","10° caudad","0° (perpendicular)"],
     "A 30–35° cephalad angle aligns the beam with the angled SI joint surfaces, opening them for visualization on the AP axial projection.",
     "Spinal Imaging", 3, ["sacroiliac joints","AP axial","cephalad","SI"]),

    ("An AP pelvis radiograph requires the lower limbs to be:",
     ["Internally rotated 15° to place the femoral necks parallel to the receptor","Externally rotated 15°","Positioned in neutral with no rotation","Flexed 30° at the knee"],
     "15° internal rotation of both feet overcomes the anteversion of the femoral necks, placing them parallel to the image receptor for true AP demonstration.",
     "Spinal Imaging", 3, ["pelvis","AP","internal rotation","femoral neck"]),

    ("The Waters projection (PA axial) is performed with the OML at what angle to the image receptor?",
     ["37° (chin extended so OML is 37° from perpendicular)","15°","45°","Perpendicular (0°)"],
     "Extending the chin until the OML forms a 37° angle to the receptor projects the petrous ridges below the maxillary sinus floors for unobstructed sinus visualization.",
     "Skull and Facial Bones", 3, ["Waters","OML","37 degrees","sinuses"]),

    ("For a lateral cervical spine, all seven cervical vertebrae must be demonstrated. If C7 is not visible, the NEXT step is:",
     ["Apply downward traction on both arms (Swimmer's if needed) or use the Twining method","Increase kVp by 15%","Angle the CR 15° cephalad","Obtain a Towne projection instead"],
     "Shoulder mass obscures C7; downward arm traction drops the shoulders and if still inadequate, the Twining (Swimmer's) lateral demonstrates the cervicothoracic junction.",
     "Spinal Imaging", 3, ["cervical spine","C7","lateral","swimmer's"]),

    ("The sella turcica is best demonstrated on which projection?",
     ["Lateral skull","PA Caldwell","Waters","AP Towne"],
     "The lateral skull places the sella turcica in profile, allowing accurate measurement of its dimensions for pituitary gland assessment.",
     "Skull and Facial Bones", 2, ["sella turcica","lateral skull","pituitary"]),

    ("For AP and lateral sacrum projections, the SID should be:",
     ["100 cm (40 inches) — standard tabletop SID","180 cm (72 inches)","150 cm (60 inches)","75 cm (30 inches)"],
     "Sacrum projections use the standard 100 cm SID for tabletop radiography; no extended distance is required.",
     "Spinal Imaging", 2, ["sacrum","SID","positioning"]),
]


def build_batch4():
    rng = random.Random(42)
    all_q = []
    counter = 700

    for stem, opts_list, exp, sub, diff, tags in PROCEDURES_B4:
        positions = ['A','B','C','D']
        shuffled = positions[:]
        rng.shuffle(shuffled)
        mapping = {positions[j]: shuffled[j] for j in range(4)}
        new_opts = {shuffled[j]: opts_list[j] for j in range(4)}
        correct_ans = [mapping['A']]

        counter += 1
        all_q.append({
            "id": f"PROC-NEW-{counter:03d}",
            "cat": "Procedures",
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
    batch4 = build_batch4()

    dist = Counter(q['ans'][0] for q in batch4)
    subs = Counter(q['sub'] for q in batch4)

    print(f"Batch 4: {len(batch4)} Procedures questions")
    print("Answer dist:", {l: f"{dist[l]} ({dist[l]/len(batch4)*100:.1f}%)" for l in 'ABCD'})
    print("Subcategories:")
    for sub, n in sorted(subs.items()):
        print(f"  {sub}: {n}")

    # Load and merge
    with open('questions.json') as f:
        existing = json.load(f)

    combined = existing + batch4

    # Final stats
    final_cats = Counter(q['cat'] for q in combined)
    final_dist = Counter(q['ans'][0] for q in combined)
    total = len(combined)

    official = {'Patient Care': 0.165, 'Safety': 0.25, 'Image Production': 0.255, 'Procedures': 0.33}
    print(f"\nFinal bank: {total} questions")
    print(f"\n{'Category':<20} {'Count':>6} {'Our%':>6} {'ARRT%':>6} {'Gap':>6}")
    print('-' * 50)
    for cat in ['Patient Care','Safety','Image Production','Procedures']:
        n = final_cats[cat]
        pct = n/total*100
        target = official[cat]*100
        ideal = round(official[cat]*total)
        gap = ideal - n
        sign = '+' if gap > 0 else ''
        print(f"{cat:<20} {n:>6} {pct:>5.1f}% {target:>5.1f}% {sign+str(gap):>6}")

    print("\nAnswer distribution:")
    for l in 'ABCD':
        print(f"  {l}: {final_dist[l]} ({final_dist[l]/total*100:.1f}%)")

    with open('questions.json', 'w') as f:
        json.dump(combined, f, separators=(',',':'))
    print(f"\nSaved questions.json ({len(open('questions.json').read())//1024} KB)")
