"""
Page 2: Edit Content
Edit I Do, We Do, You Do, and Exit Ticket content
"""
import streamlit as st

st.set_page_config(page_title="Edit Content", page_icon="✏️", layout="wide")

st.markdown("# ✏️ Edit Lesson Content")

# Check if lesson data exists
if 'lesson_data' not in st.session_state or not st.session_state.lesson_data:
    st.warning("⚠️ No lesson data found. Please create a lesson first.")
    if st.button("← Go to Create Lesson"):
        st.switch_page("pages/1_Create_Lesson.py")
    st.stop()

lesson = st.session_state.lesson_data

# Display summary
with st.expander("📋 Lesson Summary", expanded=False):
    st.markdown(f"**Subject:** {lesson.get('subject', 'N/A')}")
    st.markdown(f"**Topic:** {lesson.get('topic', 'N/A')}")
    st.markdown(f"**Curriculum:** {lesson.get('curriculum', 'N/A')}")
    st.markdown(f"**Learning Outcome:** {lesson.get('learning_outcome', 'N/A')}")

st.markdown("---")

# I Do Section
st.markdown("## 👁️ I Do (Teacher Modelling)")
st.caption("Explicit instruction - model the skill step by step")

i_do_title = st.text_input(
    "I Do Title",
    value=lesson.get('i_do_title', f"Modelling: {lesson.get('topic', '')}"),
    key="i_do_title"
)

i_do_content = st.text_area(
    "I Do Content",
    value=lesson.get('i_do_content', ''),
    height=200,
    placeholder="Enter step-by-step modelling content...\n\nExample:\nStep 1: Identify the known values\nStep 2: Write the formula\nStep 3: Substitute and calculate",
    key="i_do_content"
)

st.markdown("---")

# We Do Section
st.markdown("## 👥 We Do (Guided Practice)")
st.caption("Scaffolded practice - work through together with class")

we_do_question = st.text_area(
    "We Do Question",
    value=lesson.get('we_do_question', ''),
    height=100,
    placeholder="Enter a scaffolded practice question...",
    key="we_do_question"
)

we_do_steps = st.text_area(
    "We Do Steps/Scaffolding",
    value=lesson.get('we_do_steps', ''),
    height=150,
    placeholder="Enter scaffolding steps (one per line)...\n\nExample:\n• Step 1: Calculate moles of known\n• Step 2: Use ratio to find moles of unknown\n• Step 3: Calculate concentration",
    key="we_do_steps"
)

st.markdown("---")

# You Do Section
st.markdown("## 🎯 You Do (Independent Practice)")
st.caption("Differentiated tasks - Bronze (Grade 5), Silver (Grade 7), Gold (Grade 9)")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🥉 Bronze (Grade 5)")
    bronze_q = st.text_area("Question", key="bronze_q", height=100, placeholder="Basic application...")
    bronze_a = st.text_input("Answer", key="bronze_a", placeholder="Answer")

with col2:
    st.markdown("### 🥈 Silver (Grade 7)")
    silver_q = st.text_area("Question", key="silver_q", height=100, placeholder="Intermediate application...")
    silver_a = st.text_input("Answer", key="silver_a", placeholder="Answer")

with col3:
    st.markdown("### 🥇 Gold (Grade 9)")
    gold_q = st.text_area("Question", key="gold_q", height=100, placeholder="Advanced/extension...")
    gold_a = st.text_input("Answer", key="gold_a", placeholder="Answer")

st.markdown("---")

# Affirmative Checking
st.markdown("## ✔️ Affirmative Checking")
st.caption("Exam-style question with mark scheme")

exam_question = st.text_area(
    "Exam Question",
    value=lesson.get('exam_question', ''),
    height=100,
    placeholder="Enter an exam-style question (include marks)...",
    key="exam_question"
)

mark_scheme = st.text_area(
    "Mark Scheme",
    value=lesson.get('mark_scheme', ''),
    height=150,
    placeholder="Enter mark scheme (one mark per line)...\n\nExample:\n1. Calculate moles = 0.006 mol\n2. Use ratio 1:2 = 0.012 mol\n3. Calculate concentration = 0.48 mol/dm³",
    key="mark_scheme"
)

st.markdown("---")

# Exit Ticket
st.markdown("## 🎟️ Exit Ticket")
st.caption("Quick check of the Learning Outcome (skill application, not just recall)")

exit_question = st.text_area(
    "Exit Ticket Question",
    value=lesson.get('exit_question', ''),
    height=100,
    placeholder="Enter a quick-check question that tests the skill...",
    key="exit_question"
)

exit_options = st.text_area(
    "Options (if multiple choice)",
    value=lesson.get('exit_options', ''),
    height=100,
    placeholder="A) Option 1\nB) Option 2\nC) Option 3",
    key="exit_options"
)

exit_answer = st.text_input(
    "Correct Answer",
    value=lesson.get('exit_answer', ''),
    placeholder="e.g., B) It will be 1000x too small",
    key="exit_answer"
)

st.markdown("---")

# Save and Continue
col1, col2 = st.columns(2)

with col1:
    if st.button("← Back to Create Lesson", use_container_width=True):
        st.switch_page("pages/1_Create_Lesson.py")

with col2:
    if st.button("Save & Export →", type="primary", use_container_width=True):
        # Save content to session state
        st.session_state.lesson_data.update({
            'i_do_title': i_do_title,
            'i_do_content': i_do_content,
            'we_do_question': we_do_question,
            'we_do_steps': we_do_steps,
            'you_do_tasks': [
                {'name': 'Bronze (Grade 5)', 'question': bronze_q, 'answer': bronze_a},
                {'name': 'Silver (Grade 7)', 'question': silver_q, 'answer': silver_a},
                {'name': 'Gold (Grade 9)', 'question': gold_q, 'answer': gold_a}
            ],
            'exam_question': exam_question,
            'mark_scheme': mark_scheme,
            'exit_question': exit_question,
            'exit_options': exit_options,
            'exit_answer': exit_answer
        })
        st.success("✅ Content saved!")
        st.switch_page("pages/3_Export.py")
