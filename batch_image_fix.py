import re
import os

base_dir = '/Users/raulbols/Projects/Drones360/drones360-sitio-completo/v5/'

# 1. FIX FPV DRONES (Inject real images into rank-item)
fpv_file = os.path.join(base_dir, 'drones-fpv-mexico.html')
with open(fpv_file, 'r') as f:
    fpv_html = f.read()

fpv_html = fpv_html.replace(
    '<div class="rank-top"><span class="rank-model">DJI Avata 2</span>',
    '<img src="../assets/drones/dji-avata-2.jpg" alt="DJI Avata 2" style="width: 100px; height: 100px; object-fit: contain; mix-blend-mode: multiply; margin-right: 15px; grid-row: span 3;" class="rank-img"/><div class="rank-top" style="display:flex; flex-direction:column; align-items:flex-start;"><span class="rank-model">DJI Avata 2</span>'
)
fpv_html = fpv_html.replace(
    '<div class="rank-top"><span class="rank-model">DJI Neo 2 + Motion Pack</span>',
    '<img src="../assets/drones/dji-neo.jpg" alt="DJI Neo 2" style="width: 100px; height: 100px; object-fit: contain; mix-blend-mode: multiply; margin-right: 15px; grid-row: span 3;" class="rank-img"/><div class="rank-top" style="display:flex; flex-direction:column; align-items:flex-start;"><span class="rank-model">DJI Neo 2 + Motion Pack</span>'
)
fpv_html = fpv_html.replace(
    '<div class="rank-top"><span class="rank-model">DJI Avata 2 — 3 Baterías</span>',
    '<img src="../assets/drones/dji-avata-2.jpg" alt="DJI Avata 2" style="width: 100px; height: 100px; object-fit: contain; mix-blend-mode: multiply; margin-right: 15px; grid-row: span 3;" class="rank-img"/><div class="rank-top" style="display:flex; flex-direction:column; align-items:flex-start;"><span class="rank-model">DJI Avata 2 — 3 Baterías</span>'
)
fpv_html = re.sub(r'(<style>.*?)(\s*</style>)', r'\1\n    .rank-body { flex-direction: row; align-items: center; display: flex; }\n\2', fpv_html, flags=re.DOTALL)
with open(fpv_file, 'w') as f:
    f.write(fpv_html)


# 2. FIX PROFESIONALES (Mavic 3 Pro Image too big)
pro_file = os.path.join(base_dir, 'drones-profesionales-mexico.html')
with open(pro_file, 'r') as f:
    pro_html = f.read()

pro_html = pro_html.replace(
    '<img alt="DJI Mavic 3 Pro" class="drone-img" src="../assets/drones/dji-mavic-3-pro.jpg"',
    '<img alt="DJI Mavic 3 Pro" class="drone-img" src="../assets/drones/dji-mavic-3-pro.jpg" style="max-height: 250px; width: auto; max-width: 100%;"'
)
with open(pro_file, 'w') as f:
    f.write(pro_html)


# 3. FIX TOPOGRAFIA & MINI DRONES (Replace <svg class="drone-svg"> with real images in related/variants)
files_to_check = ['drones-topografia-mexico.html', 'mini-drones-bolsillo-mexico.html', 'drones-para-ninos-mexico.html', 'drones-fumigacion-agricultura-mexico.html']

for file_name in files_to_check:
    path = os.path.join(base_dir, file_name)
    with open(path, 'r') as f:
        html = f.read()
    
    # Generic SVG replacement for variant cards (assuming they were missed)
    # The original script targeted index, perhaps these subpages still have SVGs
    if '<svg class="drone-svg"' in html:
        # A bit hacky, but robust enough for the V5 structure where we just need *a* drone image instead of a grey square
        html = re.sub(
            r'<div class="vcard-img">.*?<svg class="drone-svg".*?</svg>.*?</div>',
            '<div class="vcard-img" style="display:flex; justify-content:center; align-items:center; height:180px; padding:10px;"><img src="../assets/drones/dji-air-3s.jpg" style="max-width:100%; max-height:100%; object-fit:contain; mix-blend-mode:multiply; filter:drop-shadow(0 10px 15px rgba(0,0,0,0.1));" /></div>',
            html,
            flags=re.DOTALL
        )
    
        with open(path, 'w') as f:
            f.write(html)
            
print("Batch image replacement complete.")
