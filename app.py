"""
GEMS TLAG Lesson Creator
Main Streamlit Application - Clean Design
"""
import streamlit as st

# Page config
st.set_page_config(
    page_title="GEMS TLAG Lesson Creator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Simple, clean CSS
st.markdown("""
<style>
    /* Clean base styles */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1100px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Button styling */
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
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER
# ============================================================================
st.markdown("# 🎓 GEMS TLAG Lesson Creator")
st.markdown("**Create professional PowerPoint lessons in seconds** using the Teach Like a GEM methodology.")

st.markdown("---")

# ============================================================================
# MAIN CTA
# ============================================================================
col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Create a Lesson", type="primary", use_container_width=True):
        st.switch_page("pages/1_Create_Lesson.py")
with col2:
    if st.button("📖 Browse Curriculum & Exam Questions", use_container_width=True):
        st.switch_page("pages/2_Curriculum_Content.py")

st.markdown("")
st.markdown("")

# ============================================================================
# HOW IT WORKS
# ============================================================================
st.markdown("## How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📚 Step 1")
    st.markdown("**Choose Topic**")
    st.markdown("Browse the AQA GCSE Science curriculum. Select your subject, topic, and subtopic.")

with col2:
    st.markdown("### 📝 Step 2")
    st.markdown("**Select Lesson**")
    st.markdown("Pick from our library of pre-made TLAG lessons with all sections included.")

with col3:
    st.markdown("### 📥 Step 3")
    st.markdown("**Download**")
    st.markdown("Generate and download your professional PowerPoint instantly.")

st.markdown("---")

# ============================================================================
# STATS
# ============================================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Ready Lessons", "35+")

with col2:
    st.metric("Science Subjects", "3")

with col3:
    st.metric("Topic Images", "35+")

with col4:
    st.metric("Lesson Sections", "7")

st.markdown("---")

# ============================================================================
# SUBJECTS
# ============================================================================
st.markdown("## Subjects Available")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚗️ Chemistry")
    st.markdown("""
    - Atomic Structure & Periodic Table
    - Bonding & Structure
    - Quantitative Chemistry
    - Chemical Changes
    - Energy Changes
    - Rates of Reaction
    - Organic Chemistry
    - Chemical Analysis
    - Atmosphere
    - Using Resources
    """)

with col2:
    st.markdown("### 🧬 Biology")
    st.markdown("""
    - Cell Biology
    - Organisation
    - Infection & Response
    - Bioenergetics
    - Homeostasis
    - Inheritance & Evolution
    - Ecology
    """)

with col3:
    st.markdown("### ⚡ Physics")
    st.markdown("""
    - Energy
    - Electricity
    - Particle Model
    - Atomic Structure
    - Forces
    - Waves
    - Magnetism
    - Space Physics
    """)

st.markdown("---")

# ============================================================================
# TLAG STRUCTURE
# ============================================================================
st.markdown("## The TLAG Lesson Structure")
st.markdown("Every lesson follows the proven Teach Like a GEM sequence:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("🕰️ **Do Now** - Retrieval practice to activate prior knowledge")
    st.markdown("🎯 **Learning Outcome** - Clear success criteria for the lesson")
    st.markdown("🧠 **To Know** - Key knowledge points students must learn")

with col2:
    st.markdown("👁️ **I Do / We Do / You Do** - Gradual release of responsibility")
    st.markdown("✔️ **Affirmative Checking** - Check understanding throughout")
    st.markdown("🎟️ **Exit Ticket** - Assess learning at the end")

st.markdown("---")

# ============================================================================
# FINAL CTA
# ============================================================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✨ Create Your First Lesson", type="primary", use_container_width=True, key="cta2"):
        st.switch_page("pages/1_Create_Lesson.py")

st.markdown("")
st.caption("Built with ❤️ for GEMS Education Teachers")
