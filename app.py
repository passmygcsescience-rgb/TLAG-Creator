"""
GEMS TLAG Lesson Creator
Main Streamlit Application
"""
import streamlit as st

# Page config
st.set_page_config(
    page_title="GEMS TLAG Lesson Creator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #336699;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton > button {
        background-color: #336699;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<p class="main-header">🎓 GEMS TLAG Lesson Creator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Create professional lesson PowerPoints following the Teach Like a GEM methodology</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=GEMS", width=150)
    st.markdown("---")
    st.markdown("### 📚 Navigation")
    st.markdown("""
    1. **Create Lesson** - Enter lesson details
    2. **Edit Content** - Review and edit
    3. **Export** - Download PowerPoint
    """)
    st.markdown("---")
    st.markdown("### 📖 TLAG Sequence")
    st.markdown("""
    1. 🕰️ Do Now
    2. 🎯 Learning Outcome
    3. 🧠 To Know
    4. 👁️ I Do / We Do / You Do
    5. ✔️ Affirmative Checking
    6. 🎟️ Exit Ticket
    """)

# Main page content
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✨ Quick Start")
    st.markdown("""
    1. Click **Create Lesson** in the sidebar
    2. Enter your lesson details
    3. Edit and review content
    4. Export your PowerPoint
    """)
    
    if st.button("🚀 Create New Lesson", type="primary", use_container_width=True):
        st.switch_page("pages/1_Create_Lesson.py")

with col2:
    st.markdown("### 📊 Recent Lessons")
    st.info("No lessons created yet. Click 'Create New Lesson' to get started!")

# Footer
st.markdown("---")
st.markdown("*Built with ❤️ for GEMS Education*")
