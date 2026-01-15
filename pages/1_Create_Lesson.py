"""
Page 1: Create Lesson
Enter lesson details and generate initial content
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
from core.lesson_generator import generate_lesson_content
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


st.set_page_config(page_title="Create Lesson", page_icon="📝", layout="wide")

st.markdown("# 📝 Create New Lesson")
st.markdown("Select your curriculum topic and generate a complete TLAG lesson.")

# Initialize session state
if 'lesson_data' not in st.session_state:
    st.session_state.lesson_data = {}

# Curriculum Browser Section
st.markdown("## 📚 Curriculum Browser")

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

# Show content preview
subtopic_id = subtopic_options.get(selected_subtopic) if subtopic_options else None
content_points = get_subtopic_content(subject, topic_id, subtopic_id) if subtopic_id else []

if content_points:
    with st.expander("📋 Specification Content Preview", expanded=False):
        for point in content_points:
            st.markdown(f"• {point}")

# Check for pre-made lessons (works for all subjects)
available_lessons = get_all_available_lessons(subject, subtopic_id) if subtopic_id else []

# Also check for related practicals
related_practicals = get_related_practicals(subject, topic_id) if topic_id else []
if related_practicals:
    with st.expander(f"🔬 Related Required Practicals ({len(related_practicals)})", expanded=False):
        for p in related_practicals:
            st.markdown(f"**{p['name']}**: {p['description']}")

if available_lessons:
    st.success(f"✅ {len(available_lessons)} pre-made lesson(s) ready for this subtopic!")
    
    lesson_options = [f"Lesson {l['number']}: {l['title']}" for l in available_lessons]
    selected_lesson = st.selectbox("📚 Select Lesson", lesson_options)
    
    lesson_num = int(selected_lesson.split(":")[0].replace("Lesson ", ""))
    lesson_data = get_lesson_data(subject, subtopic_id, lesson_num)
    
    if lesson_data:
        # Preview in expander
        with st.expander("📋 Lesson Preview", expanded=True):
            st.markdown(f"**Learning Outcome:** {lesson_data.get('learning_outcome', 'N/A')}")
            st.markdown("**To Know:**")
            for i, item in enumerate(lesson_data.get('to_know', [])[:3], 1):
                st.markdown(f"  {i}. {item}")
            st.markdown("  ...")
            st.markdown(f"**Do Now Questions:** {len(lesson_data.get('do_now', {}).get('questions', []))} questions ready")
            st.markdown(f"**Differentiation:** Bronze, Silver, Gold tasks included")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📝 Edit Before Export", use_container_width=True):
                # Load into session and go to edit page
                st.session_state.lesson_data = {
                    'subject': subject,
                    'curriculum': f"AQA GCSE ({curriculum_data.get('code', '')})",
                    'topic': lesson_data.get('title', ''),
                    'topic_id': topic_id,
                    'subtopic_id': subtopic_id,
                    'lesson_number': lesson_data.get('lesson_number', 1),
                    'unit': topics.get(topic_id, {}).get("name", ""),
                    'year_group': "Year 10",
                    'do_now_questions': lesson_data.get('do_now', {}).get('questions', []),
                    'do_now_answers': lesson_data.get('do_now', {}).get('answers', []),
                    'learning_outcome': lesson_data.get('learning_outcome', ''),
                    'to_know': lesson_data.get('to_know', []),
                    'content_points': content_points,
                    'i_do_title': lesson_data.get('i_do', {}).get('title', ''),
                    'i_do_content': '\n'.join(lesson_data.get('i_do', {}).get('content', [])),
                    'we_do_question': lesson_data.get('we_do', {}).get('question', ''),
                    'we_do_steps': '\n'.join(['• ' + s for s in lesson_data.get('we_do', {}).get('steps', [])]),
                    'you_do_tasks': lesson_data.get('you_do', []),
                    'exam_question': '',
                    'mark_scheme': '',
                    'exit_question': lesson_data.get('exit_ticket', {}).get('question', ''),
                    'exit_options': '\n'.join(lesson_data.get('exit_ticket', {}).get('options', [])),
                    'exit_answer': lesson_data.get('exit_ticket', {}).get('answer', '')
                }
                st.switch_page("pages/2_Edit_Content.py")
        
        with col2:
            if st.button("🚀 Generate PowerPoint Now", type="primary", use_container_width=True):
                with st.spinner("⏳ Generating PowerPoint..."):
                    try:
                        from core.pptx_builder import TLAGPowerPointBuilder
                        import os
                        
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
                        filename = f"Lesson_{lesson_data.get('lesson_number', 1)}_{lesson_data.get('title', 'Untitled').replace(' ', '_')}.pptx"
                        
                        # Save to a BytesIO buffer for download
                        import io
                        buffer = io.BytesIO()
                        builder.prs.save(buffer)
                        buffer.seek(0)
                        
                        st.success(f"✅ PowerPoint generated!")
                        st.balloons()
                        
                        # Provide download button
                        st.download_button(
                            label="📥 Download PowerPoint",
                            data=buffer,
                            file_name=filename,
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                            type="primary",
                            use_container_width=True
                        )
                        
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        import traceback
                        st.code(traceback.format_exc())

else:
    st.warning("⚠️ No pre-made lessons for this subtopic. Use AI Generator below or manual entry.")

st.markdown("---")

# AI Lesson Generation Section
st.markdown("## 🤖 AI Lesson Generator")
st.markdown("Generate a complete TLAG lesson using AI based on the selected topic.")

# API Key - check secrets first (for cloud), then allow manual input
with st.sidebar:
    st.markdown("### 🔑 OpenAI API Key")
    
    # Check if running on Streamlit Cloud with secrets configured
    api_key = None
    if hasattr(st, 'secrets') and 'OPENAI_API_KEY' in st.secrets:
        api_key = st.secrets['OPENAI_API_KEY']
        st.success("✅ API key configured (from secrets)")
    else:
        api_key = st.text_input("Enter your API key", type="password", 
                               help="Required for AI lesson generation")
        if api_key:
            st.success("✅ API key configured")

# Get subtopic name for display
subtopic_name = subtopics.get(subtopic_id, {}).get("name", "Unknown") if subtopic_id else "Unknown"
topic_name = topics.get(topic_id, {}).get("name", "Unknown") if topic_id else "Unknown"

col1, col2 = st.columns([3, 1])

with col1:
    st.info(f"**Ready to generate:** {subject} → {topic_name} → {subtopic_name}")

with col2:
    generate_clicked = st.button("🚀 Generate with AI", type="primary", use_container_width=True)

if generate_clicked:
    if not api_key:
        st.error("❌ Please enter your OpenAI API key in the sidebar first.")
    elif not subtopic_id:
        st.error("❌ Please select a subtopic first.")
    else:
        with st.spinner("🤖 Generating lesson content with AI... This may take 30-60 seconds."):
            result = generate_lesson_content(
                subject=subject,
                topic=topic_name,
                subtopic=subtopic_name,
                spec_content=content_points,
                api_key=api_key
            )
            
            if result.get("success"):
                lesson = result.get("lesson", {})
                
                # Build session state from AI response
                st.session_state.lesson_data = {
                    'subject': subject,
                    'curriculum': f"AQA GCSE ({curriculum_data.get('code', '')})",
                    'topic': subtopic_name,
                    'topic_id': topic_id,
                    'subtopic_id': subtopic_id,
                    'lesson_number': 1,
                    'unit': topic_name,
                    'year_group': "Year 10",
                    'do_now_questions': lesson.get('do_now', {}).get('questions', []),
                    'do_now_answers': lesson.get('do_now', {}).get('answers', []),
                    'learning_outcome': lesson.get('learning_outcome', ''),
                    'to_know': lesson.get('to_know', []),
                    'content_points': content_points,
                    'i_do_title': lesson.get('i_do', {}).get('title', ''),
                    'i_do_content': '\n'.join(lesson.get('i_do', {}).get('content', [])),
                    'we_do_question': lesson.get('we_do', {}).get('question', ''),
                    'we_do_steps': '\n'.join(['• ' + s for s in lesson.get('we_do', {}).get('steps', [])]),
                    'you_do_tasks': lesson.get('you_do', []),
                    'exam_question': '',
                    'mark_scheme': '',
                    'exit_question': lesson.get('exit_ticket', {}).get('question', ''),
                    'exit_options': '\n'.join(lesson.get('exit_ticket', {}).get('options', [])),
                    'exit_answer': lesson.get('exit_ticket', {}).get('answer', '')
                }
                
                st.success("✅ Lesson generated successfully!")
                st.balloons()
                
                # Show preview
                with st.expander("📋 Preview Generated Content", expanded=True):
                    st.markdown(f"**Learning Outcome:** {lesson.get('learning_outcome', 'N/A')}")
                    st.markdown("**To Know:**")
                    for i, item in enumerate(lesson.get('to_know', []), 1):
                        st.markdown(f"{i}. {item}")
                
                if st.button("✏️ Edit & Export Lesson", type="primary"):
                    st.switch_page("pages/2_Edit_Content.py")
            else:
                st.error(f"❌ Error generating lesson: {result.get('error', 'Unknown error')}")

st.markdown("---")

# Lesson Details Form
st.markdown("## 📝 Lesson Details (Manual Entry)")

with st.form("lesson_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        lesson_number = st.number_input(
            "Lesson Number",
            min_value=1,
            max_value=100,
            value=1
        )
        
        # Get topic name from selection
        topic_name = subtopics.get(subtopic_id, {}).get("name", "") if subtopic_id else ""
        topic = st.text_input(
            "Lesson Topic",
            value=topic_name,
            placeholder="e.g., Titration Calculations"
        )
    
    with col2:
        unit = topics.get(topic_id, {}).get("name", "") if topic_id else ""
        unit_display = st.text_input(
            "Unit/Chapter",
            value=unit,
            placeholder="e.g., Quantitative Chemistry"
        )
        
        year_group = st.selectbox(
            "Year Group",
            ["Year 10", "Year 11", "Year 12", "Year 13"],
            index=0
        )
    
    st.markdown("---")
    st.markdown("### 📌 Do Now Questions (Retrieval Practice)")
    st.caption("Enter 3-5 questions based on PRIOR learning (not new content)")
    
    do_now_questions = []
    do_now_answers = []
    
    for i in range(5):
        cols = st.columns([3, 1])
        with cols[0]:
            q = st.text_input(f"Question {i+1}", key=f"q_{i}", placeholder="Enter question...")
        with cols[1]:
            a = st.text_input(f"Answer", key=f"a_{i}", placeholder="Answer")
        if q:
            do_now_questions.append(q)
            do_now_answers.append(a)
    
    st.markdown("---")
    st.markdown("### 🎯 Learning Outcome")
    st.caption("ONE precise skill-based outcome (not activities)")
    
    learning_outcome = st.text_area(
        "Learning Outcome",
        placeholder="e.g., Calculate the unknown concentration of a solution using titration results and balanced symbol equations.",
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 🧠 To Know (Substantive Knowledge)")
    st.caption("Essential facts/concepts needed to achieve the outcome")
    
    # Pre-fill with content points if available
    to_know = []
    for i in range(5):
        default_value = content_points[i] if i < len(content_points) else ""
        tk = st.text_input(f"To Know {i+1}", key=f"tk_{i}", value=default_value, placeholder=f"Knowledge point {i+1}...")
        if tk:
            to_know.append(tk)
    
    submitted = st.form_submit_button("📝 Save & Continue", type="primary", use_container_width=True)

if submitted:
    if not topic:
        st.error("Please enter a topic")
    elif not learning_outcome:
        st.error("Please enter a learning outcome")
    elif len(do_now_questions) < 3:
        st.error("Please enter at least 3 Do Now questions")
    else:
        # Save to session state
        st.session_state.lesson_data = {
            'subject': subject,
            'curriculum': f"AQA GCSE ({curriculum_data.get('code', '')})",
            'topic': topic,
            'topic_id': topic_id,
            'subtopic_id': subtopic_id,
            'lesson_number': lesson_number,
            'unit': unit_display,
            'year_group': year_group,
            'do_now_questions': do_now_questions,
            'do_now_answers': do_now_answers,
            'learning_outcome': learning_outcome,
            'to_know': to_know,
            'content_points': content_points
        }
        st.success("✅ Lesson details saved!")
        st.switch_page("pages/2_Edit_Content.py")
