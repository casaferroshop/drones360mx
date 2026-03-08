import os
import glob

html_files = glob.glob('/Users/raulbols/Projects/Drones360/drones360-sitio-completo/v5/*.html')
css_addition = """
    /* V5 HERO CONTRAST FIX */
    .phero .qspec, .phero .aw, .phero .ph-rating-row, .phero .ph-badge {
        background: rgba(255, 255, 255, 0.92) !important;
        border: 1px solid rgba(255, 255, 255, 1) !important;
        position: relative;
        z-index: 2;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
    }
    .phero .qspec-val, .phero .aw-v, .phero .aw-t, .phero .ph-rating-cnt {
        color: #111827 !important;
        font-weight: 700;
    }
"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if "/* V5 HERO CONTRAST FIX */" not in content and "</style>" in content:
        parts = content.split("</style>", 1)
        new_content = parts[0] + css_addition + "</style>" + parts[1]
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Patched {os.path.basename(file)}")
