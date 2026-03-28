#!/usr/bin/env python3
"""
Add image-based questions for downloaded medical images.
Run AFTER download_images.sh has completed.

Usage:
  cd /Users/jaredmaligacedar/arrt_exam_mvp
  python3 add_image_questions.py
"""

import json, os, re

QUESTIONS_FILE = "questions.json"
INDEX_FILE = "index.html"
IMG_DIR = "images"

# ═══════════════════════════════════════════════════════════════════════════════
# QUESTIONS FOR DOWNLOADED IMAGES
# Only questions whose images actually exist will be added.
# ═══════════════════════════════════════════════════════════════════════════════

ALL_NEW_QUESTIONS = [

    # ─── X-RAY TUBE DIAGRAM ─────────────────────────────────────────────────
    {
        "id": "IMG-D01", "cat": "Image Production", "sub": "Equipment Operation and Quality Assurance",
        "diff": 2, "type": "single",
        "stem": "In this x-ray tube diagram, what is the function of the rotating anode?",
        "img": "images/xray_tube_diagram.png",
        "imgAlt": "Schematic diagram of an x-ray tube showing cathode and anode",
        "opts": {
            "A": "To produce electrons via thermionic emission",
            "B": "To serve as the target where electrons are converted to x-rays and heat",
            "C": "To filter the x-ray beam",
            "D": "To focus the electron beam"
        },
        "ans": ["B"],
        "exp": "The anode serves as the target where high-speed electrons from the cathode are decelerated, producing x-rays (about 1%) and heat (about 99%). Rotating the anode distributes heat over a larger area, preventing target damage.",
        "tags": ["x-ray tube", "anode", "equipment"]
    },
    {
        "id": "IMG-D02", "cat": "Image Production", "sub": "Equipment Operation and Quality Assurance",
        "diff": 2, "type": "single",
        "stem": "In this x-ray tube, what component produces the electron cloud via thermionic emission?",
        "img": "images/xray_tube_diagram.png",
        "imgAlt": "X-ray tube schematic",
        "opts": {
            "A": "The anode",
            "B": "The glass envelope",
            "C": "The cathode filament",
            "D": "The rotor"
        },
        "ans": ["C"],
        "exp": "The cathode contains a tungsten filament that, when heated by a low-voltage current, releases electrons through thermionic emission. These electrons are then accelerated toward the anode by the high-voltage potential difference (kVp).",
        "tags": ["cathode", "thermionic emission", "x-ray tube"]
    },
    {
        "id": "IMG-D03", "cat": "Image Production", "sub": "Equipment Operation and Quality Assurance",
        "diff": 3, "type": "single",
        "stem": "Approximately what percentage of kinetic energy is converted to x-rays at the anode target?",
        "img": "images/xray_tube_diagram.png",
        "imgAlt": "X-ray tube diagram",
        "opts": {
            "A": "About 1%",
            "B": "About 25%",
            "C": "About 50%",
            "D": "About 75%"
        },
        "ans": ["A"],
        "exp": "Only about 1% of the kinetic energy of electrons striking the anode is converted to x-ray photons. The remaining 99% is converted to heat, which is why heat dissipation is a critical design concern for x-ray tubes.",
        "tags": ["x-ray production", "efficiency", "heat"]
    },

    # ─── C-ARM FLUOROSCOPY ──────────────────────────────────────────────────
    {
        "id": "IMG-D04", "cat": "Image Production", "sub": "Equipment Operation and Quality Assurance",
        "diff": 1, "type": "single",
        "stem": "This photograph shows what type of imaging equipment commonly used in the operating room?",
        "img": "images/c_arm.jpg",
        "imgAlt": "C-arm fluoroscopy unit in a medical setting",
        "opts": {
            "A": "Upright chest unit",
            "B": "C-arm fluoroscopy unit",
            "C": "CT scanner",
            "D": "Portable radiography unit"
        },
        "ans": ["B"],
        "exp": "A C-arm is a mobile fluoroscopy unit shaped like the letter C. The x-ray tube is on one end and the image intensifier/flat panel detector on the other. C-arms are widely used in surgery, orthopedics, and pain management for real-time imaging.",
        "tags": ["C-arm", "fluoroscopy", "equipment identification"]
    },
    {
        "id": "IMG-D05", "cat": "Safety", "sub": "Radiation Protection",
        "diff": 2, "type": "single",
        "stem": "When using this C-arm unit, where should the x-ray tube be positioned relative to the patient to minimize operator dose?",
        "img": "images/c_arm.jpg",
        "imgAlt": "C-arm fluoroscopy unit",
        "opts": {
            "A": "Tube above, detector below the patient",
            "B": "Tube below, detector above the patient",
            "C": "It does not matter",
            "D": "Tube should be at the patient's side"
        },
        "ans": ["B"],
        "exp": "The tube should be positioned below the table with the image receptor above. Scatter radiation is greatest at the tube side. With the tube below, scatter is directed downward rather than toward the operator and surgical team standing beside the patient.",
        "tags": ["C-arm positioning", "scatter radiation", "operator safety"]
    },

    # ─── CT SCANNER ─────────────────────────────────────────────────────────
    {
        "id": "IMG-D06", "cat": "Image Production", "sub": "Equipment Operation and Quality Assurance",
        "diff": 1, "type": "single",
        "stem": "This photograph shows what type of imaging equipment?",
        "img": "images/ct_scanner.jpg",
        "imgAlt": "CT scanner in a hospital radiology department",
        "opts": {
            "A": "Open MRI scanner",
            "B": "PET scanner",
            "C": "Computed Tomography (CT) scanner",
            "D": "Mammography unit"
        },
        "ans": ["C"],
        "exp": "This is a CT (computed tomography) scanner. CT uses a rotating x-ray tube and detector array to acquire cross-sectional images. The large donut-shaped gantry houses the tube and detectors that rotate around the patient.",
        "tags": ["CT scanner", "equipment identification"]
    },
    {
        "id": "IMG-D07", "cat": "Safety", "sub": "Radiation Protection",
        "diff": 2, "type": "single",
        "stem": "Compared to conventional radiography, CT scanning typically delivers:",
        "img": "images/ct_scanner.jpg",
        "imgAlt": "CT scanner",
        "opts": {
            "A": "Lower patient dose because it uses digital detectors",
            "B": "Equivalent patient dose",
            "C": "Significantly higher patient dose",
            "D": "No measurable radiation dose"
        },
        "ans": ["C"],
        "exp": "CT delivers significantly higher radiation doses than conventional radiography — often 10 to 100 times more. A single CT abdomen/pelvis can deliver 10-20 mSv compared to about 0.7 mSv for an AP abdomen radiograph. Dose optimization through protocols like automatic exposure control is essential.",
        "tags": ["CT dose", "radiation comparison", "patient safety"]
    },

    # ─── EM SPECTRUM ────────────────────────────────────────────────────────
    {
        "id": "IMG-D08", "cat": "Image Production", "sub": "Equipment Operation and Quality Assurance",
        "diff": 1, "type": "single",
        "stem": "On this electromagnetic spectrum diagram, where do diagnostic x-rays fall?",
        "img": "images/em_spectrum.png",
        "imgAlt": "Electromagnetic spectrum showing wavelength and frequency ranges",
        "opts": {
            "A": "Between radio waves and microwaves",
            "B": "Between visible light and ultraviolet",
            "C": "Between ultraviolet and gamma rays (short wavelength, high frequency)",
            "D": "Beyond gamma rays"
        },
        "ans": ["C"],
        "exp": "X-rays occupy the electromagnetic spectrum between ultraviolet radiation and gamma rays. They have short wavelengths (0.01-10 nm) and high frequencies, giving them the energy to penetrate tissue. Higher-energy x-rays have shorter wavelengths.",
        "tags": ["EM spectrum", "x-ray properties", "physics"]
    },
    {
        "id": "IMG-D09", "cat": "Image Production", "sub": "Equipment Operation and Quality Assurance",
        "diff": 2, "type": "single",
        "stem": "According to the electromagnetic spectrum, as x-ray wavelength decreases, what happens to photon energy?",
        "img": "images/em_spectrum.png",
        "imgAlt": "Electromagnetic spectrum with wavelength and frequency",
        "opts": {
            "A": "Energy decreases",
            "B": "Energy stays the same",
            "C": "Energy increases",
            "D": "Energy becomes zero"
        },
        "ans": ["C"],
        "exp": "Photon energy is inversely proportional to wavelength (E = hf = hc/λ). As wavelength decreases, frequency and energy increase. Higher kVp produces shorter-wavelength, higher-energy x-ray photons with greater penetrating power.",
        "tags": ["wavelength", "photon energy", "inverse relationship"]
    },

    # ─── PNEUMOTHORAX ───────────────────────────────────────────────────────
    {
        "id": "IMG-D10", "cat": "Procedures", "sub": "Chest Procedures",
        "diff": 2, "type": "single",
        "stem": "This chest radiograph demonstrates a finding on the left side. What is the most likely diagnosis?",
        "img": "images/pneumothorax.jpg",
        "imgAlt": "Chest x-ray showing pneumothorax",
        "opts": {
            "A": "Pleural effusion",
            "B": "Pneumothorax",
            "C": "Consolidation/pneumonia",
            "D": "Atelectasis"
        },
        "ans": ["B"],
        "exp": "A pneumothorax is visible as an area of hyperlucency (increased blackness) without lung markings peripheral to a visible pleural line. Air in the pleural space causes the lung to collapse away from the chest wall.",
        "tags": ["pneumothorax", "chest pathology", "identification"]
    },
    {
        "id": "IMG-D11", "cat": "Procedures", "sub": "Chest Procedures",
        "diff": 2, "type": "single",
        "stem": "What additional view can improve detection of a small pneumothorax that may not be visible on a standard PA chest?",
        "img": "images/pneumothorax.jpg",
        "imgAlt": "Chest x-ray with pneumothorax",
        "opts": {
            "A": "Inspiration PA",
            "B": "Expiration PA",
            "C": "AP lordotic",
            "D": "Bilateral decubitus"
        },
        "ans": ["B"],
        "exp": "An expiration chest radiograph makes a small pneumothorax more conspicuous. During expiration, lung volume decreases but the air in the pleural space remains the same, making the pneumothorax appear relatively larger and easier to identify.",
        "tags": ["pneumothorax", "expiration view", "supplemental views"]
    },

    # ─── PLEURAL EFFUSION ───────────────────────────────────────────────────
    {
        "id": "IMG-D12", "cat": "Procedures", "sub": "Chest Procedures",
        "diff": 2, "type": "single",
        "stem": "This chest radiograph shows opacification of the lower hemithorax with a meniscus sign. What is the most likely finding?",
        "img": "images/pleural_effusion.jpg",
        "imgAlt": "Chest x-ray showing pleural effusion with meniscus sign",
        "opts": {
            "A": "Pneumothorax",
            "B": "Lobar pneumonia",
            "C": "Pleural effusion",
            "D": "Pulmonary edema"
        },
        "ans": ["C"],
        "exp": "A pleural effusion appears as homogeneous opacification of the lower hemithorax with a characteristic concave upper border (meniscus sign) on an upright film. Fluid layers dependently and blunts the costophrenic angle.",
        "tags": ["pleural effusion", "meniscus sign", "chest pathology"]
    },
    {
        "id": "IMG-D13", "cat": "Procedures", "sub": "Chest Procedures",
        "diff": 2, "type": "single",
        "stem": "What positioning technique is used to confirm a suspected small pleural effusion?",
        "img": "images/pleural_effusion.jpg",
        "imgAlt": "Chest x-ray with pleural effusion",
        "opts": {
            "A": "AP supine",
            "B": "Lateral decubitus with affected side down",
            "C": "PA upright with expiration",
            "D": "AP lordotic"
        },
        "ans": ["B"],
        "exp": "A lateral decubitus view with the affected side down allows free-flowing fluid to layer along the dependent chest wall. If at least 175 mL of fluid is present, it will be visible as a band of opacity between the lung and the chest wall.",
        "tags": ["decubitus", "pleural effusion", "positioning"]
    },

    # ─── PNEUMONIA ──────────────────────────────────────────────────────────
    {
        "id": "IMG-D14", "cat": "Procedures", "sub": "Chest Procedures",
        "diff": 2, "type": "single",
        "stem": "This chest radiograph shows an area of airspace consolidation. What is the most likely diagnosis?",
        "img": "images/pneumonia.jpg",
        "imgAlt": "Chest x-ray showing consolidation consistent with pneumonia",
        "opts": {
            "A": "Pneumothorax",
            "B": "Pleural effusion",
            "C": "Pneumonia",
            "D": "Pulmonary embolism"
        },
        "ans": ["C"],
        "exp": "The area of increased opacity (whiteness) within the lung parenchyma represents airspace consolidation — fluid, pus, or inflammatory exudate filling the alveoli. This is the classic radiographic appearance of pneumonia, often with air bronchograms visible.",
        "tags": ["pneumonia", "consolidation", "chest pathology"]
    },

    # ─── COLLES FRACTURE ────────────────────────────────────────────────────
    {
        "id": "IMG-D15", "cat": "Procedures", "sub": "Extremity Procedures",
        "diff": 2, "type": "single",
        "stem": "This wrist radiograph shows a fracture of the distal radius with dorsal displacement. What is this fracture called?",
        "img": "images/colles_fracture.jpg",
        "imgAlt": "Lateral wrist radiograph showing Colles fracture with dorsal angulation",
        "opts": {
            "A": "Smith fracture",
            "B": "Colles fracture",
            "C": "Barton fracture",
            "D": "Galeazzi fracture"
        },
        "ans": ["B"],
        "exp": "A Colles fracture is a distal radius fracture with dorsal displacement and angulation, creating a 'dinner fork' deformity on lateral view. It is the most common wrist fracture and typically results from a fall on an outstretched hand (FOOSH). A Smith fracture is the reverse — volar displacement.",
        "tags": ["Colles fracture", "distal radius", "wrist fracture"]
    },
    {
        "id": "IMG-D16", "cat": "Procedures", "sub": "Extremity Procedures",
        "diff": 3, "type": "single",
        "stem": "How does a Smith fracture differ from the Colles fracture shown here?",
        "img": "images/colles_fracture.jpg",
        "imgAlt": "Colles fracture with dorsal displacement",
        "opts": {
            "A": "Smith fracture involves the ulna instead of radius",
            "B": "Smith fracture has volar (anterior) displacement instead of dorsal",
            "C": "Smith fracture involves the carpal bones",
            "D": "Smith fracture only occurs in children"
        },
        "ans": ["B"],
        "exp": "A Smith fracture is a 'reverse Colles' — the distal radius fragment is displaced volarly (anteriorly) instead of dorsally. Colles = dorsal displacement (dinner fork deformity), Smith = volar displacement (garden spade deformity).",
        "tags": ["Smith fracture", "Colles fracture", "fracture comparison"]
    },

    # ─── HIP FRACTURE ───────────────────────────────────────────────────────
    {
        "id": "IMG-D17", "cat": "Procedures", "sub": "Spine and Pelvis Procedures",
        "diff": 2, "type": "single",
        "stem": "This hip radiograph demonstrates a fracture. Where is the fracture located?",
        "img": "images/hip_fracture.jpg",
        "imgAlt": "AP hip radiograph showing intertrochanteric fracture",
        "opts": {
            "A": "Femoral neck (subcapital)",
            "B": "Intertrochanteric region",
            "C": "Femoral shaft",
            "D": "Acetabular rim"
        },
        "ans": ["B"],
        "exp": "An intertrochanteric fracture runs between the greater and lesser trochanters. These are extracapsular fractures (outside the hip joint capsule) and generally have better blood supply and healing than femoral neck fractures, which are intracapsular.",
        "tags": ["hip fracture", "intertrochanteric", "fracture classification"]
    },
    {
        "id": "IMG-D18", "cat": "Procedures", "sub": "Spine and Pelvis Procedures",
        "diff": 2, "type": "single",
        "stem": "When imaging a patient with suspected hip fracture, why is a cross-table lateral preferred over a frog-leg lateral?",
        "img": "images/hip_fracture.jpg",
        "imgAlt": "AP hip with fracture",
        "opts": {
            "A": "It provides better bony detail",
            "B": "It uses less radiation",
            "C": "It does not require movement of the injured leg",
            "D": "It demonstrates the acetabulum better"
        },
        "ans": ["C"],
        "exp": "A cross-table (horizontal beam) lateral allows imaging without moving or rotating the injured leg. A frog-leg lateral requires abduction and external rotation, which could displace a fracture and cause severe pain, vascular injury, or damage to the femoral head blood supply.",
        "tags": ["trauma hip", "cross-table lateral", "positioning"]
    },

    # ─── SCOLIOSIS ──────────────────────────────────────────────────────────
    {
        "id": "IMG-D19", "cat": "Procedures", "sub": "Spine and Pelvis Procedures",
        "diff": 2, "type": "single",
        "stem": "This spine radiograph demonstrates an abnormal lateral curvature. What is this condition?",
        "img": "images/scoliosis.jpg",
        "imgAlt": "AP spine radiograph showing scoliosis with brace",
        "opts": {
            "A": "Kyphosis",
            "B": "Lordosis",
            "C": "Scoliosis",
            "D": "Spondylolisthesis"
        },
        "ans": ["C"],
        "exp": "Scoliosis is an abnormal lateral curvature of the spine, typically measured using the Cobb angle method. It is most commonly diagnosed in adolescents. The image shows the spine with a corrective brace. Kyphosis and lordosis are anterior-posterior curvatures.",
        "tags": ["scoliosis", "spinal curvature", "Cobb angle"]
    },
    {
        "id": "IMG-D20", "cat": "Procedures", "sub": "Spine and Pelvis Procedures",
        "diff": 3, "type": "single",
        "stem": "Scoliosis series radiographs are typically taken with the patient in which position, and why?",
        "img": "images/scoliosis.jpg",
        "imgAlt": "Scoliosis spine radiograph",
        "opts": {
            "A": "Supine — to eliminate gravity effects on the spine",
            "B": "Upright (PA) — to show functional curvature under weight-bearing",
            "C": "Lateral recumbent — for patient comfort",
            "D": "Prone — to reduce breast dose"
        },
        "ans": ["B"],
        "exp": "Scoliosis series are taken upright (standing) to demonstrate the functional curvature under weight-bearing conditions. PA orientation is preferred over AP to reduce breast dose in adolescent patients, who are the most common population for scoliosis screening.",
        "tags": ["scoliosis series", "upright positioning", "breast dose"]
    },

    # ─── BOWEL OBSTRUCTION ──────────────────────────────────────────────────
    {
        "id": "IMG-D21", "cat": "Procedures", "sub": "Abdomen and GI Procedures",
        "diff": 2, "type": "single",
        "stem": "This abdominal radiograph shows multiple dilated loops of bowel with air-fluid levels. What is the most likely diagnosis?",
        "img": "images/bowel_obstruction.jpg",
        "imgAlt": "Abdominal radiograph showing small bowel obstruction with dilated loops",
        "opts": {
            "A": "Normal bowel gas pattern",
            "B": "Small bowel obstruction (SBO)",
            "C": "Pneumoperitoneum",
            "D": "Ascites"
        },
        "ans": ["B"],
        "exp": "Dilated loops of small bowel (>3 cm) with air-fluid levels on an upright film are the hallmark of small bowel obstruction. The valvulae conniventes (circular folds) that cross the entire diameter of the bowel help distinguish small bowel from large bowel.",
        "tags": ["bowel obstruction", "SBO", "abdomen pathology"]
    },
    {
        "id": "IMG-D22", "cat": "Procedures", "sub": "Abdomen and GI Procedures",
        "diff": 2, "type": "single",
        "stem": "To demonstrate air-fluid levels in suspected bowel obstruction, which projection is essential?",
        "img": "images/bowel_obstruction.jpg",
        "imgAlt": "Abdominal x-ray with bowel obstruction",
        "opts": {
            "A": "AP supine abdomen only",
            "B": "Upright or left lateral decubitus abdomen",
            "C": "PA prone abdomen",
            "D": "Oblique abdomen"
        },
        "ans": ["B"],
        "exp": "Air-fluid levels require a horizontal beam — either an upright abdomen or left lateral decubitus position. A supine abdomen alone cannot demonstrate air-fluid levels because the beam is vertical and fluid distributes evenly.",
        "tags": ["air-fluid levels", "upright abdomen", "horizontal beam"]
    },

    # ─── FILM BADGE DOSIMETER ───────────────────────────────────────────────
    {
        "id": "IMG-D23", "cat": "Safety", "sub": "Radiation Protection",
        "diff": 1, "type": "single",
        "stem": "This device is worn by radiation workers to measure cumulative exposure. What is it?",
        "img": "images/film_badge.jpg",
        "imgAlt": "Film badge dosimeter used for radiation monitoring",
        "opts": {
            "A": "Geiger-Mueller counter",
            "B": "Ion chamber survey meter",
            "C": "Personnel dosimeter (film badge)",
            "D": "Pocket dosimeter"
        },
        "ans": ["C"],
        "exp": "This is a personnel dosimeter (film badge) worn to measure cumulative radiation exposure over a monitoring period. Modern versions use OSL (optically stimulated luminescence) or TLD (thermoluminescent) technology rather than film, but the badge design remains similar.",
        "tags": ["film badge", "dosimeter", "personnel monitoring"]
    },
    {
        "id": "IMG-D24", "cat": "Safety", "sub": "Radiation Protection",
        "diff": 2, "type": "single",
        "stem": "Where should this personnel dosimeter be worn during routine radiographic procedures?",
        "img": "images/film_badge.jpg",
        "imgAlt": "Film badge dosimeter",
        "opts": {
            "A": "On the waist under the lead apron",
            "B": "At collar level outside the lead apron",
            "C": "On the wrist",
            "D": "Attached to the x-ray tube housing"
        },
        "ans": ["B"],
        "exp": "The primary dosimeter should be worn at the collar level (C-collar region) outside the lead apron. This position measures the maximum dose to the head, neck, and lenses of the eyes — the areas most exposed when wearing a lead apron.",
        "tags": ["dosimeter placement", "collar level", "radiation monitoring"]
    },

    # ─── RADIATION SYMBOL ───────────────────────────────────────────────────
    {
        "id": "IMG-D25", "cat": "Safety", "sub": "Radiation Protection",
        "diff": 1, "type": "single",
        "stem": "This symbol must be posted at the entrance to any area where radiation exposure could occur. What does it indicate?",
        "img": "images/radiation_symbol.png",
        "imgAlt": "International radiation warning trefoil symbol",
        "opts": {
            "A": "Biohazard area",
            "B": "High-voltage electrical hazard",
            "C": "Radiation hazard — caution area",
            "D": "Laser hazard"
        },
        "ans": ["C"],
        "exp": "The three-bladed trefoil is the international symbol for ionizing radiation. It must be displayed on radiation-producing equipment, areas where radioactive materials are stored, and at the entrance to rooms where radiation exposure may occur.",
        "tags": ["radiation symbol", "trefoil", "signage"]
    },

    # ─── BARIUM SWALLOW ─────────────────────────────────────────────────────
    {
        "id": "IMG-D26", "cat": "Procedures", "sub": "Abdomen and GI Procedures",
        "diff": 2, "type": "single",
        "stem": "This image shows the esophagus opacified with contrast media. What type of study is this?",
        "img": "images/barium_swallow.jpg",
        "imgAlt": "Barium swallow showing contrast-filled esophagus",
        "opts": {
            "A": "Upper GI series (barium swallow / esophagram)",
            "B": "Barium enema",
            "C": "IV pyelogram",
            "D": "Myelogram"
        },
        "ans": ["A"],
        "exp": "This is a barium swallow (esophagram), part of an upper GI series. The patient swallows barium sulfate contrast, which coats and fills the esophagus, allowing evaluation of swallowing function, mucosal abnormalities, strictures, and reflux under fluoroscopy.",
        "tags": ["barium swallow", "upper GI", "contrast study"]
    },
    {
        "id": "IMG-D27", "cat": "Patient Care", "sub": "Patient Interactions and Management",
        "diff": 2, "type": "single",
        "stem": "Before administering barium sulfate for a study like this, which patient condition is a contraindication?",
        "img": "images/barium_swallow.jpg",
        "imgAlt": "Barium swallow contrast study",
        "opts": {
            "A": "Hypertension",
            "B": "Suspected bowel perforation",
            "C": "Diabetes",
            "D": "Mild arthritis"
        },
        "ans": ["B"],
        "exp": "Barium sulfate is contraindicated when bowel perforation is suspected. If barium leaks into the peritoneal cavity, it causes severe peritonitis. Water-soluble contrast (e.g., Gastrografin) should be used instead when perforation is a concern.",
        "tags": ["barium contraindication", "perforation", "contrast safety"]
    },

    # ─── ANGIOGRAM ──────────────────────────────────────────────────────────
    {
        "id": "IMG-D28", "cat": "Procedures", "sub": "Special Procedures",
        "diff": 2, "type": "single",
        "stem": "This image shows vascular structures opacified with contrast media. What type of examination is this?",
        "img": "images/angiogram.jpg",
        "imgAlt": "Cerebral angiogram showing contrast-filled vessels",
        "opts": {
            "A": "Barium enema",
            "B": "Angiography (vascular study)",
            "C": "Myelography",
            "D": "Arthrography"
        },
        "ans": ["B"],
        "exp": "Angiography uses iodinated contrast media injected into blood vessels to visualize the vascular system under fluoroscopy or digital subtraction. It is used to diagnose vascular disease, aneurysms, stenosis, and malformations, and can be used for interventional treatments.",
        "tags": ["angiography", "vascular study", "iodinated contrast"]
    },
    {
        "id": "IMG-D29", "cat": "Patient Care", "sub": "Patient Interactions and Management",
        "diff": 2, "type": "single",
        "stem": "The iodinated contrast media used in this vascular study can cause what serious adverse reaction in some patients?",
        "img": "images/angiogram.jpg",
        "imgAlt": "Cerebral angiogram with iodinated contrast",
        "opts": {
            "A": "Constipation",
            "B": "Anaphylactic reaction",
            "C": "Muscle weakness",
            "D": "Increased appetite"
        },
        "ans": ["B"],
        "exp": "Iodinated contrast can cause allergic-type reactions ranging from mild (hives, nausea) to severe anaphylaxis (bronchospasm, hypotension, cardiac arrest). Patients must be screened for prior contrast reactions, allergies, and renal function. Emergency equipment and medications must be immediately available.",
        "tags": ["contrast reaction", "anaphylaxis", "iodinated contrast"]
    },
    {
        "id": "IMG-D30", "cat": "Patient Care", "sub": "Patient Interactions and Management",
        "diff": 3, "type": "single",
        "stem": "Before administering iodinated contrast, which lab value must be checked to assess renal function?",
        "img": "images/angiogram.jpg",
        "imgAlt": "Angiogram with iodinated contrast",
        "opts": {
            "A": "Hemoglobin",
            "B": "White blood cell count",
            "C": "Creatinine / eGFR (estimated glomerular filtration rate)",
            "D": "Prothrombin time (PT)"
        },
        "ans": ["C"],
        "exp": "Serum creatinine and eGFR are checked before IV contrast administration to assess kidney function. Iodinated contrast is nephrotoxic and can cause contrast-induced nephropathy, especially in patients with pre-existing renal impairment (eGFR <30 mL/min is high risk).",
        "tags": ["creatinine", "eGFR", "contrast nephropathy", "renal function"]
    },

    # ─── LATERAL C-SPINE ────────────────────────────────────────────────────
    {
        "id": "IMG-D31", "cat": "Procedures", "sub": "Spine and Pelvis Procedures",
        "diff": 2, "type": "single",
        "stem": "This lateral cervical spine radiograph must demonstrate which vertebral levels to be considered adequate?",
        "img": "images/lateral_cspine.jpg",
        "imgAlt": "Lateral cervical spine radiograph",
        "opts": {
            "A": "C1 through C5",
            "B": "C1 through C7 (including the C7-T1 junction)",
            "C": "C3 through C7",
            "D": "C1 through C4"
        },
        "ans": ["B"],
        "exp": "An adequate lateral cervical spine must demonstrate C1 through C7 and the C7-T1 junction. Failure to visualize C7-T1 can miss injuries at this commonly injured level. If the shoulders obscure C7-T1, a swimmer's lateral view is needed.",
        "tags": ["lateral c-spine", "adequacy criteria", "C7-T1"]
    },

    # ─── AP PELVIS ──────────────────────────────────────────────────────────
    {
        "id": "IMG-D32", "cat": "Procedures", "sub": "Spine and Pelvis Procedures",
        "diff": 2, "type": "single",
        "stem": "On this AP pelvis radiograph, what positioning criteria indicates the legs were properly rotated?",
        "img": "images/ap_pelvis.jpg",
        "imgAlt": "AP pelvis radiograph with proper positioning",
        "opts": {
            "A": "The lesser trochanters are prominent",
            "B": "The femoral necks are fully demonstrated without foreshortening",
            "C": "The obturator foramina are closed",
            "D": "The greater trochanters overlap the femoral necks"
        },
        "ans": ["B"],
        "exp": "On a properly positioned AP pelvis, the legs are internally rotated 15-20° so the femoral necks are seen in full profile without foreshortening. The lesser trochanters should be only minimally visible. If the feet are externally rotated, the femoral necks appear foreshortened.",
        "tags": ["AP pelvis", "internal rotation", "femoral neck"]
    },

    # ─── LATERAL KNEE ───────────────────────────────────────────────────────
    {
        "id": "IMG-D33", "cat": "Procedures", "sub": "Extremity Procedures",
        "diff": 2, "type": "single",
        "stem": "This lateral knee radiograph shows the patella. What degree of knee flexion is standard for this projection?",
        "img": "images/lateral_knee.jpg",
        "imgAlt": "Lateral knee radiograph",
        "opts": {
            "A": "Full extension (0 degrees)",
            "B": "20-30 degrees",
            "C": "45 degrees",
            "D": "90 degrees"
        },
        "ans": ["B"],
        "exp": "The standard lateral knee is taken with 20-30° of flexion. This relaxes the muscles and ligaments enough to open the joint space while keeping the patella in a normal position. Over-flexion (>30°) can pull the patella into the intercondylar notch.",
        "tags": ["lateral knee", "flexion", "positioning"]
    },

    # ─── PA HAND ────────────────────────────────────────────────────────────
    {
        "id": "IMG-D34", "cat": "Procedures", "sub": "Extremity Procedures",
        "diff": 1, "type": "single",
        "stem": "This PA hand radiograph demonstrates normal anatomy. How many phalanges does each finger have (excluding the thumb)?",
        "img": "images/pa_hand.jpg",
        "imgAlt": "Normal PA hand radiograph showing all bones",
        "opts": {
            "A": "2 (proximal and distal)",
            "B": "3 (proximal, middle, and distal)",
            "C": "4",
            "D": "1"
        },
        "ans": ["B"],
        "exp": "Each finger (2nd through 5th digits) has three phalanges: proximal, middle, and distal. The thumb (1st digit) has only two phalanges — proximal and distal. The hand has 27 bones total: 14 phalanges, 5 metacarpals, and 8 carpals.",
        "tags": ["hand anatomy", "phalanges", "bone count"]
    },

    # ─── SKULL PA ───────────────────────────────────────────────────────────
    {
        "id": "IMG-D35", "cat": "Procedures", "sub": "Head Procedures",
        "diff": 2, "type": "single",
        "stem": "On this PA skull radiograph, the petrous ridges should be projected into which anatomical structure?",
        "img": "images/skull_pa.jpg",
        "imgAlt": "PA skull radiograph",
        "opts": {
            "A": "The orbits (filling the lower third)",
            "B": "Below the maxillary sinuses",
            "C": "Above the orbits",
            "D": "Through the frontal sinuses"
        },
        "ans": ["A"],
        "exp": "On a true PA skull (0° angle), the petrous ridges are projected into the lower third of the orbits. With a 15° caudal angle (Caldwell method), the petrous ridges are projected below the orbits into the maxillary sinuses, better demonstrating the frontal sinuses.",
        "tags": ["PA skull", "petrous ridges", "positioning criteria"]
    },
]


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN — merge only questions whose images exist
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    # Check which images exist
    valid = []
    missing = []
    for q in ALL_NEW_QUESTIONS:
        if os.path.isfile(q["img"]) and os.path.getsize(q["img"]) > 5000:
            valid.append(q)
        else:
            missing.append(q["img"])

    if not valid:
        print("ERROR: No images found. Run download_images.sh first.")
        return

    # Remove duplicate missing
    missing = sorted(set(missing))

    print(f"Found images for {len(valid)} questions")
    if missing:
        print(f"Skipping {len(missing)} missing images:")
        for m in missing:
            print(f"  ✗ {m}")

    # Load existing questions
    with open(QUESTIONS_FILE) as f:
        questions = json.load(f)

    # Remove any existing IMG-D* questions (re-run safe)
    before = len(questions)
    questions = [q for q in questions if not q.get("id", "").startswith("IMG-D")]
    if before != len(questions):
        print(f"Removed {before - len(questions)} existing IMG-D questions (re-run)")

    # Add new
    questions.extend(valid)
    print(f"Total questions: {len(questions)} ({len(valid)} new image-based)")

    with open(QUESTIONS_FILE, "w") as f:
        json.dump(questions, f, indent=2)

    # Update embedded QUESTIONS_DATA in index.html
    with open(INDEX_FILE, "r") as f:
        html = f.read()

    js_data = json.dumps(questions, ensure_ascii=False)
    new_line = f"<script>const QUESTIONS_DATA = {js_data};</script>"
    pattern = r"<script>const QUESTIONS_DATA = \[.*?\];</script>"
    match = re.search(pattern, html)
    if match:
        html = html[:match.start()] + new_line + html[match.end():]
        with open(INDEX_FILE, "w") as f:
            f.write(html)
        print("Updated embedded QUESTIONS_DATA in index.html")
    else:
        print("WARNING: Could not find QUESTIONS_DATA in index.html")

    # Summary
    img_total = sum(1 for q in questions if q.get("img"))
    print(f"\nDone! {img_total} total image-based questions in the app.")
    print("\nNext steps:")
    print("  git add images/ questions.json index.html")
    print("  git commit -m 'Add image-based questions with medical images'")
    print("  git push origin main")


if __name__ == "__main__":
    main()
