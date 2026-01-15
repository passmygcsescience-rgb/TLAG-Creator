"""
EXPANDED Lesson Templates with Rich Content
Contains detailed I Do sections, multiple We Do examples, and extra You Do tasks.
"""

# =============================================================================
# EXPANDED CHEMISTRY LESSON - IONIC BONDING (Example of rich content)
# =============================================================================
EXPANDED_CHEMISTRY_LESSONS = {
    "4.2.1": [
        {
            "lesson_number": 1,
            "title": "Ionic Bonding",
            "spec_reference": "AQA Chemistry 4.2.1",
            "learning_outcome": "Describe how ionic bonds form between metals and non-metals and draw dot and cross diagrams for ionic compounds.",
            "to_know": [
                "Ionic bonds form between metals and non-metals",
                "Metals LOSE electrons to form positive ions (cations)",
                "Non-metals GAIN electrons to form negative ions (anions)",
                "The electrostatic attraction between opposite charges forms an ionic bond",
                "Ionic compounds form giant ionic lattice structures"
            ],
            "to_know_image": "[TEACHER NOTE: Insert diagram showing the periodic table with metals highlighted on the left and non-metals on the right, with arrows showing electron transfer direction]",
            "do_now": {
                "questions": [
                    "How many electrons are in the outer shell of sodium (Na)?",
                    "How many electrons are in the outer shell of chlorine (Cl)?",
                    "What is the charge on a proton?",
                    "What is the charge on an electron?",
                    "What happens to the reactivity as you go down Group 1?"
                ],
                "answers": [
                    "1 electron",
                    "7 electrons",
                    "+1 (positive)",
                    "-1 (negative)",
                    "Reactivity increases"
                ],
                "focus": "Atomic structure and Group 1 properties"
            },
            
            # =========================================================
            # EXPANDED I DO - Multiple slides worth of content
            # =========================================================
            "i_do": {
                "title": "How Ionic Bonds Form",
                "content": [
                    "Ionic bonds form between metals and non-metals",
                    "Metals have 1-3 outer electrons - easier to LOSE them",
                    "Non-metals have 5-7 outer electrons - easier to GAIN electrons",
                    "When electrons transfer, both atoms achieve full outer shells",
                    "Full outer shells = stable electron configuration like noble gases"
                ],
                "examples": [
                    {
                        "problem": "Show the formation of NaCl (sodium chloride)",
                        "steps": [
                            "Draw sodium atom: 2,8,1 electrons (1 in outer shell)",
                            "Draw chlorine atom: 2,8,7 electrons (7 in outer shell)",
                            "Sodium LOSES 1 electron → becomes Na⁺ (2,8)",
                            "Chlorine GAINS 1 electron → becomes Cl⁻ (2,8,8)",
                            "Na⁺ and Cl⁻ attract due to opposite charges"
                        ],
                        "answer": "Na⁺Cl⁻ (sodium chloride)"
                    },
                    {
                        "problem": "Show the formation of MgO (magnesium oxide)",
                        "steps": [
                            "Magnesium: 2,8,2 (2 outer electrons to lose)",
                            "Oxygen: 2,6 (needs 2 electrons to fill outer shell)",
                            "Mg loses 2 electrons → Mg²⁺",
                            "O gains 2 electrons → O²⁻",
                            "Ratio is 1:1 because charges balance"
                        ],
                        "answer": "Mg²⁺O²⁻ (magnesium oxide)"
                    }
                ],
                "key_points": [
                    "Metals LOSE electrons → POSITIVE ions (cations)",
                    "Non-metals GAIN electrons → NEGATIVE ions (anions)",
                    "The number of electrons lost/gained depends on group number",
                    "Opposite charges attract = ionic bond",
                    "Dot and cross diagrams show electron transfer clearly"
                ],
                "technique": "Cold Call - I will ask you to predict the next step",
                "image_description": "[TEACHER NOTE: Insert dot and cross diagram showing a Sodium atom (2,8,1) losing one electron to a Chlorine atom (2,8,7), with arrow showing electron transfer, resulting in Na+ and Cl- ions with full outer shells]"
            },
            
            # =========================================================
            # EXPANDED WE DO - Multiple guided examples
            # =========================================================
            "we_do": {
                "examples": [
                    {
                        "question": "Draw the dot and cross diagram for sodium chloride (NaCl).",
                        "steps": [
                            "Step 1: Draw sodium atom with electron configuration [2,8,1]",
                            "Step 2: Draw chlorine atom with configuration [2,8,7]",
                            "Step 3: Show the electron from Na transferring to Cl with an arrow",
                            "Step 4: Show final ions: Na⁺ [2,8] and Cl⁻ [2,8,8]",
                            "Step 5: Add square brackets and charges around each ion"
                        ],
                        "answer": "[Na]⁺ [Cl]⁻ with full outer shells shown"
                    },
                    {
                        "question": "Draw the dot and cross diagram for magnesium chloride (MgCl₂).",
                        "steps": [
                            "Step 1: Mg loses 2 electrons, needs 2 Cl atoms to accept them",
                            "Step 2: Draw Mg [2,8,2] and two Cl atoms [2,8,7]",
                            "Step 3: Each Cl gains 1 electron from Mg",
                            "Step 4: Final ions: Mg²⁺ and 2× Cl⁻",
                            "Step 5: Formula is MgCl₂ (1 magnesium, 2 chlorides)"
                        ],
                        "answer": "[Mg]²⁺ [Cl]⁻ [Cl]⁻ or MgCl₂"
                    },
                    {
                        "question": "Predict the formula for calcium oxide.",
                        "steps": [
                            "Step 1: Ca is in Group 2 → loses 2 electrons → Ca²⁺",
                            "Step 2: O is in Group 6 → gains 2 electrons → O²⁻",
                            "Step 3: Charges balance 1:1 (2+ and 2-)",
                            "Step 4: Formula is CaO",
                            "Turn and Talk: Why is this ratio 1:1?"
                        ],
                        "answer": "CaO (calcium oxide)"
                    },
                    {
                        "question": "Predict the formula for aluminium oxide.",
                        "steps": [
                            "Step 1: Al is in Group 3 → loses 3 electrons → Al³⁺",
                            "Step 2: O is in Group 6 → gains 2 electrons → O²⁻",
                            "Step 3: Need to balance charges: 2×Al³⁺ = 6+ and 3×O²⁻ = 6-",
                            "Step 4: Ratio is 2:3",
                            "Step 5: Formula is Al₂O₃"
                        ],
                        "answer": "Al₂O₃ (aluminium oxide)"
                    }
                ],
                "technique": "Turn and Talk with your partner before each step",
                "image_description": "[TEACHER NOTE: Insert blank dot and cross diagram template for students to complete, with spaces for Na (2,8,1), Cl (2,8,7), and the resulting ions]"
            },
            
            # =========================================================
            # EXPANDED YOU DO - More differentiated tasks
            # =========================================================
            "you_do": [
                {
                    "name": "Bronze (Grade 4-5)",
                    "question": "Complete the sentences: Metals _____ electrons to form _____ ions. Non-metals _____ electrons to form _____ ions.",
                    "answer": "Metals LOSE electrons to form POSITIVE ions. Non-metals GAIN electrons to form NEGATIVE ions."
                },
                {
                    "name": "Bronze (Grade 4-5)",
                    "question": "State whether each element will form a positive or negative ion: (a) Potassium (b) Sulfur (c) Calcium (d) Fluorine",
                    "answer": "(a) Positive (b) Negative (c) Positive (d) Negative"
                },
                {
                    "name": "Silver (Grade 5-6)",
                    "question": "Draw a dot and cross diagram to show the formation of lithium fluoride (LiF).",
                    "steps": [
                        "Draw Li [2,1] and F [2,7]",
                        "Show electron transfer",
                        "Label final ions Li⁺ and F⁻"
                    ],
                    "answer": "[Li]⁺ [F]⁻ with electron configuration [2] and [2,8] respectively"
                },
                {
                    "name": "Silver (Grade 5-6)",
                    "question": "Explain why sodium chloride has a high melting point.",
                    "answer": "NaCl has strong electrostatic forces of attraction between oppositely charged ions. A lot of energy is needed to overcome these strong ionic bonds, so the melting point is high."
                },
                {
                    "name": "Gold (Grade 7-8)",
                    "question": "Draw a dot and cross diagram for calcium chloride (CaCl₂). Explain why the formula is CaCl₂ and not CaCl.",
                    "answer": "Calcium loses 2 electrons (Ca²⁺). Each chlorine can only accept 1 electron (Cl⁻). So 2 chlorine atoms are needed to accept all of calcium's electrons. The charges balance: 2+ = 1- + 1-"
                },
                {
                    "name": "Gold (Grade 7-8)",
                    "question": "Predict the formula for the ionic compound formed between aluminium and sulfur. Explain your reasoning.",
                    "answer": "Al³⁺ and S²⁻. Need LCM of 3 and 2 = 6. So 2×Al³⁺ (=6+) and 3×S²⁻ (=6-). Formula: Al₂S₃"
                },
                {
                    "name": "Extension (Grade 9)",
                    "question": "Explain why ionic compounds conduct electricity when molten but not when solid.",
                    "answer": "In solid ionic compounds, ions are held in fixed positions in the lattice and cannot move. When molten, the ions are free to move and carry charge through the liquid. Conduction requires mobile charged particles."
                }
            ],
            
            # =========================================================
            # AFFIRMATIVE CHECKING
            # =========================================================
            "affirmative_checking": {
                "checkpoint": "Check students are showing electron TRANSFER not sharing. Common error: drawing covalent-style diagrams with shared electrons.",
                "action": "Real-time feedback: 'Remember, electrons move completely from metal to non-metal - show this with an arrow!'"
            },
            
            "exit_ticket": {
                "question": "When sodium reacts with chlorine, what happens to the sodium atom?",
                "options": [
                    "A) It gains one electron and becomes Na⁻",
                    "B) It loses one electron and becomes Na⁺",
                    "C) It shares one electron with chlorine",
                    "D) It loses one proton and becomes Na⁻"
                ],
                "answer": "B"
            }
        }
    ]
}


# =============================================================================
# EXPANDED BIOLOGY LESSON - CELL STRUCTURE
# =============================================================================
EXPANDED_BIOLOGY_LESSONS = {
    "4.1.1": [
        {
            "lesson_number": 1,
            "title": "Eukaryotic Cell Structure",
            "spec_reference": "AQA Biology 4.1.1",
            "learning_outcome": "Describe the structure of eukaryotic cells and explain the function of each organelle.",
            "to_know": [
                "Eukaryotic cells have a nucleus containing genetic material (DNA)",
                "Mitochondria are the site of aerobic respiration - release energy",
                "Ribosomes synthesise proteins from amino acids",
                "Chloroplasts (plants only) absorb light for photosynthesis",
                "The cell membrane controls what enters and leaves the cell"
            ],
            "to_know_image": "[TEACHER NOTE: Insert side-by-side comparison diagram of plant cell and animal cell with all organelles labelled - nucleus, mitochondria, ribosomes, cell membrane, cytoplasm, and plant-only: cell wall, chloroplasts, vacuole]",
            "do_now": {
                "questions": [
                    "Name the two types of cell (pro_____ and eu_____)",
                    "Which kingdom do bacteria belong to?",
                    "What is the function of the cell membrane?",
                    "Name one difference between plant and animal cells.",
                    "What is respiration?"
                ],
                "answers": [
                    "Prokaryotes and Eukaryotes",
                    "Prokaryotes / Monera",
                    "Controls what enters and leaves the cell",
                    "Plant cells have cell wall/chloroplasts/vacuole",
                    "The release of energy from glucose"
                ],
                "focus": "Prior learning from KS3 cells topic"
            },
            "i_do": {
                "title": "Identifying and Describing Organelles",
                "content": [
                    "We will learn to identify organelles in plant and animal cells",
                    "Each organelle has a specific function like organs in our body",
                    "We'll start with organelles found in BOTH plant and animal cells",
                    "Then we'll look at organelles unique to plant cells",
                    "Finally, we'll explain WHY plant cells have extra organelles"
                ],
                "examples": [
                    {
                        "problem": "Explain the function of mitochondria",
                        "steps": [
                            "Mitochondria are found in ALL eukaryotic cells",
                            "They are the site of aerobic respiration",
                            "Respiration: glucose + oxygen → carbon dioxide + water + ENERGY",
                            "More active cells have MORE mitochondria (e.g., muscle cells)",
                            "Mitochondria have a folded inner membrane for maximum surface area"
                        ],
                        "answer": "Mitochondria carry out aerobic respiration to release energy for cell activities"
                    },
                    {
                        "problem": "Explain why plant cells have chloroplasts",
                        "steps": [
                            "Plants are producers - they make their own food",
                            "Chloroplasts contain chlorophyll (green pigment)",
                            "Chlorophyll absorbs light energy",
                            "Photosynthesis occurs in chloroplasts",
                            "CO₂ + H₂O + light → glucose + oxygen"
                        ],
                        "answer": "Chloroplasts enable photosynthesis to produce glucose for energy"
                    }
                ],
                "key_points": [
                    "Nucleus = contains DNA (genetic material)",
                    "Mitochondria = respiration (energy release)",
                    "Ribosomes = protein synthesis",
                    "Cell membrane = controls entry/exit",
                    "Plant extras: Cell wall (support), Chloroplast (photosynthesis), Vacuole (storage)"
                ],
                "technique": "Cold Call - be ready to name organelle functions",
                "image_description": "[TEACHER NOTE: Insert electron microscope image of a mitochondrion showing the folded inner membrane (cristae) and outer membrane, with labels]"
            },
            "we_do": {
                "examples": [
                    {
                        "question": "Label this diagram of an animal cell with all organelles.",
                        "steps": [
                            "Find the largest structure (usually central) = Nucleus",
                            "Identify the outer boundary = Cell membrane",
                            "Locate small oval structures = Mitochondria",
                            "Find tiny dots on membrane = Ribosomes",
                            "Fill in the rest = Cytoplasm"
                        ],
                        "answer": "Nucleus, cell membrane, mitochondria, ribosomes, cytoplasm"
                    },
                    {
                        "question": "Compare animal and plant cells - create a Venn diagram.",
                        "steps": [
                            "SHARED (middle): Nucleus, cell membrane, cytoplasm, mitochondria, ribosomes",
                            "PLANT ONLY (right): Cell wall, chloroplasts, permanent vacuole",
                            "ANIMAL ONLY (left): Sometimes smaller vacuoles (not permanent)",
                            "Turn and Talk: Which organelle is most important?"
                        ],
                        "answer": "Venn diagram with 5 shared features, 3 plant-only features"
                    },
                    {
                        "question": "Explain why root cells have no chloroplasts.",
                        "steps": [
                            "Root cells are underground",
                            "No light reaches them",
                            "Chloroplasts need light for photosynthesis",
                            "Without light, chloroplasts would be useless",
                            "Root cells don't photosynthesise - they absorb water and minerals instead"
                        ],
                        "answer": "Root cells don't receive light, so chloroplasts (which need light) are not needed"
                    }
                ],
                "technique": "Turn and Talk after each step",
                "image_description": "[TEACHER NOTE: Insert unlabelled diagram of animal cell for students to annotate, and Venn diagram template with 'Animal only', 'Both', 'Plant only' sections]"
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 4-5)",
                    "question": "Match each organelle to its function: (a) Nucleus (b) Mitochondria (c) Ribosome (d) Cell membrane",
                    "answer": "(a) Contains DNA (b) Respiration (c) Protein synthesis (d) Controls entry/exit"
                },
                {
                    "name": "Bronze (Grade 4-5)",
                    "question": "List THREE organelles found in both plant AND animal cells.",
                    "answer": "Any 3 from: Nucleus, cell membrane, cytoplasm, mitochondria, ribosomes"
                },
                {
                    "name": "Silver (Grade 5-6)",
                    "question": "Explain why muscle cells contain many mitochondria.",
                    "answer": "Muscle cells need lots of energy for contraction. Mitochondria carry out respiration to release energy. More mitochondria = more energy available."
                },
                {
                    "name": "Silver (Grade 5-6)",
                    "question": "State TWO differences between plant and animal cells and explain ONE of them.",
                    "answer": "Differences: cell wall/chloroplast/vacuole. Explanation: e.g., Plants have chloroplasts because they need to photosynthesise to make their own food."
                },
                {
                    "name": "Gold (Grade 7-8)",
                    "question": "A student says 'Animal cells are simpler than plant cells.' Evaluate this statement.",
                    "answer": "Partially true - plant cells have more organelles. However, 'complexity' depends on specialisation. Nerve cells are very complex animal cells. Complexity isn't just about number of organelles."
                },
                {
                    "name": "Gold (Grade 7-8)",
                    "question": "Explain why red blood cells have no nucleus or mitochondria.",
                    "answer": "Red blood cells carry oxygen. Removing the nucleus makes more space for haemoglobin. No mitochondria means the cell doesn't use the oxygen it carries - all oxygen goes to body cells."
                },
                {
                    "name": "Extension (Grade 9)",
                    "question": "Suggest why scientists believe mitochondria were once independent organisms.",
                    "answer": "Mitochondria have their own DNA (separate from nucleus). They have double membranes. They replicate independently. This supports the endosymbiotic theory - ancient bacteria were engulfed by larger cells."
                }
            ],
            "affirmative_checking": {
                "checkpoint": "Check students correctly distinguish cell MEMBRANE (thin, controls entry) from cell WALL (thick, provides support).",
                "action": "Common error: Saying 'cell wall controls what enters'. Remind: membrane = gateway, wall = structural support."
            },
            "exit_ticket": {
                "question": "Where in the cell does respiration occur?",
                "options": [
                    "A) Nucleus",
                    "B) Chloroplast",
                    "C) Mitochondria",
                    "D) Ribosome"
                ],
                "answer": "C"
            }
        }
    ]
}


# =============================================================================
# EXPANDED PHYSICS LESSON - NEWTON'S LAWS
# =============================================================================
EXPANDED_PHYSICS_LESSONS = {
    "4.5.5": [
        {
            "lesson_number": 1,
            "title": "Newton's Three Laws of Motion",
            "spec_reference": "AQA Physics 4.5.5",
            "learning_outcome": "Apply Newton's laws to explain motion and calculate force, mass, and acceleration using F = ma.",
            "to_know": [
                "Newton's 1st Law: An object stays at rest or constant velocity unless acted on by a resultant force",
                "Newton's 2nd Law: F = ma (Force = mass × acceleration)",
                "Newton's 3rd Law: Every action has an equal and opposite reaction",
                "Resultant force = 0 means no acceleration (constant velocity or stationary)",
                "Force is measured in Newtons (N), mass in kg, acceleration in m/s²"
            ],
            "to_know_image": "[TEACHER NOTE: Insert F=ma formula triangle with F at top, m and a at bottom corners, showing how to cover the one you want to find]",
            "do_now": {
                "questions": [
                    "What is the unit of force?",
                    "What is the formula for speed?",
                    "If a car is accelerating, what does this mean?",
                    "What is the unit of mass?",
                    "Give an example of a contact force."
                ],
                "answers": [
                    "Newtons (N)",
                    "Speed = distance ÷ time",
                    "Its velocity is changing (speeding up or slowing down)",
                    "Kilograms (kg)",
                    "Friction, air resistance, tension, normal force (any one)"
                ],
                "focus": "Prior forces and motion topic"
            },
            "i_do": {
                "title": "Understanding and Applying Newton's Laws",
                "content": [
                    "Newton's 1st Law explains inertia - objects resist changes to their motion",
                    "Newton's 2nd Law gives us the equation F = ma for calculations",
                    "Newton's 3rd Law explains why forces come in pairs",
                    "We'll use these laws to solve problems about motion",
                    "The triangle method helps rearrange F = ma"
                ],
                "examples": [
                    {
                        "problem": "Calculate the force needed to accelerate a 50kg trolley at 2 m/s²",
                        "steps": [
                            "Step 1: Identify values - m = 50 kg, a = 2 m/s², F = ?",
                            "Step 2: Write the formula F = m × a",
                            "Step 3: Substitute values F = 50 × 2",
                            "Step 4: Calculate F = 100 N",
                            "Step 5: Write full answer with unit: The force is 100 Newtons"
                        ],
                        "answer": "F = 100 N"
                    },
                    {
                        "problem": "A 1200 kg car experiences a resultant force of 3600 N. Calculate the acceleration.",
                        "steps": [
                            "Step 1: Identify - m = 1200 kg, F = 3600 N, a = ?",
                            "Step 2: Rearrange F = ma to get a = F ÷ m",
                            "Step 3: Substitute a = 3600 ÷ 1200",
                            "Step 4: Calculate a = 3 m/s²",
                            "Step 5: The car accelerates at 3 metres per second squared"
                        ],
                        "answer": "a = 3 m/s²"
                    }
                ],
                "key_points": [
                    "F = ma: Cover the one you want to find",
                    "Force in Newtons (N), mass in kg, acceleration in m/s²",
                    "Resultant force = sum of all forces (consider direction!)",
                    "If resultant = 0, velocity is constant (1st Law)",
                    "Forces always occur in pairs (3rd Law)"
                ],
                "technique": "Cold Call - predict the next step before I reveal it",
                "image_description": "[TEACHER NOTE: Insert free body diagram of a car showing: driving force arrow pointing right, friction arrow pointing left, weight arrow pointing down, normal reaction arrow pointing up, with values labelled]"
            },
            "we_do": {
                "examples": [
                    {
                        "question": "A 70 kg athlete accelerates at 5 m/s². Calculate the resultant force.",
                        "steps": [
                            "Step 1: Write what we know - m = 70 kg, a = 5 m/s²",
                            "Step 2: Write the formula - F = m × a",
                            "Step 3: Substitute - F = 70 × 5",
                            "Step 4: Calculate - F = 350 N",
                            "Step 5: Check units - Force should be in Newtons ✓"
                        ],
                        "answer": "F = 350 N"
                    },
                    {
                        "question": "A resultant force of 240 N acts on a 60 kg skateboarder. Calculate the acceleration.",
                        "steps": [
                            "Step 1: Identify - F = 240 N, m = 60 kg, a = ?",
                            "Step 2: Rearrange - a = F ÷ m",
                            "Step 3: Substitute - a = 240 ÷ 60",
                            "Step 4: Calculate - a = 4 m/s²",
                            "Turn and Talk: What would happen if the mass doubled?"
                        ],
                        "answer": "a = 4 m/s² (if mass doubled, acceleration would halve)"
                    },
                    {
                        "question": "A car has a driving force of 5000 N and friction of 2000 N. Mass is 1000 kg. Find acceleration.",
                        "steps": [
                            "Step 1: Calculate resultant force = 5000 - 2000 = 3000 N",
                            "Step 2: Use F = ma with resultant force",
                            "Step 3: a = F ÷ m = 3000 ÷ 1000",
                            "Step 4: a = 3 m/s²",
                            "Key point: Always use RESULTANT force, not just driving force"
                        ],
                        "answer": "a = 3 m/s²"
                    },
                    {
                        "question": "Explain using Newton's 1st Law why passengers lurch forward when a bus brakes suddenly.",
                        "steps": [
                            "Step 1: Before braking, passengers move at same velocity as bus",
                            "Step 2: When bus brakes, a force acts on the bus",
                            "Step 3: No force acts directly on passengers (they're not attached)",
                            "Step 4: By 1st Law, passengers continue at original velocity",
                            "Step 5: Bus slows but passengers keep moving forward = lurch"
                        ],
                        "answer": "Passengers' inertia keeps them moving at original velocity when bus decelerates"
                    }
                ],
                "technique": "Turn and Talk before solving each step",
                "image_description": "[TEACHER NOTE: Insert diagram showing a bus braking suddenly with passengers inside, arrows showing bus velocity decreasing but passengers continuing forward due to inertia]"
            },
            "you_do": [
                {
                    "name": "Bronze (Grade 4-5)",
                    "question": "State Newton's Second Law as an equation.",
                    "answer": "F = m × a (Force = mass × acceleration)"
                },
                {
                    "name": "Bronze (Grade 4-5)",
                    "question": "Calculate the force when m = 10 kg and a = 3 m/s².",
                    "answer": "F = 10 × 3 = 30 N"
                },
                {
                    "name": "Silver (Grade 5-6)",
                    "question": "A 5 kg object accelerates at 4 m/s². Calculate the resultant force.",
                    "answer": "F = m × a = 5 × 4 = 20 N"
                },
                {
                    "name": "Silver (Grade 5-6)",
                    "question": "A force of 450 N acts on a 90 kg object. Calculate the acceleration.",
                    "answer": "a = F ÷ m = 450 ÷ 90 = 5 m/s²"
                },
                {
                    "name": "Gold (Grade 7-8)",
                    "question": "A 800 kg car experiences a driving force of 4000 N and friction of 1200 N. Calculate its acceleration.",
                    "answer": "Resultant = 4000 - 1200 = 2800 N. a = 2800 ÷ 800 = 3.5 m/s²"
                },
                {
                    "name": "Gold (Grade 7-8)",
                    "question": "Use Newton's 3rd Law to explain why a rocket can travel in space where there is no air.",
                    "answer": "The rocket pushes exhaust gases backwards (action). By Newton's 3rd Law, the gases push the rocket forwards (reaction). This works in a vacuum because the forces act on different objects."
                },
                {
                    "name": "Extension (Grade 9)",
                    "question": "A parachutist reaches terminal velocity. Explain this using Newton's Laws.",
                    "answer": "At terminal velocity: weight (down) = air resistance (up). Resultant force = 0. By Newton's 1st Law, zero resultant means constant velocity. So the parachutist falls at steady speed."
                }
            ],
            "affirmative_checking": {
                "checkpoint": "Check students are using RESULTANT force in F=ma, not just one force. Common error: Using driving force when friction is also present.",
                "action": "Ask: 'Have you subtracted friction?' - ensure they calculate resultant first."
            },
            "exit_ticket": {
                "question": "If the resultant force on an object is zero, what happens to its velocity?",
                "options": [
                    "A) It increases",
                    "B) It decreases",
                    "C) It stays constant",
                    "D) It becomes zero"
                ],
                "answer": "C"
            }
        }
    ]
}


# =============================================================================
# COMBINED EXPANDED LESSONS DICTIONARY
# =============================================================================
EXPANDED_LESSONS = {
    "Chemistry": EXPANDED_CHEMISTRY_LESSONS,
    "Biology": EXPANDED_BIOLOGY_LESSONS,
    "Physics": EXPANDED_PHYSICS_LESSONS
}


def get_expanded_lesson(subject: str, subtopic_id: str, lesson_num: int = 1) -> dict:
    """Get an expanded lesson with rich content."""
    subject_lessons = EXPANDED_LESSONS.get(subject, {})
    lessons = subject_lessons.get(subtopic_id, [])
    for lesson in lessons:
        if lesson.get("lesson_number") == lesson_num:
            return lesson
    return None
