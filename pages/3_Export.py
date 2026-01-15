"""
Page 3: Export
Preview and download the PowerPoint
"""
import streamlit as st
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.pptx_builder import TLAGPowerPointBuilder

st.set_page_config(page_title="Export", page_icon="📥", layout="wide")

st.markdown("# 📥 Export PowerPoint")

# Check if lesson data exists
if 'lesson_data' not in st.session_state or not st.session_state.lesson_data:
    st.warning("⚠️ No lesson data found. Please create a lesson first.")
    if st.button("← Go to Create Lesson"):
        st.switch_page("pages/1_Create_Lesson.py")
    st.stop()

lesson = st.session_state.lesson_data

# Display lesson summary
st.markdown("## 📋 Lesson Summary")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"**Subject:** {lesson.get('subject', 'N/A')}")
    st.markdown(f"**Topic:** {lesson.get('topic', 'N/A')}")
    st.markdown(f"**Lesson Number:** {lesson.get('lesson_number', 'N/A')}")

with col2:
    st.markdown(f"**Curriculum:** {lesson.get('curriculum', 'N/A')}")
    st.markdown(f"**Unit:** {lesson.get('unit', 'N/A')}")
    st.markdown(f"**Year Group:** {lesson.get('year_group', 'N/A')}")

st.markdown("---")

# Slide Preview
st.markdown("## 📊 Slide Preview")

slides = [
    ("🕰️ Do Now", f"{len(lesson.get('do_now_questions', []))} questions"),
    ("🎯 Learning Outcome", lesson.get('learning_outcome', 'N/A')[:50] + "..."),
    ("🧠 To Know", f"{len(lesson.get('to_know', []))} points"),
    ("👁️ I Do", lesson.get('i_do_title', 'N/A')),
    ("👥 We Do", "Scaffolded Practice"),
    ("🎯 You Do", "3 differentiated tasks"),
    ("✔️ Affirmative Checking", "Exam Question"),
    ("🎟️ Exit Ticket", lesson.get('exit_question', 'N/A')[:30] + "...")
]

cols = st.columns(4)
for i, (title, desc) in enumerate(slides):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="border: 2px solid #336699; border-radius: 8px; padding: 10px; margin: 5px; text-align: center; min-height: 80px;">
            <strong>{title}</strong><br>
            <small style="color: #666;">{desc}</small>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Export Options
st.markdown("## 📁 Export Settings")

filename = st.text_input(
    "Filename",
    value=f"Lesson_{lesson.get('lesson_number', 1)}_{lesson.get('topic', 'Untitled').replace(' ', '_')}.pptx"
)

template_path = "templates/WSO Learn Like A GEM Template (1).pptx"

# Check if template exists
if not os.path.exists(template_path):
    # Try alternative path
    template_path = "WSO Learn Like A GEM Template (1).pptx"
    if not os.path.exists(template_path):
        st.error("❌ Template file not found! Please ensure the TLAG template is in the templates folder.")
        st.stop()

st.markdown("---")

# Generate Button
if st.button("🚀 Generate PowerPoint", type="primary", use_container_width=True):
    with st.spinner("Generating PowerPoint..."):
        try:
            # Build the presentation
            builder = TLAGPowerPointBuilder(template_path)
            builder.create_presentation()
            
            # Add Do Now
            builder.add_do_now(
                lesson.get('do_now_questions', []),
                lesson.get('do_now_answers', [])
            )
            
            # Add Outcomes
            builder.add_outcomes(
                lesson.get('learning_outcome', ''),
                lesson.get('to_know', [])
            )
            
            # Add I Do
            i_do_content = lesson.get('i_do_content', '').split('\n')
            builder.add_i_do(
                lesson.get('i_do_title', 'I Do'),
                i_do_content
            )
            
            # Add We Do
            we_do_steps = lesson.get('we_do_steps', '').split('\n')
            builder.add_we_do(
                "Scaffolded Practice",
                lesson.get('we_do_question', ''),
                we_do_steps
            )
            
            # Add You Do
            builder.add_you_do(lesson.get('you_do_tasks', []))
            
            # Add Affirmative Checking
            mark_scheme_lines = lesson.get('mark_scheme', '').split('\n')
            mark_scheme = []
            for line in mark_scheme_lines:
                if '=' in line:
                    parts = line.split('=')
                    mark_scheme.append({'step': parts[0].strip(), 'answer': parts[1].strip()})
                elif line.strip():
                    mark_scheme.append({'step': line.strip(), 'answer': ''})
            
            builder.add_affirmative_checking(
                lesson.get('exam_question', ''),
                mark_scheme
            )
            
            # Add Exit Ticket
            options = lesson.get('exit_options', '').split('\n')
            builder.add_exit_ticket(
                lesson.get('exit_question', ''),
                options,
                lesson.get('exit_answer', '')
            )
            
            # Save
            output_path = f"output/{filename}"
            os.makedirs("output", exist_ok=True)
            builder.save(output_path)
            
            st.success(f"✅ PowerPoint generated successfully!")
            
            # Download button
            with open(output_path, "rb") as file:
                st.download_button(
                    label="⬇️ Download PowerPoint",
                    data=file,
                    file_name=filename,
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    use_container_width=True
                )
            
        except Exception as e:
            st.error(f"❌ Error generating PowerPoint: {str(e)}")
            st.exception(e)

st.markdown("---")

# Navigation
col1, col2 = st.columns(2)

with col1:
    if st.button("← Back to Edit Content", use_container_width=True):
        st.switch_page("pages/2_Edit_Content.py")

with col2:
    if st.button("🆕 Create New Lesson", use_container_width=True):
        st.session_state.lesson_data = {}
        st.switch_page("pages/1_Create_Lesson.py")
