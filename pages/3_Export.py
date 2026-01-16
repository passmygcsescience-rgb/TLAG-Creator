"""
Page 3: Export - Modern Premium Design
Preview and download the PowerPoint
"""
import streamlit as st
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.pptx_builder import TLAGPowerPointBuilder

st.set_page_config(
    page_title="Export",
    page_icon="📥",
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
    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #ffffff;
        margin: 2rem 0 1.5rem 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    /* Summary Card */
    .summary-card {
        background: linear-gradient(145deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.1));
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 20px;
        padding: 1.5rem 2rem;
        margin-bottom: 2rem;
    }
    
    .summary-item {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .summary-item:last-child {
        border-bottom: none;
    }
    
    .summary-label {
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.95rem;
    }
    
    .summary-value {
        color: #ffffff;
        font-weight: 500;
    }
    
    /* Slide Cards Grid */
    .slide-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.25rem;
        text-align: center;
        transition: all 0.3s ease;
        min-height: 100px;
    }
    
    .slide-card:hover {
        transform: translateY(-4px);
        border-color: rgba(99, 102, 241, 0.4);
        background: rgba(99, 102, 241, 0.1);
    }
    
    .slide-icon {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .slide-title {
        font-weight: 600;
        color: #ffffff;
        font-size: 0.95rem;
        margin-bottom: 0.25rem;
    }
    
    .slide-desc {
        font-size: 0.8rem;
        color: rgba(255, 255, 255, 0.5);
    }
    
    /* Export Settings Card */
    .export-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 1.5rem 2rem;
        margin-bottom: 2rem;
    }
    
    /* Primary Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        padding: 1rem 2rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 10px 40px rgba(99, 102, 241, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 0 15px 50px rgba(99, 102, 241, 0.5) !important;
    }
    
    /* Download Button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        padding: 1rem 2rem !important;
        box-shadow: 0 10px 40px rgba(16, 185, 129, 0.4) !important;
        transition: all 0.4s ease !important;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 15px 50px rgba(16, 185, 129, 0.5) !important;
    }
    
    /* Secondary buttons in navigation */
    div.row-widget.stButton:first-child > button {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
    }
    
    /* Text Input Styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        padding: 0.875rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* Labels */
    .stTextInput label {
        color: rgba(255, 255, 255, 0.7) !important;
        font-weight: 500 !important;
    }
    
    /* Alert boxes */
    .stAlert {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
    }
    
    /* Success Message */
    [data-testid="stAlert"][data-baseweb="notification"] {
        background: rgba(16, 185, 129, 0.15) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
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
    <h1 class="page-title">📥 Export PowerPoint</h1>
    <p class="page-subtitle">Preview and download your lesson</p>
</div>
""", unsafe_allow_html=True)

# Check if lesson data exists
if 'lesson_data' not in st.session_state or not st.session_state.lesson_data:
    st.warning("⚠️ No lesson data found. Please create a lesson first.")
    if st.button("← Go to Create Lesson"):
        st.switch_page("pages/1_Create_Lesson.py")
    st.stop()

lesson = st.session_state.lesson_data

# Display lesson summary
st.markdown('<h3 class="section-title">📋 Lesson Summary</h3>', unsafe_allow_html=True)

st.markdown(f"""
<div class="summary-card">
    <div class="summary-item">
        <span class="summary-label">Subject</span>
        <span class="summary-value">{lesson.get('subject', 'N/A')}</span>
    </div>
    <div class="summary-item">
        <span class="summary-label">Topic</span>
        <span class="summary-value">{lesson.get('topic', 'N/A')}</span>
    </div>
    <div class="summary-item">
        <span class="summary-label">Lesson Number</span>
        <span class="summary-value">{lesson.get('lesson_number', 'N/A')}</span>
    </div>
    <div class="summary-item">
        <span class="summary-label">Curriculum</span>
        <span class="summary-value">{lesson.get('curriculum', 'N/A')}</span>
    </div>
    <div class="summary-item">
        <span class="summary-label">Unit</span>
        <span class="summary-value">{lesson.get('unit', 'N/A')}</span>
    </div>
    <div class="summary-item">
        <span class="summary-label">Year Group</span>
        <span class="summary-value">{lesson.get('year_group', 'N/A')}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Slide Preview
st.markdown('<h3 class="section-title">📊 Slide Preview</h3>', unsafe_allow_html=True)

slides = [
    ("🕰️", "Do Now", f"{len(lesson.get('do_now_questions', []))} questions"),
    ("🎯", "Learning Outcome", "Success criteria"),
    ("🧠", "To Know", f"{len(lesson.get('to_know', []))} points"),
    ("👁️", "I Do", lesson.get('i_do_title', 'Teacher modelling')),
    ("👥", "We Do", "Scaffolded Practice"),
    ("🎯", "You Do", "3 differentiated tasks"),
    ("✔️", "Affirmative Check", "Exam Question"),
    ("🎟️", "Exit Ticket", "Assessment")
]

cols = st.columns(4)
for i, (icon, title, desc) in enumerate(slides):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="slide-card">
            <span class="slide-icon">{icon}</span>
            <div class="slide-title">{title}</div>
            <div class="slide-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# Export Options
st.markdown('<h3 class="section-title">📁 Export Settings</h3>', unsafe_allow_html=True)

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

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# Generate Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
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
                st.balloons()
                
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

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# Navigation
col1, col2 = st.columns(2)

with col1:
    if st.button("← Back to Edit Content", use_container_width=True):
        st.switch_page("pages/2_Edit_Content.py")

with col2:
    if st.button("🆕 Create New Lesson", use_container_width=True):
        st.session_state.lesson_data = {}
        st.switch_page("pages/1_Create_Lesson.py")
