"""
Page 1: Create Lesson
Professional two-option workflow: Quick Download or Customise First
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

# Professional CSS - Light Glassmorphism Theme with 3D Effects
st.markdown("""
<style>
    /* Light background with subtle pattern */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 50%, #f0fdf4 100%);
    }
    
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1100px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 3D Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.08),
            0 2px 8px rgba(0, 0, 0, 0.04),
            inset 0 1px 0 rgba(255, 255, 255, 0.9);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 
            0 16px 48px rgba(0, 0, 0, 0.12),
            0 4px 12px rgba(0, 0, 0, 0.06),
            inset 0 1px 0 rgba(255, 255, 255, 1);
    }
    
    /* Section Headers with 3D effect */
    .section-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 16px;
        margin: 1.5rem 0 1rem 0;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 
            0 8px 24px rgba(102, 126, 234, 0.35),
            0 4px 8px rgba(118, 75, 162, 0.2);
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }
    
    /* 3D Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        padding: 0.875rem 2rem !important;
        font-size: 1rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 
            0 4px 14px rgba(16, 185, 129, 0.4),
            0 2px 4px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 
            0 8px 25px rgba(16, 185, 129, 0.5),
            0 4px 8px rgba(0, 0, 0, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98) !important;
    }
    
    /* Download button with blue 3D effect */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
        color: white !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        padding: 0.875rem 2rem !important;
        box-shadow: 
            0 4px 14px rgba(59, 130, 246, 0.4),
            0 2px 4px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        transition: all 0.3s ease !important;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 
            0 8px 25px rgba(59, 130, 246, 0.5),
            0 4px 8px rgba(0, 0, 0, 0.15) !important;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(203, 213, 225, 0.6) !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(203, 213, 225, 0.6) !important;
        box-shadow: 
            inset 0 2px 4px rgba(0, 0, 0, 0.02),
            0 1px 2px rgba(0, 0, 0, 0.02) !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        box-shadow: 
            0 0 0 3px rgba(102, 126, 234, 0.15),
            inset 0 2px 4px rgba(0, 0, 0, 0.02) !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.8) !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
    }
    
    /* Info/Success/Warning boxes with glass effect */
    .stAlert {
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(8px) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06) !important;
    }
    
    /* Title styling */
    h1 {
        background: linear-gradient(135deg, #1e40af 0%, #7c3aed 50%, #db2777 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800 !important;
    }
    
    /* Subtle animations */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
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
st.markdown("# 📝 Create Your Lesson")
st.markdown("Generate professional TLAG PowerPoints in seconds")

st.markdown("---")

# ============================================================================
# MODE SELECTION
# ============================================================================
st.markdown("### Choose Your Workflow")

col1, col2 = st.columns(2)

with col1:
    quick_active = "active" if st.session_state.mode == "quick" else ""
    if st.button("⚡ Quick Download", use_container_width=True, key="quick_btn"):
        st.session_state.mode = "quick"
        st.session_state.pptx_ready = None
        st.rerun()
    st.markdown("**Select a ready-made lesson and download instantly.** Best for when you want a complete lesson with no changes.")

with col2:
    custom_active = "active" if st.session_state.mode == "custom" else ""
    if st.button("✏️ Customise First", use_container_width=True, key="custom_btn"):
        st.session_state.mode = "custom"
        st.session_state.pptx_ready = None
        st.rerun()
    st.markdown("**Edit lesson content before generating.** Best for when you want to tailor the lesson to your class.")

# Show active mode indicator
if st.session_state.mode == "quick":
    st.info("⚡ **Quick Download Mode** - Select and download a ready-made lesson")
else:
    st.success("✏️ **Customise Mode** - Edit content before generating")

st.markdown("---")

# ============================================================================
# STEP 1: TOPIC SELECTION (Same for both modes)
# ============================================================================
st.markdown('<div class="section-header">📚 Step 1: Select Your Topic</div>', unsafe_allow_html=True)

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
st.markdown('<div class="section-header">📖 Step 2: Choose a Lesson</div>', unsafe_allow_html=True)

available_lessons = get_all_available_lessons(subject, subtopic_id) if subtopic_id else []

if not available_lessons:
    st.warning("⚠️ No lessons available for this subtopic yet. Try a different topic!")
    st.stop()

st.success(f"✅ **{len(available_lessons)} lesson(s) available**")

lesson_options = [f"Lesson {l['number']}: {l['title']}" for l in available_lessons]
selected_lesson = st.selectbox("Select lesson", lesson_options, label_visibility="collapsed")

lesson_num = int(selected_lesson.split(":")[0].replace("Lesson ", ""))
lesson_data = get_lesson_data(subject, subtopic_id, lesson_num)

if not lesson_data:
    st.error("Could not load lesson data")
    st.stop()

# ============================================================================
# MODE-SPECIFIC CONTENT
# ============================================================================

if st.session_state.mode == "quick":
    # ========================================================================
    # QUICK DOWNLOAD MODE
    # ========================================================================
    st.markdown('<div class="section-header">👁️ Lesson Preview</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**🎯 Learning Outcome**")
        st.info(lesson_data.get('learning_outcome', 'N/A'))
        
        st.markdown("**🧠 Key Knowledge**")
        for i, item in enumerate(lesson_data.get('to_know', [])[:5], 1):
            st.markdown(f"{i}. {item}")
        if len(lesson_data.get('to_know', [])) > 5:
            st.caption(f"+ {len(lesson_data.get('to_know', [])) - 5} more...")
    
    with col2:
        st.markdown("**📋 Lesson Contents**")
        st.markdown(f"✓ {len(lesson_data.get('do_now', {}).get('questions', []))} Do Now questions")
        st.markdown("✓ I Do - Teacher explanation")
        st.markdown("✓ We Do - Guided practice")
        st.markdown(f"✓ {len(lesson_data.get('you_do', []))} You Do tasks")
        st.markdown("✓ Exit Ticket assessment")
    
    st.markdown("---")
    st.markdown('<div class="section-header">⬇️ Step 3: Download</div>', unsafe_allow_html=True)
    
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
    st.markdown('<div class="section-header">✏️ Step 3: Customise Your Lesson</div>', unsafe_allow_html=True)
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
    
    st.markdown("---")
    st.markdown('<div class="section-header">⬇️ Step 4: Generate & Download</div>', unsafe_allow_html=True)
    
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

st.markdown("---")
st.caption("Built with ❤️ for GEMS Education Teachers")
