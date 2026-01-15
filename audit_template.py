import os
from pptx import Presentation

# FILENAME is fixed as per spec
FILENAME = "WSO Learn Like A GEM Template (1).pptx"

def audit_file():
    print(f"--- 🔍 INITIATING TEMPLATE AUDIT: {FILENAME} ---")
    
    if not os.path.exists(FILENAME):
        print(f"❌ ERROR: '{FILENAME}' not found.")
        print("👉 ACTION: Please drag and drop the PowerPoint template into this folder.")
        return

    try:
        prs = Presentation(FILENAME)
        print("\n✅ Template loaded successfully.\n")
        print("="*75)
        print(f"{'IDX':<6} | {'LAYOUT NAME':<40} | {'PLACEHOLDERS (Type/Idx)'}")
        print("="*75)
        
        for i, layout in enumerate(prs.slide_layouts):
            # Collect placeholder info to help identify Title (Type 1) vs Body (Type 7/2)
            ph_info = []
            for ph in layout.placeholders:
                p_type = ph.placeholder_format.type
                p_idx = ph.placeholder_format.idx
                ph_info.append(f"[Type {p_type}/ID {p_idx}]")
            
            print(f"{i:<6} | {layout.name:<40} | {' '.join(ph_info)}")

        print("="*75)
        print("\n📋 INSTRUCTIONS FOR USER:")
        print("1. Look at the list above.")
        print("2. Identify the Index ID (integer) for each required slide type (Do Now, I Do, etc).")
        print("3. Open 'lesson_builder.py' and update the 'LAYOUT_MAP' dictionary with these numbers.")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    audit_file()
