#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# ARRT Exam MVP — Download Public Domain Medical Images
# ═══════════════════════════════════════════════════════════════════════════════
# Run this on your Mac:
#   cd /Users/jaredmaligacedar/arrt_exam_mvp
#   chmod +x download_images.sh
#   ./download_images.sh
#
# Uses the Wikimedia COMMONS API (not en.wikipedia) to get current image URLs.
# Sources: Wikimedia Commons (public domain / CC licensed medical images)
# ═══════════════════════════════════════════════════════════════════════════════

set -e
mkdir -p images

# Wikimedia blocks requests without a proper User-Agent
UA="ARRTExamMVP/1.0 (https://github.com/jaredcedar-hue/mvpexam; educational project) curl"

# Helper: download from Wikimedia Commons using the COMMONS API to get the real URL
# Usage: wiki_dl "File:Example.jpg" "local_filename.jpg" [width]
wiki_dl() {
    local file_title="$1"
    local local_name="$2"
    local width="${3:-800}"

    # IMPORTANT: Use commons.wikimedia.org (NOT en.wikipedia.org)
    # Many medical images only exist on Commons, not on English Wikipedia
    local api_url="https://commons.wikimedia.org/w/api.php?action=query&titles=${file_title}&prop=imageinfo&iiprop=url&iiurlwidth=${width}&format=json"
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
echo "Using Wikimedia Commons API for reliable URLs..."
echo ""

# ─── X-RAY EQUIPMENT & PHYSICS ───────────────────────────────────────────────
echo "=== Equipment & Physics ==="
wiki_dl "File:Roentgen-Roehre.svg" "xray_tube_diagram.png" 800
wiki_dl "File:Mobile_X-ray_machine.jpg" "c_arm.jpg" 600
wiki_dl "File:Lachine_Hospital_CT_Scanner.jpg" "ct_scanner.jpg" 800
wiki_dl "File:EM_Spectrum_Properties_edit.svg" "em_spectrum.png" 900

echo ""
echo "=== Chest Pathology ==="
wiki_dl "File:Pneumothorax_CXR.jpg" "pneumothorax.jpg" 500
wiki_dl "File:Pleural_effusion.jpg" "pleural_effusion.jpg" 500
wiki_dl "File:Pneumonia_x-ray.jpg" "pneumonia.jpg" 500

echo ""
echo "=== Fractures ==="
wiki_dl "File:Colles_fracture.JPG" "colles_fracture.jpg" 400
wiki_dl "File:X-ray_of_a_comminuted_hip_fracture.jpg" "hip_fracture.jpg" 500
wiki_dl "File:Scoliosis.jpg" "scoliosis.jpg" 400

echo ""
echo "=== Abdomen ==="
wiki_dl "File:Upright_X-ray_demonstrating_small_bowel_obstruction.jpg" "bowel_obstruction.jpg" 500

echo ""
echo "=== Radiation Safety ==="
wiki_dl "File:Fast_Neutron_Film_Badge,_extracted_from_A_simplified_film_dosimeter_for_fission_neutrons_(1958).jpg" "film_badge.jpg" 500
wiki_dl "File:Radiation_warning_symbol.svg" "radiation_symbol.png" 600

echo ""
echo "=== Contrast Studies ==="
wiki_dl "File:Barium_swallow.png" "barium_swallow.jpg" 400
wiki_dl "File:Cerebral_angiography,_arteria_vertebralis_sinister_injection.JPG" "angiogram.jpg" 500

echo ""
echo "=== Additional Anatomy ==="
wiki_dl "File:X-ray_of_the_cervical_spine_of_a_20_year_old_male_-_lateral.jpg" "lateral_cspine.jpg" 400
wiki_dl "File:Boy_pelvic_x-ray_pic.jpg" "ap_pelvis.jpg" 500
wiki_dl "File:Radiograph_with_knee_angles.jpg" "lateral_knee.jpg" 400
wiki_dl "File:Two_hands,_viewed_through_x-ray._Photoprint_from_radiograph_Wellcome_L0013210.jpg" "pa_hand.jpg" 500
wiki_dl "File:Lateral_projectional_radiograph_scan_of_skull.jpg" "skull_pa.jpg" 400

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
