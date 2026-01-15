"""
Page 1: Create Lesson
Modern, streamlined lesson creation
"""
import streamlit as st
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.curriculum_data import AQA_GCSE_CURRICULA, get_topics_list, get_subtopic_content
from core.chemistry_lessons import get_lesson_content as get_chemistry_lesson, get_available_lessons as get_chemistry_available, CHEMISTRY_LESSONS
from core.science_lessons import BIOLOGY_LESSONS, PHYSICS_LESSONS, get_biology_lesson, get_physics_lesson, get_available_biology_lessons, get_available_physics_lessons
from core.expanded_lessons import EXPANDED_LESSONS, get_expanded_lesson
from core.aqa_curriculum import get_curriculum, get_practicals, get_related_practicals


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
    """Get lesson content for any subject. Prefers expanded lessons with richer content."""
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


# Page configuration
st.set_page_config(
    page_title="Create Lesson | GEMS TLAG",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern CSS styling
st.markdown("""
<style>
    /* Base styles */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1000px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Page header */
    .page-header {
        margin-bottom: 2rem;
    }
    
    .page-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    
    .page-subtitle {
        color: #6b7280;
        font-size: 1rem;
    }
    
    /* Step indicators */
    .step-indicator {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 2rem 0 1rem;
    }
    
    .step-badge {
        background: #10b981;
        color: white;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.85rem;
        flex-shrink: 0;
    }
    
    .step-label {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1f2937;
    }
    
    /* Selector cards */
    .selector-row {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    /* Lesson available banner */
    .success-banner {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        margin: 1.5rem 0;
        font-size: 1rem;
    }
    
    /* Preview card */
    .preview-card {
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .preview-title {
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Checklist items */
    .checklist {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .checklist li {
        padding: 0.5rem 0;
        color: #4b5563;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .checklist li::before {
        content: "✓";
        color: #10b981;
        font-weight: bold;
    }
    
    /* Buttons */
    .stButton > button {
        background: #10b981 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: #059669 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.3) !important;
    }
    
    /* Download button special styling */
    .stDownloadButton > button {
        background: #10b981 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        width: 100% !important;
    }
    
    /* Selectbox styling */
    .stSelectbox > label {
        font-weight: 600;
        color: #374151;
    }
    
    .stSelectbox > div > div {
        border-radius: 8px;
        border-color: #d1d5db;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: #374151;
        background: #f9fafb;
        border-radius: 8px;
    }
    
    /* Info box styling */
    .info-box {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        padding: 1rem;
        color: #1e40af;
    }
    
    /* Warning styling */
    .warning-box {
        background: #fffbeb;
        border: 1px solid #fcd34d;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        color: #92400e;
    }
    
    /* Back link */
    .back-link {
        color: #6b7280;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1rem;
        font-size: 0.9rem;
    }
    
    .back-link:hover {
        color: #10b981;
    }
    
    /* Divider */
    .divider {
        height: 1px;
        background: #e5e7eb;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'lesson_data' not in st.session_state:
    st.session_state.lesson_data = {}

# ============================================================================
# BACK NAVIGATION
# ============================================================================
st.markdown('<a href="/" target="_self" class="back-link">← Back to Home</a>', unsafe_allow_html=True)

# ============================================================================
# PAGE HEADER
# ============================================================================
st.markdown("""
<div class="page-header">
    <h1 class="page-title">📝 Create Your Lesson</h1>
    <p class="page-subtitle">Select a topic, choose a lesson, and download your PowerPoint</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# STEP 1: CHOOSE TOPIC
# ============================================================================
st.markdown("""
<div class="step-indicator">
    <div class="step-badge">1</div>
    <span class="step-label">Choose Your Topic</span>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    subject = st.selectbox(
        "Subject",
        ["Chemistry", "Biology", "Physics"],
        index=0
    )

# Get topics for selected subject
curriculum_data = AQA_GCSE_CURRICULA.get(subject, {})
topics = curriculum_data.get("topics", {})
topic_options = {f"{k}: {v['name']}": k for k, v in topics.items()}

with col2:
    selected_topic = st.selectbox(
        "Topic",
        list(topic_options.keys()) if topic_options else ["No topics available"]
    )

# Get subtopics for selected topic
topic_id = topic_options.get(selected_topic) if topic_options else None
subtopics = topics.get(topic_id, {}).get("subtopics", {}) if topic_id else {}
subtopic_options = {f"{k}: {v['name']}": k for k, v in subtopics.items()}

with col3:
    selected_subtopic = st.selectbox(
        "Subtopic",
        list(subtopic_options.keys()) if subtopic_options else ["No subtopics available"]
    )

# Get subtopic details
subtopic_id = subtopic_options.get(selected_subtopic) if subtopic_options else None
content_points = get_subtopic_content(subject, topic_id, subtopic_id) if subtopic_id else []

# Optional: Show specification content
if content_points:
    with st.expander("📋 View specification content"):
        for point in content_points:
            st.markdown(f"• {point}")

# Show related practicals if any
related_practicals = get_related_practicals(subject, topic_id) if topic_id else []
if related_practicals:
    with st.expander(f"🔬 Related practicals ({len(related_practicals)})"):
        for p in related_practicals:
            st.markdown(f"**{p['name']}**: {p['description']}")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================================================
# STEP 2: SELECT LESSON
# ============================================================================
st.markdown("""
<div class="step-indicator">
    <div class="step-badge">2</div>
    <span class="step-label">Select a Lesson</span>
</div>
""", unsafe_allow_html=True)

# Check for available lessons
available_lessons = get_all_available_lessons(subject, subtopic_id) if subtopic_id else []

if available_lessons:
    # Success banner
    st.markdown(f"""
    <div class="success-banner">
        ✓ {len(available_lessons)} lesson(s) available for this topic
    </div>
    """, unsafe_allow_html=True)
    
    lesson_options = [f"Lesson {l['number']}: {l['title']}" for l in available_lessons]
    selected_lesson = st.selectbox(
        "Choose a lesson",
        lesson_options,
        label_visibility="collapsed"
    )
    
    lesson_num = int(selected_lesson.split(":")[0].replace("Lesson ", ""))
    lesson_data = get_lesson_data(subject, subtopic_id, lesson_num)
    
    if lesson_data:
        # Lesson preview
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("#### 🎯 Learning Outcome")
            st.info(lesson_data.get('learning_outcome', 'N/A'))
            
            st.markdown("#### 🧠 Key Knowledge")
            to_know_items = lesson_data.get('to_know', [])[:4]
            for i, item in enumerate(to_know_items, 1):
                st.markdown(f"{i}. {item}")
            if len(lesson_data.get('to_know', [])) > 4:
                st.caption(f"+ {len(lesson_data.get('to_know', [])) - 4} more items")
        
        with col2:
            st.markdown("#### ✓ Includes")
            st.markdown(f"""
            <ul class="checklist">
                <li>{len(lesson_data.get('do_now', {}).get('questions', []))} Do Now questions</li>
                <li>I Do demonstration</li>
                <li>We Do practice</li>
                <li>You Do (differentiated)</li>
                <li>Exit Ticket</li>
            </ul>
            """, unsafe_allow_html=True)
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # ============================================================================
        # STEP 3: GENERATE POWERPOINT
        # ============================================================================
        st.markdown("""
        <div class="step-indicator">
            <div class="step-badge">3</div>
            <span class="step-label">Generate & Download</span>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🚀 Generate PowerPoint", type="primary", use_container_width=True):
                with st.spinner("Creating your PowerPoint..."):
                    try:
                        from core.pptx_builder import TLAGPowerPointBuilder
                        import io
                        
                        # Template path
                        template_path = "templates/WSO Learn Like A GEM Template (1).pptx"
                        if not os.path.exists(template_path):
                            template_path = "WSO Learn Like A GEM Template (1).pptx"
                        
                        # Build presentation
                        builder = TLAGPowerPointBuilder(template_path)
                        builder.create_presentation()
                        
                        # Add slides
                        builder.add_do_now(
                            lesson_data.get('do_now', {}).get('questions', []),
                            lesson_data.get('do_now', {}).get('answers', [])
                        )
                        
                        builder.add_outcomes(
                            lesson_data.get('learning_outcome', ''),
                            lesson_data.get('to_know', [])
                        )
                        
                        i_do_data = lesson_data.get('i_do', {})
                        if i_do_data.get('examples') or i_do_data.get('key_points'):
                            builder.add_i_do_slides(i_do_data)
                        else:
                            builder.add_i_do(
                                i_do_data.get('title', 'I Do'),
                                i_do_data.get('content', [])
                            )
                        
                        we_do_data = lesson_data.get('we_do', {})
                        if we_do_data.get('examples'):
                            builder.add_we_do_slides(we_do_data)
                        else:
                            builder.add_we_do(
                                "Scaffolded Practice",
                                we_do_data.get('question', ''),
                                we_do_data.get('steps', [])
                            )
                        
                        builder.add_you_do_slides(lesson_data.get('you_do', []))
                        
                        aff_check = lesson_data.get('affirmative_checking', {})
                        if aff_check:
                            builder.add_affirmative_checking(
                                checkpoint=aff_check.get('checkpoint', ''),
                                action=aff_check.get('action', '')
                            )
                        
                        exit_data = lesson_data.get('exit_ticket', {})
                        builder.add_exit_ticket(
                            exit_data.get('question', ''),
                            exit_data.get('options', []),
                            exit_data.get('answer', '')
                        )
                        
                        # Generate filename
                        filename = f"Lesson_{lesson_data.get('lesson_number', 1)}_{lesson_data.get('title', 'Untitled').replace(' ', '_').replace(',', '')}.pptx"
                        
                        # Save to buffer
                        buffer = io.BytesIO()
                        builder.prs.save(buffer)
                        buffer.seek(0)
                        
                        st.success("✅ Your PowerPoint is ready!")
                        st.balloons()
                        
                        st.download_button(
                            label="📥 Download PowerPoint",
                            data=buffer,
                            file_name=filename,
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                            use_container_width=True
                        )
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                        with st.expander("Error details"):
                            import traceback
                            st.code(traceback.format_exc())

else:
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ No lessons available for this subtopic yet</strong><br>
        <span style="font-size: 0.9rem;">We're adding new lessons regularly. Try a different subtopic!</span>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.caption("Built with ❤️ for GEMS Education Teachers")
