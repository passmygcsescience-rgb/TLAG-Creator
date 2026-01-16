"""
GEMS TLAG Lesson Creator
Main Streamlit Application - Modern Premium Design
"""
import streamlit as st

# Page config
st.set_page_config(
    page_title="GEMS TLAG Lesson Creator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern Premium CSS with Dark Theme & Glassmorphism
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
        max-width: 1200px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Remove default Streamlit styling */
    .stMarkdown {
        color: #e0e0e0;
    }
    
    /* Hero Section Styling */
    .hero-container {
        text-align: center;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
    }
    
    .hero-badge {
        display: inline-block;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2));
        border: 1px solid rgba(99, 102, 241, 0.4);
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        font-size: 0.85rem;
        color: #a78bfa;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(10px);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #a78bfa 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        line-height: 1.1;
        text-align: center;
        width: 100%;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.7);
        font-weight: 400;
        max-width: 600px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
        text-align: center;
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    }
    
    .glass-card:hover {
        transform: translateY(-8px);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 
            0 25px 60px rgba(99, 102, 241, 0.15),
            0 10px 20px rgba(0, 0, 0, 0.3);
    }
    
    /* Feature Cards */
    .feature-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 2rem 1.5rem;
        text-align: center;
        transition: all 0.4s ease;
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px) scale(1.02);
        border-color: rgba(99, 102, 241, 0.3);
        background: linear-gradient(145deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.05));
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }
    
    .feature-text {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.6);
        line-height: 1.5;
    }
    
    /* Stat Cards */
    .stat-card {
        background: linear-gradient(145deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.1));
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.6);
        margin-top: 0.5rem;
    }
    
    /* Subject Cards */
    .subject-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 1.75rem;
        transition: all 0.3s ease;
    }
    
    .subject-card:hover {
        background: rgba(255, 255, 255, 0.06);
        border-color: rgba(99, 102, 241, 0.3);
    }
    
    .subject-icon {
        font-size: 2rem;
        display: block;
        margin-bottom: 0.75rem;
    }
    
    .subject-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    
    .subject-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .subject-list li {
        color: rgba(255, 255, 255, 0.6);
        padding: 0.3rem 0;
        font-size: 0.9rem;
        position: relative;
        padding-left: 1rem;
    }
    
    .subject-list li::before {
        content: '›';
        position: absolute;
        left: 0;
        color: #a78bfa;
    }
    
    /* TLAG Method Section */
    .method-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 1rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .method-item:last-child {
        border-bottom: none;
    }
    
    .method-icon {
        font-size: 1.5rem;
        width: 40px;
        text-align: center;
    }
    
    .method-content {
        flex: 1;
    }
    
    .method-title {
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.25rem;
    }
    
    .method-desc {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.5);
    }
    
    /* Primary Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        padding: 1rem 2.5rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 
            0 10px 40px rgba(99, 102, 241, 0.4),
            0 4px 12px rgba(0, 0, 0, 0.2) !important;
        letter-spacing: 0.025em !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 
            0 20px 60px rgba(99, 102, 241, 0.5),
            0 8px 20px rgba(0, 0, 0, 0.25) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(0.98) !important;
    }
    
    /* Secondary Button */
    div[data-testid="column"]:nth-child(2) .stButton > button {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
    }
    
    div[data-testid="column"]:nth-child(2) .stButton > button:hover {
        background: rgba(255, 255, 255, 0.15) !important;
        border-color: rgba(99, 102, 241, 0.4) !important;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: #ffffff;
        margin: 3rem 0 1.5rem 0;
        text-align: center;
    }
    
    .section-subheader {
        text-align: center;
        color: rgba(255, 255, 255, 0.5);
        margin-bottom: 2.5rem;
        font-size: 1.1rem;
    }
    
    /* Divider */
    .modern-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        margin: 3rem 0;
        border: none;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-bottom: 2rem;
    }
    
    /* Floating Animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .floating {
        animation: float 4s ease-in-out infinite;
    }
    
    /* Glow Effect */
    @keyframes glow {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }
    
    .glow-orb {
        position: fixed;
        width: 400px;
        height: 400px;
        border-radius: 50%;
        filter: blur(100px);
        opacity: 0.3;
        pointer-events: none;
        animation: glow 8s ease-in-out infinite;
    }
    
    /* Hide Streamlit Metric styling */
    [data-testid="stMetric"] {
        background: transparent !important;
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        color: #a78bfa !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.6) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HERO SECTION
# ============================================================================
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">✨ Powered by TLAG Methodology</div>
    <h1 class="hero-title">GEMS TLAG<br>Lesson Creator</h1>
    <p class="hero-subtitle">Create stunning, pedagogically-sound PowerPoint lessons in seconds. Built for science teachers by the GEMS Education community.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# MAIN CTA BUTTONS
# ============================================================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    bcol1, bcol2 = st.columns(2)
    with bcol1:
        if st.button("🚀 Create a Lesson", type="primary", use_container_width=True):
            st.switch_page("pages/1_Create_Lesson.py")
    with bcol2:
        if st.button("📖 Browse Curriculum", use_container_width=True):
            st.switch_page("pages/2_Curriculum_Content.py")

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# STATS SECTION
# ============================================================================
st.markdown('<h2 class="section-header">Platform at a Glance</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <span class="stat-number">35+</span>
        <span class="stat-label">Ready Lessons</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <span class="stat-number">3</span>
        <span class="stat-label">Science Subjects</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <span class="stat-number">35+</span>
        <span class="stat-label">Topic Images</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <span class="stat-number">7</span>
        <span class="stat-label">Lesson Sections</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# HOW IT WORKS
# ============================================================================
st.markdown('<h2 class="section-header">How It Works</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subheader">Three simple steps to professional lessons</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📚</span>
        <div class="feature-title">1. Choose Topic</div>
        <p class="feature-text">Browse the AQA GCSE Science curriculum. Select your subject, topic, and subtopic.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📝</span>
        <div class="feature-title">2. Select Lesson</div>
        <p class="feature-text">Pick from our library of pre-made TLAG lessons with all sections included.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">⬇️</span>
        <div class="feature-title">3. Download</div>
        <p class="feature-text">Generate and download your professional PowerPoint instantly.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# SUBJECTS AVAILABLE
# ============================================================================
st.markdown('<h2 class="section-header">Subjects Available</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subheader">Comprehensive coverage of AQA GCSE Science</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="subject-card">
        <span class="subject-icon">⚗️</span>
        <div class="subject-title">Chemistry</div>
        <ul class="subject-list">
            <li>Atomic Structure & Periodic Table</li>
            <li>Bonding & Structure</li>
            <li>Quantitative Chemistry</li>
            <li>Chemical Changes</li>
            <li>Energy Changes</li>
            <li>Rates of Reaction</li>
            <li>Organic Chemistry</li>
            <li>Chemical Analysis</li>
            <li>Atmosphere</li>
            <li>Using Resources</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="subject-card">
        <span class="subject-icon">🧬</span>
        <div class="subject-title">Biology</div>
        <ul class="subject-list">
            <li>Cell Biology</li>
            <li>Organisation</li>
            <li>Infection & Response</li>
            <li>Bioenergetics</li>
            <li>Homeostasis</li>
            <li>Inheritance & Evolution</li>
            <li>Ecology</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="subject-card">
        <span class="subject-icon">⚡</span>
        <div class="subject-title">Physics</div>
        <ul class="subject-list">
            <li>Energy</li>
            <li>Electricity</li>
            <li>Particle Model</li>
            <li>Atomic Structure</li>
            <li>Forces</li>
            <li>Waves</li>
            <li>Magnetism</li>
            <li>Space Physics</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# TLAG STRUCTURE
# ============================================================================
st.markdown('<h2 class="section-header">The TLAG Lesson Structure</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subheader">Every lesson follows the proven Teach Like a GEM sequence</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card">
        <div class="method-item">
            <span class="method-icon">🕰️</span>
            <div class="method-content">
                <div class="method-title">Do Now</div>
                <div class="method-desc">Retrieval practice to activate prior knowledge</div>
            </div>
        </div>
        <div class="method-item">
            <span class="method-icon">🎯</span>
            <div class="method-content">
                <div class="method-title">Learning Outcome</div>
                <div class="method-desc">Clear success criteria for the lesson</div>
            </div>
        </div>
        <div class="method-item">
            <span class="method-icon">🧠</span>
            <div class="method-content">
                <div class="method-title">To Know</div>
                <div class="method-desc">Key knowledge points students must learn</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <div class="method-item">
            <span class="method-icon">👁️</span>
            <div class="method-content">
                <div class="method-title">I Do / We Do / You Do</div>
                <div class="method-desc">Gradual release of responsibility model</div>
            </div>
        </div>
        <div class="method-item">
            <span class="method-icon">✔️</span>
            <div class="method-content">
                <div class="method-title">Affirmative Checking</div>
                <div class="method-desc">Check understanding throughout the lesson</div>
            </div>
        </div>
        <div class="method-item">
            <span class="method-icon">🎟️</span>
            <div class="method-content">
                <div class="method-title">Exit Ticket</div>
                <div class="method-desc">Assess learning at the end of the lesson</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="modern-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# FINAL CTA
# ============================================================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if st.button("✨ Create Your First Lesson", type="primary", use_container_width=True, key="cta2"):
        st.switch_page("pages/1_Create_Lesson.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p class="footer-text">Built with ❤️ for GEMS Education Teachers</p>', unsafe_allow_html=True)
