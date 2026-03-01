import os
import random
import pandas as pd
import streamlit as st

st.set_page_config(page_title="ARRT Radiography Prep", layout="centered")

# ---- Config ----
CSV_PATH = "RAD_2022_Jan_plus_Sprint1150_MULTISEL.csv"  # update if your bank filename differs

SINGLE_TYPES = {"single", "mcq", "multiple_choice", ""}
MULTI_TYPES = {"multi", "multiple_response", "select_all"}

@st.cache_data
def load_bank(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Required for legacy banks
    required = ["item_id","stem","option_a","option_b","option_c","option_d"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Add new-schema columns if absent
    if "question_type" not in df.columns:
        df["question_type"] = "single"
    if "correct_options" not in df.columns:
        # fallback to correct_option for legacy
        df["correct_options"] = df.get("correct_option", "")
    if "correct_option" not in df.columns:
        df["correct_option"] = ""

    # Normalize
    df["item_id"] = df["item_id"].astype(str).str.strip()
    df["question_type"] = df["question_type"].astype(str).str.strip().str.lower()
    df["correct_option"] = df["correct_option"].astype(str).str.strip().str.upper()
    df["correct_options"] = df["correct_options"].astype(str).str.strip().str.upper()
    if "image_path" not in df.columns:
        df["image_path"] = ""

    # Index by item_id so qids are stable strings (avoids KeyError on RangeIndex)
    df = df.set_index("item_id", drop=False)
    return df

def is_multi(qtype: str) -> bool:
    qtype = (qtype or "").strip().lower()
    return qtype in MULTI_TYPES

def parse_correct_set(row) -> set:
    # Multi: A|C|D ; Single fallback to correct_option
    s = (row.get("correct_options") or "").strip().upper()
    if s:
        parts = [p.strip() for p in s.split("|") if p.strip()]
        return set(parts)
    one = (row.get("correct_option") or "").strip().upper()
    return {one} if one else set()

def start_exam(df: pd.DataFrame, n: int, category: str):
    work = df
    if category != "(All)" and "major_category" in work.columns:
        work = work[work["major_category"] == category]

    qids = work["item_id"].tolist()
    random.shuffle(qids)
    qids = qids[:min(n, len(qids))]

    st.session_state.exam_ids = qids
    st.session_state.i = 0
    st.session_state.answers = {}      # {item_id: "A" or ["A","C"]}
    st.session_state.submitted = set() # set(item_id)
    st.session_state.score = 0

df = load_bank(CSV_PATH)

st.title("ARRT Radiography — Exam MVP (Multi-select enabled)")

cats = ["(All)"] + (sorted(df["major_category"].dropna().unique().tolist()) if "major_category" in df.columns else [])

with st.sidebar:
    st.header("Build exam")
    category = st.selectbox("Category", cats)
    n = st.slider("Questions", 10, 220, 25, step=5)
    if st.button("Start / Restart"):
        start_exam(df, n, category)

if "exam_ids" not in st.session_state:
    start_exam(df, 25, "(All)")

exam_ids = st.session_state.exam_ids
i = st.session_state.i
qid = exam_ids[i]
q = df.loc[qid]

st.write(f"**Question {i+1} / {len(exam_ids)}**")
if "major_category" in q.index:
    st.caption(f"{q.get('major_category','')} • {q.get('subcategory','')}")

# Optional image
img_val = q.get("image_path", "")
img_path = "" if pd.isna(img_val) else str(img_val).strip()

if img_path:
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    # optional: else do nothing (I recommend this for now)

st.markdown(str(q["stem"]))

opts = {
    "A": str(q["option_a"]),
    "B": str(q["option_b"]),
    "C": str(q["option_c"]),
    "D": str(q["option_d"]),
}

qtype = str(q.get("question_type","single"))
is_multi_item = is_multi(qtype)

# ---- Answer UI ----
if is_multi_item:
    prev = st.session_state.answers.get(qid, [])
    if not isinstance(prev, list):
        prev = []
    choices = st.multiselect(
        "Select all that apply:",
        ["A","B","C","D"],
        default=prev,
        format_func=lambda k: f"{k}. {opts[k]}",
        key=f"multi_{qid}",
    )
    # Save selections (even empty is fine; submission will guard)
    st.session_state.answers[qid] = choices
else:
    prev = st.session_state.answers.get(qid, None)
    # No default selection until user chooses
    if prev in ["A","B","C","D"]:
        idx = ["A","B","C","D"].index(prev)
    else:
        idx = None
    choice = st.radio(
        "Choose one:",
        ["A","B","C","D"],
        index=idx,
        format_func=lambda k: f"{k}. {opts[k]}",
        key=f"single_{qid}",
    )
    if choice is not None:
        st.session_state.answers[qid] = choice

# ---- Nav / Submit ----
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Submit", use_container_width=True):
        if qid in st.session_state.submitted:
            st.info("Already submitted.")
        else:
            if is_multi_item:
                sel = st.session_state.answers.get(qid, [])
                if not sel:
                    st.warning("Select at least one answer before submitting.")
                else:
                    st.session_state.submitted.add(qid)
                    correct = parse_correct_set(q)
                    if set(sel) == correct:
                        st.session_state.score += 1
            else:
                sel = st.session_state.answers.get(qid, None)
                if sel is None:
                    st.warning("Pick an answer before submitting.")
                else:
                    st.session_state.submitted.add(qid)
                    correct = parse_correct_set(q)
                    if sel in correct:
                        st.session_state.score += 1

with c2:
    if st.button("Previous", disabled=(i == 0), use_container_width=True):
        st.session_state.i -= 1
        st.rerun()

with c3:
    if st.button("Next", disabled=(i == len(exam_ids) - 1), use_container_width=True):
        st.session_state.i += 1
        st.rerun()

# ---- Feedback ----
if qid in st.session_state.submitted:
    correct = parse_correct_set(q)
    if is_multi_item:
        sel = st.session_state.answers.get(qid, [])
        if set(sel) == correct:
            st.success("Correct ✅")
        else:
            st.error(f"Incorrect ❌  Correct: **{' + '.join(sorted(correct))}**")
    else:
        sel = st.session_state.answers.get(qid, None)
        if sel in correct:
            st.success("Correct ✅")
        else:
            st.error(f"Incorrect ❌  Correct: **{next(iter(correct)) if correct else ''}**")

    expl = str(q.get("explanation","") or "").strip()
    if expl:
        st.info(expl)

answered = len(st.session_state.submitted)
st.progress(answered / len(exam_ids))
st.write(f"Score: **{st.session_state.score} / {answered}**")

if answered == len(exam_ids):
    st.divider()
    st.subheader("Done")
    st.write(f"Final: **{st.session_state.score} / {len(exam_ids)}**")
