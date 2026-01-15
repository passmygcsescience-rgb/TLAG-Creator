"""
Pre-built Lesson Templates for Biology and Physics
Complete TLAG lessons ready for one-click PowerPoint generation.
"""

# =============================================================================
# BIOLOGY LESSONS
# =============================================================================
BIOLOGY_LESSONS = {
    "4.1.1": [  # Cell Structure
        {
            "lesson_number": 1,
            "title": "Eukaryotic Cell Structure",
            "learning_outcome": "Describe the structure of eukaryotic cells and the function of organelles.",
            "to_know": [
                "Eukaryotic cells contain a nucleus with genetic material",
                "Mitochondria are the site of aerobic respiration",
                "Ribosomes are where protein synthesis occurs",
                "Plant cells also have: cell wall, chloroplasts, permanent vacuole",
                "Animal and plant cells share: nucleus, cytoplasm, cell membrane, mitochondria, ribosomes"
            ],
            "do_now": {
                "questions": [
                    "Name the organelle that contains genetic material.",
                    "Where does respiration occur in a cell?",
                    "Which organelle makes proteins?",
                    "Name two features found in plant cells but not animal cells.",
                    "What is the function of the cell membrane?"
                ],
                "answers": [
                    "Nucleus",
                    "Mitochondria",
                    "Ribosomes",
                    "Cell wall, chloroplasts, permanent vacuole (any two)",
                    "Controls what enters and leaves the cell"
                ]
            },
            "i_do": {
                "title": "Identifying Organelles Under a Microscope",
                "content": [
                    "Step 1: Prepare a slide with onion epidermis",
                    "Step 2: Add iodine stain to make structures visible",
                    "Step 3: Focus using low power first, then high power",
                    "Step 4: Identify the cell wall, nucleus, and cytoplasm",
                    "Step 5: Draw a labelled diagram with scale bar"
                ]
            },
            "we_do": {
                "question": "Compare the structure of an animal cell and a plant cell.",
                "steps": [
                    "List organelles found in both (shared features)",
                    "List organelles unique to plant cells",
                    "Explain the function of chloroplasts",
                    "Explain why plant cells have a cell wall",
                    "Create a Venn diagram to show the comparison"
                ]
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 5)",
                    "question": "Label the diagram of a plant cell with the following: nucleus, cell membrane, cell wall, chloroplast, vacuole, mitochondria.",
                    "answer": "All 6 labels correctly placed on diagram."
                },
                {
                    "name": "Silver (Grade 7)",
                    "question": "Explain why muscle cells have many mitochondria.",
                    "answer": "Muscle cells require lots of energy for contraction. Mitochondria carry out aerobic respiration to release energy. More mitochondria = more ATP produced."
                },
                {
                    "name": "Gold (Grade 9)",
                    "question": "A student says 'Animal cells are less complex than plant cells because they have fewer organelles.' Evaluate this statement.",
                    "answer": "Partially correct. Plant cells have additional structures (wall, chloroplasts, vacuole). However, complexity depends on specialisation. Nerve cells are highly complex animal cells despite lacking plant organelles."
                }
            ],
            "exit_ticket": {
                "question": "Which organelle is found in plant cells but NOT animal cells?",
                "options": ["A) Mitochondria", "B) Chloroplast", "C) Nucleus", "D) Ribosome"],
                "answer": "B"
            }
        },
        {
            "lesson_number": 2,
            "title": "Prokaryotic Cells",
            "learning_outcome": "Compare prokaryotic and eukaryotic cells and describe bacterial cell structure.",
            "to_know": [
                "Prokaryotic cells (bacteria) lack a true nucleus",
                "Bacterial DNA is a single circular chromosome in cytoplasm",
                "Plasmids are small rings of extra DNA",
                "Bacteria have: cell wall, cell membrane, cytoplasm, ribosomes",
                "Prokaryotic cells are smaller than eukaryotic cells (1-5 μm vs 10-100 μm)"
            ],
            "do_now": {
                "questions": [
                    "What type of cell is a bacterium?",
                    "Do prokaryotic cells have a nucleus?",
                    "Where is the DNA found in a bacterial cell?",
                    "What are plasmids?",
                    "Give one example of a prokaryotic organism."
                ],
                "answers": [
                    "Prokaryotic cell",
                    "No - they have no true nucleus",
                    "In the cytoplasm (as a circular chromosome)",
                    "Small rings of extra DNA",
                    "Bacteria (e.g., E. coli, Salmonella)"
                ]
            },
            "i_do": {
                "title": "Drawing and Comparing Cell Types",
                "content": [
                    "Step 1: Draw a labelled prokaryotic cell (bacterium)",
                    "Step 2: Include: cell wall, membrane, cytoplasm, ribosome, DNA, plasmid",
                    "Step 3: Draw a labelled eukaryotic cell alongside",
                    "Step 4: Annotate key differences (size, nucleus, organelles)",
                    "Step 5: Create comparison table"
                ]
            },
            "we_do": {
                "question": "Complete a table comparing prokaryotic and eukaryotic cells.",
                "steps": [
                    "Column 1: Feature (nucleus, size, DNA, organelles)",
                    "Column 2: Eukaryotic cell description",
                    "Column 3: Prokaryotic cell description",
                    "Add row for examples of each",
                    "Check: what do they have in common?"
                ]
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 5)",
                    "question": "List three structures found in bacterial cells.",
                    "answer": "Cell wall, cell membrane, cytoplasm, ribosomes, circular DNA, plasmids (any 3)"
                },
                {
                    "name": "Silver (Grade 7)",
                    "question": "Explain why bacteria can evolve quickly.",
                    "answer": "Bacteria reproduce rapidly (binary fission). Plasmids allow genes to be transferred between bacteria. Mutations in circular DNA can spread quickly through populations."
                },
                {
                    "name": "Gold (Grade 9)",
                    "question": "Suggest why mitochondria in eukaryotic cells have their own DNA.",
                    "answer": "Evidence suggests mitochondria were once free-living prokaryotes that were engulfed by larger cells (endosymbiotic theory). They retain some original DNA from when they were independent organisms."
                }
            ],
            "exit_ticket": {
                "question": "Which of these is NOT found in a bacterial cell?",
                "options": ["A) Cell wall", "B) Nucleus", "C) Ribosome", "D) Plasmid"],
                "answer": "B"
            }
        }
    ],
    "4.1.3": [  # Transport in Cells
        {
            "lesson_number": 1,
            "title": "Diffusion",
            "learning_outcome": "Describe diffusion and explain factors affecting the rate of diffusion.",
            "to_know": [
                "Diffusion is the net movement of particles from high to low concentration",
                "Diffusion is a passive process - no energy required",
                "Factors affecting rate: concentration gradient, temperature, surface area",
                "Examples: oxygen and carbon dioxide in lungs, glucose into cells",
                "Diffusion continues until equilibrium is reached"
            ],
            "do_now": {
                "questions": [
                    "Define diffusion.",
                    "Does diffusion require energy from cells?",
                    "Which way do particles move in diffusion - from high or low concentration?",
                    "Give one example of diffusion in the body.",
                    "What happens to diffusion rate if temperature increases?"
                ],
                "answers": [
                    "Net movement of particles from high to low concentration",
                    "No - it is passive",
                    "From high concentration to low concentration",
                    "Oxygen diffusing into blood in lungs (accept any valid example)",
                    "Rate increases (particles have more kinetic energy)"
                ]
            },
            "i_do": {
                "title": "Demonstrating Diffusion with Potassium Permanganate",
                "content": [
                    "Step 1: Add drop of potassium permanganate to beaker of water",
                    "Step 2: Observe spread of purple colour over time",
                    "Step 3: Explain: particles move randomly from concentrated drop",
                    "Step 4: Show how warming the water speeds up diffusion",
                    "Step 5: Link to particle movement and concentration gradient"
                ]
            },
            "we_do": {
                "question": "Explain why alveoli are adapted for efficient gas exchange.",
                "steps": [
                    "Identify that gas exchange occurs by diffusion",
                    "Large surface area increases diffusion rate",
                    "Thin walls (one cell thick) reduce diffusion distance",
                    "Good blood supply maintains concentration gradient",
                    "Moist surface dissolves gases"
                ]
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 5)",
                    "question": "List three factors that affect the rate of diffusion.",
                    "answer": "Concentration gradient, temperature, surface area, distance (any 3)"
                },
                {
                    "name": "Silver (Grade 7)",
                    "question": "Explain why crushed soluble tablets dissolve faster than whole tablets.",
                    "answer": "Crushing increases surface area. More particles are exposed to the solvent. Diffusion occurs at more points simultaneously, increasing overall rate."
                },
                {
                    "name": "Gold (Grade 9)",
                    "question": "A fish gill has a large surface area and is only one cell thick. Explain how these features maximise oxygen uptake.",
                    "answer": "Large surface area: more area for diffusion to occur, increasing rate. Thin membrane: reduces diffusion distance, so oxygen reaches blood faster. Combined with blood flow maintaining concentration gradient, this maximises efficiency."
                }
            ],
            "exit_ticket": {
                "question": "What happens to the rate of diffusion when the concentration gradient increases?",
                "options": ["A) Decreases", "B) Stays the same", "C) Increases", "D) Stops completely"],
                "answer": "C"
            }
        }
    ],
    "4.4.1": [  # Photosynthesis
        {
            "lesson_number": 1,
            "title": "Photosynthesis Equation and Factors",
            "learning_outcome": "Describe photosynthesis and explain factors affecting its rate.",
            "to_know": [
                "Photosynthesis equation: carbon dioxide + water → glucose + oxygen",
                "Symbol equation: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
                "Photosynthesis is endothermic - energy transferred from light",
                "Occurs in chloroplasts which contain chlorophyll",
                "Rate factors: light intensity, CO₂ concentration, temperature"
            ],
            "do_now": {
                "questions": [
                    "Write the word equation for photosynthesis.",
                    "Where in the cell does photosynthesis occur?",
                    "Is photosynthesis exothermic or endothermic?",
                    "What is the green pigment that absorbs light?",
                    "Name one gas released during photosynthesis."
                ],
                "answers": [
                    "Carbon dioxide + water → glucose + oxygen",
                    "Chloroplasts",
                    "Endothermic",
                    "Chlorophyll",
                    "Oxygen"
                ]
            },
            "i_do": {
                "title": "Investigating Rate of Photosynthesis with Pondweed",
                "content": [
                    "Step 1: Set up pondweed in water with lamp at set distance",
                    "Step 2: Count oxygen bubbles produced per minute",
                    "Step 3: Move lamp closer and repeat measurement",
                    "Step 4: Plot graph of light intensity vs bubble count",
                    "Step 5: Identify limiting factor when graph plateaus"
                ]
            },
            "we_do": {
                "question": "A plant is placed in bright light but the rate of photosynthesis stops increasing. Explain why.",
                "steps": [
                    "Identify that another factor has become limiting",
                    "Could be CO₂ concentration too low",
                    "Could be temperature too low",
                    "Both are needed along with light",
                    "Increasing light alone won't help if other factors are limited"
                ]
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 5)",
                    "question": "State the three factors that affect the rate of photosynthesis.",
                    "answer": "Light intensity, carbon dioxide concentration, temperature"
                },
                {
                    "name": "Silver (Grade 7)",
                    "question": "Explain why farmers might add extra CO₂ to greenhouses.",
                    "answer": "CO₂ is a reactant in photosynthesis. Increasing CO₂ concentration increases rate of photosynthesis. Plants grow faster and produce more biomass, increasing crop yield."
                },
                {
                    "name": "Gold (Grade 9)",
                    "question": "A graph shows that increasing light intensity increases rate of photosynthesis, but only up to a point. Explain the shape of this graph in terms of limiting factors.",
                    "answer": "Initially, light is the limiting factor - more light = faster rate. At higher intensities, the rate plateaus because CO₂ or temperature becomes limiting. All factors must be optimum for maximum rate; increasing one alone beyond the limit has no effect."
                }
            ],
            "exit_ticket": {
                "question": "Which is a product of photosynthesis?",
                "options": ["A) Carbon dioxide", "B) Water", "C) Glucose", "D) Chlorophyll"],
                "answer": "C"
            }
        }
    ]
}

# =============================================================================
# PHYSICS LESSONS  
# =============================================================================
PHYSICS_LESSONS = {
    "4.1.1": [  # Energy Stores
        {
            "lesson_number": 1,
            "title": "Energy Stores and Transfers",
            "learning_outcome": "Describe energy stores and explain how energy is transferred between them.",
            "to_know": [
                "Energy stores: kinetic, gravitational potential, elastic, thermal, chemical, nuclear, magnetic",
                "Energy is transferred between stores, not created or destroyed",
                "Work done = force × distance (W = Fd)",
                "Power = energy transferred ÷ time (P = E/t)",
                "Energy is measured in joules (J); power in watts (W)"
            ],
            "do_now": {
                "questions": [
                    "Name three types of energy store.",
                    "What is the unit of energy?",
                    "State the equation for work done.",
                    "What is power measured in?",
                    "A ball is thrown upwards. What energy transfer occurs?"
                ],
                "answers": [
                    "Kinetic, gravitational potential, thermal, elastic, chemical, nuclear, magnetic (any 3)",
                    "Joules (J)",
                    "Work done = force × distance (W = Fd)",
                    "Watts (W)",
                    "Kinetic energy store → gravitational potential energy store"
                ]
            },
            "i_do": {
                "title": "Calculating Work Done",
                "content": [
                    "Step 1: Identify the formula: W = F × d",
                    "Step 2: A person lifts a 20N box up 3m. What is the work done?",
                    "Step 3: Substitute values: W = 20 × 3",
                    "Step 4: Calculate: W = 60 J",
                    "Step 5: State the unit and check it makes sense"
                ]
            },
            "we_do": {
                "question": "A crane lifts a 500N crate through a height of 12m in 30 seconds. Calculate the power.",
                "steps": [
                    "Step 1: Calculate work done W = F × d = 500 × 12 = 6000 J",
                    "Step 2: State the power formula P = E ÷ t",
                    "Step 3: Substitute values P = 6000 ÷ 30",
                    "Step 4: Calculate P = 200 W",
                    "Step 5: The crane has a power output of 200 watts"
                ]
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 5)",
                    "question": "A force of 15N pushes a box 4m. Calculate the work done.",
                    "answer": "W = F × d = 15 × 4 = 60 J"
                },
                {
                    "name": "Silver (Grade 7)",
                    "question": "A motor transfers 900 J of energy in 30 seconds. Calculate its power.",
                    "answer": "P = E ÷ t = 900 ÷ 30 = 30 W"
                },
                {
                    "name": "Gold (Grade 9)",
                    "question": "A 2000 W motor lifts a 400N load. Calculate how high it lifts the load in 10 seconds.",
                    "answer": "Energy = Power × time = 2000 × 10 = 20000 J. Height = Energy ÷ Force = 20000 ÷ 400 = 50 m"
                }
            ],
            "exit_ticket": {
                "question": "Which equation is correct for work done?",
                "options": ["A) W = m × g", "B) W = F × d", "C) W = E × t", "D) W = P × E"],
                "answer": "B"
            }
        }
    ],
    "4.2.1": [  # Circuits
        {
            "lesson_number": 1,
            "title": "Current, Voltage and Resistance",
            "learning_outcome": "Describe current, voltage and resistance and use V = IR.",
            "to_know": [
                "Current (I) is the flow of charge, measured in amperes (A)",
                "Potential difference (V) is the energy per unit charge, measured in volts (V)",
                "Resistance (R) opposes current flow, measured in ohms (Ω)",
                "Ohm's Law: V = I × R",
                "Current is the same throughout a series circuit"
            ],
            "do_now": {
                "questions": [
                    "What is the unit of current?",
                    "What is the symbol for potential difference?",
                    "State Ohm's Law.",
                    "Name the instrument used to measure current.",
                    "What is resistance measured in?"
                ],
                "answers": [
                    "Amperes (A)",
                    "V",
                    "V = I × R",
                    "Ammeter",
                    "Ohms (Ω)"
                ]
            },
            "i_do": {
                "title": "Calculating Resistance",
                "content": [
                    "Step 1: State Ohm's Law: V = I × R, rearrange to R = V ÷ I",
                    "Step 2: Problem: A component has 12V across it and 3A flowing through",
                    "Step 3: Substitute: R = 12 ÷ 3",
                    "Step 4: Calculate: R = 4 Ω",
                    "Step 5: The component has a resistance of 4 ohms"
                ]
            },
            "we_do": {
                "question": "A lamp has a resistance of 6Ω and a current of 2A flows through it. Calculate the voltage across the lamp.",
                "steps": [
                    "Step 1: Identify values: R = 6Ω, I = 2A, V = ?",
                    "Step 2: State formula: V = I × R",
                    "Step 3: Substitute: V = 2 × 6",
                    "Step 4: Calculate: V = 12 V",
                    "Step 5: The voltage across the lamp is 12 volts"
                ]
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 5)",
                    "question": "Calculate the current when V = 10V and R = 5Ω.",
                    "answer": "I = V ÷ R = 10 ÷ 5 = 2 A"
                },
                {
                    "name": "Silver (Grade 7)",
                    "question": "A resistor has 2A flowing through it when connected to a 6V supply. Calculate its resistance.",
                    "answer": "R = V ÷ I = 6 ÷ 2 = 3 Ω"
                },
                {
                    "name": "Gold (Grade 9)",
                    "question": "Two 4Ω resistors are connected in series. Calculate the total resistance and the current when connected to a 12V supply.",
                    "answer": "Total R = 4 + 4 = 8Ω. Current I = V ÷ R = 12 ÷ 8 = 1.5 A"
                }
            ],
            "exit_ticket": {
                "question": "If voltage doubles and resistance stays the same, what happens to current?",
                "options": ["A) Halves", "B) Stays same", "C) Doubles", "D) Quadruples"],
                "answer": "C"
            }
        }
    ],
    "4.5.5": [  # Newton's Laws (matches curriculum_data.py)
        {
            "lesson_number": 1,
            "title": "Newton's Three Laws of Motion",
            "learning_outcome": "Describe Newton's three laws of motion and apply F = ma.",
            "to_know": [
                "1st Law: Object stays at rest or constant velocity unless acted on by resultant force",
                "2nd Law: F = ma (force = mass × acceleration)",
                "3rd Law: Every action has an equal and opposite reaction",
                "Resultant force = 0 means constant velocity (or stationary)",
                "Force is measured in newtons (N)"
            ],
            "do_now": {
                "questions": [
                    "State Newton's First Law.",
                    "Write the equation linking force, mass and acceleration.",
                    "What is the unit of force?",
                    "If resultant force is zero, what happens to an object's motion?",
                    "State Newton's Third Law."
                ],
                "answers": [
                    "Object at rest stays at rest, or object in motion stays at constant velocity, unless acted on by a resultant force",
                    "F = m × a",
                    "Newtons (N)",
                    "It stays at rest or moves at constant velocity",
                    "Every action has an equal and opposite reaction"
                ]
            },
            "i_do": {
                "title": "Calculating Force Using F = ma",
                "content": [
                    "Step 1: State the formula: F = m × a",
                    "Step 2: Problem: A 1200kg car accelerates at 2 m/s². Find the force.",
                    "Step 3: Substitute: F = 1200 × 2",
                    "Step 4: Calculate: F = 2400 N",
                    "Step 5: The engine provides 2400 newtons of force"
                ]
            },
            "we_do": {
                "question": "A 70kg sprinter accelerates from rest to 10 m/s in 2 seconds. Calculate the resultant force.",
                "steps": [
                    "Step 1: Calculate acceleration a = (v-u)/t = (10-0)/2 = 5 m/s²",
                    "Step 2: State the formula F = ma",
                    "Step 3: Substitute: F = 70 × 5",
                    "Step 4: Calculate: F = 350 N",
                    "Step 5: The resultant force on the sprinter is 350 newtons"
                ]
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 5)",
                    "question": "Calculate the force needed to accelerate a 5kg mass at 3 m/s².",
                    "answer": "F = m × a = 5 × 3 = 15 N"
                },
                {
                    "name": "Silver (Grade 7)",
                    "question": "A 2000N force acts on a 500kg object. Calculate its acceleration.",
                    "answer": "a = F ÷ m = 2000 ÷ 500 = 4 m/s²"
                },
                {
                    "name": "Gold (Grade 9)",
                    "question": "A 1500kg car experiences a driving force of 6000N and friction of 2000N. Calculate its acceleration.",
                    "answer": "Resultant force = 6000 - 2000 = 4000N. a = F ÷ m = 4000 ÷ 1500 = 2.67 m/s²"
                }
            ],
            "exit_ticket": {
                "question": "According to Newton's 2nd Law, if mass doubles and force stays the same, what happens to acceleration?",
                "options": ["A) Doubles", "B) Halves", "C) Stays same", "D) Quadruples"],
                "answer": "B"
            }
        }
    ]
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================
def get_biology_lesson(subtopic_id: str, lesson_num: int) -> dict:
    """Get a specific biology lesson."""
    lessons = BIOLOGY_LESSONS.get(subtopic_id, [])
    for lesson in lessons:
        if lesson.get("lesson_number") == lesson_num:
            return lesson
    return None


def get_physics_lesson(subtopic_id: str, lesson_num: int) -> dict:
    """Get a specific physics lesson."""
    lessons = PHYSICS_LESSONS.get(subtopic_id, [])
    for lesson in lessons:
        if lesson.get("lesson_number") == lesson_num:
            return lesson
    return None


def get_available_biology_lessons(subtopic_id: str) -> list:
    """Get list of available lessons for a biology subtopic."""
    lessons = BIOLOGY_LESSONS.get(subtopic_id, [])
    return [{"number": l["lesson_number"], "title": l["title"]} for l in lessons]


def get_available_physics_lessons(subtopic_id: str) -> list:
    """Get list of available lessons for a physics subtopic."""
    lessons = PHYSICS_LESSONS.get(subtopic_id, [])
    return [{"number": l["lesson_number"], "title": l["title"]} for l in lessons]
