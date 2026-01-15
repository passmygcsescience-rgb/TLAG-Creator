"""
AQA GCSE Chemistry Comprehensive Curriculum Data
Contains detailed content modules, exam questions, and teaching resources.
"""

# ============================================================================
# TOPIC 4.1: ATOMIC STRUCTURE AND THE PERIODIC TABLE
# ============================================================================

TOPIC_4_1_DATA = {
    "topic_metadata": {
        "course": "AQA GCSE Chemistry (8462) & Combined Science: Trilogy",
        "topic_id": "4.1",
        "topic_title": "Atomic Structure and the Periodic Table",
        "exam_paper": "Paper 1",
        "spec_reference": "AQA Specification 2023"
    },
    
    "content_modules": [
        {
            "module_id": "4.1.1",
            "sub_topic": "A Simple Model of the Atom",
            "key_concepts": [
                {
                    "concept": "Atoms, Elements and Compounds",
                    "details": [
                        "All substances are made of atoms. An atom is the smallest part of an element that can exist.",
                        "Atoms of each element are represented by a chemical symbol (e.g., O for oxygen, Na for sodium).",
                        "There are about 100 different elements shown in the periodic table.",
                        "Compounds contain two or more elements chemically combined in fixed proportions.",
                        "Compounds can only be separated into elements by chemical reactions.",
                        "Chemical reactions always involve the formation of one or more new substances and often involve a detectable energy change."
                    ],
                    "key_terms": {
                        "Atom": "The smallest part of an element that can exist",
                        "Element": "A substance made of only one type of atom",
                        "Compound": "Two or more elements chemically combined in fixed proportions",
                        "Chemical reaction": "A process that forms new substances, often with energy change"
                    },
                    "common_misconceptions": [
                        "Students confuse atoms and molecules - molecules are groups of atoms bonded together",
                        "Students think compounds can be separated by physical methods - they require chemical reactions"
                    ],
                    "image_keyword": "atom"
                },
                {
                    "concept": "Mixtures",
                    "details": [
                        "A mixture consists of two or more substances that are not chemically combined.",
                        "The chemical properties of each substance in the mixture are unchanged.",
                        "Mixtures can be separated by physical processes: filtration, crystallisation, simple distillation, fractional distillation, and chromatography."
                    ],
                    "examples": [
                        {"substance": "Air", "type": "Mixture", "components": "N₂, O₂, Ar, CO₂"},
                        {"substance": "Steel", "type": "Mixture (Alloy)", "components": "Iron and carbon"},
                        {"substance": "Carbon Dioxide", "type": "Compound", "components": "Carbon and oxygen chemically bonded"},
                        {"substance": "Sea water", "type": "Mixture", "components": "Water and dissolved salts"}
                    ],
                    "key_comparison": {
                        "Mixture": "Not chemically combined, variable proportions, separated by physical methods",
                        "Compound": "Chemically combined, fixed proportions, separated by chemical methods"
                    },
                    "image_keyword": "mixture"
                }
            ]
        },
        {
            "module_id": "4.1.2",
            "sub_topic": "Separation Techniques",
            "is_required_practical": True,
            "techniques": [
                {
                    "name": "Filtration",
                    "purpose": "Separating an insoluble solid from a liquid",
                    "example": "Separating sand from salt water",
                    "apparatus": ["Filter funnel", "Filter paper", "Conical flask", "Retort stand"],
                    "method_steps": [
                        "Set up filter funnel in retort stand over conical flask",
                        "Fold filter paper and place in funnel",
                        "Pour mixture into filter",
                        "Residue (solid) stays on paper, filtrate (liquid) passes through"
                    ],
                    "key_terms": {
                        "Residue": "The solid left on the filter paper",
                        "Filtrate": "The liquid that passes through"
                    },
                    "image_keyword": "filtration"
                },
                {
                    "name": "Crystallisation",
                    "purpose": "Obtaining pure solid crystals from a solution",
                    "example": "Obtaining copper sulfate crystals from copper sulfate solution",
                    "apparatus": ["Evaporating basin", "Bunsen burner", "Tripod", "Gauze"],
                    "method_steps": [
                        "Heat the solution gently to evaporate some water",
                        "Stop when crystals start to appear at edges",
                        "Leave to cool and allow crystals to form",
                        "Filter and dry the crystals"
                    ],
                    "safety": "Do not heat to dryness - crystals may spit",
                    "image_keyword": "crystallisation"
                },
                {
                    "name": "Simple Distillation",
                    "purpose": "Separating a solvent from a solution",
                    "example": "Obtaining pure water from salt solution",
                    "apparatus": ["Distillation flask", "Condenser", "Collection flask", "Thermometer"],
                    "method_steps": [
                        "Heat the solution until it boils",
                        "Vapour rises and enters condenser",
                        "Condenser cools vapour back to liquid",
                        "Pure liquid collects in collection flask"
                    ],
                    "image_keyword": "distillation"
                },
                {
                    "name": "Fractional Distillation",
                    "purpose": "Separating a mixture of liquids with different boiling points",
                    "example": "Separating ethanol from water",
                    "key_principle": "Liquids with lower boiling points evaporate first",
                    "apparatus": ["Fractionating column", "Distillation flask", "Condenser", "Thermometer"],
                    "image_keyword": "distillation"
                },
                {
                    "name": "Chromatography",
                    "purpose": "Separating mixtures of coloured substances or testing purity",
                    "example": "Separating food colourings in ink",
                    "apparatus": ["Chromatography paper", "Beaker", "Solvent", "Pencil line"],
                    "method_steps": [
                        "Draw pencil line near bottom of paper",
                        "Place spots of sample on the line",
                        "Lower paper into solvent (solvent below pencil line)",
                        "Allow solvent to rise up the paper",
                        "Remove when solvent near top and allow to dry"
                    ],
                    "key_terms": {
                        "Rf value": "Distance moved by substance ÷ distance moved by solvent",
                        "Stationary phase": "The paper",
                        "Mobile phase": "The solvent"
                    },
                    "calculation": "Rf = distance moved by substance / distance moved by solvent front",
                    "image_keyword": "chromatography"
                }
            ]
        },
        {
            "module_id": "4.1.3",
            "sub_topic": "Atomic Structure",
            "key_concepts": [
                {
                    "concept": "Subatomic Particles",
                    "particles": [
                        {"name": "Proton", "location": "Nucleus", "relative_charge": "+1", "relative_mass": "1"},
                        {"name": "Neutron", "location": "Nucleus", "relative_charge": "0", "relative_mass": "1"},
                        {"name": "Electron", "location": "Shells around nucleus", "relative_charge": "-1", "relative_mass": "Very small (≈0)"}
                    ],
                    "key_facts": [
                        "Atoms have no overall charge because protons (+) = electrons (−)",
                        "The nucleus is very small compared to the overall size of the atom",
                        "Most of the atom is empty space"
                    ],
                    "image_keyword": "subatomic"
                },
                {
                    "concept": "Atomic Number and Mass Number",
                    "definitions": {
                        "Atomic number": "The number of protons in an atom (also equals electrons in neutral atom)",
                        "Mass number": "The total number of protons and neutrons in the nucleus"
                    },
                    "calculations": [
                        "Protons = Atomic number",
                        "Electrons = Atomic number (in neutral atom)",
                        "Neutrons = Mass number − Atomic number"
                    ],
                    "image_keyword": "atom"
                },
                {
                    "concept": "Isotopes",
                    "definition": "Atoms of the same element with the same number of protons but different numbers of neutrons",
                    "examples": [
                        {"isotope": "Carbon-12", "protons": 6, "neutrons": 6},
                        {"isotope": "Carbon-14", "protons": 6, "neutrons": 8}
                    ],
                    "key_fact": "Isotopes have the same chemical properties but different physical properties (e.g., mass)"
                }
            ]
        },
        {
            "module_id": "4.1.4",
            "sub_topic": "Electronic Structure",
            "key_concepts": [
                {
                    "concept": "Electron Shells",
                    "rules": [
                        "Electrons occupy shells (energy levels) around the nucleus",
                        "First shell holds maximum 2 electrons",
                        "Second shell holds maximum 8 electrons",
                        "Third shell holds maximum 8 electrons (simplified model)"
                    ],
                    "examples": [
                        {"element": "Hydrogen (H)", "atomic_number": 1, "configuration": "1"},
                        {"element": "Carbon (C)", "atomic_number": 6, "configuration": "2,4"},
                        {"element": "Oxygen (O)", "atomic_number": 8, "configuration": "2,6"},
                        {"element": "Sodium (Na)", "atomic_number": 11, "configuration": "2,8,1"},
                        {"element": "Chlorine (Cl)", "atomic_number": 17, "configuration": "2,8,7"},
                        {"element": "Calcium (Ca)", "atomic_number": 20, "configuration": "2,8,8,2"}
                    ],
                    "image_keyword": "electronic"
                },
                {
                    "concept": "Electronic Structure and the Periodic Table",
                    "key_facts": [
                        "Elements in the same group have the same number of electrons in their outer shell",
                        "The group number equals the number of outer shell electrons",
                        "Elements in the same group have similar chemical properties"
                    ]
                }
            ]
        },
        {
            "module_id": "4.1.5",
            "sub_topic": "The Periodic Table",
            "key_concepts": [
                {
                    "concept": "Development of the Periodic Table",
                    "history": [
                        "Early scientists arranged by atomic weight but found problems",
                        "Mendeleev left gaps for undiscovered elements",
                        "Modern table arranged by atomic number (number of protons)"
                    ]
                },
                {
                    "concept": "Structure of the Periodic Table",
                    "key_facts": [
                        "Groups - vertical columns (elements with similar properties)",
                        "Periods - horizontal rows (elements with same number of shells)",
                        "Metals on the left, non-metals on the right"
                    ],
                    "image_keyword": "periodic table"
                }
            ],
            "group_properties": {
                "Group 0 (Noble Gases)": {
                    "elements": ["Helium (He)", "Neon (Ne)", "Argon (Ar)", "Krypton (Kr)", "Xenon (Xe)"],
                    "properties": [
                        "Unreactive - have full outer electron shells",
                        "Exist as single atoms (monatomic)",
                        "Colourless gases at room temperature"
                    ],
                    "trends": [
                        "Boiling points INCREASE going down the group",
                        "This is because atoms get larger, so intermolecular forces increase"
                    ],
                    "uses": ["Helium in balloons", "Argon in light bulbs", "Neon in signs"],
                    "image_keyword": "noble gas"
                },
                "Group 1 (Alkali Metals)": {
                    "elements": ["Lithium (Li)", "Sodium (Na)", "Potassium (K)", "Rubidium (Rb)", "Caesium (Cs)"],
                    "properties": [
                        "Soft metals - can be cut with a knife",
                        "Low density - Li, Na, K float on water",
                        "Low melting points compared to other metals",
                        "Shiny when freshly cut, but tarnish quickly in air",
                        "Very reactive, especially with water"
                    ],
                    "reactions": {
                        "with_water": "Metal + Water → Metal hydroxide + Hydrogen",
                        "with_oxygen": "Metal + Oxygen → Metal oxide",
                        "with_chlorine": "Metal + Chlorine → Metal chloride"
                    },
                    "trends": [
                        "Reactivity INCREASES down the group",
                        "Melting point DECREASES down the group",
                        "Reason: Outer electron is further from nucleus, easier to lose"
                    ],
                    "image_keyword": "alkali metal"
                },
                "Group 7 (Halogens)": {
                    "elements": ["Fluorine (F₂)", "Chlorine (Cl₂)", "Bromine (Br₂)", "Iodine (I₂)"],
                    "properties": [
                        "Exist as diatomic molecules (pairs of atoms)",
                        "Coloured: F₂ pale yellow, Cl₂ green, Br₂ brown, I₂ purple vapour",
                        "Poisonous"
                    ],
                    "trends": [
                        "Reactivity DECREASES down the group",
                        "Melting/boiling points INCREASE down the group",
                        "Reason: Harder to gain electron as atom gets larger"
                    ],
                    "displacement": "A more reactive halogen can displace a less reactive halogen from its salt solution",
                    "image_keyword": "halogen"
                },
                "Transition Metals": {
                    "examples": ["Iron (Fe)", "Copper (Cu)", "Zinc (Zn)", "Nickel (Ni)", "Gold (Au)"],
                    "properties": [
                        "High melting points and densities",
                        "Hard and strong",
                        "Good conductors of heat and electricity",
                        "Less reactive than Group 1"
                    ],
                    "special_properties": [
                        "Form ions with different charges (e.g., Fe²⁺ and Fe³⁺)",
                        "Form coloured compounds",
                        "Often used as catalysts (e.g., iron in Haber process)"
                    ],
                    "comparison_with_group1": {
                        "Transition Metals": "High MP, high density, hard, low reactivity, coloured compounds, variable ions, catalysts",
                        "Group 1": "Low MP, low density, soft, very reactive, white compounds, +1 ions only, not catalysts"
                    },
                    "image_keyword": "transition metal"
                }
            }
        }
    ],

    "assessment_bank": [
        {
            "question_id": "MC_4.1_001",
            "type": "Multiple Choice",
            "difficulty": "Foundation",
            "topic": "Atoms, Elements and Compounds",
            "question": "Substance A contains only one type of atom and does not conduct electricity. What type of substance is A?",
            "options": ["Compound", "Metallic element", "Mixture", "Non-metallic element"],
            "correct_answer": "Non-metallic element",
            "marks": 1,
            "rationale": "Metals conduct electricity. Compounds contain more than one type of atom. A substance with only one atom type that doesn't conduct is a non-metallic element."
        },
        {
            "question_id": "MC_4.1_002",
            "type": "Multiple Choice",
            "difficulty": "Foundation",
            "topic": "Compounds",
            "question": "Substance B contains two types of atoms chemically combined in fixed proportions. What type of substance is B?",
            "options": ["Compound", "Metallic element", "Mixture", "Non-metallic element"],
            "correct_answer": "Compound",
            "marks": 1,
            "rationale": "Fixed proportions and chemical combination are the defining features of a compound."
        },
        {
            "question_id": "DA_4.1_001",
            "type": "Data Analysis",
            "difficulty": "Higher",
            "topic": "Periodic Table Properties",
            "context": "Element Q is a dull solid with a melting point of 44°C and does not conduct electricity.",
            "question": "Which section of the periodic table is most likely to contain element Q? Explain your answer.",
            "model_answer": "Right side (non-metals section). Non-metals are typically dull, have low melting points, and do not conduct electricity.",
            "marks": 2,
            "mark_scheme": [
                "Right side / non-metals (1 mark)",
                "Low melting point / does not conduct / dull - these are properties of non-metals (1 mark)"
            ]
        },
        {
            "question_id": "CALC_4.1_001",
            "type": "Calculation",
            "difficulty": "Foundation",
            "topic": "Subatomic Particles",
            "question": "Calculate the number of neutrons in an atom with Mass Number 11 and Atomic Number 5.",
            "correct_answer": "6",
            "marks": 1,
            "working": "Neutrons = Mass Number − Atomic Number = 11 − 5 = 6"
        },
        {
            "question_id": "CALC_4.1_002",
            "type": "Calculation",
            "difficulty": "Foundation",
            "topic": "Subatomic Particles",
            "question": "An atom has 17 protons and 18 neutrons. Calculate its mass number.",
            "correct_answer": "35",
            "marks": 1,
            "working": "Mass Number = Protons + Neutrons = 17 + 18 = 35"
        },
        {
            "question_id": "CALC_4.1_003",
            "type": "Calculation",
            "difficulty": "Higher",
            "topic": "Chromatography",
            "question": "A substance travels 4.2 cm and the solvent front travels 7.0 cm. Calculate the Rf value.",
            "correct_answer": "0.6",
            "marks": 2,
            "working": "Rf = distance moved by substance / distance moved by solvent = 4.2 / 7.0 = 0.6"
        },
        {
            "question_id": "SHORT_4.1_001",
            "type": "Short Answer",
            "difficulty": "Foundation",
            "topic": "Isotopes",
            "question": "Define the term 'isotope'.",
            "model_answer": "Atoms of the same element with the same number of protons but different numbers of neutrons.",
            "marks": 2,
            "mark_scheme": [
                "Same element / same number of protons (1 mark)",
                "Different numbers of neutrons (1 mark)"
            ]
        },
        {
            "question_id": "SHORT_4.1_002",
            "type": "Short Answer",
            "difficulty": "Foundation",
            "topic": "Electronic Structure",
            "question": "Write the electronic structure of sodium (atomic number 11).",
            "correct_answer": "2,8,1",
            "marks": 1
        },
        {
            "question_id": "EXT_4.1_001",
            "type": "Extended Response",
            "difficulty": "Higher",
            "topic": "Group Comparisons",
            "question": "Compare the physical and chemical properties of Transition Elements and Group 1 elements.",
            "marks": 6,
            "mark_scheme": [
                "Physical: Transition elements have high melting points (1)",
                "Physical: Transition elements have high densities (1)",
                "Physical: Group 1 have low melting points and low densities (1)",
                "Physical: Transition metals are hard and strong, Group 1 are soft (1)",
                "Chemical: Transition elements have low reactivity, Group 1 very reactive (1)",
                "Chemical: Transition elements form coloured compounds, Group 1 form white compounds (1)",
                "Chemical: Transition elements can be catalysts, Group 1 cannot (1)",
                "Chemical: Transition elements form ions with variable charges, Group 1 only +1 (1)"
            ],
            "model_answer": "Transition elements have much higher melting points and densities than Group 1 metals. They are hard and strong, while Group 1 metals are soft enough to cut with a knife. \n\nChemically, transition elements are much less reactive than Group 1 - they react slowly with water or oxygen while Group 1 metals react vigorously. Transition elements form coloured compounds and ions with different charges (e.g., Fe²⁺ and Fe³⁺), whereas Group 1 only form white compounds and +1 ions. Transition elements are often used as catalysts, but Group 1 metals are not."
        },
        {
            "question_id": "EXT_4.1_002",
            "type": "Extended Response",
            "difficulty": "Higher",
            "topic": "Group 7 Trends",
            "question": "Explain why reactivity decreases down Group 7.",
            "marks": 3,
            "mark_scheme": [
                "Atoms get larger going down the group (1)",
                "Outer shell is further from the nucleus (1)",
                "Harder to attract/gain an electron into outer shell (1)"
            ]
        },
        {
            "question_id": "PRAC_4.1_001",
            "type": "Required Practical",
            "difficulty": "Foundation",
            "topic": "Chromatography",
            "question": "Describe how you would use chromatography to determine if a food colouring contains one dye or a mixture of dyes.",
            "marks": 6,
            "mark_scheme": [
                "Draw pencil line near bottom of chromatography paper (1)",
                "Put spot of food colouring on line (1)",
                "Put known dyes as spots on the same line (1)",
                "Lower paper into solvent, solvent below the line (1)",
                "Allow solvent to rise, then remove and dry (1)",
                "Compare Rf values / spots to identify dyes (1)"
            ]
        }
    ],

    "teaching_resources": {
        "common_misconceptions": [
            {
                "misconception": "Mixtures and compounds are the same thing",
                "correction": "Compounds are chemically bonded with fixed proportions; mixtures are just physically combined with variable proportions"
            },
            {
                "misconception": "Noble gas boiling points decrease down the group",
                "correction": "Boiling points INCREASE down Group 0 because atoms get larger and intermolecular forces increase"
            },
            {
                "misconception": "Isotopes have different chemical properties",
                "correction": "Isotopes have the same chemical properties because they have the same electron configuration"
            },
            {
                "misconception": "The nucleus takes up most of the space in an atom",
                "correction": "Most of an atom is empty space; the nucleus is tiny compared to the overall atom"
            }
        ],
        "key_equations": [
            "Neutrons = Mass Number − Atomic Number",
            "Rf = Distance moved by substance / Distance moved by solvent"
        ],
        "practical_tips": [
            "When doing chromatography, always use a pencil line (not pen) as pen ink will run",
            "For crystallisation, stop heating when crystals start to form at the edges",
            "In filtration, fold the filter paper into a cone shape for best results"
        ]
    },
    
    # ============================================================================
    # ADDITIONAL DETAILED CONTENT (from mark schemes and specifications)
    # ============================================================================
    
    "purity_and_definitions": {
        "module_id": "4.1.1.4",
        "sub_topic": "Mixtures & Purity (Definitions)",
        "key_concepts": [
            {
                "concept": "Pure Substances: Chemistry vs. Everyday Life",
                "details": [
                    "In Chemistry: A pure substance is a single element or a single compound.",
                    "In Everyday Life: A pure substance is a substance that has had nothing added to it (e.g., 'pure orange juice').",
                    "Melting/Boiling Points: Pure substances melt and boil at specific temperatures. Impure substances boil over a range of temperatures."
                ],
                "key_distinction": {
                    "Chemistry definition": "A single element or compound (e.g., pure water = H₂O only)",
                    "Everyday definition": "Nothing added (e.g., 'pure' orange juice still contains water, sugars, acids)"
                },
                "exam_tip": "If asked about purity in chemistry, always refer to single element/compound, not 'nothing added'",
                "quiz_question": {
                    "question": "Which definition describes a pure substance in chemistry?",
                    "correct_answer": "A single element or a single compound",
                    "distractors": [
                        "A substance that has had nothing added to it",
                        "A substance with no impurities",
                        "A substance that is clean"
                    ]
                }
            }
        ],
        "melting_point_analysis": {
            "pure_substance": "Sharp, specific melting/boiling point",
            "impure_substance": "Melting/boiling point is lower and occurs over a range",
            "exam_application": "Use melting point data to determine if a substance is pure or impure"
        }
    },
    
    "comparison_tables": {
        "transition_vs_group1": {
            "note": "This is a frequent 6-mark extended response question",
            "physical_properties": {
                "headers": ["Property", "Transition Elements", "Group 1 Elements"],
                "rows": [
                    ["Melting Point", "High", "Low"],
                    ["Density", "High", "Low"],
                    ["Hardness", "Hard and strong", "Soft (can cut with knife)"],
                    ["Conductivity", "Good conductors", "Good conductors"]
                ]
            },
            "chemical_properties": {
                "headers": ["Property", "Transition Elements", "Group 1 Elements"],
                "rows": [
                    ["Reactivity", "Low - react slowly with water/oxygen", "Very high - react vigorously with water"],
                    ["Ion charges", "Variable (e.g., Fe²⁺, Fe³⁺)", "Always +1 only"],
                    ["Compound colours", "Coloured compounds", "White or colourless compounds"],
                    ["Catalyst use", "Often used as catalysts", "Not used as catalysts"]
                ]
            },
            "model_6_mark_answer": """
Transition elements have much higher melting points than Group 1 metals. 
Transition elements have high densities while Group 1 have low densities - Li, Na, K float on water.
Transition elements are hard and strong, but Group 1 metals are soft enough to cut with a knife.

Chemically, transition elements have low reactivity and react slowly with water or oxygen.
Group 1 metals are very reactive and react vigorously with water and non-metals.
Transition elements form ions with different charges (e.g., Fe can form Fe²⁺ and Fe³⁺).
Group 1 elements only form +1 ions.
Transition elements form coloured compounds while Group 1 form white or colourless compounds.
Transition elements are often used as catalysts (e.g., iron in Haber process), but Group 1 are not used as catalysts.
"""
        }
    },
    
    "maths_skills": {
        "topic_relevance": "Topic 1 - Atomic Structure",
        "skills": [
            {
                "skill": "Surface Area Calculations",
                "context": "Calculating surface area of nanoparticles to understand their high surface area to volume ratio",
                "formula": "Surface Area of Cube = 6 × (side length)²",
                "worked_examples": [
                    {
                        "question": "Calculate the surface area of a cube with side length 2.8 nm.",
                        "working": [
                            "Surface Area = 6 × (side length)²",
                            "Surface Area = 6 × (2.8)²",
                            "Surface Area = 6 × 7.84",
                            "Surface Area = 47.04 nm²"
                        ],
                        "answer": "47.04 nm² (or 47 nm² to 2 s.f.)",
                        "marks": 2
                    },
                    {
                        "question": "A nanoparticle has side length 5.0 nm. Calculate its surface area.",
                        "working": [
                            "Surface Area = 6 × (5.0)²",
                            "Surface Area = 6 × 25",
                            "Surface Area = 150 nm²"
                        ],
                        "answer": "150 nm²",
                        "marks": 2
                    }
                ],
                "marking_note": "Allow answers correct to 2 significant figures even if calculation stage is incorrect",
                "common_errors": [
                    "Forgetting to multiply by 6 (only calculating one face)",
                    "Forgetting to square the side length"
                ]
            },
            {
                "skill": "Calculating Subatomic Particles",
                "formulas": [
                    "Neutrons = Mass Number − Atomic Number",
                    "Protons = Atomic Number",
                    "Electrons = Atomic Number (for neutral atoms)"
                ],
                "worked_example": {
                    "question": "An atom has mass number 23 and atomic number 11. Calculate the number of protons, neutrons, and electrons.",
                    "working": [
                        "Protons = Atomic Number = 11",
                        "Electrons = Atomic Number = 11 (neutral atom)",
                        "Neutrons = Mass Number − Atomic Number = 23 − 11 = 12"
                    ],
                    "answer": "11 protons, 11 electrons, 12 neutrons"
                }
            }
        ]
    },
    
    "practical_marking_points": {
        "filtration": {
            "diagram_requirements": [
                "Must draw a filter funnel containing filter paper",
                "Must include a suitable vessel (beaker/conical flask) to collect the filtrate",
                "Labels 'sand' and 'water' (or residue/filtrate) must be in correct places",
                "Sand/residue labelled in the filter paper",
                "Water/filtrate labelled in the collection vessel"
            ],
            "common_errors": [
                "Drawing a sealed vessel (no way for liquid to enter)",
                "Missing the filter paper line inside the funnel",
                "Labelling sand in the beaker instead of in the filter",
                "Not showing the funnel sitting above the collection vessel"
            ],
            "full_marks_checklist": [
                "Filter funnel drawn (1)",
                "Filter paper shown in funnel (1)",
                "Collection vessel below funnel (1)",
                "Labels correctly placed (1)"
            ]
        },
        "chromatography": {
            "diagram_requirements": [
                "Beaker/container with solvent at the bottom",
                "Chromatography paper standing in solvent",
                "Pencil line visible ABOVE the solvent level",
                "Spots on the pencil line (not in the solvent)"
            ],
            "common_errors": [
                "Drawing pencil line below the solvent level (spots would dissolve)",
                "Using pen instead of pencil for baseline (pen ink runs)",
                "Not showing solvent front or spots"
            ]
        },
        "distillation": {
            "diagram_requirements": [
                "Round-bottom flask with solution",
                "Condenser connected at an angle",
                "Water in and water out labels on condenser (water in at bottom)",
                "Collection vessel at end",
                "Thermometer in neck of flask"
            ],
            "common_errors": [
                "Water flow direction wrong (should enter at bottom, exit at top)",
                "Missing thermometer",
                "Condenser pointing upwards instead of angled down"
            ]
        }
    }
}


# Export function for easy access
def get_topic_4_1_data():
    """Get all data for Topic 4.1 Atomic Structure."""
    return TOPIC_4_1_DATA


def get_exam_questions(topic_id: str = "4.1", difficulty: str = None, question_type: str = None) -> list:
    """Get exam questions filtered by difficulty and/or type."""
    questions = TOPIC_4_1_DATA.get("assessment_bank", [])
    
    if difficulty:
        questions = [q for q in questions if q.get("difficulty", "").lower() == difficulty.lower()]
    
    if question_type:
        questions = [q for q in questions if q.get("type", "").lower() == question_type.lower()]
    
    return questions


def get_content_module(module_id: str) -> dict:
    """Get a specific content module by ID."""
    for module in TOPIC_4_1_DATA.get("content_modules", []):
        if module.get("module_id") == module_id:
            return module
    return None


def get_separation_techniques() -> list:
    """Get all separation techniques with methods."""
    module = get_content_module("4.1.2")
    if module:
        return module.get("techniques", [])
    return []


def get_group_properties(group_name: str) -> dict:
    """Get properties for a specific group."""
    module = get_content_module("4.1.5")
    if module:
        return module.get("group_properties", {}).get(group_name, {})
    return {}


def get_misconceptions() -> list:
    """Get common misconceptions for this topic."""
    return TOPIC_4_1_DATA.get("teaching_resources", {}).get("common_misconceptions", [])
