import random
import pandas as pd
import streamlit as st

st.set_page_config(page_title="ARRT Radiography Prep", layout="centered")

@st.cache_data
def load_bank(path: str):
    df = pd.read_csv(path)
    df["correct_option"] = df["correct_option"].astype(str).str.strip().str.upper()
    return df

def start_exam(df, n, category):
    if category != "(All)":
        df = df[df["major_category"] == category]
    ids = list(df.index)
    random.shuffle(ids)
    ids = ids[:min(n, len(ids))]
    st.session_state.exam_ids = ids
    st.session_state.i = 0
    st.session_state.answers = {}
    st.session_state.submitted = set()
    st.session_state.score = 0

# ---- Config ----
CSV_PATH = "RAD_2022_Jan_plus_Sprint200.csv"

df = load_bank(CSV_PATH)

st.title("ARRT Radiography — Exam MVP")

cats = ["(All)"] + sorted(df["major_category"].dropna().unique().tolist())
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
st.caption(f"{q.get('major_category','')} • {q.get('subcategory','')}")

st.markdown(q["stem"])

opts = {"A": q["option_a"], "B": q["option_b"], "C": q["option_c"], "D": q["option_d"]}
prev = st.session_state.answers.get(qid, None)
choice = st.radio(
    "Choose one:",
    ["A","B","C","D"],
    format_func=lambda k: f"{k}. {opts[k]}",
    index=(["A","B","C","D"].index(prev) if prev else 0),
    key=f"pick_{qid}",
)
st.session_state.answers[qid] = choice

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Submit"):
        if qid not in st.session_state.submitted:
            st.session_state.submitted.add(qid)
            if choice == q["correct_option"]:
                st.session_state.score += 1

with c2:
    if st.button("Previous", disabled=(i==0)):
        st.session_state.i -= 1
        st.rerun()

with c3:
    if st.button("Next", disabled=(i==len(exam_ids)-1)):
        st.session_state.i += 1
        st.rerun()

if qid in st.session_state.submitted:
    correct = q["correct_option"]
    if choice == correct:
        st.success("Correct ✅")
    else:
        st.error(f"Incorrect ❌  Correct: **{correct}**")
    if isinstance(q.get("explanation",""), str) and q["explanation"].strip():
        st.info(q["explanation"])

answered = len(st.session_state.submitted)
st.progress(answered / len(exam_ids))
st.write(f"Score: **{st.session_state.score} / {answered}**")

if answered == len(exam_ids):
    st.divider()
    st.subheader("Done")
    st.write(f"Final: **{st.session_state.score} / {len(exam_ids)}**")
