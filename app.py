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
    initial_sidebar_state="collapsed"  # Start collapsed for cleaner look
)

# Custom CSS for modern design
st.markdown("""
<style>
    /* Main styling */
    .main .block-container {
        padding-top: 2rem;
        max-width: 1000px;
    }
    
    /* Hero section */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid #e0e0e0;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #666;
        font-size: 0.95rem;
    }
    
    /* Step indicator */
    .steps-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .step-item {
        text-align: center;
    }
    
    .step-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 0 auto 0.5rem;
    }
    
    /* TLAG sequence styling */
    .tlag-item {
        display: flex;
        align-items: center;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        background: linear-gradient(90deg, #f8f9fa 0%, #fff 100%);
        border-left: 4px solid #667eea;
    }
    
    .tlag-emoji {
        font-size: 1.5rem;
        margin-right: 1rem;
    }
    
    /* CTA button styling */
    .cta-container {
        text-align: center;
        margin: 2rem 0;
    }
    
    .stButton > button {
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #999;
        padding: 2rem;
        margin-top: 3rem;
    }
    
    /* Hide default sidebar content */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HERO SECTION
# ============================================================================
st.markdown('<p class="hero-title">🎓 GEMS TLAG Lesson Creator</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Create professional PowerPoint lessons in seconds using the Teach Like a GEM methodology</p>', unsafe_allow_html=True)

# ============================================================================
# MAIN CTA
# ============================================================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Create a New Lesson", type="primary", use_container_width=True):
        st.switch_page("pages/1_Create_Lesson.py")

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================================
# HOW IT WORKS
# ============================================================================
st.markdown("### 🔄 How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">1. Choose Topic</div>
        <div class="feature-desc">Browse the AQA GCSE curriculum and select your lesson topic</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📝</div>
        <div class="feature-title">2. Select Lesson</div>
        <div class="feature-desc">Pick from our library of pre-made TLAG lessons</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📥</div>
        <div class="feature-title">3. Download</div>
        <div class="feature-desc">Generate and download your professional PowerPoint</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================================
# TLAG STRUCTURE
# ============================================================================
st.markdown("### 📖 The TLAG Lesson Structure")
st.markdown("Every lesson follows the proven Teach Like a GEM sequence:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="tlag-item">
        <span class="tlag-emoji">🕰️</span>
        <div><strong>Do Now</strong> - Retrieval practice to activate prior knowledge</div>
    </div>
    <div class="tlag-item">
        <span class="tlag-emoji">🎯</span>
        <div><strong>Learning Outcome</strong> - Clear success criteria</div>
    </div>
    <div class="tlag-item">
        <span class="tlag-emoji">🧠</span>
        <div><strong>To Know</strong> - Key knowledge points</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tlag-item">
        <span class="tlag-emoji">👁️</span>
        <div><strong>I Do / We Do / You Do</strong> - Gradual release of responsibility</div>
    </div>
    <div class="tlag-item">
        <span class="tlag-emoji">✔️</span>
        <div><strong>Affirmative Checking</strong> - Check understanding</div>
    </div>
    <div class="tlag-item">
        <span class="tlag-emoji">🎟️</span>
        <div><strong>Exit Ticket</strong> - Assess learning</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================================
# SUBJECTS AVAILABLE
# ============================================================================
st.markdown("### 🔬 Subjects Available")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    #### ⚗️ Chemistry
    - Atomic Structure
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
    st.markdown("""
    #### 🧬 Biology
    - Cell Biology
    - Organisation
    - Infection & Response
    - Bioenergetics
    - Homeostasis
    - Inheritance & Evolution
    - Ecology
    """)

with col3:
    st.markdown("""
    #### ⚡ Physics
    - Energy
    - Electricity
    - Particle Model
    - Atomic Structure
    - Forces
    - Waves
    - Magnetism
    - Space Physics
    """)

# ============================================================================
# SECOND CTA
# ============================================================================
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✨ Start Creating Your Lesson", type="primary", use_container_width=True):
        st.switch_page("pages/1_Create_Lesson.py")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
<div class="footer">
    <p>Built with ❤️ for GEMS Education Teachers</p>
    <p style="font-size: 0.85rem;">Powered by the Teach Like a GEM methodology</p>
</div>
""", unsafe_allow_html=True)
