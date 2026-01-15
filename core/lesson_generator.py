"""
AI Lesson Generator
Generates complete TLAG lesson content using OpenAI API
Uses the official GEMS TLAG methodology with cognitive-science-based structure.
"""
import os
import json
from openai import OpenAI

# =============================================================================
# TLAG SYSTEM PROMPT - Official GEMS Methodology
# =============================================================================
TLAG_SYSTEM_PROMPT = """# ROLE
You are the "GEMS TLAG Lesson Creator." You are an expert science teacher specializing in AQA GCSE (Biology, Chemistry, Physics) and IB DP Chemistry.

# OBJECTIVE
Generate a high-quality, cognitive-science-based lesson plan following the "Teach Like a GEM" (TLAG) methodology.

# 1. TLAG METHODOLOGY (NON-NEGOTIABLE)
You must follow this exact 6-step sequence for every lesson. Do not deviate.

## Step 1: Do Now (Retrieval Practice)
* **Function:** Activate prior knowledge.
* **Rule:** Focus ONLY on *previously learned* material (prior lessons/units). Do NOT introduce new content here.
* **Format:** Mix of free recall ("List 3...") and cued recall (fill-in-the-blank).

## Step 2: Learning Outcome
* **Function:** Define the goal.
* **Rule:** Generate **ONE** single, precise outcome describing a **skill** or **procedural knowledge** (e.g., "Calculate rate of reaction").
* **Constraint:** Do NOT differentiate (no "All/Most/Some"). All students aim for this one outcome.

## Step 3: To Know (Substantive Knowledge)
* **Function:** The "ingredients" of the lesson.
* **Rule:** List the essential facts/concepts needed to achieve the outcome. Write these as clear knowledge statements.

## Step 4: I Do, We Do, You Do (Instructional Phase)
* **A. I Do (Modelling):** Script for explicit instruction. Suggest using **Cold Call** to check listening.
* **B. We Do (Guided Practice):** A joint activity with scaffolding (e.g., sentence starters). Suggest using **Turn and Talk**.
* **C. You Do (Independent Practice):** Independent task with scaffolding removed. Differentiate by support tools, not task.

## Step 5: Affirmative Checking (Feedback Loop)
* **Function:** Active monitoring during the 'You Do' phase.
* **Rule:** Define a specific "Check Point" (e.g., "Check specifically for [Common Misconception]. Give real-time feedback.").

## Step 6: Exit Ticket
* **Function:** Final assessment.
* **Rule:** Must directly assess the **Learning Outcome** (Step 2) to check if the skill was mastered.

---

# 2. CURRICULUM KNOWLEDGE BASE
Use these specifications to ensure content accuracy:

## AQA GCSE Biology (8461)
* **4.1 Cell Biology:** Eukaryotes/Prokaryotes, Mitosis, Stem cells, Diffusion/Osmosis/Active transport.
* **4.2 Organisation:** Enzymes, Digestion, Heart/Circulatory system, Plant transport, Non-communicable diseases.
* **4.3 Infection:** Pathogens (Viral/Bacterial/Fungal), Immune system, Vaccines, Antibiotics, Monoclonal antibodies (Bio Only).
* **4.4 Bioenergetics:** Photosynthesis (Rate factors, Inverse square law), Respiration (Aerobic/Anaerobic), Metabolism.
* **4.5 Homeostasis:** Nervous system, Reflex arc, Hormones (Glucose/Reproduction), Kidney/Dialysis (Bio Only).
* **4.6 Inheritance:** DNA structure, Meiosis, Genetic crosses, Evolution, Selective breeding, Genetic engineering.
* **4.7 Ecology:** Adaptations, Food chains, Carbon/Water cycles, Biodiversity, Global warming.

## AQA GCSE Chemistry (8462)
* **4.1 Atomic Structure:** Periodic table history, Groups 1/7/0, Transition metals.
* **4.2 Bonding:** Ionic, Covalent, Metallic, Nanoparticles, States of matter.
* **4.3 Quantitative:** Moles, Concentration (mol/dm3), Atom economy, Titrations (Chem Only).
* **4.4 Chemical Changes:** Reactivity series, Acids/Alkalis, Electrolysis (Molten/Aqueous).
* **4.5 Energy Changes:** Exothermic/Endothermic profiles, Cells/Batteries (Chem Only).
* **4.6 Rates:** Collision theory, Catalysts, Reversible reactions, Equilibrium (Le Chatelier).
* **4.7 Organic:** Alkanes, Alkenes, Cracking, Alcohols/Carboxylic Acids/Polymers (Chem Only).
* **4.8 Analysis:** Purity, Chromatography, Gas tests, Ion tests (Chem Only).
* **4.9 Atmosphere:** Evolution of atmosphere, Greenhouse gases, Pollutants.
* **4.10 Resources:** Potable water, Life Cycle Assessment (LCA), Haber Process (Chem Only).

## AQA GCSE Physics (8463)
* **4.1 Energy:** Stores, SHC, Power, Efficiency, Renewables.
* **4.2 Electricity:** Circuits (I-V characteristics), Mains (AC/DC), National Grid.
* **4.3 Particle Model:** Density, Internal energy, Latent heat, Gas pressure.
* **4.4 Atomic Structure:** Radiation types (Alpha/Beta/Gamma), Half-life, Fission/Fusion.
* **4.5 Forces:** Scalars/Vectors, Newton's Laws, Elasticity, Braking distance, Momentum.
* **4.6 Waves:** Transverse/Longitudinal, Sound/Light, Lenses (Phys Only), Black body (Phys Only).
* **4.7 Magnetism:** Electromagnets, Motor effect, Transformers/Generators (Phys Only).
* **4.8 Space:** Solar system, Red-shift, Big Bang.

## IB DP Chemistry (2025 Spec)
* **Structure:** Particle model, Atomic structure, Electron config, Moles, Ideal gases.
* **Reactivity:** Enthalpy, Entropy (HL), Kinetics (Rates), Equilibrium, Acids/Bases, Redox, Organic mechanisms.

---

# 3. VISUAL DESCRIPTION RULES
For slides where a visual diagram is essential (To Know, I Do, We Do), include an `image_description` field.

**Rules for Image Descriptions:**
1. **Goal:** Describe the exact image the teacher should search for and insert later.
2. **Detail:** Be specific and educational.
   * *Bad:* "Diagram of bonding."
   * *Good:* "Diagram showing a Sodium atom losing one electron to a Chlorine atom, illustrating the formation of Na+ and Cl- ions."
3. **Format:** Start with "[TEACHER NOTE: Insert diagram showing..." and end with "]"

**Examples:**
* Chemistry: "[TEACHER NOTE: Insert dot and cross diagram showing electron transfer from Mg (2,8,2) to O (2,6) forming Mg2+ and O2-]"
* Biology: "[TEACHER NOTE: Insert labelled diagram of animal cell showing nucleus, mitochondria, ribosomes, and cell membrane]"
* Physics: "[TEACHER NOTE: Insert force diagram showing weight, normal force, friction, and driving force on a car]"

---

# 4. OUTPUT REQUIREMENTS
You must output VALID JSON only. No markdown formatting. Follow the schema exactly."""


# =============================================================================
# JSON SCHEMA - Matches TLAG 6-Step Structure with Image Descriptions
# =============================================================================
LESSON_JSON_SCHEMA = """{
  "title": "Lesson Title",
  "spec_reference": "AQA Spec Reference (e.g., AQA Chem 4.2.1)",
  "do_now": {
    "questions": ["Q1 (retrieval from prior learning)", "Q2", "Q3", "Q4", "Q5"],
    "answers": ["A1", "A2", "A3", "A4", "A5"],
    "focus": "Topic this retrieves from"
  },
  "learning_outcome": "To Be Able To: [Single Precise Skill]",
  "to_know": [
    "Substantive Knowledge Statement 1",
    "Substantive Knowledge Statement 2",
    "Substantive Knowledge Statement 3",
    "Substantive Knowledge Statement 4",
    "Substantive Knowledge Statement 5"
  ],
  "to_know_image": "[TEACHER NOTE: Insert diagram showing... (specific description)]",
  "i_do": {
    "title": "Title of Teacher Modelling",
    "content": ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5"],
    "technique": "Cold Call to check listening",
    "image_description": "[TEACHER NOTE: Insert diagram showing... (specific educational diagram description)]"
  },
  "we_do": {
    "question": "Guided practice question",
    "steps": ["Step 1 with scaffold", "Step 2", "Step 3", "Step 4", "Step 5"],
    "technique": "Turn and Talk",
    "image_description": "[TEACHER NOTE: Insert diagram showing... (specific visual aid description)]"
  },
  "you_do": [
    {"name": "Bronze (Grade 5)", "question": "Basic application", "answer": "Model answer"},
    {"name": "Silver (Grade 7)", "question": "Intermediate challenge", "answer": "Model answer"},
    {"name": "Gold (Grade 9)", "question": "Extension/mastery", "answer": "Model answer"}
  ],
  "affirmative_checking": {
    "checkpoint": "Specific error/misconception to check for",
    "action": "Real-time feedback strategy"
  },
  "exit_ticket": {
    "question": "Assessment question directly linked to Learning Outcome",
    "options": ["A) option", "B) option", "C) option", "D) option"],
    "answer": "Correct letter"
  }
}"""


# =============================================================================
# LESSON GENERATOR CLASS
# =============================================================================
class LessonGenerator:
    """Generates TLAG lessons using OpenAI API."""
    
    def __init__(self, api_key: str = None):
        """Initialize with OpenAI API key."""
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None
    
    def generate_lesson(self, subject: str, topic: str, subtopic: str, 
                       spec_content: list = None) -> dict:
        """Generate a complete TLAG lesson for the given topic."""
        
        if not self.client:
            raise ValueError("OpenAI API key not configured. Please set OPENAI_API_KEY.")
        
        # Build the prompt
        user_prompt = f"""Generate a complete TLAG lesson for:

Subject: {subject}
Topic: {topic}
Subtopic: {subtopic}
"""
        
        if spec_content:
            user_prompt += f"""
Specification Content to cover:
{chr(10).join('- ' + point for point in spec_content)}
"""
        
        user_prompt += f"""
Return your response as valid JSON matching this schema:
{LESSON_JSON_SCHEMA}

IMPORTANT:
- Do Now must focus on PRIOR learning (not today's new content)
- Learning Outcome must be ONE precise skill (no All/Most/Some)
- To Know are the substantive knowledge "ingredients" for this lesson
- I Do uses Cold Call technique
- We Do uses Turn and Talk technique
- Affirmative Checking identifies a specific misconception to monitor
- Exit Ticket directly assesses the Learning Outcome

Ensure all content is accurate, appropriate for GCSE level, and follows TLAG methodology exactly."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": TLAG_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.7
            )
            
            content = response.choices[0].message.content
            lesson_data = json.loads(content)
            
            # Normalize the response to match our internal format
            normalized = self._normalize_lesson_data(lesson_data)
            
            return {
                "success": True,
                "lesson": normalized
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _normalize_lesson_data(self, data: dict) -> dict:
        """Normalize AI response to match our internal lesson format."""
        # Handle both old and new schema formats
        lesson = {
            "title": data.get("title", "Generated Lesson"),
            "spec_reference": data.get("spec_reference", ""),
            "learning_outcome": data.get("learning_outcome", ""),
            "to_know": data.get("to_know", []),
            "do_now": data.get("do_now", {"questions": [], "answers": []}),
            "i_do": data.get("i_do", {"title": "", "content": []}),
            "we_do": data.get("we_do", {"question": "", "steps": []}),
            "you_do": data.get("you_do", []),
            "affirmative_checking": data.get("affirmative_checking", {}),
            "exit_ticket": data.get("exit_ticket", {})
        }
        return lesson


def generate_lesson_content(subject: str, topic: str, subtopic: str, 
                           spec_content: list = None, api_key: str = None) -> dict:
    """Convenience function to generate lesson content."""
    generator = LessonGenerator(api_key)
    return generator.generate_lesson(subject, topic, subtopic, spec_content)
