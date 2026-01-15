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
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📚 Content Modules", "📝 Exam Questions", "🔬 Practicals", "💡 Teaching Tips", "📜 History", "🎓 Higher Tier"])

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
    
    # Purity definitions
    purity_data = topic_data.get("purity_and_definitions", {})
    if purity_data:
        st.markdown("#### 🧪 Purity Definitions (Important for Exams)")
        for concept in purity_data.get("key_concepts", []):
            st.markdown(f"**{concept.get('concept', '')}**")
            for detail in concept.get("details", []):
                st.markdown(f"• {detail}")
            
            key_dist = concept.get("key_distinction", {})
            if key_dist:
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"🔬 **Chemistry:** {key_dist.get('Chemistry definition', '')}")
                with col2:
                    st.warning(f"🏠 **Everyday:** {key_dist.get('Everyday definition', '')}")
            
            exam_tip = concept.get("exam_tip", "")
            if exam_tip:
                st.success(f"💡 **Exam Tip:** {exam_tip}")
    
    st.markdown("---")
    
    # Comparison tables
    comp_tables = topic_data.get("comparison_tables", {})
    if comp_tables:
        st.markdown("#### 📊 Comparison Tables")
        
        trans_vs_g1 = comp_tables.get("transition_vs_group1", {})
        if trans_vs_g1:
            st.markdown("**Transition Elements vs Group 1** (6-mark question)")
            st.caption(trans_vs_g1.get("note", ""))
            
            # Physical properties table
            phys = trans_vs_g1.get("physical_properties", {})
            if phys:
                st.markdown("**Physical Properties:**")
                headers = phys.get("headers", [])
                rows = phys.get("rows", [])
                
                cols = st.columns(3)
                for i, h in enumerate(headers):
                    cols[i].markdown(f"**{h}**")
                for row in rows:
                    cols = st.columns(3)
                    for i, cell in enumerate(row):
                        cols[i].markdown(cell)
            
            # Chemical properties table
            chem = trans_vs_g1.get("chemical_properties", {})
            if chem:
                st.markdown("**Chemical Properties:**")
                headers = chem.get("headers", [])
                rows = chem.get("rows", [])
                
                cols = st.columns(3)
                for i, h in enumerate(headers):
                    cols[i].markdown(f"**{h}**")
                for row in rows:
                    cols = st.columns(3)
                    for i, cell in enumerate(row):
                        cols[i].markdown(cell)
            
            # Model answer
            model = trans_vs_g1.get("model_6_mark_answer", "")
            if model:
                with st.expander("📝 View Model 6-Mark Answer"):
                    st.markdown(model)
    
    st.markdown("---")
    
    # Maths skills
    maths_data = topic_data.get("maths_skills", {})
    if maths_data:
        st.markdown("#### 📐 Maths Skills")
        
        for skill in maths_data.get("skills", []):
            with st.expander(f"🔢 {skill.get('skill', '')}"):
                context = skill.get("context", "")
                if context:
                    st.markdown(f"**Context:** {context}")
                
                formula = skill.get("formula", "")
                if formula:
                    st.code(formula, language=None)
                
                # Worked examples
                for ex in skill.get("worked_examples", []):
                    st.markdown(f"**Q:** {ex.get('question', '')}")
                    st.markdown("**Working:**")
                    for step in ex.get("working", []):
                        st.markdown(f"   {step}")
                    st.success(f"**A:** {ex.get('answer', '')}")
                    st.markdown("---")
                
                # Single worked example
                we = skill.get("worked_example", {})
                if we:
                    st.markdown(f"**Q:** {we.get('question', '')}")
                    st.markdown("**Working:**")
                    for step in we.get("working", []):
                        st.markdown(f"   {step}")
                    st.success(f"**A:** {we.get('answer', '')}")
                
                # Common errors
                errors = skill.get("common_errors", [])
                if errors:
                    st.markdown("**Common Errors:**")
                    for err in errors:
                        st.error(f"❌ {err}")
    
    st.markdown("---")
    
    # Practical marking points
    marking = topic_data.get("practical_marking_points", {})
    if marking:
        st.markdown("#### ✅ Practical Diagram Marking Points")
        
        for prac_name, prac_data in marking.items():
            with st.expander(f"🔬 {prac_name.title()} Diagram Requirements"):
                reqs = prac_data.get("diagram_requirements", [])
                if reqs:
                    st.markdown("**Must include:**")
                    for req in reqs:
                        st.markdown(f"✓ {req}")
                
                errors = prac_data.get("common_errors", [])
                if errors:
                    st.markdown("**Common Errors (avoid these):**")
                    for err in errors:
                        st.error(f"❌ {err}")
                
                checklist = prac_data.get("full_marks_checklist", [])
                if checklist:
                    st.markdown("**Full Marks Checklist:**")
                    for item in checklist:
                        st.markdown(f"• {item}")

# ============================================================================
# TAB 5: HISTORY
# ============================================================================
with tab5:
    st.markdown("### History of the Atom & Periodic Table")
    
    # Atom timeline
    atom_history = topic_data.get("history_of_atom", {})
    if atom_history:
        st.markdown("#### ⏳ Development of the Atomic Model")
        
        timeline = atom_history.get("timeline", [])
        for event in timeline:
            with st.expander(f"**{event.get('era', '')}** - {event.get('model', '')} ({event.get('scientist', '')})"):
                st.markdown(f"**Details:** {event.get('details', '')}")
                
                if event.get('discovery'):
                    st.info(f"🔬 **Discovery:** {event.get('discovery')}")
                
                if event.get('experiment'):
                    st.markdown(f"**Experiment:** {event.get('experiment')}")
                
                observations = event.get('observations', [])
                if observations:
                    st.markdown("**Observations:**")
                    for obs in observations:
                        st.markdown(f"• {obs}")
                
                if event.get('conclusion'):
                    st.success(f"✓ **Conclusion:** {event.get('conclusion')}")
                
                if event.get('key_idea'):
                    st.markdown(f"**Key Idea:** {event.get('key_idea')}")
        
        # Exam question
        exam_q = atom_history.get("common_exam_question", {})
        if exam_q:
            st.markdown("---")
            st.markdown("**📝 Common Exam Question:**")
            st.warning(exam_q.get("question", ""))
            with st.expander("View Mark Scheme"):
                for point in exam_q.get("mark_scheme", []):
                    st.markdown(f"• {point}")
    
    st.markdown("---")
    
    # Periodic table history
    pt_history = topic_data.get("periodic_table_history", {})
    if pt_history:
        st.markdown("#### 📊 Development of the Periodic Table")
        
        for figure in pt_history.get("key_figures", []):
            with st.expander(f"**{figure.get('era', '')}** - {figure.get('name', '')}"):
                st.markdown(f"**Method:** {figure.get('method', '')}")
                
                if figure.get('idea'):
                    st.markdown(f"**Idea:** {figure.get('idea')}")
                
                limitations = figure.get('limitations', [])
                if limitations:
                    st.markdown("**Limitations:**")
                    for lim in limitations:
                        st.error(f"❌ {lim}")
                
                genius = figure.get('genius_moves', [])
                if genius:
                    st.markdown("**Genius Moves:**")
                    for g in genius:
                        st.success(f"✓ {g}")
                
                if figure.get('validation'):
                    st.info(f"🎯 **Validation:** {figure.get('validation')}")
                
                if figure.get('key_change'):
                    st.markdown(f"**Key Change:** {figure.get('key_change')}")
        
        exam_tip = pt_history.get("exam_tip", "")
        if exam_tip:
            st.success(f"💡 **Exam Tip:** {exam_tip}")
    
    st.markdown("---")
    
    # Halogens detailed
    halogens = topic_data.get("group_7_halogens", {})
    if halogens:
        st.markdown("#### 🧪 Group 7 Halogens - Detailed")
        
        # Elements table
        elements = halogens.get("elements", [])
        if elements:
            st.markdown("**Halogen Elements:**")
            cols = st.columns(4)
            cols[0].markdown("**Element**")
            cols[1].markdown("**Symbol**")
            cols[2].markdown("**Colour**")
            cols[3].markdown("**State at RT**")
            for el in elements:
                cols = st.columns(4)
                cols[0].markdown(el.get("name", ""))
                cols[1].markdown(el.get("symbol", ""))
                cols[2].markdown(el.get("colour", ""))
                cols[3].markdown(el.get("state_at_RT", ""))
        
        # Displacement reactions
        disp = halogens.get("displacement_reactions", {})
        if disp:
            st.markdown("---")
            st.markdown("**Displacement Reactions:**")
            st.info(f"📜 **Rule:** {disp.get('rule', '')}")
            
            for ex in disp.get("examples", []):
                st.markdown(f"**{ex.get('word_equation', ex.get('reaction', ''))}**")
                st.code(ex.get("symbol_equation", ""), language=None)
                if ex.get("observation"):
                    st.markdown(f"👁️ Observation: {ex.get('observation')}")
            
            no_reaction = disp.get("no_reaction_examples", [])
            if no_reaction:
                st.markdown("**No Reaction Examples:**")
                for nr in no_reaction:
                    st.error(f"❌ {nr}")
    
    st.markdown("---")
    
    # Standard form
    sf = topic_data.get("standard_form_skills", {})
    if sf:
        st.markdown("#### 📐 Standard Form & Atomic Sizes")
        
        for fact in sf.get("key_facts", []):
            st.markdown(f"• {fact}")
        
        reminder = sf.get("standard_form_reminder", {})
        if reminder:
            st.code(reminder.get("format", ""), language=None)
            
            examples = reminder.get("examples", [])
            for ex in examples:
                st.markdown(f"• {ex.get('value')} = **{ex.get('standard_form')}** ({ex.get('context')})")

# ============================================================================
# TAB 6: HIGHER TIER
# ============================================================================
with tab6:
    st.markdown("### 🎓 Higher Tier Content")
    st.info("This content is specifically for **Higher Tier** students aiming for grades 7-9.")
    
    ht_content = topic_data.get("higher_tier_content", {})
    
    # Atomic Sizes
    atomic_sizes = ht_content.get("atomic_sizes", {})
    if atomic_sizes:
        with st.expander("📏 Size and Mass of Atoms (Memorisation Required)", expanded=True):
            st.markdown(f"**{atomic_sizes.get('module_id', '')}** - {atomic_sizes.get('sub_topic', '')}")
            
            for fact in atomic_sizes.get("key_facts", []):
                st.markdown(f"**{fact.get('fact')}:** {fact.get('value')}")
                if fact.get('detail'):
                    st.caption(fact.get('detail'))
                if fact.get('visual_analogy'):
                    st.info(f"🏟️ **Analogy:** {fact.get('visual_analogy')}")
    
    # Relative Atomic Mass
    ar_content = ht_content.get("relative_atomic_mass", {})
    if ar_content:
        with st.expander("⚗️ Relative Atomic Mass (Ar) Calculation", expanded=True):
            st.warning(f"⚠️ **{ar_content.get('tier', '')}**")
            st.markdown(f"**Concept:** {ar_content.get('concept', '')}")
            st.markdown(f"**Definition:** {ar_content.get('definition', '')}")
            
            st.markdown("**Formula:**")
            st.code(ar_content.get("formula", ""), language=None)
            st.code(ar_content.get("formula_expanded", ""), language=None)
            
            st.markdown("---")
            st.markdown("**Worked Examples:**")
            
            for ex in ar_content.get("worked_examples", []):
                st.markdown(f"**{ex.get('element', '')}:** {ex.get('question', '')}")
                st.markdown("**Working:**")
                for step in ex.get("working", []):
                    st.markdown(f"   {step}")
                st.success(f"**Answer:** {ex.get('answer', '')}")
                if ex.get("explanation"):
                    st.info(f"💡 {ex.get('explanation')}")
                st.markdown("---")
            
            if ar_content.get("exam_tip"):
                st.success(f"📝 **Exam Tip:** {ar_content.get('exam_tip')}")
    
    # Chemical Equations
    chem_eq = ht_content.get("chemical_equations", {})
    if chem_eq:
        with st.expander("⚖️ Chemical Equations & State Symbols"):
            for fund in chem_eq.get("fundamentals", []):
                st.markdown(f"**{fund.get('concept', '')}**")
                
                symbols = fund.get("symbols", {})
                if symbols:
                    cols = st.columns(4)
                    for i, (sym, meaning) in enumerate(symbols.items()):
                        cols[i].code(sym)
                        cols[i].caption(meaning)
                
                if fund.get("exam_tip"):
                    st.warning(f"⚠️ {fund.get('exam_tip')}")
                
                examples = fund.get("examples", [])
                if examples:
                    st.markdown("**Examples:**")
                    for ex in examples:
                        st.code(ex, language=None)
                
                steps = fund.get("steps", [])
                if steps:
                    for i, step in enumerate(steps, 1):
                        st.markdown(f"{i}. {step}")
                
                st.markdown("---")
    
    # Half Equations
    half_eq = ht_content.get("half_equations", {})
    if half_eq:
        with st.expander("⚡ Half Equations (Higher Tier Only)"):
            st.warning(f"⚠️ **{half_eq.get('tier', '')}**")
            st.markdown(f"**Purpose:** {half_eq.get('purpose', '')}")
            
            st.markdown("**Key Terms:**")
            terms = half_eq.get("key_terms", {})
            for term, meaning in terms.items():
                if term == "OILRIG":
                    st.success(f"🧠 **{term}:** {meaning}")
                else:
                    st.markdown(f"• **{term}:** {meaning}")
            
            examples = half_eq.get("examples", {})
            
            # Group 1 oxidation
            g1 = examples.get("group_1_oxidation", {})
            if g1:
                st.markdown(f"**{g1.get('description', '')}**")
                for eq in g1.get("equations", []):
                    st.code(eq, language=None)
                st.caption(g1.get("explanation", ""))
            
            # Group 7 reduction
            g7 = examples.get("group_7_reduction", {})
            if g7:
                st.markdown(f"**{g7.get('description', '')}**")
                for eq in g7.get("equations", []):
                    st.code(eq, language=None)
                st.caption(g7.get("explanation", ""))
            
            # Combining
            combining = half_eq.get("combining_half_equations", {})
            if combining:
                st.markdown("---")
                st.markdown(f"**Combining Half Equations:** {combining.get('example', '')}")
                st.markdown("Oxidation:")
                st.code(combining.get("oxidation", ""), language=None)
                st.markdown("Reduction:")
                st.code(combining.get("reduction", ""), language=None)
                st.markdown("Overall:")
                st.code(combining.get("overall", ""), language=None)
                st.info(combining.get("note", ""))
    
    # Electronic Structure
    elec = ht_content.get("electronic_structure_diagrams", {})
    if elec:
        with st.expander("⚛️ Drawing Electronic Structures"):
            st.markdown("**Method:**")
            for i, step in enumerate(elec.get("method", []), 1):
                st.markdown(f"{i}. {step}")
            
            st.markdown("---")
            st.markdown("**Common Examples:**")
            examples = elec.get("common_examples", [])
            cols = st.columns(4)
            cols[0].markdown("**Element**")
            cols[1].markdown("**Atomic #**")
            cols[2].markdown("**Config**")
            cols[3].markdown("**Description**")
            
            for ex in examples:
                cols = st.columns(4)
                cols[0].markdown(f"{ex.get('element')} ({ex.get('symbol')})")
                cols[1].markdown(str(ex.get("atomic_number")))
                cols[2].code(ex.get("config"))
                cols[3].caption(ex.get("description"))
            
            if elec.get("exam_tip"):
                st.success(f"📝 **Exam Tip:** {elec.get('exam_tip')}")

st.markdown("---")
st.caption("Built with ❤️ for GEMS Education Teachers")
