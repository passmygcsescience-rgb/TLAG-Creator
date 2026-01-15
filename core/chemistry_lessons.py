"""
AQA GCSE Chemistry Lesson Content
Detailed lesson content for each subtopic
"""

# ==============================================================================
# CHEMISTRY LESSON CONTENT
# Format: Each subtopic has complete TLAG lesson components
# ==============================================================================

CHEMISTRY_LESSONS = {
    # =========================================================================
    # 4.1 ATOMIC STRUCTURE AND THE PERIODIC TABLE
    # =========================================================================
    "4.1.1": {
        "name": "A simple model of the atom",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "Atoms, Elements and Compounds",
                "learning_outcome": "Describe the structure of atoms and explain the difference between elements, compounds and mixtures.",
                "to_know": [
                    "All matter is made of atoms - the smallest part of an element that can exist",
                    "Elements contain only one type of atom",
                    "Compounds contain two or more different types of atoms chemically bonded together",
                    "Atoms have a nucleus containing protons and neutrons, surrounded by electrons",
                    "The number of protons equals the number of electrons in a neutral atom"
                ],
                "do_now": {
                    "questions": [
                        "What is the smallest particle of matter?",
                        "Name three examples of elements",
                        "What is the chemical symbol for oxygen?",
                        "How many elements are there in the periodic table?",
                        "What is water made of?"
                    ],
                    "answers": [
                        "Atom",
                        "Any 3 from: hydrogen, oxygen, carbon, iron, gold, etc.",
                        "O",
                        "118",
                        "Hydrogen and oxygen (H₂O)"
                    ]
                },
                "i_do": {
                    "title": "Atomic Structure",
                    "content": [
                        "All substances are made of atoms - the smallest particle of an element",
                        "Atoms contain a nucleus at the centre made of protons and neutrons",
                        "Electrons orbit the nucleus in shells (energy levels)",
                        "Protons have a +1 charge, neutrons have no charge (0), electrons have a -1 charge",
                        "Atoms are neutral because the number of protons equals the number of electrons"
                    ],
                    "definitions": {
                        "Atom": "The smallest particle of an element that can exist",
                        "Element": "A substance made of only one type of atom",
                        "Compound": "Two or more different types of atoms chemically bonded together",
                        "Nucleus": "The centre of an atom containing protons and neutrons"
                    },
                    "facts": [
                        "Protons have a relative mass of 1 and a charge of +1",
                        "Neutrons have a relative mass of 1 and a charge of 0",
                        "Electrons have a negligible mass and a charge of -1",
                        "The atomic number = number of protons",
                        "The mass number = protons + neutrons"
                    ]
                },
                "we_do": {
                    "question": "Draw the atomic structure of lithium (3 protons, 4 neutrons, 3 electrons) and explain why it's neutral.",
                    "steps": [
                        "Draw a circle for the nucleus",
                        "Write '3p+ 4n' in the nucleus",
                        "Draw electron shells around the nucleus",
                        "Place 2 electrons in the first shell, 1 in the second",
                        "Explain: 3 protons (+3) + 3 electrons (-3) = 0 (neutral)"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Draw the atomic structure of carbon (6 protons, 6 neutrons, 6 electrons)",
                        "answer": "Nucleus with 6p+ 6n, 2 electrons in first shell, 4 in second shell"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Explain why sodium chloride (NaCl) is a compound but not a mixture.",
                        "answer": "NaCl contains two different elements (Na and Cl) that are chemically bonded together, not just mixed."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Predict what happens to the properties when hydrogen and oxygen form water. Why?",
                        "answer": "Properties change completely - gases become liquid, because atoms bond together forming new substances with different properties."
                    }
                ],
                "exit_ticket": {
                    "question": "What is the key difference between a mixture and a compound?",
                    "options": [
                        "A) A mixture contains only one element",
                        "B) A compound has atoms chemically bonded together",
                        "C) A mixture is always a solid",
                        "D) A compound can be separated by filtration"
                    ],
                    "answer": "B) A compound has atoms chemically bonded together"
                }
            },
            {
                "lesson_number": 2,
                "title": "Electronic Structure",
                "learning_outcome": "Draw electronic structures of the first 20 elements and explain how electron configuration relates to position in the periodic table.",
                "to_know": [
                    "Electrons occupy shells (energy levels) around the nucleus",
                    "The first shell holds up to 2 electrons, the second and third hold up to 8",
                    "Electrons fill the lowest energy shell first",
                    "The electronic structure is written as numbers separated by dots (e.g., 2.8.1)",
                    "Elements in the same group have the same number of outer electrons"
                ],
                "do_now": {
                    "questions": [
                        "How many protons does carbon have?",
                        "What charge does an electron have?",
                        "Where are protons found in an atom?",
                        "How many electrons can the first shell hold?",
                        "What is the atomic number of oxygen?"
                    ],
                    "answers": [
                        "6",
                        "Negative (-1)",
                        "In the nucleus",
                        "2",
                        "8"
                    ]
                },
                "i_do": {
                    "title": "Electronic Structure",
                    "content": [
                        "Electrons are arranged in shells (energy levels) around the nucleus",
                        "The first shell can hold up to 2 electrons",
                        "The second and third shells can hold up to 8 electrons each",
                        "Electrons always fill the lowest energy shell first",
                        "The electronic structure is written as numbers separated by dots (e.g., 2.8.1)"
                    ],
                    "definitions": {
                        "Shell": "An energy level around the nucleus where electrons are found",
                        "Electronic structure": "The arrangement of electrons in an atom",
                        "Outer electrons": "Electrons in the outermost shell, which determine chemical properties"
                    },
                    "facts": [
                        "First shell: maximum 2 electrons",
                        "Second shell: maximum 8 electrons",
                        "Third shell: maximum 8 electrons (at GCSE level)",
                        "The number of outer electrons = the group number (for Groups 1-7)",
                        "The number of shells = the period number"
                    ],
                    "examples": [
                        {
                            "problem": "Sodium has atomic number 11 - what is its electronic structure?",
                            "steps": [
                                "11 electrons total (atomic number = electrons)",
                                "First shell: 2 electrons",
                                "Second shell: 8 electrons",
                                "Third shell: 11 - 2 - 8 = 1 electron"
                            ],
                            "answer": "2.8.1"
                        }
                    ]
                },
                "we_do": {
                    "question": "Draw the electronic structure of chlorine (atomic number 17) and identify which group it belongs to.",
                    "steps": [
                        "Total electrons = 17 (same as atomic number)",
                        "First shell: 2 electrons",
                        "Second shell: 8 electrons",
                        "Third shell: 17 - 2 - 8 = 7 electrons",
                        "Electronic structure: 2.8.7",
                        "Group 7 because 7 outer electrons"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Draw the electronic structure of magnesium (atomic number 12)",
                        "answer": "2.8.2"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "An element has electronic structure 2.8.6. What group is it in and what is the element?",
                        "answer": "Group 6, Sulfur (S)"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why elements in Group 0 are unreactive using their electronic structure.",
                        "answer": "Group 0 elements have full outer shells (2 or 8 electrons), so they don't need to gain, lose or share electrons."
                    }
                ],
                "exit_ticket": {
                    "question": "An element has 2.8.4 as its electronic structure. Which group is it in?",
                    "options": [
                        "A) Group 2",
                        "B) Group 4",
                        "C) Group 8",
                        "D) Group 14"
                    ],
                    "answer": "B) Group 4"
                }
            }
        ]
    },
    
    "4.1.2": {
        "name": "The periodic table",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "Development of the Periodic Table",
                "learning_outcome": "Describe how the periodic table was developed and explain how elements are arranged.",
                "to_know": [
                    "Mendeleev arranged elements by atomic mass and left gaps for undiscovered elements",
                    "The modern periodic table arranges elements by atomic number",
                    "Groups are vertical columns - elements have similar properties",
                    "Periods are horizontal rows",
                    "Elements in a group have the same number of outer electrons"
                ],
                "do_now": {
                    "questions": [
                        "What is an element?",
                        "What is the atomic number of an element?",
                        "Name the first element in the periodic table",
                        "What are vertical columns called?",
                        "What are horizontal rows called?"
                    ],
                    "answers": [
                        "A substance made of only one type of atom",
                        "The number of protons in an atom",
                        "Hydrogen",
                        "Groups",
                        "Periods"
                    ]
                },
                "i_do": {
                    "title": "The Periodic Table",
                    "content": [
                        "The periodic table organises all known elements based on their atomic number",
                        "Elements are arranged in rows (periods) and columns (groups)",
                        "Groups are vertical columns - elements in the same group have similar properties",
                        "Periods are horizontal rows - elements in the same period have the same number of electron shells",
                        "Elements in the same group have the same number of outer electrons"
                    ],
                    "definitions": {
                        "Group": "A vertical column of elements with similar properties",
                        "Period": "A horizontal row of elements with the same number of electron shells",
                        "Atomic number": "The number of protons in an atom - determines position in the periodic table"
                    },
                    "facts": [
                        "Mendeleev arranged elements by atomic mass and left gaps for undiscovered elements",
                        "Mendeleev predicted the properties of 'missing' elements - later discovered!",
                        "The modern periodic table arranges elements by atomic number, not mass",
                        "Group 1 elements have 1 outer electron",
                        "Group 7 elements have 7 outer electrons",
                        "Group 0 elements have full outer shells (8, or 2 for helium)"
                    ]
                },
                "we_do": {
                    "question": "Using the periodic table, explain why sodium and potassium have similar properties.",
                    "steps": [
                        "Find sodium (Na) - atomic number 11",
                        "Find potassium (K) - atomic number 19",
                        "Both in Group 1",
                        "Both have 1 outer electron (2.8.1 and 2.8.8.1)",
                        "Similar properties because same number of outer electrons"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "What group and period is carbon in?",
                        "answer": "Group 4, Period 2"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Explain why Mendeleev left gaps in his periodic table.",
                        "answer": "He predicted undiscovered elements would fill the gaps. He left spaces so elements with similar properties would stay in the same group."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Why was changing from atomic mass to atomic number important for the periodic table?",
                        "answer": "Some elements were in wrong order by mass (e.g., Ar before K). Atomic number correctly shows number of protons/electrons which determine properties."
                    }
                ],
                "exit_ticket": {
                    "question": "Elements in the same group have similar properties because they have...",
                    "options": [
                        "A) The same number of protons",
                        "B) The same number of outer electrons",
                        "C) The same atomic mass",
                        "D) The same number of neutrons"
                    ],
                    "answer": "B) The same number of outer electrons"
                }
            },
            {
                "lesson_number": 2,
                "title": "Group 1 - Alkali Metals",
                "learning_outcome": "Describe the properties and reactions of Group 1 metals and explain the trend in reactivity.",
                "to_know": [
                    "Group 1 metals are called alkali metals: lithium, sodium, potassium",
                    "They are soft, have low density, and low melting points",
                    "They react with water to produce hydrogen gas and a metal hydroxide",
                    "Reactivity increases down the group",
                    "They have 1 outer electron which they lose easily to form +1 ions"
                ],
                "do_now": {
                    "questions": [
                        "How many outer electrons do Group 1 elements have?",
                        "What charge ion does sodium form?",
                        "Name the three alkali metals you need to know",
                        "What is produced when metals react with water?",
                        "Which is more reactive: lithium or sodium?"
                    ],
                    "answers": [
                        "1",
                        "+1 (Na⁺)",
                        "Lithium, sodium, potassium",
                        "Hydrogen gas and metal hydroxide",
                        "Sodium"
                    ]
                },
                "i_do": {
                    "title": "Group 1 - The Alkali Metals",
                    "content": [
                        "The alkali metals are lithium (Li), sodium (Na), and potassium (K)",
                        "They are soft metals that can be cut with a knife",
                        "They have low density - lithium, sodium, and potassium float on water",
                        "They react vigorously with water to produce hydrogen gas and a metal hydroxide",
                        "Reactivity INCREASES down the group"
                    ],
                    "definitions": {
                        "Alkali metal": "A Group 1 metal that reacts with water to form an alkaline solution",
                        "Hydroxide": "A compound containing the OH⁻ ion, produced when alkali metals react with water"
                    },
                    "facts": [
                        "All Group 1 metals have 1 electron in their outer shell",
                        "They lose this electron easily to form +1 ions",
                        "Lithium fizzes gently in water",
                        "Sodium melts into a ball and fizzes rapidly",
                        "Potassium ignites with a lilac flame"
                    ],
                    "examples": [
                        {
                            "problem": "Word equation for sodium reacting with water",
                            "answer": "sodium + water → sodium hydroxide + hydrogen"
                        },
                        {
                            "problem": "Symbol equation for potassium reacting with water",
                            "answer": "2K + 2H₂O → 2KOH + H₂"
                        }
                    ],
                    "key_points": [
                        "Reactivity increases down the group because the outer electron is further from the nucleus",
                        "Further from nucleus = weaker attraction = easier to lose"
                    ]
                },
                "we_do": {
                    "question": "Write the word and symbol equation for potassium reacting with water. Explain why potassium is more reactive than sodium.",
                    "steps": [
                        "Word: potassium + water → potassium hydroxide + hydrogen",
                        "Symbol: 2K + 2H₂O → 2KOH + H₂",
                        "Potassium has more shells than sodium",
                        "Outer electron is further from nucleus",
                        "Weaker attraction = easier to lose = more reactive"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Write the word equation for lithium reacting with water.",
                        "answer": "lithium + water → lithium hydroxide + hydrogen"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Predict how rubidium (below potassium) would react with water compared to potassium.",
                        "answer": "More violently - would explode/ignite immediately as it's lower in the group so more reactive."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain in terms of electron structure why Group 1 reactivity increases down the group.",
                        "answer": "More shells = outer electron further from nucleus = weaker electrostatic attraction = easier to lose the electron = more reactive."
                    }
                ],
                "exit_ticket": {
                    "question": "Why does potassium react more violently with water than sodium?",
                    "options": [
                        "A) Potassium has more neutrons",
                        "B) Potassium's outer electron is easier to lose",
                        "C) Potassium has more outer electrons",
                        "D) Potassium is a smaller atom"
                    ],
                    "answer": "B) Potassium's outer electron is easier to lose"
                }
            },
            {
                "lesson_number": 3,
                "title": "Group 7 - Halogens",
                "learning_outcome": "Describe the properties of halogens and explain the trend in reactivity down the group.",
                "to_know": [
                    "Group 7 elements are called halogens: fluorine, chlorine, bromine, iodine",
                    "They exist as diatomic molecules (F₂, Cl₂, Br₂, I₂)",
                    "Reactivity DECREASES down the group",
                    "They gain 1 electron to form -1 ions (halide ions)",
                    "A more reactive halogen displaces a less reactive halide from solution"
                ],
                "do_now": {
                    "questions": [
                        "How many outer electrons do Group 7 elements have?",
                        "What is a diatomic molecule?",
                        "What colour is chlorine gas?",
                        "What charge ion does chlorine form?",
                        "Name the halogen that is a solid at room temperature"
                    ],
                    "answers": [
                        "7",
                        "A molecule made of two atoms",
                        "Green-yellow",
                        "-1 (Cl⁻)",
                        "Iodine"
                    ]
                },
                "i_do": {
                    "title": "Group 7 - The Halogens",
                    "content": [
                        "The halogens are fluorine (F₂), chlorine (Cl₂), bromine (Br₂), and iodine (I₂)",
                        "They all exist as diatomic molecules - two atoms bonded together",
                        "Halogens have 7 electrons in their outer shell and want to GAIN 1 more",
                        "Reactivity DECREASES down the group (opposite to Group 1)",
                        "A more reactive halogen can displace a less reactive halide from solution"
                    ],
                    "definitions": {
                        "Halogen": "A Group 7 element that forms salts when combined with metals",
                        "Diatomic": "A molecule made of two atoms (e.g., Cl₂, Br₂)",
                        "Displacement": "When a more reactive element takes the place of a less reactive one"
                    },
                    "facts": [
                        "Chlorine (Cl₂) is a green-yellow gas",
                        "Bromine (Br₂) is a red-brown liquid",
                        "Iodine (I₂) is a grey solid that sublimes to purple vapour",
                        "Halogens form -1 ions called halide ions (Cl⁻, Br⁻, I⁻)",
                        "Reactivity decreases because larger atoms attract electrons less strongly"
                    ],
                    "examples": [
                        {
                            "problem": "Chlorine + potassium bromide → ?",
                            "answer": "potassium chloride + bromine (Cl₂ + 2KBr → 2KCl + Br₂)"
                        }
                    ]
                },
                "we_do": {
                    "question": "Predict what happens when chlorine water is added to potassium iodide solution. Write the equation.",
                    "steps": [
                        "Chlorine is more reactive than iodine",
                        "Chlorine will displace iodine",
                        "Word: chlorine + potassium iodide → potassium chloride + iodine",
                        "Symbol: Cl₂ + 2KI → 2KCl + I₂",
                        "Observation: solution turns brown (iodine colour)"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Will bromine displace chlorine from sodium chloride solution? Explain.",
                        "answer": "No - bromine is less reactive than chlorine so cannot displace it."
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Write the equation for bromine displacing iodine from potassium iodide.",
                        "answer": "Br₂ + 2KI → 2KBr + I₂"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why chlorine is more reactive than bromine in terms of atomic structure.",
                        "answer": "Chlorine has fewer shells so outer shell is closer to nucleus. Stronger attraction for incoming electron = easier to gain electron = more reactive."
                    }
                ],
                "exit_ticket": {
                    "question": "Which halogen is the MOST reactive?",
                    "options": [
                        "A) Iodine",
                        "B) Bromine",
                        "C) Chlorine",
                        "D) Fluorine"
                    ],
                    "answer": "D) Fluorine"
                }
            },
            {
                "lesson_number": 4,
                "title": "Group 0 - Noble Gases",
                "learning_outcome": "Explain why noble gases are unreactive and describe their uses.",
                "to_know": [
                    "Group 0 elements are called noble gases: helium, neon, argon",
                    "They have full outer electron shells (2 for He, 8 for others)",
                    "They are unreactive because they don't need to gain or lose electrons",
                    "They exist as single atoms (monatomic)",
                    "Uses include: helium in balloons, argon in light bulbs, neon in signs"
                ],
                "do_now": {
                    "questions": [
                        "Where are noble gases found in the periodic table?",
                        "How many outer electrons does neon have?",
                        "Are noble gases reactive or unreactive?",
                        "What is a stable electron configuration?",
                        "Name one use of helium"
                    ],
                    "answers": [
                        "Group 0 (far right)",
                        "8",
                        "Unreactive",
                        "Full outer shell of electrons",
                        "Balloons / airships / deep sea diving"
                    ]
                },
                "i_do": {
                    "title": "Why Noble Gases Are Unreactive",
                    "content": [
                        "Draw electronic structures: He (2), Ne (2.8), Ar (2.8.8)",
                        "All have FULL outer shells",
                        "No need to gain, lose or share electrons",
                        "Therefore don't form bonds = unreactive",
                        "Show uses: light bulbs (argon prevents filament oxidising)"
                    ]
                },
                "we_do": {
                    "question": "Compare the electronic structure of argon (Ar) with chlorine (Cl). Explain why one is reactive and one isn't.",
                    "steps": [
                        "Argon: 2.8.8 (full outer shell)",
                        "Chlorine: 2.8.7 (needs 1 more electron)",
                        "Argon is stable - doesn't need to change",
                        "Chlorine is unstable - wants to gain 1 electron",
                        "This makes chlorine reactive and argon unreactive"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Draw the electronic structure of helium and explain why it's unreactive.",
                        "answer": "2 electrons in one shell (full first shell). Doesn't need to gain or lose electrons."
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Explain why argon is used in light bulbs instead of air.",
                        "answer": "Argon is unreactive so won't react with the hot tungsten filament. Air contains oxygen which would oxidise (burn) the filament."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Predict the boiling point trend of noble gases down the group and explain why.",
                        "answer": "Boiling points increase down the group. Larger atoms have more electrons = stronger intermolecular forces (London forces) = more energy needed to overcome them."
                    }
                ],
                "exit_ticket": {
                    "question": "Noble gases are unreactive because they have...",
                    "options": [
                        "A) No electrons",
                        "B) Full outer electron shells",
                        "C) No protons",
                        "D) Extra neutrons"
                    ],
                    "answer": "B) Full outer electron shells"
                }
            }
        ]
    },
    
    # =========================================================================
    # 4.3 QUANTITATIVE CHEMISTRY
    # =========================================================================
    "4.3.2": {
        "name": "Amount of substance",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "The Mole and Avogadro's Constant",
                "learning_outcome": "Calculate the number of moles in a given mass of substance using the formula n = mass/Mr.",
                "to_know": [
                    "The mole is a unit for counting particles (6.02 × 10²³)",
                    "Avogadro's constant = 6.02 × 10²³",
                    "Mr (relative formula mass) is the sum of all atomic masses in a formula",
                    "n = mass ÷ Mr (moles = mass divided by relative formula mass)",
                    "One mole of any substance contains Avogadro's number of particles"
                ],
                "do_now": {
                    "questions": [
                        "What is the Ar of carbon?",
                        "What is the Ar of oxygen?",
                        "Calculate the Mr of H₂O (H=1, O=16)",
                        "Calculate the Mr of CO₂ (C=12, O=16)",
                        "What is 12 ÷ 4?"
                    ],
                    "answers": [
                        "12",
                        "16",
                        "18",
                        "44",
                        "3"
                    ]
                },
                "i_do": {
                    "title": "Calculating Moles from Mass",
                    "content": [
                        "Formula: n = mass ÷ Mr (write in triangle)",
                        "Example: How many moles in 44g of CO₂?",
                        "Step 1: Mr of CO₂ = 12 + 16 + 16 = 44",
                        "Step 2: n = 44 ÷ 44 = 1 mole",
                        "Key: always calculate Mr first!"
                    ]
                },
                "we_do": {
                    "question": "Calculate the number of moles in 80g of sodium hydroxide, NaOH. (Na=23, O=16, H=1)",
                    "steps": [
                        "Step 1: Calculate Mr",
                        "Mr = 23 + 16 + 1 = 40",
                        "Step 2: Use formula n = mass ÷ Mr",
                        "n = 80 ÷ 40",
                        "n = 2 moles"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Calculate the moles in 36g of water, H₂O (H=1, O=16)",
                        "answer": "Mr = 18, n = 36 ÷ 18 = 2 moles"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Calculate the moles in 7.1g of chlorine gas, Cl₂ (Cl=35.5)",
                        "answer": "Mr = 71, n = 7.1 ÷ 71 = 0.1 moles"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Calculate the mass of 0.25 moles of calcium carbonate, CaCO₃ (Ca=40, C=12, O=16)",
                        "answer": "Mr = 100, mass = 0.25 × 100 = 25g"
                    }
                ],
                "exit_ticket": {
                    "question": "What is the formula for calculating moles?",
                    "options": [
                        "A) n = mass × Mr",
                        "B) n = Mr ÷ mass",
                        "C) n = mass ÷ Mr",
                        "D) n = mass + Mr"
                    ],
                    "answer": "C) n = mass ÷ Mr"
                }
            },
            {
                "lesson_number": 2,
                "title": "Concentration of Solutions",
                "learning_outcome": "Calculate the concentration of a solution in mol/dm³ and g/dm³.",
                "to_know": [
                    "Concentration measures how much solute is dissolved in a solution",
                    "Concentration (mol/dm³) = moles ÷ volume (dm³)",
                    "Concentration (g/dm³) = mass ÷ volume (dm³)",
                    "1 dm³ = 1000 cm³ (divide cm³ by 1000 to get dm³)",
                    "mol/dm³ × Mr = g/dm³"
                ],
                "do_now": {
                    "questions": [
                        "How many cm³ are in 1 dm³?",
                        "Convert 500 cm³ to dm³",
                        "Convert 25 cm³ to dm³",
                        "What is the formula for moles?",
                        "Calculate 0.5 ÷ 0.025"
                    ],
                    "answers": [
                        "1000",
                        "0.5 dm³",
                        "0.025 dm³",
                        "n = mass ÷ Mr",
                        "20"
                    ]
                },
                "i_do": {
                    "title": "Calculating Concentration",
                    "content": [
                        "Formula: Concentration = moles ÷ volume",
                        "CRITICAL: Volume must be in dm³ (÷1000 if in cm³)",
                        "Example: 0.2 moles in 500 cm³",
                        "Convert: 500 ÷ 1000 = 0.5 dm³",
                        "C = 0.2 ÷ 0.5 = 0.4 mol/dm³"
                    ]
                },
                "we_do": {
                    "question": "Calculate the concentration of a solution containing 2 moles of HCl in 250 cm³.",
                    "steps": [
                        "Identify: moles = 2, volume = 250 cm³",
                        "Convert volume: 250 ÷ 1000 = 0.25 dm³",
                        "Apply formula: C = n ÷ V",
                        "C = 2 ÷ 0.25",
                        "C = 8 mol/dm³"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Calculate the concentration of 0.5 moles in 1000 cm³ (1 dm³)",
                        "answer": "C = 0.5 ÷ 1 = 0.5 mol/dm³"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Calculate the concentration of 0.1 moles of NaOH in 200 cm³",
                        "answer": "V = 0.2 dm³, C = 0.1 ÷ 0.2 = 0.5 mol/dm³"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "A solution has concentration 2 mol/dm³. Convert this to g/dm³ for HCl (Mr = 36.5)",
                        "answer": "g/dm³ = mol/dm³ × Mr = 2 × 36.5 = 73 g/dm³"
                    }
                ],
                "exit_ticket": {
                    "question": "A student calculates concentration but forgets to convert cm³ to dm³. Their answer will be...",
                    "options": [
                        "A) 1000× too big",
                        "B) 1000× too small",
                        "C) Correct",
                        "D) 10× too big"
                    ],
                    "answer": "B) 1000× too small"
                }
            }
        ]
    },
    
    # =========================================================================
    # 4.4 CHEMICAL CHANGES
    # =========================================================================
    "4.4.2": {
        "name": "Reactions of acids",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "Titration Calculations",
                "learning_outcome": "Calculate the unknown concentration of a solution using titration results and balanced symbol equations.",
                "to_know": [
                    "Concentration is the amount of solute (moles) dissolved in dm³",
                    "Stoichiometry is the ratio of moles in a balanced equation",
                    "Titration finds the concentration of an unknown solution",
                    "Golden Rule: cm³ ÷ 1000 = dm³",
                    "Extension: mol/dm³ × Mr = g/dm³"
                ],
                "do_now": {
                    "questions": [
                        "How many cm³ are in 1 dm³?",
                        "Convert 25.0 cm³ into dm³",
                        "Convert 500 cm³ into dm³",
                        "Write the formula linking Moles, Concentration, and Volume",
                        "What are the standard units for Concentration?"
                    ],
                    "answers": [
                        "1000",
                        "0.025 dm³",
                        "0.500 dm³",
                        "n = C × V",
                        "mol/dm³"
                    ]
                },
                "i_do": {
                    "title": "The R-V-C-n Grid Method",
                    "content": [
                        "The Problem: Titration questions hide numbers in long paragraphs",
                        "The Solution: Use the R-V-C-n Grid",
                        "Step 1 - Ratio: Fill from the balanced equation",
                        "Step 2 - Volume: Fill knowns (Convert ÷ 1000)",
                        "Step 3 - Moles: Calculate moles of Known (n = C × V)",
                        "Step 4 - Bridge: Use Ratio to find moles of Unknown",
                        "Step 5 - Concentration: Calculate concentration (C = n ÷ V)"
                    ]
                },
                "we_do": {
                    "question": "25.0 cm³ of 0.1 mol/dm³ NaOH reacts with 20.0 cm³ of HCl. Calculate [HCl]. Equation: HCl + NaOH → NaCl + H₂O",
                    "steps": [
                        "Ratio: 1:1 (from equation)",
                        "Volume: NaOH = 0.025 dm³, HCl = 0.020 dm³",
                        "Moles NaOH: n = 0.1 × 0.025 = 0.0025 mol",
                        "Bridge (1:1): Moles HCl = 0.0025 mol",
                        "Concentration HCl: C = 0.0025 ÷ 0.020 = 0.125 mol/dm³"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "25 cm³ of 1.0 mol/dm³ NaOH neutralises 50 cm³ of HCl. Calculate [HCl]. (Ratio 1:1)",
                        "answer": "n = 0.025, [HCl] = 0.025/0.050 = 0.5 mol/dm³"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "20 cm³ of 0.1 mol/dm³ H₂SO₄ neutralises 25 cm³ of NaOH. H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O. Calculate [NaOH].",
                        "answer": "n(H₂SO₄) = 0.002, Ratio 1:2 → n(NaOH) = 0.004, [NaOH] = 0.004/0.025 = 0.16 mol/dm³"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Convert the Silver answer to g/dm³. (Mr of NaOH = 40)",
                        "answer": "0.16 × 40 = 6.4 g/dm³"
                    }
                ],
                "exit_ticket": {
                    "question": "A student forgets to convert 25 cm³ to dm³ and uses '25' instead of '0.025'. Their concentration answer will be...",
                    "options": [
                        "A) 1000× too big",
                        "B) 1000× too small",
                        "C) Correct (units cancel)",
                        "D) 100× too small"
                    ],
                    "answer": "B) 1000× too small"
                }
            }
        ]
    },
    
    # =========================================================================
    # 4.2 BONDING, STRUCTURE AND PROPERTIES
    # =========================================================================
    "4.2.1": {
        "name": "Chemical bonds",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "Ionic Bonding",
                "learning_outcome": "Describe how ionic bonds form and draw dot and cross diagrams for ionic compounds.",
                "to_know": [
                    "Ionic bonds form between metals and non-metals",
                    "Metals LOSE electrons to form positive ions (cations)",
                    "Non-metals GAIN electrons to form negative ions (anions)",
                    "Opposite charges attract = electrostatic attraction = ionic bond",
                    "Ionic compounds form giant ionic lattices"
                ],
                "do_now": {
                    "questions": [
                        "How many outer electrons does sodium have?",
                        "How many outer electrons does chlorine have?",
                        "What charge does Na form when it loses 1 electron?",
                        "What charge does Cl form when it gains 1 electron?",
                        "What happens when opposite charges are near each other?"
                    ],
                    "answers": [
                        "1",
                        "7",
                        "+1 (Na⁺)",
                        "-1 (Cl⁻)",
                        "They attract each other"
                    ]
                },
                "i_do": {
                    "title": "Drawing Dot and Cross Diagrams for NaCl",
                    "content": [
                        "Draw Na atom: 2.8.1 (one outer electron shown as dot)",
                        "Draw Cl atom: 2.8.7 (seven outer electrons shown as crosses)",
                        "Show electron transfer: Na's dot moves to Cl",
                        "Result: Na⁺ [2.8] and Cl⁻ [2.8.8]",
                        "Both now have full outer shells = stable"
                    ]
                },
                "we_do": {
                    "question": "Draw a dot and cross diagram for magnesium oxide (MgO). Mg is 2.8.2 and O is 2.6.",
                    "steps": [
                        "Draw Mg with 2 outer electrons (dots)",
                        "Draw O with 6 outer electrons (crosses)",
                        "Transfer BOTH electrons from Mg to O",
                        "Mg becomes Mg²⁺ [2.8]",
                        "O becomes O²⁻ [2.8]",
                        "Both have full outer shells"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "What type of elements form ionic bonds?",
                        "answer": "Metals and non-metals"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Draw the dot and cross diagram for lithium fluoride (LiF).",
                        "answer": "Li (2.1) transfers 1 electron to F (2.7). Li⁺ [2] and F⁻ [2.8]"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why sodium chloride has a high melting point.",
                        "answer": "Strong electrostatic forces between oppositely charged ions in the giant lattice require lots of energy to overcome."
                    }
                ],
                "exit_ticket": {
                    "question": "In ionic bonding, electrons are...",
                    "options": [
                        "A) Shared between atoms",
                        "B) Transferred from metal to non-metal",
                        "C) Lost by non-metals",
                        "D) Destroyed"
                    ],
                    "answer": "B) Transferred from metal to non-metal"
                }
            },
            {
                "lesson_number": 2,
                "title": "Covalent Bonding",
                "learning_outcome": "Describe how covalent bonds form and draw dot and cross diagrams for simple molecules.",
                "to_know": [
                    "Covalent bonds form between non-metals",
                    "Atoms SHARE pairs of electrons",
                    "Each shared pair = one covalent bond",
                    "Single bond = 1 shared pair, double bond = 2 shared pairs",
                    "Molecules are groups of atoms joined by covalent bonds"
                ],
                "do_now": {
                    "questions": [
                        "How many outer electrons does hydrogen have?",
                        "How many outer electrons does oxygen have?",
                        "How many electrons does hydrogen need to fill its shell?",
                        "How many electrons does oxygen need to fill its shell?",
                        "What type of elements form covalent bonds?"
                    ],
                    "answers": [
                        "1",
                        "6",
                        "1",
                        "2",
                        "Non-metals"
                    ]
                },
                "i_do": {
                    "title": "Drawing Dot and Cross Diagrams for H₂O",
                    "content": [
                        "Oxygen needs 2 electrons, hydrogen needs 1",
                        "Draw O with 6 outer electrons",
                        "Draw 2 H atoms, each with 1 electron",
                        "Share: O shares 1 electron with each H",
                        "O now has 8 (6+2), each H has 2 (1+1)",
                        "Show overlapping circles with shared pairs"
                    ]
                },
                "we_do": {
                    "question": "Draw a dot and cross diagram for methane (CH₄).",
                    "steps": [
                        "Carbon needs 4 electrons (has 4)",
                        "Each hydrogen needs 1 electron (has 1)",
                        "4 hydrogen atoms share with 1 carbon",
                        "Carbon shares 1 electron with each H",
                        "Carbon: 4 + 4 = 8 (full shell)",
                        "Each H: 1 + 1 = 2 (full shell)"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Draw the dot and cross diagram for H₂ (hydrogen gas).",
                        "answer": "Two H atoms share 1 electron each. Each H has 2 electrons (full first shell)."
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Draw the dot and cross diagram for CO₂ (carbon dioxide).",
                        "answer": "Carbon double bonds with each oxygen. O=C=O with 4 shared electrons on each side."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why water has a low boiling point despite strong covalent bonds.",
                        "answer": "Covalent bonds within molecules are strong, but intermolecular forces between molecules are weak. Only weak forces need breaking to boil."
                    }
                ],
                "exit_ticket": {
                    "question": "How many shared pairs are in a double covalent bond?",
                    "options": [
                        "A) 1",
                        "B) 2",
                        "C) 3",
                        "D) 4"
                    ],
                    "answer": "B) 2"
                }
            },
            {
                "lesson_number": 3,
                "title": "Metallic Bonding",
                "learning_outcome": "Describe metallic bonding and explain the properties of metals.",
                "to_know": [
                    "Metallic bonding occurs in metals only",
                    "Metal atoms lose outer electrons to form positive ions",
                    "Electrons become 'delocalised' (free to move)",
                    "Positive ions are held in a 'sea of delocalised electrons'",
                    "Properties: conduct electricity, malleable, ductile, high melting points"
                ],
                "do_now": {
                    "questions": [
                        "What type of ion does a metal form?",
                        "What does 'delocalised' mean?",
                        "Name a property of metals",
                        "Can metals conduct electricity?",
                        "Are metals generally hard or soft?"
                    ],
                    "answers": [
                        "Positive ion (cation)",
                        "Free to move, not fixed in place",
                        "Conduct electricity/malleable/ductile/shiny",
                        "Yes",
                        "Hard (most metals)"
                    ]
                },
                "i_do": {
                    "title": "Understanding Metallic Bonding",
                    "content": [
                        "Draw metal atoms losing outer electrons",
                        "Show positive ions in regular arrangement",
                        "Draw electrons moving freely between ions (sea of electrons)",
                        "Explain: strong electrostatic attraction between + ions and - electrons",
                        "Link to properties: electrons move = conduct electricity"
                    ]
                },
                "we_do": {
                    "question": "Explain why metals can conduct electricity and are malleable using metallic bonding.",
                    "steps": [
                        "Conduct: delocalised electrons are free to move",
                        "Electrons carry charge through the metal",
                        "Malleable: layers of ions can slide over each other",
                        "Sea of electrons moves with them",
                        "Bonds don't break when shape changes"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "What are the two parts of metallic bonding?",
                        "answer": "Positive metal ions and a sea of delocalised electrons"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Explain why metals have high melting points.",
                        "answer": "Strong electrostatic attraction between positive ions and delocalised electrons requires lots of energy to overcome."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why alloys are harder than pure metals.",
                        "answer": "Different sized atoms disrupt the regular lattice. Layers can't slide over each other as easily."
                    }
                ],
                "exit_ticket": {
                    "question": "Metals conduct electricity because they have...",
                    "options": [
                        "A) Shared electrons",
                        "B) Delocalised electrons",
                        "C) No electrons",
                        "D) Covalent bonds"
                    ],
                    "answer": "B) Delocalised electrons"
                }
            }
        ]
    },
    
    # =========================================================================
    # 4.4 CHEMICAL CHANGES - Reactivity
    # =========================================================================
    "4.4.1": {
        "name": "Reactivity of metals",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "The Reactivity Series",
                "learning_outcome": "Use the reactivity series to predict displacement reactions.",
                "to_know": [
                    "The reactivity series ranks metals by how easily they react",
                    "Order: K > Na > Ca > Mg > Al > Zn > Fe > Cu > Ag > Au",
                    "More reactive metals lose electrons more easily",
                    "A more reactive metal displaces a less reactive metal from a compound",
                    "Displacement is a type of redox reaction"
                ],
                "do_now": {
                    "questions": [
                        "Which is more reactive: sodium or iron?",
                        "What happens in a displacement reaction?",
                        "What type of ion does a metal form?",
                        "Is gold reactive or unreactive?",
                        "What does 'oxidation' mean for metals?"
                    ],
                    "answers": [
                        "Sodium",
                        "A more reactive element takes the place of a less reactive one",
                        "Positive ion",
                        "Unreactive",
                        "Losing electrons"
                    ]
                },
                "i_do": {
                    "title": "Predicting Displacement Reactions",
                    "content": [
                        "Write reactivity series on board",
                        "Example: Can zinc displace copper from copper sulfate?",
                        "Zinc is MORE reactive than copper",
                        "YES - zinc will displace copper",
                        "Zn + CuSO₄ → ZnSO₄ + Cu",
                        "Observation: blue solution turns colourless, brown copper forms"
                    ]
                },
                "we_do": {
                    "question": "Predict if iron will react with magnesium sulfate. Write an equation if it will.",
                    "steps": [
                        "Check reactivity: Mg is ABOVE Fe in series",
                        "Magnesium is MORE reactive than iron",
                        "Iron CANNOT displace magnesium",
                        "No reaction will occur",
                        "Rule: A metal can only displace one BELOW it in the series"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Will copper react with silver nitrate? Explain.",
                        "answer": "Yes - copper is more reactive than silver, so it displaces silver."
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Write the equation for magnesium reacting with copper sulfate.",
                        "answer": "Mg + CuSO₄ → MgSO₄ + Cu"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain in terms of electrons why zinc displaces copper from copper sulfate.",
                        "answer": "Zinc loses electrons more easily than copper. Zinc atoms become Zn²⁺ ions, giving electrons to Cu²⁺ ions which become Cu atoms."
                    }
                ],
                "exit_ticket": {
                    "question": "Which metal will NOT displace copper from copper sulfate?",
                    "options": [
                        "A) Zinc",
                        "B) Magnesium",
                        "C) Iron",
                        "D) Silver"
                    ],
                    "answer": "D) Silver"
                }
            },
            {
                "lesson_number": 2,
                "title": "Oxidation and Reduction (Redox)",
                "learning_outcome": "Identify oxidation and reduction in terms of electron transfer.",
                "to_know": [
                    "Oxidation Is Loss of electrons (OIL)",
                    "Reduction Is Gain of electrons (RIG)",
                    "OIL RIG helps you remember",
                    "In redox reactions, one species is oxidised and another is reduced",
                    "The reducing agent gets oxidised; the oxidising agent gets reduced"
                ],
                "do_now": {
                    "questions": [
                        "What charge does Zn²⁺ have?",
                        "How many electrons has zinc lost to become Zn²⁺?",
                        "What does 'reduction' mean?",
                        "In CuSO₄, what is the charge on Cu?",
                        "What is formed when Cu²⁺ gains 2 electrons?"
                    ],
                    "answers": [
                        "+2",
                        "2",
                        "Gaining electrons",
                        "+2",
                        "Cu (copper metal)"
                    ]
                },
                "i_do": {
                    "title": "Identifying Oxidation and Reduction",
                    "content": [
                        "Write OIL RIG on board",
                        "Example: Zn + Cu²⁺ → Zn²⁺ + Cu",
                        "Zn → Zn²⁺ (LOSES 2 electrons) = OXIDISED",
                        "Cu²⁺ → Cu (GAINS 2 electrons) = REDUCED",
                        "Zinc is the reducing agent (it causes reduction)",
                        "Copper ions are the oxidising agent"
                    ]
                },
                "we_do": {
                    "question": "In the reaction 2Na + Cl₂ → 2NaCl, identify what is oxidised and what is reduced.",
                    "steps": [
                        "Na → Na⁺ (loses 1 electron) = OXIDISED",
                        "Cl₂ → 2Cl⁻ (each Cl gains 1 electron) = REDUCED",
                        "Sodium is the reducing agent",
                        "Chlorine is the oxidising agent",
                        "Remember: OIL RIG"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "What does OIL RIG stand for?",
                        "answer": "Oxidation Is Loss, Reduction Is Gain (of electrons)"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "In Mg + CuSO₄ → MgSO₄ + Cu, which species is oxidised?",
                        "answer": "Magnesium (Mg → Mg²⁺, loses 2 electrons)"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Write half equations for the reaction: Fe + CuSO₄ → FeSO₄ + Cu",
                        "answer": "Oxidation: Fe → Fe²⁺ + 2e⁻. Reduction: Cu²⁺ + 2e⁻ → Cu"
                    }
                ],
                "exit_ticket": {
                    "question": "When a metal atom becomes a positive ion, it has been...",
                    "options": [
                        "A) Reduced",
                        "B) Oxidised",
                        "C) Neutralised",
                        "D) Dissolved"
                    ],
                    "answer": "B) Oxidised"
                }
            }
        ]
    },
    
    # =========================================================================
    # 4.5 ENERGY CHANGES
    # =========================================================================
    "4.5.1": {
        "name": "Exothermic and endothermic reactions",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "Exothermic and Endothermic Reactions",
                "learning_outcome": "Identify exothermic and endothermic reactions and interpret reaction profiles.",
                "to_know": [
                    "Exothermic reactions RELEASE energy to surroundings (temperature increases)",
                    "Endothermic reactions ABSORB energy from surroundings (temperature decreases)",
                    "Combustion, neutralisation and oxidation are exothermic",
                    "Thermal decomposition and citric acid + sodium bicarbonate are endothermic",
                    "Reaction profiles show energy changes during a reaction"
                ],
                "do_now": {
                    "questions": [
                        "What does 'exo' mean?",
                        "What does 'endo' mean?",
                        "What happens to temperature when energy is released?",
                        "Name a type of reaction that releases heat",
                        "What is thermal decomposition?"
                    ],
                    "answers": [
                        "Out/outside",
                        "In/inside",
                        "Temperature increases",
                        "Combustion/neutralisation",
                        "Breaking down a substance using heat"
                    ]
                },
                "i_do": {
                    "title": "Drawing Reaction Profiles",
                    "content": [
                        "Draw axes: Energy (y) vs Progress of reaction (x)",
                        "Exothermic: reactants HIGH, products LOW, energy is released",
                        "Arrow pointing DOWN shows energy given out",
                        "Endothermic: reactants LOW, products HIGH, energy absorbed",
                        "Arrow pointing UP shows energy taken in",
                        "Activation energy = energy needed to start reaction (hump)"
                    ]
                },
                "we_do": {
                    "question": "Draw a reaction profile for burning methane (exothermic). Label reactants, products, activation energy and energy change.",
                    "steps": [
                        "Draw axes: Energy vs Progress",
                        "Start with reactants (CH₄ + 2O₂) at HIGH energy",
                        "Draw curve going UP (activation energy hump)",
                        "End with products (CO₂ + 2H₂O) at LOW energy",
                        "Label downward arrow as 'Energy released'",
                        "This shows net ENERGY OUT"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Is combustion exothermic or endothermic? How do you know?",
                        "answer": "Exothermic - it releases heat (you can feel the warmth from fire)"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Draw a reaction profile for thermal decomposition (endothermic).",
                        "answer": "Reactants LOW, products HIGH. Arrow pointing up showing energy absorbed."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "A reaction is exothermic but requires heating to start. Explain this using activation energy.",
                        "answer": "Activation energy is needed to break bonds and start the reaction. Once started, the reaction releases more energy than was put in."
                    }
                ],
                "exit_ticket": {
                    "question": "In an endothermic reaction, the products have...",
                    "options": [
                        "A) Less energy than reactants",
                        "B) More energy than reactants",
                        "C) The same energy as reactants",
                        "D) No energy"
                    ],
                    "answer": "B) More energy than reactants"
                }
            },
            {
                "lesson_number": 2,
                "title": "Bond Energy Calculations",
                "learning_outcome": "Calculate the overall energy change of a reaction using bond energies.",
                "to_know": [
                    "Breaking bonds requires energy (ENDOTHERMIC)",
                    "Making bonds releases energy (EXOTHERMIC)",
                    "Energy change = Energy to break bonds - Energy released making bonds",
                    "Negative answer = exothermic, positive answer = endothermic",
                    "Bond energy is measured in kJ/mol"
                ],
                "do_now": {
                    "questions": [
                        "Is breaking bonds exothermic or endothermic?",
                        "Is making bonds exothermic or endothermic?",
                        "What does a negative energy value mean?",
                        "What units is bond energy measured in?",
                        "Calculate: 800 - 1200"
                    ],
                    "answers": [
                        "Endothermic (needs energy)",
                        "Exothermic (releases energy)",
                        "Exothermic (energy released)",
                        "kJ/mol",
                        "-400"
                    ]
                },
                "i_do": {
                    "title": "Calculating Energy Change",
                    "content": [
                        "H₂ + Cl₂ → 2HCl",
                        "Bonds broken: 1 × H-H (436) + 1 × Cl-Cl (242) = 678 kJ",
                        "Bonds made: 2 × H-Cl (431) = 862 kJ",
                        "Energy change = 678 - 862 = -184 kJ",
                        "Negative = EXOTHERMIC",
                        "More energy released making bonds than needed to break them"
                    ]
                },
                "we_do": {
                    "question": "Calculate the energy change for CH₄ + 2O₂ → CO₂ + 2H₂O. Bond energies: C-H 412, O=O 496, C=O 743, O-H 463 kJ/mol.",
                    "steps": [
                        "Bonds broken: 4 × C-H (4×412=1648) + 2 × O=O (2×496=992) = 2640 kJ",
                        "Bonds made: 2 × C=O (2×743=1486) + 4 × O-H (4×463=1852) = 3338 kJ",
                        "Energy change = 2640 - 3338 = -698 kJ",
                        "Negative = EXOTHERMIC",
                        "Combustion releases energy"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Which releases energy: breaking or making bonds?",
                        "answer": "Making bonds releases energy"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "If breaking bonds needs 500 kJ and making bonds releases 700 kJ, is the reaction exo or endothermic?",
                        "answer": "500 - 700 = -200 kJ. Negative = exothermic"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Calculate energy change for H₂ + Br₂ → 2HBr. H-H=436, Br-Br=193, H-Br=366 kJ/mol",
                        "answer": "Broken: 436+193=629. Made: 2×366=732. Change: 629-732=-103 kJ (exothermic)"
                    }
                ],
                "exit_ticket": {
                    "question": "A reaction has energy change of +50 kJ. This reaction is...",
                    "options": [
                        "A) Exothermic",
                        "B) Endothermic",
                        "C) Neutral",
                        "D) Cannot tell"
                    ],
                    "answer": "B) Endothermic"
                }
            }
        ]
    },
    
    # =========================================================================
    # 4.6 RATE OF REACTION
    # =========================================================================
    "4.6.1": {
        "name": "Rate of reaction",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "Factors Affecting Rate of Reaction",
                "learning_outcome": "Explain how temperature, concentration, surface area and catalysts affect rate of reaction.",
                "to_know": [
                    "Rate of reaction = how fast reactants are converted to products",
                    "Increasing temperature increases rate (particles move faster, more collisions)",
                    "Increasing concentration increases rate (more particles, more collisions)",
                    "Increasing surface area increases rate (more area for collisions)",
                    "Catalysts increase rate without being used up"
                ],
                "do_now": {
                    "questions": [
                        "What is a collision?",
                        "What happens to particles when you heat them?",
                        "What does concentration mean?",
                        "What is surface area?",
                        "What is a catalyst?"
                    ],
                    "answers": [
                        "When particles hit each other",
                        "They move faster/have more energy",
                        "How much solute is dissolved in solution",
                        "The total area of exposed surface",
                        "A substance that speeds up a reaction without being used up"
                    ]
                },
                "i_do": {
                    "title": "Collision Theory",
                    "content": [
                        "For a reaction to happen, particles must COLLIDE",
                        "Collisions must have enough ENERGY (activation energy)",
                        "More collisions per second = faster rate",
                        "Temperature: faster particles = more frequent and more energetic collisions",
                        "Concentration: more particles = more frequent collisions",
                        "Surface area: more exposed particles = more collisions"
                    ]
                },
                "we_do": {
                    "question": "Explain why powdered calcium carbonate reacts faster with acid than large lumps.",
                    "steps": [
                        "Powdered form has GREATER surface area",
                        "More particles are exposed on the surface",
                        "More acid particles can collide with CaCO₃",
                        "More frequent collisions = faster rate",
                        "Same mass, but different surface area"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Name three factors that affect rate of reaction.",
                        "answer": "Temperature, concentration, surface area (also: catalyst, pressure for gases)"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Explain why increasing temperature increases rate of reaction.",
                        "answer": "Particles move faster, so there are more collisions per second AND more collisions have enough energy to react."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "A reaction doubles in rate for every 10°C increase. If rate at 20°C is 1, what is rate at 50°C?",
                        "answer": "30°C increase = 3 doublings. 1 × 2 × 2 × 2 = 8 times faster"
                    }
                ],
                "exit_ticket": {
                    "question": "Which does NOT increase rate of reaction?",
                    "options": [
                        "A) Increasing temperature",
                        "B) Increasing concentration",
                        "C) Using larger lumps instead of powder",
                        "D) Adding a catalyst"
                    ],
                    "answer": "C) Using larger lumps instead of powder"
                }
            },
            {
                "lesson_number": 2,
                "title": "Measuring Rate of Reaction",
                "learning_outcome": "Calculate rate of reaction from experimental data and interpret rate graphs.",
                "to_know": [
                    "Rate = amount of reactant used ÷ time OR amount of product formed ÷ time",
                    "Units: g/s, cm³/s, mol/s",
                    "Steeper gradient on graph = faster rate",
                    "Horizontal line = reaction finished",
                    "Initial rate = gradient at start of graph"
                ],
                "do_now": {
                    "questions": [
                        "What is the formula for rate?",
                        "What does a steep line on a graph show?",
                        "What happens to the line when a reaction finishes?",
                        "Calculate: 60 ÷ 30",
                        "What units could rate be measured in?"
                    ],
                    "answers": [
                        "Rate = change/time",
                        "Fast rate",
                        "It becomes horizontal/flat",
                        "2",
                        "g/s, cm³/s, mol/s"
                    ]
                },
                "i_do": {
                    "title": "Calculating Rate from Data",
                    "content": [
                        "Example: 50 cm³ gas produced in 25 seconds",
                        "Rate = volume ÷ time = 50 ÷ 25 = 2 cm³/s",
                        "On a graph: rate = gradient = rise ÷ run",
                        "Draw tangent at point to find rate at that moment",
                        "Steeper tangent = faster rate at that point"
                    ]
                },
                "we_do": {
                    "question": "A reaction produces gas. At 20s, 40cm³ produced. At 40s, 70cm³ produced. Calculate the average rate between these times.",
                    "steps": [
                        "Volume change = 70 - 40 = 30 cm³",
                        "Time change = 40 - 20 = 20 s",
                        "Rate = 30 ÷ 20 = 1.5 cm³/s",
                        "This is the average rate over that period",
                        "Initial rate would be faster (steeper)"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "A reaction produces 60 cm³ of gas in 30 seconds. Calculate the rate.",
                        "answer": "Rate = 60 ÷ 30 = 2 cm³/s"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Look at two reaction graphs. One is steeper. Which has the faster rate?",
                        "answer": "The steeper graph has the faster rate (greater gradient)."
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why the gradient of a rate graph decreases as the reaction proceeds.",
                        "answer": "Concentration of reactants decreases, so fewer successful collisions per second. Rate slows down until reactants are used up."
                    }
                ],
                "exit_ticket": {
                    "question": "A horizontal line on a rate graph means...",
                    "options": [
                        "A) The reaction is speeding up",
                        "B) The reaction has finished",
                        "C) The reaction is slowing down",
                        "D) No reaction is occurring"
                    ],
                    "answer": "B) The reaction has finished"
                }
            }
        ]
    },
    
    # =========================================================================
    # 4.7 ORGANIC CHEMISTRY
    # =========================================================================
    "4.7.1": {
        "name": "Carbon compounds as fuels",
        "lessons": [
            {
                "lesson_number": 1,
                "title": "Crude Oil and Fractional Distillation",
                "learning_outcome": "Describe how crude oil is separated by fractional distillation.",
                "to_know": [
                    "Crude oil is a mixture of hydrocarbons (compounds of C and H only)",
                    "Hydrocarbons are separated by fractional distillation",
                    "Separation works because fractions have different boiling points",
                    "Smaller molecules have lower boiling points (collected at top)",
                    "Larger molecules have higher boiling points (collected at bottom)"
                ],
                "do_now": {
                    "questions": [
                        "What is a hydrocarbon?",
                        "What two elements make up hydrocarbons?",
                        "What is crude oil?",
                        "What is distillation?",
                        "Do small or large molecules have higher boiling points?"
                    ],
                    "answers": [
                        "A compound of hydrogen and carbon only",
                        "Carbon and hydrogen",
                        "A mixture of hydrocarbons formed from ancient organisms",
                        "Separating liquids by boiling point",
                        "Large molecules"
                    ]
                },
                "i_do": {
                    "title": "How Fractional Distillation Works",
                    "content": [
                        "Crude oil is heated and vapours rise up the column",
                        "Column is hot at bottom, cool at top",
                        "Each fraction condenses at its boiling point",
                        "Top: gases, petrol (small molecules)",
                        "Bottom: bitumen (large molecules)",
                        "Fractions: gases, petrol, kerosene, diesel, fuel oil, bitumen"
                    ]
                },
                "we_do": {
                    "question": "Explain why petrol is collected near the top of the fractionating column but bitumen at the bottom.",
                    "steps": [
                        "Petrol has SMALL molecules",
                        "Small = weak intermolecular forces = LOW boiling point",
                        "Condenses at the COOL top of column",
                        "Bitumen has LARGE molecules",
                        "Large = strong intermolecular forces = HIGH boiling point",
                        "Condenses at the HOT bottom"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "What property is used to separate crude oil into fractions?",
                        "answer": "Boiling point"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Put these in order from top to bottom of column: diesel, petrol, bitumen, kerosene",
                        "answer": "Petrol, kerosene, diesel, bitumen (smallest to largest molecules)"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why larger hydrocarbon molecules have higher boiling points.",
                        "answer": "Larger molecules have more electrons, so stronger London forces between molecules. More energy needed to overcome these forces."
                    }
                ],
                "exit_ticket": {
                    "question": "Which fraction is collected at the TOP of the column?",
                    "options": [
                        "A) Bitumen",
                        "B) Diesel",
                        "C) Fuel oil",
                        "D) Gases/petrol"
                    ],
                    "answer": "D) Gases/petrol"
                }
            },
            {
                "lesson_number": 2,
                "title": "Alkanes",
                "learning_outcome": "Name and draw the first four alkanes and describe their properties.",
                "to_know": [
                    "Alkanes are saturated hydrocarbons (single bonds only)",
                    "General formula: CₙH₂ₙ₊₂",
                    "Methane CH₄, Ethane C₂H₆, Propane C₃H₈, Butane C₄H₁₀",
                    "As chain length increases: boiling point increases, viscosity increases",
                    "As chain length increases: flammability decreases"
                ],
                "do_now": {
                    "questions": [
                        "What is a hydrocarbon?",
                        "What is a saturated hydrocarbon?",
                        "How many carbons in methane?",
                        "How many carbons in ethane?",
                        "What is the formula for methane?"
                    ],
                    "answers": [
                        "Compound of carbon and hydrogen only",
                        "Contains only single bonds",
                        "1",
                        "2",
                        "CH₄"
                    ]
                },
                "i_do": {
                    "title": "Drawing and Naming Alkanes",
                    "content": [
                        "Draw methane: 1C with 4H (CH₄)",
                        "Draw ethane: 2C chain with 6H (C₂H₆)",
                        "Draw propane: 3C chain with 8H (C₃H₈)",
                        "Draw butane: 4C chain with 10H (C₄H₁₀)",
                        "Pattern: add 1C = add 2H (CH₂ unit)",
                        "General formula: CₙH₂ₙ₊₂"
                    ]
                },
                "we_do": {
                    "question": "Use the general formula CₙH₂ₙ₊₂ to work out the formula of an alkane with 5 carbons (pentane).",
                    "steps": [
                        "n = 5 (number of carbons)",
                        "H = 2n + 2 = 2(5) + 2 = 12",
                        "Formula: C₅H₁₂",
                        "This is pentane",
                        "Draw: 5 carbon chain with 12 hydrogens"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "Name the alkane with formula C₃H₈",
                        "answer": "Propane"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Work out the formula of the alkane with 6 carbons (hexane).",
                        "answer": "C₆H₁₄ (2×6+2=14 hydrogens)"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why propane has a lower boiling point than butane.",
                        "answer": "Propane has shorter chain = fewer electrons = weaker intermolecular forces = less energy needed to overcome them = lower boiling point."
                    }
                ],
                "exit_ticket": {
                    "question": "What is the general formula for alkanes?",
                    "options": [
                        "A) CₙH₂ₙ",
                        "B) CₙH₂ₙ₊₂",
                        "C) CₙH₂ₙ₋₂",
                        "D) CₙHₙ"
                    ],
                    "answer": "B) CₙH₂ₙ₊₂"
                }
            },
            {
                "lesson_number": 3,
                "title": "Combustion of Hydrocarbons",
                "learning_outcome": "Write equations for complete and incomplete combustion and explain the products.",
                "to_know": [
                    "Complete combustion: hydrocarbon + oxygen → carbon dioxide + water",
                    "Incomplete combustion occurs with limited oxygen",
                    "Products of incomplete combustion: carbon monoxide (CO) and/or carbon (soot)",
                    "Carbon monoxide is toxic - binds to haemoglobin",
                    "Combustion is exothermic (releases energy)"
                ],
                "do_now": {
                    "questions": [
                        "What is combustion?",
                        "What gas is needed for combustion?",
                        "What are the products of complete combustion?",
                        "Is combustion exothermic or endothermic?",
                        "What is soot?"
                    ],
                    "answers": [
                        "Burning (reacting with oxygen)",
                        "Oxygen",
                        "Carbon dioxide and water",
                        "Exothermic",
                        "Carbon particles (unburnt carbon)"
                    ]
                },
                "i_do": {
                    "title": "Writing Combustion Equations",
                    "content": [
                        "Complete: CH₄ + 2O₂ → CO₂ + 2H₂O",
                        "Blue flame = complete combustion",
                        "Incomplete (less O₂): 2CH₄ + 3O₂ → 2CO + 4H₂O",
                        "Yellow/orange flame = incomplete",
                        "CO is dangerous - colourless, odourless, toxic",
                        "Can also form C (soot) with very limited oxygen"
                    ]
                },
                "we_do": {
                    "question": "Write the equation for complete combustion of propane (C₃H₈).",
                    "steps": [
                        "C₃H₈ + O₂ → CO₂ + H₂O (unbalanced)",
                        "Balance C: 3 carbons, need 3CO₂",
                        "Balance H: 8 hydrogens, need 4H₂O",
                        "Count O: 3×2 + 4×1 = 10 oxygens needed",
                        "Balance O: 10 ÷ 2 = 5O₂",
                        "C₃H₈ + 5O₂ → 3CO₂ + 4H₂O"
                    ]
                },
                "you_do": [
                    {
                        "name": "Bronze (Grade 5)",
                        "question": "What are the products of complete combustion?",
                        "answer": "Carbon dioxide and water"
                    },
                    {
                        "name": "Silver (Grade 7)",
                        "question": "Write the equation for complete combustion of methane (CH₄).",
                        "answer": "CH₄ + 2O₂ → CO₂ + 2H₂O"
                    },
                    {
                        "name": "Gold (Grade 9)",
                        "question": "Explain why carbon monoxide from incomplete combustion is dangerous.",
                        "answer": "CO binds to haemoglobin in red blood cells more strongly than oxygen. Reduces oxygen carried in blood. Colourless and odourless so hard to detect."
                    }
                ],
                "exit_ticket": {
                    "question": "Which is a product of incomplete combustion?",
                    "options": [
                        "A) Carbon dioxide only",
                        "B) Water only",
                        "C) Carbon monoxide",
                        "D) Nitrogen"
                    ],
                    "answer": "C) Carbon monoxide"
                }
            }
        ]
    }
}

def get_lesson_content(subtopic_id: str, lesson_number: int = 1) -> dict:
    """Get complete lesson content for a subtopic."""
    subtopic_data = CHEMISTRY_LESSONS.get(subtopic_id)
    if not subtopic_data:
        return None
    
    lessons = subtopic_data.get("lessons", [])
    for lesson in lessons:
        if lesson.get("lesson_number") == lesson_number:
            return lesson
    
    return lessons[0] if lessons else None

def get_available_lessons(subtopic_id: str) -> list:
    """Get list of available lessons for a subtopic."""
    subtopic_data = CHEMISTRY_LESSONS.get(subtopic_id)
    if not subtopic_data:
        return []
    
    return [
        {"number": l["lesson_number"], "title": l["title"]}
        for l in subtopic_data.get("lessons", [])
    ]
