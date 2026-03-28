#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# ARRT Exam MVP — Download Public Domain Medical Images
# ═══════════════════════════════════════════════════════════════════════════════
# Run this on your Mac:
#   cd /Users/jaredmaligacedar/arrt_exam_mvp
#   chmod +x download_images.sh
#   ./download_images.sh
#
# Uses the Wikimedia API to get current image URLs (immune to URL changes).
# Sources: Wikimedia Commons (public domain / CC licensed medical images)
# ═══════════════════════════════════════════════════════════════════════════════

set -e
mkdir -p images

# Wikimedia blocks requests without a proper User-Agent
UA="ARRTExamMVP/1.0 (https://github.com/jaredcedar-hue/mvpexam; educational project) curl"

# Helper: download from Wikimedia Commons using the API to get the real URL
# Usage: wiki_dl "File:Example.jpg" "local_filename.jpg" [width]
wiki_dl() {
    local file_title="$1"
    local local_name="$2"
    local width="${3:-800}"

    # Use Wikimedia API to get the thumbnail URL at desired width
    local api_url="https://en.wikipedia.org/w/api.php?action=query&titles=${file_title}&prop=imageinfo&iiprop=url&iiurlwidth=${width}&format=json"
    local img_url=$(curl -sL -A "$UA" "$api_url" | python3 -c "
import sys, json
data = json.load(sys.stdin)
pages = data.get('query',{}).get('pages',{})
for p in pages.values():
    ii = p.get('imageinfo',[{}])[0]
    # Prefer thumbnail at requested width, fallback to original
    print(ii.get('thumburl', ii.get('url', '')))
" 2>/dev/null)

    if [ -n "$img_url" ] && [ "$img_url" != "None" ]; then
        curl -sL -A "$UA" -o "images/$local_name" "$img_url"
        local fsize=$(stat -f%z "images/$local_name" 2>/dev/null || stat -c%s "images/$local_name" 2>/dev/null)
        if [ "$fsize" -gt 5000 ]; then
            echo "  ✓ $local_name (${fsize} bytes)"
            return 0
        fi
    fi
    echo "  ✗ $local_name (FAILED)"
    return 1
}

echo "Downloading public domain medical images for ARRT exam questions..."
echo "Using Wikimedia API for reliable URLs..."
echo ""

# ─── X-RAY EQUIPMENT & PHYSICS ───────────────────────────────────────────────
echo "=== Equipment & Physics ==="
wiki_dl "File:Roentgen-Roehre.svg" "xray_tube_diagram.png" 800
wiki_dl "File:OEC_9800_Plus.jpg" "c_arm.jpg" 600
wiki_dl "File:UPMCEast_CT.jpg" "ct_scanner.jpg" 800
wiki_dl "File:EM_Spectrum_Properties_edit.svg" "em_spectrum.png" 900

echo ""
echo "=== Chest Pathology ==="
wiki_dl "File:Pneumothorax_CXR.jpg" "pneumothorax.jpg" 500
wiki_dl "File:LargePleuralEffusion.jpg" "pleural_effusion.jpg" 500
wiki_dl "File:Pneumonia_x-ray.jpg" "pneumonia.jpg" 500

echo ""
echo "=== Fractures ==="
wiki_dl "File:Colles_fracture.JPG" "colles_fracture.jpg" 400
wiki_dl "File:Hip_fracture_-_trochanteric.jpg" "hip_fracture.jpg" 500
wiki_dl "File:Scoliosis_patient_in_cheneau_brace_correcting_from_56_to_27_degrees.jpg" "scoliosis.jpg" 400

echo ""
echo "=== Abdomen ==="
wiki_dl "File:Small_bowel_obstruction.jpg" "bowel_obstruction.jpg" 500

echo ""
echo "=== Radiation Safety ==="
wiki_dl "File:Film_badge_dosimeter.jpg" "film_badge.jpg" 500
wiki_dl "File:Radiation_warning_symbol.svg" "radiation_symbol.png" 600

echo ""
echo "=== Contrast Studies ==="
wiki_dl "File:Barium_swallow.jpg" "barium_swallow.jpg" 400
wiki_dl "File:Cerebral_angiography,_arteria_vertebralis_sinister_injection.JPG" "angiogram.jpg" 500

echo ""
echo "=== Additional Anatomy ==="
wiki_dl "File:Cervical_Xray_Lateral.jpg" "lateral_cspine.jpg" 400
wiki_dl "File:Pelvis_normal_AP.jpg" "ap_pelvis.jpg" 500
wiki_dl "File:Knee_lateral.jpg" "lateral_knee.jpg" 400
wiki_dl "File:X-ray_of_normal_hand_by_dorridge_gp_-_john_osborne.jpg" "pa_hand.jpg" 400
wiki_dl "File:Medical_X-Ray_imaging_ALP02_nevridge.jpg" "skull_pa.jpg" 400

echo ""
echo "═══════════════════════════════════════════════════════════════"

# Count successes
SUCCESS=0
FAIL=0
for f in images/xray_tube_diagram.png images/c_arm.jpg images/ct_scanner.jpg \
         images/em_spectrum.png images/pneumothorax.jpg images/pleural_effusion.jpg \
         images/pneumonia.jpg images/colles_fracture.jpg images/hip_fracture.jpg \
         images/scoliosis.jpg images/bowel_obstruction.jpg images/film_badge.jpg \
         images/radiation_symbol.png images/barium_swallow.jpg images/angiogram.jpg \
         images/lateral_cspine.jpg images/ap_pelvis.jpg images/lateral_knee.jpg \
         images/pa_hand.jpg images/skull_pa.jpg; do
    if [ -f "$f" ]; then
        fsize=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
        if [ "$fsize" -gt 5000 ]; then
            SUCCESS=$((SUCCESS + 1))
        else
            FAIL=$((FAIL + 1))
        fi
    else
        FAIL=$((FAIL + 1))
    fi
done

echo ""
echo "$SUCCESS of 20 images downloaded successfully, $FAIL failed"
echo ""
if [ "$FAIL" -gt 0 ]; then
    echo "For failures, the Wikimedia filename may have changed."
    echo "Search commons.wikimedia.org and save replacements to images/"
    echo "with the same local filename."
    echo ""
fi
echo "Next: python3 add_image_questions.py"
echo "      git add images/ questions.json index.html"
echo "      git commit -m 'Add image-based questions with medical images'"
echo "      git push origin main"
