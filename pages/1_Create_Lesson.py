"""
Page 1: Create Lesson
Streamlined lesson creation using pre-made TLAG lessons
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
    # First check if expanded lesson is available (these have richer content)
    expanded = get_expanded_lesson(subject, subtopic_id, lesson_num)
    if expanded:
        return expanded
    
    # Fallback to standard lessons
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
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }
    
    /* Header styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .lesson-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    /* Success message styling */
    .success-banner {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Button improvements */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        border-radius: 8px;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        font-weight: 600;
        font-size: 1rem;
    }
    
    /* Hide sidebar by default for cleaner look */
    [data-testid="stSidebar"] {
        min-width: 0;
    }
    
    /* Step indicators */
    .step-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'lesson_data' not in st.session_state:
    st.session_state.lesson_data = {}

# ============================================================================
# HEADER
# ============================================================================
st.markdown('<p class="main-title">📝 Create Your TLAG Lesson</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Select a topic and generate a complete PowerPoint in seconds!</p>', unsafe_allow_html=True)

# ============================================================================
# STEP 1: SELECT TOPIC
# ============================================================================
st.markdown("### <span class='step-number'>1</span> Choose Your Topic", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    subject = st.selectbox(
        "🔬 Subject",
        ["Chemistry", "Biology", "Physics"],
        index=0,
        help="Select your science subject"
    )

# Get topics for selected subject
curriculum_data = AQA_GCSE_CURRICULA.get(subject, {})
topics = curriculum_data.get("topics", {})
topic_options = {f"{k}: {v['name']}": k for k, v in topics.items()}

with col2:
    selected_topic = st.selectbox(
        "📖 Topic",
        list(topic_options.keys()) if topic_options else ["No topics available"],
        help="Select the main topic area"
    )

# Get subtopics for selected topic
topic_id = topic_options.get(selected_topic) if topic_options else None
subtopics = topics.get(topic_id, {}).get("subtopics", {}) if topic_id else {}
subtopic_options = {f"{k}: {v['name']}": k for k, v in subtopics.items()}

with col3:
    selected_subtopic = st.selectbox(
        "📚 Subtopic",
        list(subtopic_options.keys()) if subtopic_options else ["No subtopics available"],
        help="Select the specific subtopic"
    )

# Get subtopic details
subtopic_id = subtopic_options.get(selected_subtopic) if subtopic_options else None
content_points = get_subtopic_content(subject, topic_id, subtopic_id) if subtopic_id else []

# Optional: Show specification content
if content_points:
    with st.expander("📋 View Specification Content", expanded=False):
        for point in content_points:
            st.markdown(f"• {point}")

# Show related practicals if any
related_practicals = get_related_practicals(subject, topic_id) if topic_id else []
if related_practicals:
    with st.expander(f"🔬 Related Required Practicals ({len(related_practicals)})", expanded=False):
        for p in related_practicals:
            st.markdown(f"**{p['name']}**: {p['description']}")

st.markdown("---")

# ============================================================================
# STEP 2: SELECT LESSON
# ============================================================================
st.markdown("### <span class='step-number'>2</span> Select a Lesson", unsafe_allow_html=True)

# Check for available lessons
available_lessons = get_all_available_lessons(subject, subtopic_id) if subtopic_id else []

if available_lessons:
    # Success banner
    st.markdown(f"""
    <div class="success-banner">
        ✅ {len(available_lessons)} ready-made lesson(s) available for this topic!
    </div>
    """, unsafe_allow_html=True)
    
    lesson_options = [f"Lesson {l['number']}: {l['title']}" for l in available_lessons]
    selected_lesson = st.selectbox(
        "📚 Choose a lesson",
        lesson_options,
        help="Select which lesson you want to generate"
    )
    
    lesson_num = int(selected_lesson.split(":")[0].replace("Lesson ", ""))
    lesson_data = get_lesson_data(subject, subtopic_id, lesson_num)
    
    if lesson_data:
        # Lesson preview card
        st.markdown("#### 📋 Lesson Preview")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**🎯 Learning Outcome:**")
            st.info(lesson_data.get('learning_outcome', 'N/A'))
            
            st.markdown("**🧠 Key Knowledge (To Know):**")
            to_know_items = lesson_data.get('to_know', [])[:4]
            for i, item in enumerate(to_know_items, 1):
                st.markdown(f"{i}. {item}")
            if len(lesson_data.get('to_know', [])) > 4:
                st.caption(f"...and {len(lesson_data.get('to_know', [])) - 4} more items")
        
        with col2:
            st.markdown("**📊 Lesson Includes:**")
            st.markdown(f"✅ {len(lesson_data.get('do_now', {}).get('questions', []))} Do Now questions")
            st.markdown("✅ I Do demonstration")
            st.markdown("✅ We Do practice")
            st.markdown("✅ You Do tasks (Bronze/Silver/Gold)")
            st.markdown("✅ Exit Ticket")
        
        st.markdown("---")
        
        # ============================================================================
        # STEP 3: GENERATE POWERPOINT
        # ============================================================================
        st.markdown("### <span class='step-number'>3</span> Generate PowerPoint", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🚀 Generate PowerPoint", type="primary", use_container_width=True):
                with st.spinner("⏳ Creating your PowerPoint... Please wait..."):
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
                        
                        # Add all slides
                        builder.add_do_now(
                            lesson_data.get('do_now', {}).get('questions', []),
                            lesson_data.get('do_now', {}).get('answers', [])
                        )
                        
                        builder.add_outcomes(
                            lesson_data.get('learning_outcome', ''),
                            lesson_data.get('to_know', [])
                        )
                        
                        # Use expanded I Do slides if examples are available
                        i_do_data = lesson_data.get('i_do', {})
                        if i_do_data.get('examples') or i_do_data.get('key_points'):
                            builder.add_i_do_slides(i_do_data)
                        else:
                            builder.add_i_do(
                                i_do_data.get('title', 'I Do'),
                                i_do_data.get('content', [])
                            )
                        
                        # Use expanded We Do slides if multiple examples available
                        we_do_data = lesson_data.get('we_do', {})
                        if we_do_data.get('examples'):
                            builder.add_we_do_slides(we_do_data)
                        else:
                            builder.add_we_do(
                                "Scaffolded Practice",
                                we_do_data.get('question', ''),
                                we_do_data.get('steps', [])
                            )
                        
                        # Use expanded You Do slides for more tasks
                        builder.add_you_do_slides(lesson_data.get('you_do', []))
                        
                        # Add affirmative checking if available
                        aff_check = lesson_data.get('affirmative_checking', {})
                        if aff_check:
                            builder.add_affirmative_checking(
                                checkpoint=aff_check.get('checkpoint', ''),
                                action=aff_check.get('action', '')
                            )
                        
                        # Add exit ticket
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
                        
                        # Download button
                        st.download_button(
                            label="📥 Download Your PowerPoint",
                            data=buffer,
                            file_name=filename,
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                            type="primary",
                            use_container_width=True
                        )
                        
                    except Exception as e:
                        st.error(f"❌ Error generating PowerPoint: {str(e)}")
                        import traceback
                        with st.expander("🔧 Error Details"):
                            st.code(traceback.format_exc())

else:
    # No lessons available message
    st.warning("""
    ⚠️ **No pre-made lessons available for this subtopic yet.**
    
    We're constantly adding new lessons! In the meantime, try:
    - Selecting a different subtopic
    - Check back soon for updates
    """)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")

# Quick tips
with st.expander("💡 Tips for Great Lessons", expanded=False):
    st.markdown("""
    **Using Your Downloaded PowerPoint:**
    1. Open the PowerPoint in Microsoft PowerPoint or Google Slides
    2. Add your own images and diagrams to slides
    3. Customize the Bronze/Silver/Gold tasks for your class
    4. Add any additional worked examples you need
    
    **The TLAG Structure:**
    - 🕰️ **Do Now** - Retrieval practice (5 mins)
    - 🎯 **Learning Outcome** - Clear success criteria
    - 🧠 **To Know** - Key knowledge points
    - 👁️ **I Do** - Teacher demonstration
    - 🤝 **We Do** - Guided practice
    - ✏️ **You Do** - Independent practice
    - 🎟️ **Exit Ticket** - Check understanding
    """)

st.caption("Built with ❤️ for GEMS Education Teachers")
