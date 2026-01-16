"""
Page 1: Create Lesson
Professional two-option workflow with Modern Premium Design
"""
import streamlit as st
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.curriculum_data import AQA_GCSE_CURRICULA, get_topics_list, get_subtopic_content
from core.chemistry_lessons import get_lesson_content as get_chemistry_lesson, get_available_lessons as get_chemistry_available
from core.science_lessons import get_biology_lesson, get_physics_lesson, get_available_biology_lessons, get_available_physics_lessons
from core.expanded_lessons import get_expanded_lesson
from core.aqa_curriculum import get_related_practicals


def get_all_available_lessons(subject: str, subtopic_id: str) -> list:
    """Get available lessons for any subject."""
    if subject == "Chemistry":
        return get_chemistry_available(subtopic_id)
    elif subject == "Biology":
        return get_available_biology_lessons(subtopic_id)
    elif subject == "Physics":
        return get_available_physics_lessons(subtopic_id)
    return []


def get_lesson_data(subject: str, subtopic_id: str, lesson_num: int) -> dict:
    """Get lesson content for any subject."""
    expanded = get_expanded_lesson(subject, subtopic_id, lesson_num)
    if expanded:
        return expanded
    
    if subject == "Chemistry":
        return get_chemistry_lesson(subtopic_id, lesson_num)
    elif subject == "Biology":
        return get_biology_lesson(subtopic_id, lesson_num)
    elif subject == "Physics":
        return get_physics_lesson(subtopic_id, lesson_num)
    return None


def generate_pptx(lesson_data: dict) -> bytes:
    """Generate PowerPoint from lesson data and return as bytes."""
    from core.pptx_builder import TLAGPowerPointBuilder
    import io
    
    template_path = "templates/WSO Learn Like A GEM Template (1).pptx"
    if not os.path.exists(template_path):
        template_path = "WSO Learn Like A GEM Template (1).pptx"
    
    builder = TLAGPowerPointBuilder(template_path)
    builder.create_presentation()
    
    builder.add_do_now(
        lesson_data.get('do_now', {}).get('questions', []),
        lesson_data.get('do_now', {}).get('answers', [])
    )
    
    builder.add_outcomes(
        lesson_data.get('learning_outcome', ''),
        lesson_data.get('to_know', [])
    )
    
    i_do_data = lesson_data.get('i_do', {})
    if i_do_data.get('examples') or i_do_data.get('key_points') or i_do_data.get('definitions') or i_do_data.get('facts'):
        builder.add_i_do_slides(i_do_data)
    else:
        builder.add_i_do(i_do_data.get('title', 'I Do'), i_do_data.get('content', []))
    
    we_do_data = lesson_data.get('we_do', {})
    if we_do_data.get('examples'):
        builder.add_we_do_slides(we_do_data)
    else:
        builder.add_we_do("Practice", we_do_data.get('question', ''), we_do_data.get('steps', []))
    
    builder.add_you_do_slides(lesson_data.get('you_do', []))
    
    aff_check = lesson_data.get('affirmative_checking', {})
    if aff_check:
        builder.add_affirmative_checking(aff_check.get('checkpoint', ''), aff_check.get('action', ''))
    
    exit_data = lesson_data.get('exit_ticket', {})
    builder.add_exit_ticket(exit_data.get('question', ''), exit_data.get('options', []), exit_data.get('answer', ''))
    
    buffer = io.BytesIO()
    builder.prs.save(buffer)
    buffer.seek(0)
    return buffer.getvalue()


# Page configuration
st.set_page_config(
    page_title="Create Lesson | GEMS TLAG",
    page_icon="📝",
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
        max-width: 1200px;
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
    
    /* Mode Selection Cards */
    .mode-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        height: 100%;
    }
    
    .mode-card:hover {
        transform: translateY(-5px);
        border-color: rgba(99, 102, 241, 0.4);
        background: rgba(99, 102, 241, 0.1);
    }
    
    .mode-card.active {
        border-color: #6366f1;
        background: linear-gradient(145deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.1));
        box-shadow: 0 0 30px rgba(99, 102, 241, 0.3);
    }
    
    .mode-icon {
        font-size: 2.5rem;
        display: block;
        margin-bottom: 0.75rem;
    }
    
    .mode-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    .mode-desc {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.5);
        line-height: 1.4;
    }
    
    /* Step Headers */
    .step-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin: 2rem 0 1.5rem 0;
    }
    
    .step-badge {
        background: linear-gradient(135deg, #6366f1, #a855f7);
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    
    .step-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #ffffff;
    }
    
    /* Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .glass-card-header {
        font-size: 1rem;
        font-weight: 600;
        color: #a78bfa;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Preview Section */
    .preview-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.5rem 0;
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.95rem;
    }
    
    .preview-icon {
        color: #10b981;
    }
    
    /* Content Card */
    .content-card {
        background: linear-gradient(145deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05));
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 16px;
        padding: 1.25rem;
    }
    
    .content-label {
        font-size: 0.8rem;
        color: rgba(255, 255, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .content-value {
        color: #ffffff;
        font-size: 1rem;
        line-height: 1.5;
    }
    
    /* Primary Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        padding: 1rem 2rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 
            0 10px 40px rgba(99, 102, 241, 0.4),
            0 4px 12px rgba(0, 0, 0, 0.2) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 
            0 20px 60px rgba(99, 102, 241, 0.5),
            0 8px 20px rgba(0, 0, 0, 0.25) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(0.98) !important;
    }
    
    /* Download Button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        font-weight: 600 !important;
        padding: 1rem 2rem !important;
        box-shadow: 
            0 10px 40px rgba(16, 185, 129, 0.4),
            0 4px 12px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.4s ease !important;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 
            0 20px 60px rgba(16, 185, 129, 0.5),
            0 8px 20px rgba(0, 0, 0, 0.25) !important;
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: white !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(99, 102, 241, 0.4) !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        background: transparent !important;
        color: white !important;
    }
    
    /* Text Input Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        padding: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        font-weight: 600 !important;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: rgba(99, 102, 241, 0.3) !important;
        background: rgba(99, 102, 241, 0.1) !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-top: none !important;
        border-radius: 0 0 14px 14px !important;
    }
    
    /* Alert Boxes */
    .stAlert {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Success Message */  
    [data-testid="stAlert"][data-baseweb="notification"] {
        background: rgba(16, 185, 129, 0.15) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
    }
    
    /* Info Message */
    .stInfo {
        background: rgba(99, 102, 241, 0.15) !important;
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
    }
    
    /* Modern Divider */
    .modern-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        margin: 2rem 0;
        border: none;
    }
    
    /* Label styling */
    .stSelectbox label,
    .stTextInput label,
    .stTextArea label {
        color: rgba(255, 255, 255, 0.7) !important;
        font-weight: 500 !important;
    }
    
    /* Success indicator */
    .success-badge {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.1));
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 12px;
        padding: 0.75rem 1.25rem;
        color: #10b981;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-bottom: 2rem;
    }
    
    /* Metric override */
    [data-testid="stMetricValue"] {
        color: #a78bfa !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'mode' not in st.session_state:
    st.session_state.mode = "quick"
if 'edited_lesson' not in st.session_state:
    st.session_state.edited_lesson = {}
if 'pptx_ready' not in st.session_state:
    st.session_state.pptx_ready = None

# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div class="page-header">
    <h1 class="page-title">📝 Create Your Lesson</h1>
    <p class="page-subtitle">Generate professional TLAG PowerPoints in seconds</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# MODE SELECTION
# ============================================================================
st.markdown("""
<div class="step-header">
    <div class="step-badge">0</div>
    <span class="step-title">Choose Your Workflow</span>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    quick_class = "active" if st.session_state.mode == "quick" else ""
    st.markdown(f"""
    <div class="mode-card {quick_class}">
        <span class="mode-icon">⚡</span>
        <div class="mode-title">Quick Download</div>
        <div class="mode-desc">Select a ready-made lesson and download instantly. Best for complete lessons with no changes.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Select Quick Mode", use_container_width=True, key="quick_btn"):
        st.session_state.mode = "quick"
        st.session_state.pptx_ready = None
        st.rerun()

with col2:
    custom_class = "active" if st.session_state.mode == "custom" else ""
    st.markdown(f"""
    <div class="mode-card {custom_class}">
        <span class="mode-icon">✏️</span>
        <div class="mode-title">Customise First</div>
        <div class="mode-desc">Edit lesson content before generating. Best for tailoring lessons to your class needs.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Select Custom Mode", use_container_width=True, key="custom_btn"):
        st.session_state.mode = "custom"
        st.session_state.pptx_ready = None
        st.rerun()

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# STEP 1: TOPIC SELECTION
# ============================================================================
st.markdown("""
<div class="step-header">
    <div class="step-badge">1</div>
    <span class="step-title">Select Your Topic</span>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    subject = st.selectbox("Subject", ["Chemistry", "Biology", "Physics"], index=0)

# Get topics
curriculum_data = AQA_GCSE_CURRICULA.get(subject, {})
topics = curriculum_data.get("topics", {})
topic_options = {f"{k}: {v['name']}": k for k, v in topics.items()}

with col2:
    selected_topic = st.selectbox(
        "Topic",
        list(topic_options.keys()) if topic_options else ["No topics available"]
    )

# Get subtopics
topic_id = topic_options.get(selected_topic) if topic_options else None
subtopics = topics.get(topic_id, {}).get("subtopics", {}) if topic_id else {}
subtopic_options = {f"{k}: {v['name']}": k for k, v in subtopics.items()}

with col3:
    selected_subtopic = st.selectbox(
        "Subtopic",
        list(subtopic_options.keys()) if subtopic_options else ["No subtopics available"]
    )

subtopic_id = subtopic_options.get(selected_subtopic) if subtopic_options else None

# ============================================================================
# STEP 2: LESSON SELECTION
# ============================================================================
st.markdown("""
<div class="step-header">
    <div class="step-badge">2</div>
    <span class="step-title">Choose a Lesson</span>
</div>
""", unsafe_allow_html=True)

available_lessons = get_all_available_lessons(subject, subtopic_id) if subtopic_id else []

if not available_lessons:
    st.warning("⚠️ No lessons available for this subtopic yet. Try a different topic!")
    st.stop()

st.markdown(f'<div class="success-badge">✅ {len(available_lessons)} lesson(s) available</div>', unsafe_allow_html=True)
st.markdown("")

lesson_options = [f"Lesson {l['number']}: {l['title']}" for l in available_lessons]
selected_lesson = st.selectbox("Select lesson", lesson_options, label_visibility="collapsed")

lesson_num = int(selected_lesson.split(":")[0].replace("Lesson ", ""))
lesson_data = get_lesson_data(subject, subtopic_id, lesson_num)

if not lesson_data:
    st.error("Could not load lesson data")
    st.stop()

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# MODE-SPECIFIC CONTENT
# ============================================================================

if st.session_state.mode == "quick":
    # ========================================================================
    # QUICK DOWNLOAD MODE
    # ========================================================================
    st.markdown("""
    <div class="step-header">
        <div class="step-badge">3</div>
        <span class="step-title">Preview & Download</span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <div class="glass-card-header">🎯 Learning Outcome</div>
        </div>
        """, unsafe_allow_html=True)
        st.info(lesson_data.get('learning_outcome', 'N/A'))
        
        st.markdown("""
        <div class="glass-card">
            <div class="glass-card-header">🧠 Key Knowledge</div>
        </div>
        """, unsafe_allow_html=True)
        for i, item in enumerate(lesson_data.get('to_know', [])[:5], 1):
            st.markdown(f"**{i}.** {item}")
        if len(lesson_data.get('to_know', [])) > 5:
            st.caption(f"+ {len(lesson_data.get('to_know', [])) - 5} more...")
    
    with col2:
        st.markdown("""
        <div class="glass-card">
            <div class="glass-card-header">📋 Lesson Contents</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"✓ {len(lesson_data.get('do_now', {}).get('questions', []))} Do Now questions")
        st.markdown("✓ I Do - Teacher explanation")
        st.markdown("✓ We Do - Guided practice")
        st.markdown(f"✓ {len(lesson_data.get('you_do', []))} You Do tasks")
        st.markdown("✓ Exit Ticket assessment")
    
    st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Generate & Download", type="primary", use_container_width=True):
            with st.spinner("Creating your PowerPoint..."):
                try:
                    pptx_bytes = generate_pptx(lesson_data)
                    filename = f"Lesson_{lesson_data.get('lesson_number', 1)}_{lesson_data.get('title', 'Untitled').replace(' ', '_').replace(',', '')}.pptx"
                    
                    st.success("✅ Your PowerPoint is ready!")
                    st.balloons()
                    
                    st.download_button(
                        label="📥 Download PowerPoint",
                        data=pptx_bytes,
                        file_name=filename,
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")

else:
    # ========================================================================
    # CUSTOMISE MODE
    # ========================================================================
    st.markdown("""
    <div class="step-header">
        <div class="step-badge">3</div>
        <span class="step-title">Customise Your Lesson</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Edit any section below. Your changes will be included in the generated PowerPoint.")
    
    # Learning Outcome
    with st.expander("🎯 Learning Outcome", expanded=True):
        edited_outcome = st.text_area(
            "Learning Outcome",
            value=lesson_data.get('learning_outcome', ''),
            height=80,
            label_visibility="collapsed"
        )
    
    # To Know
    with st.expander("🧠 Key Knowledge (To Know)", expanded=True):
        to_know_list = lesson_data.get('to_know', [])
        edited_to_know = []
        for i, item in enumerate(to_know_list):
            edited_item = st.text_input(f"Point {i+1}", value=item, key=f"to_know_{i}")
            if edited_item.strip():
                edited_to_know.append(edited_item)
        
        new_point = st.text_input("Add new point (optional)", key="new_to_know")
        if new_point.strip():
            edited_to_know.append(new_point)
    
    # Do Now
    with st.expander("🕐 Do Now Questions"):
        do_now = lesson_data.get('do_now', {})
        questions = do_now.get('questions', [])
        answers = do_now.get('answers', [])
        
        edited_questions = []
        edited_answers = []
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Questions**")
        with col2:
            st.markdown("**Answers**")
        
        for i, (q, a) in enumerate(zip(questions, answers)):
            col1, col2 = st.columns(2)
            with col1:
                eq = st.text_input(f"Q{i+1}", value=q, key=f"q_{i}", label_visibility="collapsed")
            with col2:
                ea = st.text_input(f"A{i+1}", value=a, key=f"a_{i}", label_visibility="collapsed")
            if eq.strip():
                edited_questions.append(eq)
                edited_answers.append(ea)
    
    # I Do Content
    with st.expander("👨‍🏫 I Do - Teacher Content"):
        i_do = lesson_data.get('i_do', {})
        edited_i_do_title = st.text_input("Title", value=i_do.get('title', ''))
        
        st.markdown("**Content Points**")
        content_items = i_do.get('content', [])
        edited_content = []
        for i, item in enumerate(content_items):
            edited_item = st.text_input(f"Content {i+1}", value=item, key=f"ido_{i}", label_visibility="collapsed")
            if edited_item.strip():
                edited_content.append(edited_item)
    
    # Exit Ticket
    with st.expander("🎟️ Exit Ticket"):
        exit_data = lesson_data.get('exit_ticket', {})
        edited_exit_q = st.text_area("Question", value=exit_data.get('question', ''), height=60)
        
        st.markdown("**Options**")
        edited_options = []
        for i, opt in enumerate(exit_data.get('options', [])):
            edited_opt = st.text_input(f"Option {i+1}", value=opt, key=f"opt_{i}", label_visibility="collapsed")
            if edited_opt.strip():
                edited_options.append(edited_opt)
        
        edited_exit_answer = st.text_input("Correct Answer", value=exit_data.get('answer', ''))
    
    st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-header">
        <div class="step-badge">4</div>
        <span class="step-title">Generate & Download</span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Generate Custom PowerPoint", type="primary", use_container_width=True):
            with st.spinner("Creating your customised PowerPoint..."):
                try:
                    # Build modified lesson data
                    modified_lesson = lesson_data.copy()
                    modified_lesson['learning_outcome'] = edited_outcome
                    modified_lesson['to_know'] = edited_to_know
                    modified_lesson['do_now'] = {
                        'questions': edited_questions,
                        'answers': edited_answers
                    }
                    modified_lesson['i_do'] = {
                        **lesson_data.get('i_do', {}),
                        'title': edited_i_do_title,
                        'content': edited_content
                    }
                    modified_lesson['exit_ticket'] = {
                        'question': edited_exit_q,
                        'options': edited_options,
                        'answer': edited_exit_answer
                    }
                    
                    pptx_bytes = generate_pptx(modified_lesson)
                    filename = f"Custom_Lesson_{modified_lesson.get('lesson_number', 1)}_{modified_lesson.get('title', 'Untitled').replace(' ', '_').replace(',', '')}.pptx"
                    
                    st.success("✅ Your customised PowerPoint is ready!")
                    st.balloons()
                    
                    st.download_button(
                        label="📥 Download Custom PowerPoint",
                        data=pptx_bytes,
                        file_name=filename,
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    import traceback
                    with st.expander("Error details"):
                        st.code(traceback.format_exc())

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="footer-text">Built with ❤️ for GEMS Education Teachers</p>', unsafe_allow_html=True)
