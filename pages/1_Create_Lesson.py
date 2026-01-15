"""
Page 1: Create Lesson
Clean, streamlined lesson creation
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


# Page configuration
st.set_page_config(
    page_title="Create Lesson | GEMS TLAG",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Simple CSS
st.markdown("""
<style>
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1000px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .stButton > button {
        background: #10b981 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
    
    .stButton > button:hover {
        background: #059669 !important;
    }
    
    .stDownloadButton > button {
        background: #10b981 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'lesson_data' not in st.session_state:
    st.session_state.lesson_data = {}

# ============================================================================
# HEADER
# ============================================================================
st.markdown("# 📝 Create Your Lesson")
st.markdown("Select a topic, choose a lesson, and download your PowerPoint.")

st.markdown("---")

# ============================================================================
# STEP 1: CHOOSE TOPIC
# ============================================================================
st.markdown("### Step 1: Choose Your Topic")

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

# Get details
subtopic_id = subtopic_options.get(selected_subtopic) if subtopic_options else None
content_points = get_subtopic_content(subject, topic_id, subtopic_id) if subtopic_id else []

# Show specification content
if content_points:
    with st.expander("📋 View specification content"):
        for point in content_points:
            st.markdown(f"• {point}")

# Show practicals
related_practicals = get_related_practicals(subject, topic_id) if topic_id else []
if related_practicals:
    with st.expander(f"🔬 Related practicals ({len(related_practicals)})"):
        for p in related_practicals:
            st.markdown(f"**{p['name']}**: {p['description']}")

st.markdown("---")

# ============================================================================
# STEP 2: SELECT LESSON
# ============================================================================
st.markdown("### Step 2: Select a Lesson")

available_lessons = get_all_available_lessons(subject, subtopic_id) if subtopic_id else []

if available_lessons:
    st.success(f"✅ **{len(available_lessons)} lesson(s) available** for this topic!")
    
    lesson_options = [f"Lesson {l['number']}: {l['title']}" for l in available_lessons]
    selected_lesson = st.selectbox("Choose a lesson", lesson_options, label_visibility="collapsed")
    
    lesson_num = int(selected_lesson.split(":")[0].replace("Lesson ", ""))
    lesson_data = get_lesson_data(subject, subtopic_id, lesson_num)
    
    if lesson_data:
        # Preview
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("#### 🎯 Learning Outcome")
            st.info(lesson_data.get('learning_outcome', 'N/A'))
            
            st.markdown("#### 🧠 Key Knowledge")
            for i, item in enumerate(lesson_data.get('to_know', [])[:4], 1):
                st.markdown(f"{i}. {item}")
            if len(lesson_data.get('to_know', [])) > 4:
                st.caption(f"+ {len(lesson_data.get('to_know', [])) - 4} more items")
        
        with col2:
            st.markdown("#### ✓ Includes")
            st.markdown(f"- {len(lesson_data.get('do_now', {}).get('questions', []))} Do Now questions")
            st.markdown("- I Do demonstration")
            st.markdown("- We Do practice")
            st.markdown("- You Do (differentiated)")
            st.markdown("- Exit Ticket")
        
        st.markdown("---")
        
        # ============================================================================
        # STEP 3: GENERATE
        # ============================================================================
        st.markdown("### Step 3: Generate & Download")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🚀 Generate PowerPoint", type="primary", use_container_width=True):
                with st.spinner("Creating your PowerPoint..."):
                    try:
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
                        if i_do_data.get('examples') or i_do_data.get('key_points'):
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
                        
                        filename = f"Lesson_{lesson_data.get('lesson_number', 1)}_{lesson_data.get('title', 'Untitled').replace(' ', '_').replace(',', '')}.pptx"
                        
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
    st.warning("⚠️ **No lessons available** for this subtopic yet. Try a different topic!")

st.markdown("---")
st.caption("Built with ❤️ for GEMS Education Teachers")
