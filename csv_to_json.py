#!/usr/bin/env python3
"""Convert ARRT question bank CSV to optimized JSON for the web app."""

import csv
import json
import sys

INPUT_CSV = "RAD_2022_Jan_plus_Sprint1150_MULTISEL.csv"
OUTPUT_JSON = "questions.json"

def convert():
    questions = []
    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            q_type = (row.get("question_type") or "single").strip().lower()
            if q_type in ("multi", "multiple_response", "select_all"):
                q_type = "multi"
            else:
                q_type = "single"

            correct = (row.get("correct_option") or "").strip().upper()
            correct_multi = (row.get("correct_options") or "").strip().upper()

            # For multi-select, parse pipe-delimited answers
            if q_type == "multi" and correct_multi:
                cm = sorted([x.strip() for x in correct_multi.split("|") if x.strip()])
            elif correct:
                cm = [correct]
            else:
                cm = []

            # Collect non-empty tags
            tags = []
            for tag_col in ["tags_anatomy_region", "tags_physics_concept",
                            "tags_positioning_theme", "tags_clinical_concept",
                            "tags_imaging_system"]:
                val = (row.get(tag_col) or "").strip()
                if val:
                    tags.append(val)

            difficulty = 1
            try:
                difficulty = int(row.get("difficulty", 1))
            except (ValueError, TypeError):
                pass

            questions.append({
                "id": row.get("item_id", "").strip(),
                "cat": row.get("major_category", "").strip(),
                "sub": row.get("subcategory", "").strip(),
                "diff": difficulty,
                "type": q_type,
                "stem": row.get("stem", "").strip(),
                "opts": {
                    "A": (row.get("option_a") or "").strip(),
                    "B": (row.get("option_b") or "").strip(),
                    "C": (row.get("option_c") or "").strip(),
                    "D": (row.get("option_d") or "").strip(),
                },
                "ans": cm,
                "exp": (row.get("explanation") or "").strip(),
                "tags": tags,
            })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(questions, f, separators=(",", ":"))

    print(f"Converted {len(questions)} questions -> {OUTPUT_JSON}")

if __name__ == "__main__":
    convert()
