#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# ARRT Exam MVP — Download Public Domain Medical Images
# ═══════════════════════════════════════════════════════════════════════════════
# Run this on your Mac:
#   cd /Users/jaredmaligacedar/arrt_exam_mvp
#   chmod +x download_images.sh
#   ./download_images.sh
#
# Sources: Wikimedia Commons (public domain US medical imaging),
#          Wikipedia diagrams (CC-BY-SA or public domain)
# ═══════════════════════════════════════════════════════════════════════════════

set -e
mkdir -p images

echo "Downloading public domain medical images for ARRT exam questions..."
echo ""

# ─── X-RAY EQUIPMENT & PHYSICS ───────────────────────────────────────────────

# X-ray tube diagram (Wikimedia Commons, public domain)
echo "[1/20] X-ray tube schematic..."
curl -sL -o images/xray_tube_diagram.png \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/X-ray_tube_diagram.svg/800px-X-ray_tube_diagram.svg.png"

# Modern C-arm fluoroscopy unit (Wikimedia Commons, CC-BY-SA)
echo "[2/20] C-arm fluoroscopy unit..."
curl -sL -o images/c_arm.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/C-arm_X-ray_machine_OEC_9900_Elite.jpg/600px-C-arm_X-ray_machine_OEC_9900_Elite.jpg"

# CT scanner (Wikimedia Commons)
echo "[3/20] CT scanner..."
curl -sL -o images/ct_scanner.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/UPMCEast_CT.jpg/800px-UPMCEast_CT.jpg"

# Electromagnetic spectrum showing x-ray range
echo "[4/20] EM spectrum..."
curl -sL -o images/em_spectrum.png \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/EM_Spectrum_Properties_edit.svg/800px-EM_Spectrum_Properties_edit.svg.png"

# ─── PATHOLOGY X-RAYS (US medical imaging = public domain) ───────────────────

# Pneumothorax chest x-ray
echo "[5/20] Pneumothorax CXR..."
curl -sL -o images/pneumothorax.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/a/ab/Pneumothorax_CXR.jpg"

# Pleural effusion chest x-ray
echo "[6/20] Pleural effusion CXR..."
curl -sL -o images/pleural_effusion.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Pleural_effusion.jpg/461px-Pleural_effusion.jpg"

# Pneumonia chest x-ray
echo "[7/20] Pneumonia CXR..."
curl -sL -o images/pneumonia.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Pneumonia_x-ray.jpg/400px-Pneumonia_x-ray.jpg"

# Colles fracture (distal radius)
echo "[8/20] Colles fracture..."
curl -sL -o images/colles_fracture.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Colles_fracture.jpg/300px-Colles_fracture.jpg"

# Hip fracture
echo "[9/20] Hip fracture..."
curl -sL -o images/hip_fracture.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Hip_fracture_-_trochanteric.jpg/369px-Hip_fracture_-_trochanteric.jpg"

# Scoliosis spine x-ray
echo "[10/20] Scoliosis..."
curl -sL -o images/scoliosis.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Scoliosis_patient_in_cheneau_brace_correcting_from_56_to_27_degrees.jpg/250px-Scoliosis_patient_in_cheneau_brace_correcting_from_56_to_27_degrees.jpg"

# Small bowel obstruction (SBO) abdomen
echo "[11/20] Bowel obstruction..."
curl -sL -o images/bowel_obstruction.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Small_bowel_obstruction.jpg/400px-Small_bowel_obstruction.jpg"

# ─── RADIATION SAFETY & EQUIPMENT PHOTOS ─────────────────────────────────────

# Dosimeter / film badge
echo "[12/20] Film badge dosimeter..."
curl -sL -o images/film_badge.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Film_badge_dosimeter.jpg/440px-Film_badge_dosimeter.jpg"

# Radiation warning trefoil symbol
echo "[13/20] Radiation symbol..."
curl -sL -o images/radiation_symbol.png \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Radiation_warning_symbol.svg/600px-Radiation_warning_symbol.svg.png"

# ─── CONTRAST & PATIENT CARE ─────────────────────────────────────────────────

# Barium swallow / upper GI
echo "[14/20] Barium swallow..."
curl -sL -o images/barium_swallow.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Barium_swallow.jpg/270px-Barium_swallow.jpg"

# IV contrast injection / angiogram
echo "[15/20] Angiogram..."
curl -sL -o images/angiogram.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Cerebral_angiography%2C_arteria_vertebralis_sinister_injection.JPG/350px-Cerebral_angiography%2C_arteria_vertebralis_sinister_injection.JPG"

# ─── ADDITIONAL ANATOMY X-RAYS ───────────────────────────────────────────────

# Lateral cervical spine
echo "[16/20] Lateral C-spine..."
curl -sL -o images/lateral_cspine.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Cervical_Xray_Lateral.jpg/200px-Cervical_Xray_Lateral.jpg"

# AP pelvis
echo "[17/20] AP pelvis..."
curl -sL -o images/ap_pelvis.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Pelvis_normal_AP.jpg/400px-Pelvis_normal_AP.jpg"

# Lateral knee
echo "[18/20] Lateral knee..."
curl -sL -o images/lateral_knee.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Knee_lateral.jpg/250px-Knee_lateral.jpg"

# PA hand normal
echo "[19/20] PA hand..."
curl -sL -o images/pa_hand.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/X-ray_of_normal_hand_by_dorridge_gp_-_john_osborne.jpg/250px-X-ray_of_normal_hand_by_dorridge_gp_-_john_osborne.jpg"

# Skull PA (Caldwell)
echo "[20/20] Skull PA..."
curl -sL -o images/skull_pa.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Medical_X-Ray_imaging_ALP02_nevridge.jpg/250px-Medical_X-Ray_imaging_ALP02_nevridge.jpg"

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "Download complete!"
echo ""

# Check which files actually downloaded successfully
SUCCESS=0
FAIL=0
for f in images/xray_tube_diagram.png images/c_arm.jpg images/ct_scanner.jpg \
         images/em_spectrum.png images/pneumothorax.jpg images/pleural_effusion.jpg \
         images/pneumonia.jpg images/colles_fracture.jpg images/hip_fracture.jpg \
         images/scoliosis.jpg images/bowel_obstruction.jpg images/film_badge.jpg \
         images/radiation_symbol.png images/barium_swallow.jpg images/angiogram.jpg \
         images/lateral_cspine.jpg images/ap_pelvis.jpg images/lateral_knee.jpg \
         images/pa_hand.jpg images/skull_pa.jpg; do
    if [ -s "$f" ]; then
        SUCCESS=$((SUCCESS + 1))
        echo "  ✓ $f"
    else
        FAIL=$((FAIL + 1))
        echo "  ✗ $f (FAILED — may need manual download)"
    fi
done

echo ""
echo "$SUCCESS succeeded, $FAIL failed"
echo ""
echo "Some URLs may have changed on Wikimedia. For any failures:"
echo "  1. Search commons.wikimedia.org for the subject"
echo "  2. Download to images/ with the same filename"
echo ""
echo "Once images are ready, run:"
echo "  python3 add_image_questions.py"
echo "  git add images/ questions.json index.html"
echo "  git commit -m 'Add image-based questions with real medical images'"
echo "  git push origin main"
