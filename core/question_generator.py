"""
Tiered Question Generator
Generates questions aligned to TLAG methodology based on curriculum content.
"""
from typing import List, Dict
import random


class TieredQuestionGenerator:
    """Generates tiered questions based on curriculum To Know statements."""
    
    # Question templates by tier
    TIER1_TEMPLATES = [
        "Define {term}.",
        "State {concept}.",
        "What is {term}?",
        "Name {item}.",
        "Give the meaning of {term}.",
        "What does {term} mean?",
        "List {items}.",
        "Identify {item}.",
        "Which {question}?",
        "True or false: {statement}."
    ]
    
    TIER2_TEMPLATES = [
        "Explain why {phenomenon}.",
        "Describe how {process}.",
        "Calculate {quantity} if {given}.",
        "Compare {item1} and {item2}.",
        "What would happen if {scenario}?",
        "Using the equation {equation}, calculate {variable}.",
        "Suggest a reason for {observation}.",
        "Draw and label {diagram}.",
        "Complete the word equation: {equation}.",
        "Use the data to {task}."
    ]
    
    TIER3_TEMPLATES = [
        "Evaluate the advantages and disadvantages of {topic}.",
        "Explain how {concept1} is related to {concept2}.",
        "A student claims that {claim}. Discuss whether this is correct.",
        "Analyse the data and suggest conclusions about {topic}.",
        "Design an experiment to test {hypothesis}.",
        "Predict what would happen if {scenario} and explain your reasoning.",
        "Compare and contrast {item1} with {item2}, using examples.",
        "Justify the statement: {statement}.",
        "Explain the importance of {topic} in {context}."
    ]
    
    def __init__(self, content_points: List[str], topic_name: str = ""):
        """Initialize with content points from curriculum."""
        self.content_points = content_points
        self.topic_name = topic_name
    
    def generate_tier1_questions(self, count: int = 5) -> List[Dict]:
        """
        Generate Tier 1 (Do Now/Retrieval) questions.
        Focus on recall of facts and definitions.
        """
        questions = []
        
        for i, content in enumerate(self.content_points[:count]):
            # Create recall questions from content points
            question = self._create_recall_question(content, i)
            questions.append({
                "tier": 1,
                "question": question["question"],
                "answer": question["answer"],
                "type": "recall"
            })
        
        # Pad with additional questions if needed
        while len(questions) < count and self.content_points:
            extra = self._create_definition_question(random.choice(self.content_points))
            if extra not in [q["question"] for q in questions]:
                questions.append({
                    "tier": 1,
                    "question": extra["question"],
                    "answer": extra["answer"],
                    "type": "definition"
                })
        
        return questions[:count]
    
    def generate_tier2_questions(self, count: int = 3) -> List[Dict]:
        """
        Generate Tier 2 (Application/We Do) questions.
        Require application of knowledge or calculations.
        """
        questions = []
        
        for i, content in enumerate(self.content_points[:count]):
            question = self._create_application_question(content, i)
            questions.append({
                "tier": 2,
                "question": question["question"],
                "answer": question["answer"],
                "steps": question.get("steps", []),
                "type": "application"
            })
        
        return questions[:count]
    
    def generate_tier3_questions(self, count: int = 2) -> List[Dict]:
        """
        Generate Tier 3 (Exit Ticket/Deep Thinking) questions.
        Extended response linking multiple concepts.
        """
        questions = []
        
        # Link multiple content points for deeper thinking
        if len(self.content_points) >= 2:
            question = self._create_extended_question(
                self.content_points[0],
                self.content_points[1] if len(self.content_points) > 1 else self.content_points[0]
            )
            questions.append({
                "tier": 3,
                "question": question["question"],
                "answer": question["answer"],
                "marks": 6,
                "type": "extended"
            })
        
        return questions[:count]
    
    def generate_all_tiers(self) -> Dict[str, List[Dict]]:
        """Generate questions for all three tiers."""
        return {
            "tier1_do_now": self.generate_tier1_questions(5),
            "tier2_we_do": self.generate_tier2_questions(3),
            "tier3_exit": self.generate_tier3_questions(2)
        }
    
    def _create_recall_question(self, content: str, index: int) -> Dict:
        """Create a recall question from content."""
        # Extract key term if present
        if ":" in content:
            term, definition = content.split(":", 1)
            return {
                "question": f"What is {term.strip().lower()}?",
                "answer": definition.strip()
            }
        elif "=" in content:
            parts = content.split("=")
            return {
                "question": f"What is the formula for {parts[0].strip()}?",
                "answer": content
            }
        else:
            # Create a fill-in-blank style question
            words = content.split()
            if len(words) > 5:
                key_word = words[len(words)//2]
                blank_content = content.replace(key_word, "_______")
                return {
                    "question": f"Complete the statement: {blank_content}",
                    "answer": key_word
                }
            return {
                "question": f"State one fact about {self.topic_name}.",
                "answer": content
            }
    
    def _create_definition_question(self, content: str) -> Dict:
        """Create a definition-style question."""
        # Find key scientific terms
        terms = self._extract_key_terms(content)
        if terms:
            term = terms[0]
            return {
                "question": f"Define the term '{term}'.",
                "answer": f"{term}: {content}"
            }
        return {
            "question": f"Describe {self.topic_name.lower()}.",
            "answer": content
        }
    
    def _create_application_question(self, content: str, index: int) -> Dict:
        """Create an application question requiring deeper understanding."""
        # Look for processes or calculations
        if any(word in content.lower() for word in ["→", "=", "formula", "equation"]):
            return {
                "question": f"Using your knowledge of {self.topic_name}, explain the process: {content}",
                "answer": f"Expected explanation covering: {content}",
                "steps": ["Identify key components", "Apply the concept", "Show working"]
            }
        
        return {
            "question": f"Explain why {content.lower().rstrip('.')}.",
            "answer": f"Model answer: {content}. Because...",
            "steps": ["State the fact", "Explain the reason", "Give an example if possible"]
        }
    
    def _create_extended_question(self, content1: str, content2: str) -> Dict:
        """Create an extended response question linking concepts."""
        return {
            "question": f"Explain how '{content1.split(':')[0] if ':' in content1 else content1[:50]}' is related to '{content2.split(':')[0] if ':' in content2 else content2[:50]}'. Use examples in your answer. [6 marks]",
            "answer": f"Level 3 (5-6 marks): Clear explanation linking both concepts with relevant examples.\n- Point 1: {content1}\n- Point 2: {content2}\n- Connection explained with scientific terminology"
        }
    
    def _extract_key_terms(self, content: str) -> List[str]:
        """Extract scientific key terms from content."""
        # Common scientific terms to look for
        science_words = [
            "osmosis", "diffusion", "respiration", "photosynthesis", "mitosis", "meiosis",
            "ionic", "covalent", "metallic", "electrolysis", "neutralisation",
            "kinetic", "potential", "acceleration", "velocity", "force",
            "enzyme", "hormone", "gene", "allele", "chromosome",
            "exothermic", "endothermic", "catalyst", "equilibrium",
            "nucleus", "electron", "proton", "neutron", "isotope"
        ]
        
        found = []
        content_lower = content.lower()
        for term in science_words:
            if term in content_lower:
                found.append(term)
        
        return found


def generate_do_now_questions(content_points: List[str], topic: str = "", count: int = 5) -> List[Dict]:
    """Convenience function for Do Now questions."""
    generator = TieredQuestionGenerator(content_points, topic)
    return generator.generate_tier1_questions(count)


def generate_we_do_questions(content_points: List[str], topic: str = "", count: int = 3) -> List[Dict]:
    """Convenience function for We Do questions."""
    generator = TieredQuestionGenerator(content_points, topic)
    return generator.generate_tier2_questions(count)


def generate_exit_ticket(content_points: List[str], topic: str = "") -> Dict:
    """Convenience function for Exit Ticket."""
    generator = TieredQuestionGenerator(content_points, topic)
    questions = generator.generate_tier3_questions(1)
    if questions:
        return questions[0]
    return {
        "question": f"Explain one key concept from today's lesson on {topic}.",
        "answer": "Model answer based on learning objectives."
    }


def generate_complete_question_set(content_points: List[str], topic: str = "") -> Dict:
    """Generate a complete set of tiered questions for a lesson."""
    generator = TieredQuestionGenerator(content_points, topic)
    return generator.generate_all_tiers()
