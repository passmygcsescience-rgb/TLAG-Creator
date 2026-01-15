"""
TLAG Configuration - GEMS Lesson Generation Rules
This file contains the methodology and formatting rules for TLAG lessons.
"""

# ==============================================================================
# TLAG 6-STEP SEQUENCE (Non-Negotiable Order)
# ==============================================================================
LESSON_SEQUENCE = [
    "DO_NOW",           # 1. Retrieval Practice (3-5 questions on PRIOR material)
    "LEARNING_OUTCOME", # 2. ONE precise skill-based outcome
    "TO_KNOW",          # 3. Essential facts/concepts (substantive knowledge)
    "I_DO",             # 4a. Teacher modelling (explicit instruction)
    "WE_DO",            # 4b. Guided practice (scaffolded)
    "YOU_DO",           # 4c. Independent practice (scaffolding removed)
    "AFFIRMATIVE_CHECK",# 5. Checkpoint DURING You Do (not end marking)
    "EXIT_TICKET"       # 6. Assess the Learning Outcome skill
]

# ==============================================================================
# TEMPLATE LAYOUTS (PowerPoint indices)
# ==============================================================================
LAYOUTS = {
    "DO_NOW": 1,
    "OUTCOMES": 2,      # Learning Outcomes | To Know (two-column)
    "I_DO": 4,
    "WE_DO": 5,
    "YOU_DO": 6,
    "CHECK": 7,         # Affirmative Checking
    "EXIT": 8           # Exit Tickets
}

# ==============================================================================
# ICONS (For slide content)
# ==============================================================================
ICONS = {
    "DO_NOW": "🕰️",
    "LEARNING_OUTCOME": "🎯",
    "TO_KNOW": "🧠",
    "AFFIRMATIVE_CHECK": "✔️",
    "EXIT_TICKET": "🎟️"
}

# ==============================================================================
# TERMINOLOGY (ALWAYS use these, never alternatives)
# ==============================================================================
TERMINOLOGY = {
    "correct": {
        "outcome": "Learning Outcome",
        "knowledge": "To Know"
    },
    "never_use": {
        "outcome": ["Objective", "Aim", "Goal"],
        "knowledge": ["Key Words", "Vocabulary", "Key Terms"]
    }
}

# ==============================================================================
# CURRICULUM SOURCES
# ==============================================================================
CURRICULA = {
    "AQA_GCSE_BIOLOGY": {"code": "8461", "spec": "v1.0 (2016)"},
    "AQA_GCSE_CHEMISTRY": {"code": "8462", "spec": "v1.1 (2019)"},
    "AQA_GCSE_PHYSICS": {"code": "8463", "spec": "v1.1 (2019)"},
    "IB_DP_CHEMISTRY": {"code": "IB", "spec": "2023 Guide (First Assessment 2025)"},
    "KS3": {"code": "KS3", "spec": "National Curriculum"},
    "OCR_ALEVEL": {"code": "OCR", "spec": "A-Level (General)"}
}

# ==============================================================================
# FORMATTING RULES
# ==============================================================================
FORMATTING = {
    "font": "Arial",
    "font_size": 24,  # pt
    "position": {
        "top": 0.85,   # inches from top
        "left": 0.3,   # inches from left
        "width": 12.7, # inches
        "height": 6.3  # inches
    },
    "colors": {
        "text": (0, 0, 0),           # Black
        "answer": (192, 0, 0),       # Red
        "keyword": (0, 112, 192),    # Light Blue
        "final_answer": (0, 128, 0), # Green
        "header": (51, 102, 153)     # WSO Blue
    }
}

# ==============================================================================
# DO NOW RULES
# ==============================================================================
DO_NOW_RULES = {
    "question_count": (3, 5),  # Min, Max questions
    "content": "PRIOR material only - never new lesson content",
    "types": ["free_recall", "cued_recall"],  # Mix required
    "examples": {
        "free_recall": "List three...",
        "cued_recall": "Fill in the blank: The formula for... is ___"
    }
}

# ==============================================================================
# I DO / WE DO / YOU DO RULES
# ==============================================================================
INSTRUCTIONAL_PHASES = {
    "I_DO": {
        "description": "Explicit teacher modelling",
        "techniques": ["Cold Call", "Show Call"],
        "content": "Script or bullet points for teacher to follow"
    },
    "WE_DO": {
        "description": "Guided practice with scaffolding",
        "techniques": ["Turn and Talk"],
        "content": "Joint activity with sentence starters, partially completed examples"
    },
    "YOU_DO": {
        "description": "Independent practice - scaffolding removed",
        "techniques": [],
        "content": "Full task to build fluency",
        "differentiation": "Support tools, NOT different outcomes"
    }
}

# ==============================================================================
# AFFIRMATIVE CHECKING SCRIPT
# ==============================================================================
AFFIRMATIVE_CHECK_SCRIPT = '''
Circulate now. Check specifically for [INSERT COMMON MISCONCEPTION].
Provide real-time feedback to guide improvement.
'''

# ==============================================================================
# EXIT TICKET RULES
# ==============================================================================
EXIT_TICKET_RULES = {
    "purpose": "Assess the Learning Outcome (skill application)",
    "not_for": "Simple fact recall",
    "format": "Short task or question"
}
