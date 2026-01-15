"""
AQA GCSE Curriculum Data
Complete specifications for Biology (8461), Chemistry (8462), Physics (8463)
Including all topics, subtopics, and required practicals.
"""

# =============================================================================
# AQA GCSE BIOLOGY (8461)
# =============================================================================
BIOLOGY_SPEC = {
    "code": "8461",
    "name": "AQA GCSE Biology",
    "topics": {
        "4.1": {
            "name": "Cell Biology",
            "subtopics": {
                "4.1.1": {
                    "name": "Cell Structure",
                    "content": [
                        "Eukaryotic cells (animal and plant) contain: cell membrane, cytoplasm, nucleus, mitochondria, ribosomes",
                        "Plant cells also contain: chloroplasts, cell wall, permanent vacuole",
                        "Prokaryotic cells (bacteria) lack a true nucleus and other membrane-bound organelles",
                        "Bacteria contain: cell membrane, cytoplasm, plasmid DNA, ribosomes, cell wall",
                        "Light microscopes magnify up to 2000x; electron microscopes can magnify over 2,000,000x"
                    ]
                },
                "4.1.2": {
                    "name": "Cell Division",
                    "content": [
                        "Mitosis produces two genetically identical daughter cells for growth and repair",
                        "The cell cycle includes interphase (DNA replication), mitosis, and cytokinesis",
                        "Stem cells are undifferentiated cells that can develop into specialised cells",
                        "Embryonic stem cells can differentiate into any cell type; adult stem cells are more limited",
                        "Therapeutic cloning uses stem cells to treat diseases like diabetes and paralysis"
                    ]
                },
                "4.1.3": {
                    "name": "Transport in Cells",
                    "content": [
                        "Diffusion is the net movement of particles from high to low concentration",
                        "Osmosis is the movement of water across a partially permeable membrane from dilute to concentrated solution",
                        "Active transport moves substances from low to high concentration, requiring energy from respiration",
                        "Surface area to volume ratio affects the rate of diffusion",
                        "Exchange surfaces like alveoli and villi are adapted: thin walls, large surface area, rich blood supply"
                    ]
                }
            }
        },
        "4.2": {
            "name": "Organisation",
            "subtopics": {
                "4.2.1": {
                    "name": "Principles of Organisation",
                    "content": [
                        "Cells → Tissues → Organs → Organ systems → Organisms",
                        "A tissue is a group of similar cells working together",
                        "An organ contains several tissue types working together",
                        "Organ systems work together to form an organism"
                    ]
                },
                "4.2.2": {
                    "name": "Animal Tissues and Organs",
                    "content": [
                        "The digestive system breaks down food using enzymes",
                        "Amylase (salivary glands, pancreas) breaks starch into sugars",
                        "Protease (stomach, pancreas) breaks proteins into amino acids",
                        "Lipase (pancreas, small intestine) breaks lipids into fatty acids and glycerol",
                        "The heart is a double pump: right side pumps to lungs, left side pumps to body",
                        "Blood contains: red blood cells (oxygen), white blood cells (immunity), platelets (clotting), plasma"
                    ]
                },
                "4.2.3": {
                    "name": "Plant Tissues and Organs",
                    "content": [
                        "Plant organs include: roots, stems, leaves",
                        "Xylem transports water and minerals UP from roots (transpiration pull)",
                        "Phloem transports dissolved sugars UP and DOWN (translocation)",
                        "Stomata control gas exchange and water loss in leaves",
                        "Guard cells open stomata in light for photosynthesis"
                    ]
                },
                "4.2.4": {
                    "name": "Non-Communicable Diseases",
                    "content": [
                        "Risk factors for cardiovascular disease: smoking, high fat diet, lack of exercise",
                        "Coronary heart disease is caused by fatty deposits in coronary arteries",
                        "Cancer is caused by uncontrolled cell division due to changes in DNA",
                        "Carcinogens (e.g., UV light, smoking) increase cancer risk",
                        "Obesity increases risk of Type 2 diabetes"
                    ]
                }
            }
        },
        "4.3": {
            "name": "Infection and Response",
            "subtopics": {
                "4.3.1": {
                    "name": "Communicable Diseases",
                    "content": [
                        "Pathogens are microorganisms that cause disease: viruses, bacteria, fungi, protists",
                        "Viruses: measles (fever, rash), HIV (attacks immune system), TMV (mosaic patterns on leaves)",
                        "Bacteria: Salmonella (food poisoning), Gonorrhoea (STI)",
                        "Fungi: Rose black spot (purple/black spots on leaves)",
                        "Protists: Malaria (spread by mosquito vector)"
                    ]
                },
                "4.3.2": {
                    "name": "Human Defence Systems",
                    "content": [
                        "First line of defence: skin (barrier), mucus, stomach acid",
                        "White blood cells: phagocytosis (engulfing), antibodies (specific to antigens), antitoxins",
                        "Antibodies lock onto specific antigens on pathogen surfaces",
                        "Memory cells remain after infection for faster secondary response"
                    ]
                },
                "4.3.3": {
                    "name": "Vaccination and Antibiotics",
                    "content": [
                        "Vaccines contain dead/inactive pathogens to stimulate antibody production",
                        "Vaccination creates immunity without causing disease",
                        "Antibiotics kill bacteria but NOT viruses",
                        "Antibiotic resistance is increasing due to overuse"
                    ]
                }
            }
        },
        "4.4": {
            "name": "Bioenergetics",
            "subtopics": {
                "4.4.1": {
                    "name": "Photosynthesis",
                    "content": [
                        "Photosynthesis equation: carbon dioxide + water → glucose + oxygen",
                        "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
                        "Photosynthesis is endothermic - energy transferred from light",
                        "Rate affected by: light intensity, CO₂ concentration, temperature",
                        "Glucose used for: respiration, cellulose, starch storage, lipids, proteins"
                    ]
                },
                "4.4.2": {
                    "name": "Respiration",
                    "content": [
                        "Aerobic respiration: glucose + oxygen → carbon dioxide + water",
                        "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O",
                        "Anaerobic respiration in animals: glucose → lactic acid",
                        "Anaerobic respiration in plants/yeast: glucose → ethanol + carbon dioxide",
                        "Anaerobic releases less energy per glucose molecule than aerobic"
                    ]
                }
            }
        },
        "4.5": {
            "name": "Homeostasis and Response",
            "subtopics": {
                "4.5.1": {
                    "name": "Homeostasis",
                    "content": [
                        "Homeostasis maintains a constant internal environment",
                        "Conditions controlled: body temperature, blood glucose, water levels",
                        "Negative feedback reverses changes to return to set point",
                        "Involves receptors, coordination centre, and effectors"
                    ]
                },
                "4.5.2": {
                    "name": "The Nervous System",
                    "content": [
                        "Stimulus → Receptor → Sensory neurone → CNS → Motor neurone → Effector → Response",
                        "Reflex arc provides fast, automatic responses",
                        "Synapses transmit signals using neurotransmitters",
                        "Reaction time can be measured and affected by caffeine, tiredness, etc."
                    ]
                },
                "4.5.3": {
                    "name": "Hormonal Coordination",
                    "content": [
                        "Hormones are chemical messengers carried in blood",
                        "Insulin lowers blood glucose; glucagon raises blood glucose",
                        "Type 1 diabetes: pancreas fails to produce insulin",
                        "Type 2 diabetes: body cells no longer respond to insulin",
                        "Adrenaline prepares body for fight or flight"
                    ]
                }
            }
        },
        "4.6": {
            "name": "Inheritance, Variation and Evolution",
            "subtopics": {
                "4.6.1": {
                    "name": "Reproduction",
                    "content": [
                        "Sexual reproduction involves fusion of gametes (genetic variation)",
                        "Asexual reproduction produces genetically identical offspring (clones)",
                        "Meiosis produces gametes with half the chromosome number (haploid)",
                        "Meiosis introduces genetic variation through crossing over and random assortment"
                    ]
                },
                "4.6.2": {
                    "name": "DNA and Genetics",
                    "content": [
                        "DNA is a polymer made of nucleotides",
                        "Genes are sections of DNA that code for proteins",
                        "The genome is the entire genetic material of an organism",
                        "Alleles are different versions of the same gene",
                        "Dominant alleles are expressed when present; recessive only when homozygous"
                    ]
                },
                "4.6.3": {
                    "name": "Evolution",
                    "content": [
                        "Natural selection: variation → competition → survival of the fittest → reproduction",
                        "Darwin's theory explains how species evolve over time",
                        "Fossils provide evidence for evolution",
                        "Antibiotic resistance in bacteria is an example of natural selection"
                    ]
                }
            }
        },
        "4.7": {
            "name": "Ecology",
            "subtopics": {
                "4.7.1": {
                    "name": "Communities",
                    "content": [
                        "Ecosystem = community + habitat (living and non-living)",
                        "Abiotic factors: light, temperature, water, CO₂, O₂, pH, wind",
                        "Biotic factors: food, predators, competition, disease",
                        "Organisms compete for resources: food, water, space, mates"
                    ]
                },
                "4.7.2": {
                    "name": "Cycling Materials",
                    "content": [
                        "Carbon cycle: photosynthesis, respiration, combustion, decomposition",
                        "Water cycle: evaporation, transpiration, condensation, precipitation",
                        "Decomposers break down dead material, returning nutrients to soil"
                    ]
                },
                "4.7.3": {
                    "name": "Biodiversity",
                    "content": [
                        "Biodiversity is the variety of living organisms in an ecosystem",
                        "Human activities reducing biodiversity: deforestation, pollution, climate change",
                        "Conservation programs protect endangered species",
                        "Global warming caused by greenhouse gases: CO₂, methane"
                    ]
                }
            }
        }
    }
}

# =============================================================================
# REQUIRED PRACTICALS - BIOLOGY
# =============================================================================
BIOLOGY_PRACTICALS = [
    {
        "id": "BP1",
        "name": "Microscopy",
        "description": "Use light microscope to observe plant and animal cells",
        "topics": ["4.1.1"],
        "skills": ["Prepare slides", "Focus microscope", "Calculate magnification", "Draw scientific diagrams"]
    },
    {
        "id": "BP2",
        "name": "Osmosis Investigation",
        "description": "Investigate effect of salt/sugar solutions on plant tissue mass",
        "topics": ["4.1.3"],
        "skills": ["Control variables", "Measure mass", "Calculate percentage change", "Plot graphs"]
    },
    {
        "id": "BP3",
        "name": "Food Tests",
        "description": "Use qualitative reagents to test for carbohydrates, lipids, proteins",
        "topics": ["4.2.2"],
        "skills": ["Benedict's test (sugars)", "Iodine test (starch)", "Biuret test (proteins)", "Emulsion test (lipids)"]
    },
    {
        "id": "BP4",
        "name": "Enzyme Investigation",
        "description": "Investigate effect of pH on amylase reaction rate",
        "topics": ["4.2.2"],
        "skills": ["Use iodine to test for starch breakdown", "Time reactions", "Control temperature", "Use buffer solutions"]
    },
    {
        "id": "BP5",
        "name": "Photosynthesis Rate",
        "description": "Investigate effect of light intensity on rate of photosynthesis using pondweed",
        "topics": ["4.4.1"],
        "skills": ["Count bubbles", "Measure light intensity", "Use inverse square law", "Control variables"]
    },
    {
        "id": "BP6",
        "name": "Reaction Time",
        "description": "Investigate effect of a factor on human reaction time",
        "topics": ["4.5.2"],
        "skills": ["Ruler drop test", "Control variables", "Calculate means", "Evaluate reliability"]
    },
    {
        "id": "BP7",
        "name": "Field Investigation",
        "description": "Measure population size of a common species using sampling",
        "topics": ["4.7.1"],
        "skills": ["Random sampling", "Use quadrats", "Calculate mean", "Estimate population size"]
    }
]

# =============================================================================
# AQA GCSE CHEMISTRY (8462)
# =============================================================================
CHEMISTRY_SPEC = {
    "code": "8462",
    "name": "AQA GCSE Chemistry",
    "topics": {
        "4.1": {
            "name": "Atomic Structure and the Periodic Table",
            "subtopics": {
                "4.1.1": {
                    "name": "A Simple Model of the Atom",
                    "content": [
                        "Atoms contain protons (+1), neutrons (0), electrons (-1)",
                        "Protons and neutrons are in the nucleus; electrons orbit in shells",
                        "Atomic number = number of protons; Mass number = protons + neutrons",
                        "Isotopes have the same number of protons but different neutrons",
                        "Atoms have no overall charge (equal protons and electrons)"
                    ]
                },
                "4.1.2": {
                    "name": "The Periodic Table",
                    "content": [
                        "Elements arranged in order of atomic number",
                        "Groups are vertical columns (same number of outer electrons)",
                        "Periods are horizontal rows (same number of electron shells)",
                        "Mendeleev left gaps for undiscovered elements",
                        "Noble gases (Group 0) have full outer shells and are unreactive"
                    ]
                },
                "4.1.3": {
                    "name": "Group 1 - Alkali Metals",
                    "content": [
                        "Li, Na, K, Rb, Cs, Fr - reactivity increases down the group",
                        "Soft metals, low density, low melting points",
                        "React with water: metal + water → metal hydroxide + hydrogen",
                        "React with oxygen: metal + oxygen → metal oxide",
                        "Store under oil to prevent reaction with air/water"
                    ]
                },
                "4.1.4": {
                    "name": "Group 7 - Halogens",
                    "content": [
                        "F, Cl, Br, I, At - reactivity decreases down the group",
                        "Diatomic molecules (F₂, Cl₂, Br₂, I₂)",
                        "More reactive halogen displaces less reactive halogen from solution",
                        "Form ionic compounds with metals (e.g., NaCl)",
                        "Melting/boiling points increase down the group"
                    ]
                }
            }
        },
        "4.2": {
            "name": "Bonding, Structure and Properties of Matter",
            "subtopics": {
                "4.2.1": {
                    "name": "Chemical Bonds",
                    "content": [
                        "Ionic bonding: metal + non-metal; electrons transferred",
                        "Covalent bonding: non-metal + non-metal; electrons shared",
                        "Metallic bonding: positive ions in sea of delocalised electrons",
                        "Ions have charges: metals lose electrons (positive), non-metals gain (negative)"
                    ]
                },
                "4.2.2": {
                    "name": "Properties of Substances",
                    "content": [
                        "Ionic compounds: high melting points, conduct when molten/dissolved",
                        "Simple covalent: low melting points, don't conduct electricity",
                        "Giant covalent (diamond, graphite, silicon dioxide): very high melting points",
                        "Metals: good conductors, malleable, ductile",
                        "Graphite conducts electricity (delocalised electrons between layers)"
                    ]
                },
                "4.2.3": {
                    "name": "States of Matter",
                    "content": [
                        "Solid → Liquid → Gas as energy increases",
                        "Melting: solid to liquid; Boiling: liquid to gas",
                        "Particles have more energy and move faster as temperature increases",
                        "State changes are physical changes (reversible)"
                    ]
                }
            }
        },
        "4.3": {
            "name": "Quantitative Chemistry",
            "subtopics": {
                "4.3.1": {
                    "name": "Conservation of Mass",
                    "content": [
                        "Mass is conserved in chemical reactions",
                        "If gas escapes, apparent mass decreases",
                        "If gas is absorbed, apparent mass increases",
                        "Balanced equations have equal atoms on each side"
                    ]
                },
                "4.3.2": {
                    "name": "Amount of Substance",
                    "content": [
                        "Relative formula mass (Mr) = sum of relative atomic masses",
                        "One mole contains 6.02 × 10²³ particles (Avogadro's constant)",
                        "Moles = mass ÷ Mr",
                        "Mass = moles × Mr",
                        "Concentration (g/dm³) = mass ÷ volume"
                    ]
                }
            }
        },
        "4.4": {
            "name": "Chemical Changes",
            "subtopics": {
                "4.4.1": {
                    "name": "Reactivity of Metals",
                    "content": [
                        "Reactivity series: K, Na, Ca, Mg, Al, C, Zn, Fe, H, Cu, Ag, Au",
                        "More reactive metal displaces less reactive metal from solution",
                        "Oxidation is loss of electrons (OIL)",
                        "Reduction is gain of electrons (RIG)",
                        "Metals above carbon extracted by electrolysis; below carbon by reduction"
                    ]
                },
                "4.4.2": {
                    "name": "Reactions of Acids",
                    "content": [
                        "Acid + metal → salt + hydrogen",
                        "Acid + metal oxide → salt + water",
                        "Acid + metal hydroxide → salt + water",
                        "Acid + metal carbonate → salt + water + carbon dioxide",
                        "Neutralisation: H⁺ + OH⁻ → H₂O"
                    ]
                },
                "4.4.3": {
                    "name": "Electrolysis",
                    "content": [
                        "Electrolysis breaks down ionic compounds using electricity",
                        "Cations (positive) go to cathode (negative electrode)",
                        "Anions (negative) go to anode (positive electrode)",
                        "In aqueous solutions, hydrogen or metal forms at cathode",
                        "In aqueous solutions, oxygen or halogen forms at anode"
                    ]
                }
            }
        },
        "4.5": {
            "name": "Energy Changes",
            "subtopics": {
                "4.5.1": {
                    "name": "Exothermic and Endothermic Reactions",
                    "content": [
                        "Exothermic reactions release energy (temperature increases)",
                        "Endothermic reactions absorb energy (temperature decreases)",
                        "Exothermic: combustion, neutralisation, oxidation",
                        "Endothermic: thermal decomposition, photosynthesis",
                        "Bond breaking is endothermic; bond making is exothermic"
                    ]
                },
                "4.5.2": {
                    "name": "Bond Energy Calculations",
                    "content": [
                        "Energy change = energy to break bonds - energy released making bonds",
                        "If breaking > making: endothermic (positive ΔH)",
                        "If making > breaking: exothermic (negative ΔH)",
                        "Activation energy is minimum energy needed to start reaction"
                    ]
                }
            }
        },
        "4.6": {
            "name": "Rate and Extent of Chemical Change",
            "subtopics": {
                "4.6.1": {
                    "name": "Rate of Reaction",
                    "content": [
                        "Rate affected by: temperature, concentration, surface area, catalysts",
                        "Collision theory: particles must collide with enough energy",
                        "Increasing temperature increases collision frequency and energy",
                        "Catalysts provide alternative pathway with lower activation energy",
                        "Rate = amount of product formed ÷ time"
                    ]
                },
                "4.6.2": {
                    "name": "Reversible Reactions",
                    "content": [
                        "Reversible reactions shown with ⇌ symbol",
                        "Equilibrium reached when forward and reverse rates are equal",
                        "Changing conditions shifts equilibrium position",
                        "Le Chatelier's principle: system opposes change"
                    ]
                }
            }
        },
        "4.7": {
            "name": "Organic Chemistry",
            "subtopics": {
                "4.7.1": {
                    "name": "Carbon Compounds as Fuels",
                    "content": [
                        "Crude oil is a mixture of hydrocarbons",
                        "Fractional distillation separates by boiling point",
                        "Shorter chains: lower boiling point, more flammable, less viscous",
                        "Alkanes are saturated hydrocarbons: CₙH₂ₙ₊₂",
                        "Complete combustion: hydrocarbon + O₂ → CO₂ + H₂O"
                    ]
                },
                "4.7.2": {
                    "name": "Reactions of Hydrocarbons",
                    "content": [
                        "Cracking breaks long chain hydrocarbons into shorter useful molecules",
                        "Cracking produces alkenes (unsaturated, C=C double bond)",
                        "Alkenes: CₙH₂ₙ - react with bromine water (orange to colourless)",
                        "Incomplete combustion produces carbon monoxide (toxic) and carbon (soot)"
                    ]
                }
            }
        },
        "4.8": {
            "name": "Chemical Analysis",
            "subtopics": {
                "4.8.1": {
                    "name": "Purity and Formulations",
                    "content": [
                        "Pure substance has sharp melting/boiling point",
                        "Formulations are mixtures with precise quantities: medicines, paints, foods",
                        "Chromatography separates mixtures; Rf = distance moved by substance ÷ distance moved by solvent"
                    ]
                },
                "4.8.2": {
                    "name": "Identification of Gases",
                    "content": [
                        "Hydrogen: squeaky pop with burning splint",
                        "Oxygen: relights glowing splint",
                        "Carbon dioxide: turns limewater milky (cloudy)",
                        "Chlorine: bleaches damp litmus paper white"
                    ]
                }
            }
        },
        "4.9": {
            "name": "Chemistry of the Atmosphere",
            "subtopics": {
                "4.9.1": {
                    "name": "Composition of the Atmosphere",
                    "content": [
                        "Today's atmosphere: 78% nitrogen, 21% oxygen, 1% argon, 0.04% CO₂",
                        "Early atmosphere: mainly CO₂ and water vapour (from volcanoes)",
                        "Oxygen produced by photosynthesis from early plants/algae",
                        "CO₂ reduced by: dissolving in oceans, photosynthesis, forming fossil fuels/carbonates"
                    ]
                },
                "4.9.2": {
                    "name": "Climate Change",
                    "content": [
                        "Greenhouse gases: CO₂, methane, water vapour",
                        "Greenhouse effect: gases absorb and re-emit infrared radiation",
                        "Human activities increasing CO₂: burning fossil fuels, deforestation",
                        "Effects: rising sea levels, extreme weather, ecosystem changes"
                    ]
                }
            }
        },
        "4.10": {
            "name": "Using Resources",
            "subtopics": {
                "4.10.1": {
                    "name": "Sustainable Development",
                    "content": [
                        "Finite resources will run out; renewable resources can be replaced",
                        "Potable water is safe to drink (not pure)",
                        "UK: rainwater collected, filtered, chlorinated",
                        "Desalination of seawater: distillation or reverse osmosis (energy intensive)"
                    ]
                },
                "4.10.2": {
                    "name": "Life Cycle Assessment",
                    "content": [
                        "LCA assesses environmental impact: extraction, manufacturing, use, disposal",
                        "Reduce, Reuse, Recycle to minimise waste",
                        "Recycling metals saves energy and finite resources",
                        "Some plastics can be recycled or used as fuel"
                    ]
                }
            }
        }
    }
}

# =============================================================================
# REQUIRED PRACTICALS - CHEMISTRY
# =============================================================================
CHEMISTRY_PRACTICALS = [
    {
        "id": "CP1",
        "name": "Making Salts",
        "description": "Preparation of pure, dry soluble salt from insoluble oxide/carbonate",
        "topics": ["4.4.2"],
        "skills": ["Add excess reactant", "Filter", "Evaporate", "Crystallise"]
    },
    {
        "id": "CP2",
        "name": "Titration",
        "description": "Determine reacting volumes of strong acid and alkali",
        "topics": ["4.4.2", "4.3.2"],
        "skills": ["Use burette", "Identify end point", "Calculate concentration", "Repeat for concordant results"]
    },
    {
        "id": "CP3",
        "name": "Electrolysis",
        "description": "Investigate electrolysis of aqueous solutions using inert electrodes",
        "topics": ["4.4.3"],
        "skills": ["Set up electrolysis cell", "Identify products", "Test gases", "Write half equations"]
    },
    {
        "id": "CP4",
        "name": "Temperature Changes",
        "description": "Investigate variables affecting temperature change in reacting solutions",
        "topics": ["4.5.1"],
        "skills": ["Measure temperature change", "Insulate container", "Control variables", "Calculate energy change"]
    },
    {
        "id": "CP5",
        "name": "Rates of Reaction",
        "description": "Investigate how concentration affects rate (gas collection or disappearing cross)",
        "topics": ["4.6.1"],
        "skills": ["Collect gas in syringe", "Time reaction", "Plot rate graph", "Calculate rate"]
    },
    {
        "id": "CP6",
        "name": "Chromatography",
        "description": "Use paper chromatography to separate coloured substances",
        "topics": ["4.8.1"],
        "skills": ["Set up chromatogram", "Calculate Rf values", "Identify unknown", "Use locating agents"]
    },
    {
        "id": "CP7",
        "name": "Water Purification",
        "description": "Analysis and purification of water samples",
        "topics": ["4.10.1"],
        "skills": ["Test pH", "Measure dissolved solids", "Distil water", "Evaluate purity"]
    }
]

# =============================================================================
# AQA GCSE PHYSICS (8463)
# =============================================================================
PHYSICS_SPEC = {
    "code": "8463",
    "name": "AQA GCSE Physics",
    "topics": {
        "4.1": {
            "name": "Energy",
            "subtopics": {
                "4.1.1": {
                    "name": "Energy Stores and Systems",
                    "content": [
                        "Energy stores: kinetic, gravitational potential, elastic, thermal, chemical, nuclear, magnetic",
                        "Energy can be transferred between stores",
                        "Work done = force × distance (W = Fd)",
                        "Power = energy transferred ÷ time (P = E/t)",
                        "Power is measured in watts (W); 1W = 1 J/s"
                    ]
                },
                "4.1.2": {
                    "name": "Conservation of Energy",
                    "content": [
                        "Energy cannot be created or destroyed, only transferred",
                        "Kinetic energy: KE = ½mv²",
                        "Gravitational potential energy: GPE = mgh",
                        "Elastic potential energy: EPE = ½ke²",
                        "Specific heat capacity: E = mcΔT"
                    ]
                },
                "4.1.3": {
                    "name": "Efficiency",
                    "content": [
                        "Efficiency = useful output ÷ total input × 100%",
                        "Energy is often dissipated as heat to surroundings",
                        "Ways to reduce unwanted energy transfer: lubrication, insulation",
                        "No machine is 100% efficient (energy always dissipated)"
                    ]
                }
            }
        },
        "4.2": {
            "name": "Electricity",
            "subtopics": {
                "4.2.1": {
                    "name": "Current, Potential Difference and Resistance",
                    "content": [
                        "Current (I) = charge (Q) ÷ time (t); measured in amperes (A)",
                        "Potential difference (V) = energy ÷ charge; measured in volts (V)",
                        "Resistance (R) = V ÷ I; measured in ohms (Ω)",
                        "Ohm's Law: V = IR (at constant temperature)",
                        "Current is flow of charge; conventional current flows positive to negative"
                    ]
                },
                "4.2.2": {
                    "name": "Series and Parallel Circuits",
                    "content": [
                        "Series: same current throughout; voltages add up",
                        "Series: total resistance = R₁ + R₂ + R₃",
                        "Parallel: same voltage across each branch; currents add up",
                        "Parallel: 1/R_total = 1/R₁ + 1/R₂ + 1/R₃",
                        "Ammeters in series; voltmeters in parallel"
                    ]
                },
                "4.2.3": {
                    "name": "Domestic Uses of Electricity",
                    "content": [
                        "UK mains: 230V, 50Hz AC",
                        "Live wire (brown): carries current at 230V",
                        "Neutral wire (blue): completes circuit, 0V",
                        "Earth wire (green/yellow): safety wire, 0V",
                        "Power = current × voltage (P = IV); Energy = power × time (E = Pt)"
                    ]
                },
                "4.2.4": {
                    "name": "National Grid",
                    "content": [
                        "National Grid distributes electricity from power stations to homes",
                        "Step-up transformers increase voltage for transmission",
                        "High voltage reduces current, reducing energy loss in cables (P = I²R)",
                        "Step-down transformers reduce voltage for domestic use"
                    ]
                }
            }
        },
        "4.3": {
            "name": "Particle Model of Matter",
            "subtopics": {
                "4.3.1": {
                    "name": "Density",
                    "content": [
                        "Density = mass ÷ volume (ρ = m/V)",
                        "Units: kg/m³ or g/cm³",
                        "Solids: particles close, regular pattern, vibrate in place",
                        "Liquids: particles close, irregular, can flow",
                        "Gases: particles far apart, random motion, fill container"
                    ]
                },
                "4.3.2": {
                    "name": "Internal Energy and State Changes",
                    "content": [
                        "Internal energy = kinetic + potential energy of particles",
                        "Temperature change: kinetic energy changes",
                        "State change: potential energy changes (bonds break/form)",
                        "Specific latent heat: E = mL",
                        "Latent heat of fusion (melting); latent heat of vaporisation (boiling)"
                    ]
                }
            }
        },
        "4.4": {
            "name": "Atomic Structure",
            "subtopics": {
                "4.4.1": {
                    "name": "Atoms and Isotopes",
                    "content": [
                        "Atoms: protons and neutrons in nucleus, electrons in shells",
                        "Radius of atom ≈ 10⁻¹⁰ m; radius of nucleus ≈ 10⁻¹⁴ m",
                        "Rutherford's alpha scattering: discovered small, positive nucleus",
                        "Isotopes have same protons, different neutrons",
                        "Ions form when atoms gain or lose electrons"
                    ]
                },
                "4.4.2": {
                    "name": "Radioactive Decay",
                    "content": [
                        "Radioactive decay is random and spontaneous",
                        "Alpha (α): 2 protons + 2 neutrons, stopped by paper",
                        "Beta (β): high-speed electron, stopped by aluminium",
                        "Gamma (γ): electromagnetic radiation, reduced by lead/concrete",
                        "Half-life: time for activity or number of nuclei to halve"
                    ]
                },
                "4.4.3": {
                    "name": "Hazards of Radiation",
                    "content": [
                        "Contamination: radioactive material on/in body",
                        "Irradiation: exposure to radiation from outside",
                        "Alpha most dangerous inside body; gamma most dangerous outside",
                        "Uses: medical tracers, cancer treatment, smoke detectors"
                    ]
                }
            }
        },
        "4.5": {
            "name": "Forces",
            "subtopics": {
                "4.5.1": {
                    "name": "Forces and Motion",
                    "content": [
                        "Scalar: magnitude only (speed, mass, energy, distance)",
                        "Vector: magnitude and direction (force, velocity, acceleration, displacement)",
                        "Contact forces: friction, air resistance, tension, normal force",
                        "Non-contact forces: gravity, electrostatic, magnetic"
                    ]
                },
                "4.5.2": {
                    "name": "Speed and Velocity",
                    "content": [
                        "Speed = distance ÷ time (s = d/t)",
                        "Velocity includes direction (vector)",
                        "Typical speeds: walking 1.5 m/s, cycling 6 m/s, car 25 m/s",
                        "Distance-time graph: gradient = speed"
                    ]
                },
                "4.5.3": {
                    "name": "Acceleration",
                    "content": [
                        "Acceleration = change in velocity ÷ time (a = Δv/t)",
                        "Measured in m/s²",
                        "v² = u² + 2as (no time)",
                        "Velocity-time graph: gradient = acceleration, area = distance"
                    ]
                },
                "4.5.4": {
                    "name": "Newton's Laws",
                    "content": [
                        "1st Law: object at rest stays at rest unless acted on by resultant force",
                        "2nd Law: F = ma (force = mass × acceleration)",
                        "3rd Law: every action has an equal and opposite reaction",
                        "Resultant force = 0: constant velocity or stationary"
                    ]
                },
                "4.5.5": {
                    "name": "Terminal Velocity and Braking",
                    "content": [
                        "Terminal velocity: weight = drag force, acceleration = 0",
                        "Stopping distance = thinking distance + braking distance",
                        "Factors affecting thinking: tiredness, drugs, speed",
                        "Factors affecting braking: road conditions, tyre condition, brake condition, speed"
                    ]
                }
            }
        },
        "4.6": {
            "name": "Waves",
            "subtopics": {
                "4.6.1": {
                    "name": "Wave Properties",
                    "content": [
                        "Transverse: oscillations perpendicular to direction (light, water, S-waves)",
                        "Longitudinal: oscillations parallel to direction (sound, P-waves)",
                        "Wave speed = frequency × wavelength (v = fλ)",
                        "Period = 1 ÷ frequency (T = 1/f)",
                        "Amplitude: maximum displacement from rest position"
                    ]
                },
                "4.6.2": {
                    "name": "Electromagnetic Spectrum",
                    "content": [
                        "Radio, Microwave, Infrared, Visible, Ultraviolet, X-ray, Gamma",
                        "All travel at speed of light in vacuum (3 × 10⁸ m/s)",
                        "Frequency increases left to right; wavelength decreases",
                        "Higher frequency = higher energy = more dangerous",
                        "Uses: radio (communication), IR (heating), UV (sun beds), X-rays (medical)"
                    ]
                }
            }
        },
        "4.7": {
            "name": "Magnetism and Electromagnetism",
            "subtopics": {
                "4.7.1": {
                    "name": "Magnetic Fields",
                    "content": [
                        "Magnets have north and south poles",
                        "Like poles repel; unlike poles attract",
                        "Magnetic field lines go from north to south",
                        "Earth has a magnetic field (compass points north)",
                        "Current-carrying wire produces a magnetic field"
                    ]
                },
                "4.7.2": {
                    "name": "Electromagnets",
                    "content": [
                        "Electromagnet: coil of wire wrapped around iron core",
                        "Strength increased by: more turns, more current, iron core",
                        "Can be turned on/off (unlike permanent magnets)",
                        "Uses: scrapyard cranes, circuit breakers, electric bells"
                    ]
                },
                "4.7.3": {
                    "name": "Motor Effect",
                    "content": [
                        "Current-carrying conductor in magnetic field experiences force",
                        "Force = magnetic flux density × current × length (F = BIL)",
                        "Fleming's Left Hand Rule: thumb=motion, first finger=field, second finger=current",
                        "Electric motors use this effect"
                    ]
                }
            }
        },
        "4.8": {
            "name": "Space Physics (Physics Only)",
            "subtopics": {
                "4.8.1": {
                    "name": "Solar System",
                    "content": [
                        "Solar system: Sun + 8 planets + dwarf planets + moons + asteroids",
                        "Planets orbit Sun due to gravity",
                        "Moons orbit planets; artificial satellites orbit Earth",
                        "Light year: distance light travels in one year"
                    ]
                },
                "4.8.2": {
                    "name": "Life Cycle of Stars",
                    "content": [
                        "Nebula → Protostar → Main sequence → Red giant → White dwarf",
                        "Massive stars: Red supergiant → Supernova → Neutron star or Black hole",
                        "Fusion: hydrogen → helium (in main sequence)",
                        "Heavier elements formed in supernovae"
                    ]
                }
            }
        }
    }
}

# =============================================================================
# REQUIRED PRACTICALS - PHYSICS
# =============================================================================
PHYSICS_PRACTICALS = [
    {
        "id": "PP1",
        "name": "Specific Heat Capacity",
        "description": "Determine specific heat capacity of materials",
        "topics": ["4.1.2"],
        "skills": ["Use immersion heater", "Measure temperature change", "Calculate SHC", "Evaluate accuracy"]
    },
    {
        "id": "PP2",
        "name": "Resistance Investigation",
        "description": "Investigate factors affecting resistance of wire (length, area)",
        "topics": ["4.2.1"],
        "skills": ["Set up circuit", "Vary length", "Measure V and I", "Calculate resistance"]
    },
    {
        "id": "PP3",
        "name": "I-V Characteristics",
        "description": "Investigate I-V characteristics of filament lamp, diode, resistor",
        "topics": ["4.2.1"],
        "skills": ["Use variable resistor", "Plot I-V graph", "Interpret graphs", "Identify components"]
    },
    {
        "id": "PP4",
        "name": "Density",
        "description": "Determine density of regular and irregular solids and liquids",
        "topics": ["4.3.1"],
        "skills": ["Measure mass", "Calculate volume", "Use displacement", "Calculate density"]
    },
    {
        "id": "PP5",
        "name": "Force and Extension",
        "description": "Investigate relationship between force and extension of a spring",
        "topics": ["4.5"],
        "skills": ["Measure extension", "Plot force-extension graph", "Calculate spring constant", "Identify limit of proportionality"]
    },
    {
        "id": "PP6",
        "name": "Acceleration",
        "description": "Investigate effect of force and mass on acceleration",
        "topics": ["4.5.3", "4.5.4"],
        "skills": ["Use trolley and ramp", "Light gates", "Calculate acceleration", "Verify F=ma"]
    },
    {
        "id": "PP7",
        "name": "Waves in Ripple Tank",
        "description": "Measure frequency, wavelength, and speed of waves",
        "topics": ["4.6.1"],
        "skills": ["Use stroboscope", "Measure wavelength", "Calculate wave speed", "Observe reflection/refraction"]
    },
    {
        "id": "PP8",
        "name": "Radiation",
        "description": "Investigate absorption and emission of infrared radiation",
        "topics": ["4.6.2"],
        "skills": ["Leslie cube", "Measure temperature loss", "Compare surfaces", "Evaluate insulation"]
    }
]


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================
def get_curriculum(subject: str) -> dict:
    """Get the curriculum data for a subject."""
    curricula = {
        "Biology": BIOLOGY_SPEC,
        "Chemistry": CHEMISTRY_SPEC,
        "Physics": PHYSICS_SPEC
    }
    return curricula.get(subject, {})


def get_practicals(subject: str) -> list:
    """Get required practicals for a subject."""
    practicals = {
        "Biology": BIOLOGY_PRACTICALS,
        "Chemistry": CHEMISTRY_PRACTICALS,
        "Physics": PHYSICS_PRACTICALS
    }
    return practicals.get(subject, [])


def get_topic_content(subject: str, topic_id: str, subtopic_id: str) -> list:
    """Get content points for a specific subtopic."""
    curriculum = get_curriculum(subject)
    if not curriculum:
        return []
    
    topic = curriculum.get("topics", {}).get(topic_id, {})
    subtopic = topic.get("subtopics", {}).get(subtopic_id, {})
    return subtopic.get("content", [])


def get_all_topics(subject: str) -> dict:
    """Get all topics for a subject."""
    curriculum = get_curriculum(subject)
    return curriculum.get("topics", {})


def get_related_practicals(subject: str, topic_id: str) -> list:
    """Get practicals related to a topic."""
    practicals = get_practicals(subject)
    related = []
    for p in practicals:
        if topic_id in p.get("topics", []) or any(t.startswith(topic_id) for t in p.get("topics", [])):
            related.append(p)
    return related
