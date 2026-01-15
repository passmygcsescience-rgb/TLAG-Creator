"""
GEMS TLAG Lesson Creator
Main Streamlit Application - Modern Design
"""
import streamlit as st

# Page config
st.set_page_config(
    page_title="GEMS TLAG Lesson Creator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern CSS styling inspired by clean educational platforms
st.markdown("""
<style>
    /* Reset and base styles */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1200px;
    }
    
    /* Hide default Streamlit elements for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom navbar */
    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 0;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 2rem;
    }
    
    .nav-logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1.5rem;
        font-weight: 700;
        color: #1f2937;
    }
    
    .nav-logo span {
        color: #10b981;
    }
    
    /* Hero section */
    .hero {
        text-align: center;
        padding: 3rem 0;
    }
    
    .hero-title {
        font-size: 2.75rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #6b7280;
        max-width: 600px;
        margin: 0 auto 2rem;
        line-height: 1.6;
    }
    
    /* Section titles */
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
        text-align: center;
        margin: 3rem 0 2rem;
    }
    
    /* Step cards */
    .steps-container {
        display: flex;
        gap: 2rem;
        justify-content: center;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    
    .step-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 2rem;
        width: 320px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .step-card:hover {
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        transform: translateY(-4px);
    }
    
    .step-illustration {
        text-align: center;
        margin-bottom: 1.5rem;
        font-size: 4rem;
    }
    
    .step-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    .step-number {
        background: #10b981;
        color: white;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.9rem;
        flex-shrink: 0;
    }
    
    .step-title-group {
        flex: 1;
    }
    
    .step-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #1f2937;
        margin: 0;
    }
    
    .step-subtitle {
        font-size: 0.9rem;
        color: #9ca3af;
        margin: 0;
    }
    
    .step-description {
        color: #4b5563;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .step-quote {
        color: #10b981;
        font-weight: 600;
        font-size: 0.9rem;
        font-style: italic;
    }
    
    /* CTA Button */
    .cta-container {
        text-align: center;
        margin: 3rem 0;
    }
    
    .cta-button {
        background: #10b981;
        color: white;
        padding: 1rem 2.5rem;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .cta-button:hover {
        background: #059669;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3);
    }
    
    /* Subjects grid */
    .subjects-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .subject-card {
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .subject-card:hover {
        background: #ffffff;
        border-color: #10b981;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
    }
    
    .subject-icon {
        font-size: 2.5rem;
        margin-bottom: 0.75rem;
    }
    
    .subject-name {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    
    .subject-topics {
        font-size: 0.85rem;
        color: #6b7280;
    }
    
    /* TLAG sequence */
    .tlag-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin: 2rem 0;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .tlag-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem 1.25rem;
        background: #f9fafb;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
    }
    
    .tlag-icon {
        font-size: 1.5rem;
        width: 40px;
        text-align: center;
    }
    
    .tlag-text strong {
        color: #1f2937;
    }
    
    .tlag-text span {
        color: #6b7280;
        font-size: 0.9rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid #e5e7eb;
        color: #9ca3af;
    }
    
    /* Streamlit button override */
    .stButton > button {
        background: #10b981 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: #059669 !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3) !important;
    }
    
    /* Stats bar */
    .stats-bar {
        display: flex;
        justify-content: center;
        gap: 4rem;
        padding: 2rem 0;
        margin: 2rem 0;
        background: #f9fafb;
        border-radius: 12px;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: #10b981;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #6b7280;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# CUSTOM NAVBAR
# ============================================================================
st.markdown("""
<div class="navbar">
    <div class="nav-logo">
        🎓 <span>GEMS</span> TLAG Creator
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# HERO SECTION
# ============================================================================
st.markdown("""
<div class="hero">
    <h1 class="hero-title">Create TLAG Lessons in Seconds</h1>
    <p class="hero-subtitle">
        Professional PowerPoint lessons following the Teach Like a GEM methodology. 
        Just select a topic and download your ready-to-teach lesson.
    </p>
</div>
""", unsafe_allow_html=True)

# CTA Button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Start Creating", type="primary", use_container_width=True):
        st.switch_page("pages/1_Create_Lesson.py")

# ============================================================================
# HOW IT WORKS - STEP CARDS
# ============================================================================
st.markdown('<h2 class="section-title">How it works</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="steps-container">
    <div class="step-card">
        <div class="step-illustration">📚</div>
        <div class="step-header">
            <div class="step-number">1</div>
            <div class="step-title-group">
                <p class="step-title">Choose Topic</p>
                <p class="step-subtitle">browse the curriculum</p>
            </div>
        </div>
        <p class="step-description">
            Select from the complete AQA GCSE Science curriculum. 
            All topics organized by subject and unit for <strong>easy navigation</strong>.
        </p>
        <p class="step-quote">"Everything I need in one place"</p>
    </div>
    
    <div class="step-card">
        <div class="step-illustration">📝</div>
        <div class="step-header">
            <div class="step-number">2</div>
            <div class="step-title-group">
                <p class="step-title">Select Lesson</p>
                <p class="step-subtitle">ready-made content</p>
            </div>
        </div>
        <p class="step-description">
            Pick from our library of <strong>pre-made TLAG lessons</strong>. 
            Each includes Do Now, I Do, We Do, You Do, and Exit Ticket.
        </p>
        <p class="step-quote">"Saves me hours of planning time"</p>
    </div>
    
    <div class="step-card">
        <div class="step-illustration">📥</div>
        <div class="step-header">
            <div class="step-number">3</div>
            <div class="step-title-group">
                <p class="step-title">Download</p>
                <p class="step-subtitle">ready to teach</p>
            </div>
        </div>
        <p class="step-description">
            Generate and download your <strong>professional PowerPoint</strong> instantly. 
            Fully formatted and ready for your classroom.
        </p>
        <p class="step-quote">"Beautiful slides every time"</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# STATS BAR
# ============================================================================
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">35+</div>
        <div class="stat-label">Ready Lessons</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">3</div>
        <div class="stat-label">Science Subjects</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">35+</div>
        <div class="stat-label">Topic Images</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SUBJECTS AVAILABLE
# ============================================================================
st.markdown('<h2 class="section-title">Subjects Available</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="subjects-grid">
    <div class="subject-card">
        <div class="subject-icon">⚗️</div>
        <div class="subject-name">Chemistry</div>
        <div class="subject-topics">10 topics • 35+ lessons</div>
    </div>
    <div class="subject-card">
        <div class="subject-icon">🧬</div>
        <div class="subject-name">Biology</div>
        <div class="subject-topics">7 topics • Growing library</div>
    </div>
    <div class="subject-card">
        <div class="subject-icon">⚡</div>
        <div class="subject-name">Physics</div>
        <div class="subject-topics">8 topics • Growing library</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# TLAG STRUCTURE
# ============================================================================
st.markdown('<h2 class="section-title">The TLAG Lesson Structure</h2>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280; margin-bottom: 2rem;'>Every lesson follows the proven Teach Like a GEM sequence</p>", unsafe_allow_html=True)

st.markdown("""
<div class="tlag-grid">
    <div class="tlag-item">
        <div class="tlag-icon">🕰️</div>
        <div class="tlag-text">
            <strong>Do Now</strong><br>
            <span>Retrieval practice</span>
        </div>
    </div>
    <div class="tlag-item">
        <div class="tlag-icon">🎯</div>
        <div class="tlag-text">
            <strong>Learning Outcome</strong><br>
            <span>Clear success criteria</span>
        </div>
    </div>
    <div class="tlag-item">
        <div class="tlag-icon">🧠</div>
        <div class="tlag-text">
            <strong>To Know</strong><br>
            <span>Key knowledge points</span>
        </div>
    </div>
    <div class="tlag-item">
        <div class="tlag-icon">👁️</div>
        <div class="tlag-text">
            <strong>I Do / We Do / You Do</strong><br>
            <span>Gradual release</span>
        </div>
    </div>
    <div class="tlag-item">
        <div class="tlag-icon">✔️</div>
        <div class="tlag-text">
            <strong>Affirmative Checking</strong><br>
            <span>Check understanding</span>
        </div>
    </div>
    <div class="tlag-item">
        <div class="tlag-icon">🎟️</div>
        <div class="tlag-text">
            <strong>Exit Ticket</strong><br>
            <span>Assess learning</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# FINAL CTA
# ============================================================================
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("✨ Create Your First Lesson", type="primary", use_container_width=True, key="cta2"):
        st.switch_page("pages/1_Create_Lesson.py")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
<div class="footer">
    <p>Built with ❤️ for GEMS Education Teachers</p>
</div>
""", unsafe_allow_html=True)
