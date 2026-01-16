"""
Page 2: Edit Content - Modern Premium Design
Edit I Do, We Do, You Do, and Exit Ticket content
"""
import streamlit as st

st.set_page_config(
    page_title="Edit Content",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern Premium CSS with Dark Theme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Base styling with dark gradient background */
    .stApp {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 25%, #16213e 50%, #0f3460 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1100px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Page header */
    .page-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .page-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #a78bfa 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .page-subtitle {
        color: rgba(255, 255, 255, 0.6);
        font-size: 1.1rem;
    }
    
    /* Section Headers */
    .section-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin: 2rem 0 1rem 0;
    }
    
    .section-icon {
        font-size: 2rem;
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.15));
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 14px;
    }
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
    }
    
    .section-caption {
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.9rem;
        margin-top: 0.25rem;
    }
    
    /* Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }
    
    /* Tier Cards */
    .tier-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        padding: 1.25rem;
        height: 100%;
        transition: all 0.3s ease;
    }
    
    .tier-bronze {
        border: 1px solid rgba(205, 127, 50, 0.3);
    }
    
    .tier-bronze:hover {
        border-color: rgba(205, 127, 50, 0.5);
        background: rgba(205, 127, 50, 0.1);
    }
    
    .tier-silver {
        border: 1px solid rgba(192, 192, 192, 0.3);
    }
    
    .tier-silver:hover {
        border-color: rgba(192, 192, 192, 0.5);
        background: rgba(192, 192, 192, 0.1);
    }
    
    .tier-gold {
        border: 1px solid rgba(255, 215, 0, 0.3);
    }
    
    .tier-gold:hover {
        border-color: rgba(255, 215, 0, 0.5);
        background: rgba(255, 215, 0, 0.1);
    }
    
    .tier-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Primary Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        padding: 0.875rem 2rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.35) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 12px 40px rgba(99, 102, 241, 0.45) !important;
    }
    
    /* Secondary Button */
    div[data-testid="column"]:first-child .stButton > button {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
    }
    
    div[data-testid="column"]:first-child .stButton > button:hover {
        background: rgba(255, 255, 255, 0.15) !important;
        border-color: rgba(99, 102, 241, 0.4) !important;
    }
    
    /* Text Input Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        padding: 0.875rem !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        font-weight: 600 !important;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: rgba(99, 102, 241, 0.3) !important;
        background: rgba(99, 102, 241, 0.1) !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-top: none !important;
        border-radius: 0 0 12px 12px !important;
    }
    
    /* Label Styling */
    .stTextInput label,
    .stTextArea label {
        color: rgba(255, 255, 255, 0.7) !important;
        font-weight: 500 !important;
    }
    
    /* Warning/Success boxes */
    .stAlert {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
    }
    
    /* Modern Divider */
    .modern-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        margin: 2rem 0;
        border: none;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.9rem;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="page-header">
    <h1 class="page-title">✏️ Edit Lesson Content</h1>
    <p class="page-subtitle">Customise your lesson sections</p>
</div>
""", unsafe_allow_html=True)

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

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# I Do Section
st.markdown("""
<div class="section-header">
    <div class="section-icon">👁️</div>
    <div>
        <div class="section-title">I Do (Teacher Modelling)</div>
        <div class="section-caption">Explicit instruction - model the skill step by step</div>
    </div>
</div>
""", unsafe_allow_html=True)

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

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# We Do Section
st.markdown("""
<div class="section-header">
    <div class="section-icon">👥</div>
    <div>
        <div class="section-title">We Do (Guided Practice)</div>
        <div class="section-caption">Scaffolded practice - work through together with class</div>
    </div>
</div>
""", unsafe_allow_html=True)

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

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# You Do Section
st.markdown("""
<div class="section-header">
    <div class="section-icon">🎯</div>
    <div>
        <div class="section-title">You Do (Independent Practice)</div>
        <div class="section-caption">Differentiated tasks - Bronze (Grade 5), Silver (Grade 7), Gold (Grade 9)</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="tier-card tier-bronze">
        <div class="tier-title">🥉 Bronze (Grade 5)</div>
    </div>
    """, unsafe_allow_html=True)
    bronze_q = st.text_area("Question", key="bronze_q", height=100, placeholder="Basic application...")
    bronze_a = st.text_input("Answer", key="bronze_a", placeholder="Answer")

with col2:
    st.markdown("""
    <div class="tier-card tier-silver">
        <div class="tier-title">🥈 Silver (Grade 7)</div>
    </div>
    """, unsafe_allow_html=True)
    silver_q = st.text_area("Question", key="silver_q", height=100, placeholder="Intermediate application...")
    silver_a = st.text_input("Answer", key="silver_a", placeholder="Answer")

with col3:
    st.markdown("""
    <div class="tier-card tier-gold">
        <div class="tier-title">🥇 Gold (Grade 9)</div>
    </div>
    """, unsafe_allow_html=True)
    gold_q = st.text_area("Question", key="gold_q", height=100, placeholder="Advanced/extension...")
    gold_a = st.text_input("Answer", key="gold_a", placeholder="Answer")

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# Affirmative Checking
st.markdown("""
<div class="section-header">
    <div class="section-icon">✔️</div>
    <div>
        <div class="section-title">Affirmative Checking</div>
        <div class="section-caption">Exam-style question with mark scheme</div>
    </div>
</div>
""", unsafe_allow_html=True)

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

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# Exit Ticket
st.markdown("""
<div class="section-header">
    <div class="section-icon">🎟️</div>
    <div>
        <div class="section-title">Exit Ticket</div>
        <div class="section-caption">Quick check of the Learning Outcome (skill application, not just recall)</div>
    </div>
</div>
""", unsafe_allow_html=True)

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

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

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
