"""
Page 2: Curriculum Content
Detailed curriculum content with exam questions for teachers
"""
import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.comprehensive_curriculum import (
    TOPIC_4_1_DATA, 
    get_exam_questions, 
    get_content_module,
    get_separation_techniques,
    get_group_properties,
    get_misconceptions
)

st.set_page_config(
    page_title="Curriculum Content | GEMS TLAG",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Simple CSS
st.markdown("""
<style>
    .main .block-container { padding: 2rem 3rem; max-width: 1100px; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stButton > button {
        background: #10b981 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 📖 Curriculum Content & Exam Questions")
st.markdown("Browse detailed content and exam questions by topic.")

st.markdown("---")

# Topic selection
topic_data = TOPIC_4_1_DATA
metadata = topic_data.get("topic_metadata", {})

st.markdown(f"### {metadata.get('topic_id', '')} {metadata.get('topic_title', '')}")
st.markdown(f"**Course:** {metadata.get('course', '')} | **Exam:** {metadata.get('exam_paper', '')}")

# Tabs for different content types
tab1, tab2, tab3, tab4 = st.tabs(["📚 Content Modules", "📝 Exam Questions", "🔬 Practicals", "💡 Teaching Tips"])

# ============================================================================
# TAB 1: CONTENT MODULES
# ============================================================================
with tab1:
    st.markdown("### Content Modules")
    
    modules = topic_data.get("content_modules", [])
    
    for module in modules:
        with st.expander(f"**{module.get('module_id', '')}** {module.get('sub_topic', '')}", expanded=False):
            
            # Key concepts
            for concept in module.get("key_concepts", []):
                st.markdown(f"#### {concept.get('concept', '')}")
                
                # Details
                for detail in concept.get("details", []):
                    st.markdown(f"• {detail}")
                
                # Key terms
                key_terms = concept.get("key_terms", {})
                if key_terms:
                    st.markdown("**Key Terms:**")
                    for term, definition in key_terms.items():
                        st.markdown(f"- **{term}**: {definition}")
                
                # Examples
                examples = concept.get("examples", [])
                if examples:
                    st.markdown("**Examples:**")
                    for ex in examples:
                        if isinstance(ex, dict):
                            st.markdown(f"- {ex.get('substance', ex.get('isotope', ''))}: {ex.get('type', ex.get('components', ''))}")
                
                # Particles table
                particles = concept.get("particles", [])
                if particles:
                    st.markdown("**Subatomic Particles:**")
                    cols = st.columns(4)
                    cols[0].markdown("**Particle**")
                    cols[1].markdown("**Location**")
                    cols[2].markdown("**Charge**")
                    cols[3].markdown("**Mass**")
                    for p in particles:
                        cols = st.columns(4)
                        cols[0].markdown(p.get("name", ""))
                        cols[1].markdown(p.get("location", ""))
                        cols[2].markdown(p.get("relative_charge", ""))
                        cols[3].markdown(p.get("relative_mass", ""))
                
                st.markdown("---")
            
            # Techniques (for practical modules)
            for technique in module.get("techniques", []):
                st.markdown(f"#### 🧪 {technique.get('name', '')}")
                st.markdown(f"**Purpose:** {technique.get('purpose', '')}")
                st.markdown(f"**Example:** {technique.get('example', '')}")
                
                steps = technique.get("method_steps", [])
                if steps:
                    st.markdown("**Method:**")
                    for i, step in enumerate(steps, 1):
                        st.markdown(f"{i}. {step}")
                
                terms = technique.get("key_terms", {})
                if terms:
                    for term, defn in terms.items():
                        st.markdown(f"- **{term}**: {defn}")
                
                calc = technique.get("calculation", "")
                if calc:
                    st.info(f"📐 **Formula:** {calc}")
                
                st.markdown("---")
            
            # Group properties
            group_props = module.get("group_properties", {})
            for group_name, props in group_props.items():
                st.markdown(f"#### {group_name}")
                
                if isinstance(props, dict):
                    elements = props.get("elements", [])
                    if elements:
                        st.markdown(f"**Elements:** {', '.join(elements)}")
                    
                    properties = props.get("properties", [])
                    for prop in properties:
                        st.markdown(f"• {prop}")
                    
                    trends = props.get("trends", [])
                    if trends:
                        st.markdown("**Trends:**")
                        for trend in trends:
                            st.markdown(f"📈 {trend}")
                    
                    uses = props.get("uses", [])
                    if uses:
                        st.markdown(f"**Uses:** {', '.join(uses)}")
                
                st.markdown("---")

# ============================================================================
# TAB 2: EXAM QUESTIONS
# ============================================================================
with tab2:
    st.markdown("### Exam Questions Bank")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        diff_filter = st.selectbox("Difficulty", ["All", "Foundation", "Higher"])
    with col2:
        type_filter = st.selectbox("Question Type", ["All", "Multiple Choice", "Calculation", "Short Answer", "Extended Response", "Required Practical"])
    
    # Get filtered questions
    questions = topic_data.get("assessment_bank", [])
    
    if diff_filter != "All":
        questions = [q for q in questions if q.get("difficulty", "") == diff_filter]
    if type_filter != "All":
        questions = [q for q in questions if q.get("type", "") == type_filter]
    
    st.markdown(f"**{len(questions)} question(s) found**")
    
    for q in questions:
        with st.expander(f"**{q.get('question_id', '')}** - {q.get('type', '')} ({q.get('marks', 1)} marks)"):
            st.markdown(f"**Topic:** {q.get('topic', '')}")
            st.markdown(f"**Difficulty:** {q.get('difficulty', '')}")
            
            # Context if present
            context = q.get("context", "")
            if context:
                st.info(f"📋 **Context:** {context}")
            
            # Question
            st.markdown(f"**Question:** {q.get('question', q.get('text', ''))}")
            
            # Options for MC
            options = q.get("options", [])
            if options:
                st.markdown("**Options:**")
                for opt in options:
                    st.markdown(f"   {opt}")
            
            # Answer
            st.success(f"✅ **Answer:** {q.get('correct_answer', q.get('model_answer', ''))}")
            
            # Working/Rationale
            working = q.get("working", q.get("rationale", ""))
            if working:
                st.markdown(f"**Working/Rationale:** {working}")
            
            # Mark scheme
            mark_scheme = q.get("mark_scheme", q.get("mark_scheme_points", []))
            if mark_scheme:
                st.markdown("**Mark Scheme:**")
                for i, point in enumerate(mark_scheme, 1):
                    st.markdown(f"   {i}. {point}")
            
            # Copy button for question
            st.markdown("---")
            question_text = q.get('question', q.get('text', ''))
            st.code(question_text, language=None)

# ============================================================================
# TAB 3: PRACTICALS
# ============================================================================
with tab3:
    st.markdown("### Required Practicals & Techniques")
    
    techniques = get_separation_techniques()
    
    for tech in techniques:
        with st.expander(f"🧪 **{tech.get('name', '')}**"):
            st.markdown(f"**Purpose:** {tech.get('purpose', '')}")
            st.markdown(f"**Example:** {tech.get('example', '')}")
            
            # Apparatus
            apparatus = tech.get("apparatus", [])
            if apparatus:
                st.markdown(f"**Apparatus:** {', '.join(apparatus)}")
            
            # Method
            steps = tech.get("method_steps", [])
            if steps:
                st.markdown("**Method:**")
                for i, step in enumerate(steps, 1):
                    st.markdown(f"{i}. {step}")
            
            # Key terms
            terms = tech.get("key_terms", {})
            if terms:
                st.markdown("**Key Terms:**")
                for term, defn in terms.items():
                    st.markdown(f"- **{term}**: {defn}")
            
            # Calculation
            calc = tech.get("calculation", "")
            if calc:
                st.info(f"📐 **Formula:** {calc}")
            
            # Safety
            safety = tech.get("safety", "")
            if safety:
                st.warning(f"⚠️ **Safety:** {safety}")

# ============================================================================
# TAB 4: TEACHING TIPS
# ============================================================================
with tab4:
    st.markdown("### Teaching Tips & Resources")
    
    resources = topic_data.get("teaching_resources", {})
    
    # Misconceptions
    st.markdown("#### ⚠️ Common Misconceptions")
    misconceptions = resources.get("common_misconceptions", [])
    
    for m in misconceptions:
        col1, col2 = st.columns(2)
        with col1:
            st.error(f"❌ **Misconception:** {m.get('misconception', '')}")
        with col2:
            st.success(f"✅ **Correction:** {m.get('correction', '')}")
    
    st.markdown("---")
    
    # Key equations
    st.markdown("#### 📐 Key Equations")
    equations = resources.get("key_equations", [])
    for eq in equations:
        st.code(eq, language=None)
    
    st.markdown("---")
    
    # Practical tips
    st.markdown("#### 💡 Practical Tips")
    tips = resources.get("practical_tips", [])
    for tip in tips:
        st.markdown(f"• {tip}")

st.markdown("---")
st.caption("Built with ❤️ for GEMS Education Teachers")
