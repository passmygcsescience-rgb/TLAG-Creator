"""
TLAG PowerPoint Builder
Generates GEMS TLAG lesson PowerPoints from structured content.
Now supports multiple slides per section for richer content.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os
from io import BytesIO

class TLAGPowerPointBuilder:
    """Builds TLAG-compliant PowerPoint presentations with rich content."""
    
    # Template layouts
    LAYOUTS = {
        "DO_NOW": 1,
        "OUTCOMES": 2,
        "I_DO": 4,
        "WE_DO": 5,
        "YOU_DO": 6,
        "CHECK": 7,
        "EXIT": 8
    }
    
    # Colors
    BLACK = RGBColor(0, 0, 0)
    RED = RGBColor(192, 0, 0)
    GREEN = RGBColor(0, 128, 0)
    BLUE = RGBColor(0, 112, 192)
    PURPLE = RGBColor(102, 45, 145)
    ORANGE = RGBColor(255, 102, 0)
    
    def __init__(self, template_path: str):
        """Initialize with template path."""
        self.template_path = template_path
        self.prs = None
        
    def create_presentation(self):
        """Create a new presentation from template."""
        self.prs = Presentation(self.template_path)
        # Clear existing slides
        while len(self.prs.slides) > 0:
            rId = self.prs.slides._sldIdLst[0].rId
            self.prs.part.drop_rel(rId)
            del self.prs.slides._sldIdLst[0]
        return self
    
    def _add_slide(self, layout_name: str):
        """Add a slide with the specified layout."""
        layout_idx = self.LAYOUTS.get(layout_name, 1)
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[layout_idx])
        self._remove_title(slide)
        return slide
    
    def _remove_title(self, slide):
        """Remove title placeholder."""
        try:
            title_ph = slide.placeholders[0]
            sp = title_ph._element
            sp.getparent().remove(sp)
        except:
            pass
    
    def _set_content(self, slide, idx: int, content: list, font_size: int = 24):
        """Set content in a placeholder."""
        try:
            ph = slide.placeholders[idx]
            ph.top = Inches(0.85)
            ph.left = Inches(0.3)
            ph.width = Inches(12.7)
            ph.height = Inches(6.3)
        except KeyError:
            return
        
        tf = ph.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        
        for item in content:
            text, bold, color = item
            if text.startswith("\n"):
                p = tf.add_paragraph()
                text = text[1:]
            run = p.add_run()
            run.text = text
            run.font.name = "Arial"
            run.font.size = Pt(font_size)
            run.font.bold = bold
            run.font.color.rgb = color if color else self.BLACK
    
    def add_do_now(self, questions: list, answers: list):
        """Add Do Now slide with retrieval questions."""
        slide = self._add_slide("DO_NOW")
        content = [("🕰️ DO NOW - Complete in silence (6 mins)", True, self.BLUE), ("\n", False, None)]
        
        for i, (q, a) in enumerate(zip(questions, answers), 1):
            content.append((f"\n{i}. {q}", False, None))
            content.append(("\n    → ", False, None))
            content.append((str(a), True, self.RED))
        
        self._set_content(slide, 1, content, 22)
        return self
    
    def add_outcomes(self, outcome: str, to_know: list):
        """Add Learning Outcomes slide (two-column)."""
        slide = self._add_slide("OUTCOMES")
        
        # Left column - Learning Outcome
        self._set_content(slide, 1, [("🎯 " + outcome, False, None)])
        
        # Right column - To Know
        content = [("🧠 To Know:", True, self.BLUE), ("\n", False, None)]
        for i, item in enumerate(to_know, 1):
            content.append((f"\n{i}. {item}", False, None))
        self._set_content(slide, 2, content)
        
        return self
    
    # =========================================================================
    # EXPANDED I DO - Multiple slides with detailed modelling
    # =========================================================================
    def add_i_do_slides(self, i_do_data: dict):
        """Add multiple I Do slides with comprehensive teacher modelling."""
        title = i_do_data.get("title", "Teacher Modelling")
        content = i_do_data.get("content", [])
        examples = i_do_data.get("examples", [])
        key_points = i_do_data.get("key_points", [])
        
        # Slide 1: I Do Overview
        slide = self._add_slide("I_DO")
        slide_content = [("👨‍🏫 I DO: " + title, True, self.PURPLE), ("\n", False, None)]
        slide_content.append(("\n📋 What we will learn:", True, None))
        
        for i, item in enumerate(content[:5], 1):
            slide_content.append((f"\n   {i}. {item}", False, None))
        
        if i_do_data.get("technique"):
            slide_content.append(("\n\n", False, None))
            slide_content.append(("⚡ Technique: ", True, None))
            slide_content.append((i_do_data.get("technique"), False, self.BLUE))
        
        self._set_content(slide, 1, slide_content, 22)
        
        # Slide 2: I Do Worked Example (if examples provided)
        if examples:
            slide2 = self._add_slide("I_DO")
            content2 = [("👨‍🏫 I DO: Worked Example", True, self.PURPLE), ("\n", False, None)]
            
            for i, example in enumerate(examples[:2], 1):
                content2.append((f"\n📝 Example {i}: {example.get('problem', '')}", True, None))
                
                steps = example.get('steps', [])
                for j, step in enumerate(steps, 1):
                    content2.append((f"\n   Step {j}: {step}", False, None))
                
                if example.get('answer'):
                    content2.append(("\n   ✓ Answer: ", False, None))
                    content2.append((str(example.get('answer')), True, self.GREEN))
                content2.append(("\n", False, None))
            
            self._set_content(slide2, 1, content2, 20)
        
        # Slide 3: I Do Key Points (if key_points provided)
        if key_points:
            slide3 = self._add_slide("I_DO")
            content3 = [("👨‍🏫 I DO: Key Points to Remember", True, self.PURPLE), ("\n", False, None)]
            
            for point in key_points:
                content3.append((f"\n✨ {point}", False, None))
            
            # Add image description if present
            if i_do_data.get("image_description"):
                content3.append(("\n\n", False, None))
                content3.append(("📷 " + i_do_data.get("image_description"), False, self.BLUE))
            else:
                content3.append(("\n\n🔔 Cold Call: Be ready to answer!", True, self.ORANGE))
            
            self._set_content(slide3, 1, content3, 20)
        
        return self
    
    def add_i_do(self, title: str, content_items: list):
        """Legacy single I Do slide (for backwards compatibility)."""
        # Convert to new format
        self.add_i_do_slides({
            "title": title,
            "content": content_items,
            "technique": "Cold Call to check listening"
        })
        return self
    
    # =========================================================================
    # EXPANDED WE DO - Multiple examples with step-by-step guidance
    # =========================================================================
    def add_we_do_slides(self, we_do_data: dict):
        """Add multiple We Do slides with guided examples."""
        examples = we_do_data.get("examples", [])
        
        # If no examples structure, create from legacy format
        if not examples and we_do_data.get("question"):
            examples = [{
                "question": we_do_data.get("question"),
                "steps": we_do_data.get("steps", []),
                "answer": we_do_data.get("answer", "")
            }]
        
        # Slide 1: We Do Overview
        slide = self._add_slide("WE_DO")
        content = [("👥 WE DO: Let's Practice Together", True, self.BLUE), ("\n", False, None)]
        content.append(("\n🗣️ Turn and Talk with your partner", True, self.ORANGE))
        content.append(("\n", False, None))
        
        # Show first example on overview slide
        if examples:
            ex = examples[0]
            content.append((f"\n📝 Q1: {ex.get('question', '')}", True, None))
            for i, step in enumerate(ex.get('steps', [])[:4], 1):
                content.append((f"\n   Step {i}: {step}", False, None))
            if ex.get('answer'):
                content.append(("\n   ✓ ", False, None))
                content.append((str(ex.get('answer')), True, self.GREEN))
        
        self._set_content(slide, 1, content, 20)
        
        # Additional slides for more examples
        for i, example in enumerate(examples[1:4], 2):  # Up to 3 more examples
            slide_n = self._add_slide("WE_DO")
            content_n = [(f"👥 WE DO: Example {i}", True, self.BLUE), ("\n", False, None)]
            content_n.append(("\n🗣️ Discuss with your partner", True, self.ORANGE))
            
            content_n.append((f"\n\n📝 {example.get('question', '')}", True, None))
            
            for j, step in enumerate(example.get('steps', []), 1):
                content_n.append((f"\n   Step {j}: {step}", False, None))
            
            if example.get('answer'):
                content_n.append(("\n\n   ✓ Answer: ", False, None))
                content_n.append((str(example.get('answer')), True, self.GREEN))
            
            self._set_content(slide_n, 1, content_n, 20)
        
        # Add image description slide if present
        if we_do_data.get("image_description"):
            slide_img = self._add_slide("WE_DO")
            content_img = [("👥 WE DO: Visual Reference", True, self.BLUE), ("\n", False, None)]
            content_img.append(("\n📷 " + we_do_data.get("image_description"), False, self.BLUE))
            self._set_content(slide_img, 1, content_img, 22)
        
        return self
    
    def add_we_do(self, title: str, question: str, steps: list):
        """Legacy single We Do slide."""
        self.add_we_do_slides({
            "examples": [{
                "question": question,
                "steps": steps
            }]
        })
        return self
    
    # =========================================================================
    # EXPANDED YOU DO - Multiple differentiated tasks
    # =========================================================================
    def add_you_do_slides(self, you_do_data: list):
        """Add multiple You Do slides with differentiated tasks."""
        
        # Slide 1: Bronze + Silver tasks
        slide1 = self._add_slide("YOU_DO")
        content1 = [("✍️ YOU DO: Independent Practice", True, self.PURPLE), ("\n", False, None)]
        
        for task in you_do_data[:2]:  # Bronze and Silver
            level = task.get('name', 'Task')
            color = self.ORANGE if 'Bronze' in level else self.BLUE
            content1.append((f"\n\n🥉 {level}" if 'Bronze' in level else f"\n\n🥈 {level}", True, color))
            content1.append((f"\n{task.get('question', '')}", False, None))
            
            # Include steps if provided
            for step in task.get('steps', []):
                content1.append((f"\n   • {step}", False, None))
            
            content1.append(("\n✓ Answer: ", False, None))
            content1.append((str(task.get('answer', '')), True, self.GREEN))
        
        self._set_content(slide1, 1, content1, 18)
        
        # Slide 2: Gold + Extension tasks
        if len(you_do_data) >= 3:
            slide2 = self._add_slide("YOU_DO")
            content2 = [("✍️ YOU DO: Challenge Tasks", True, self.PURPLE), ("\n", False, None)]
            
            for task in you_do_data[2:4]:  # Gold and any extension
                level = task.get('name', 'Extension')
                content2.append((f"\n\n🥇 {level}" if 'Gold' in level else f"\n\n🚀 {level}", True, self.RED))
                content2.append((f"\n{task.get('question', '')}", False, None))
                
                for step in task.get('steps', []):
                    content2.append((f"\n   • {step}", False, None))
                
                content2.append(("\n✓ Answer: ", False, None))
                content2.append((str(task.get('answer', '')), True, self.GREEN))
            
            self._set_content(slide2, 1, content2, 18)
        
        # Slide 3: Extra practice (if more than 4 tasks)
        if len(you_do_data) > 4:
            slide3 = self._add_slide("YOU_DO")
            content3 = [("✍️ YOU DO: Extra Practice", True, self.PURPLE), ("\n", False, None)]
            
            for task in you_do_data[4:]:
                content3.append((f"\n\n📝 {task.get('name', 'Extra')}", True, None))
                content3.append((f"\n{task.get('question', '')}", False, None))
                content3.append(("\n✓ ", False, None))
                content3.append((str(task.get('answer', '')), True, self.GREEN))
            
            self._set_content(slide3, 1, content3, 18)
        
        return self
    
    def add_you_do(self, tasks: list):
        """Legacy You Do method."""
        self.add_you_do_slides(tasks)
        return self
    
    def add_affirmative_checking(self, checkpoint: str = None, action: str = None, 
                                  question: str = None, mark_scheme: list = None):
        """Add Affirmative Checking slide."""
        slide = self._add_slide("CHECK")
        content = [("✔️ Affirmative Checking", True, self.RED), ("\n", False, None)]
        
        if checkpoint:
            content.append(("\n🔍 Check Point: ", True, None))
            content.append((checkpoint, False, None))
        
        if action:
            content.append(("\n\n⚡ Action: ", True, None))
            content.append((action, False, None))
        
        if question:
            content.append((f"\n\n📝 {question}", False, None))
        
        if mark_scheme:
            content.append(("\n\n📋 Mark Scheme:", True, None))
            for i, mark in enumerate(mark_scheme, 1):
                if isinstance(mark, dict):
                    content.append((f"\n{i}. {mark.get('step', '')} = ", False, None))
                    content.append((f"{mark.get('answer', '')} ✓", True, self.GREEN))
                else:
                    content.append((f"\n{i}. {mark}", False, None))
        
        self._set_content(slide, 1, content, 22)
        return self
    
    def add_exit_ticket(self, question: str, options: list, answer: str):
        """Add Exit Ticket slide."""
        slide = self._add_slide("EXIT")
        content = [("🎟️ EXIT TICKET", True, self.RED), ("\n", False, None)]
        content.append(("\nAnswer on your post-it:", True, None))
        content.append((f"\n\n{question}", False, None))
        content.append(("\n", False, None))
        
        for opt in options:
            content.append((f"\n   {opt}", False, None))
        
        content.append(("\n\n✓ Correct Answer: ", True, None))
        content.append((answer, True, self.GREEN))
        
        self._set_content(slide, 1, content, 22)
        return self
    
    def save(self, output_path: str):
        """Save the presentation to file."""
        self.prs.save(output_path)
        return output_path
    
    def save_to_bytes(self) -> BytesIO:
        """Save the presentation to BytesIO for direct download."""
        buffer = BytesIO()
        self.prs.save(buffer)
        buffer.seek(0)
        return buffer
