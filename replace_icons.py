import re

file_path = '/Users/raulbols/Projects/Drones360/drones360-sitio-completo/v5/que-es-un-drone-guia-completa.html'

with open(file_path, 'r') as f:
    html = f.read()

replacements = {
    '<div class="gc-icon">🎮</div>': '<div class="gc-img-wrap" style="height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; padding:5px;"><img src="../assets/drones/dji-neo.jpg" alt="Drones Recreativos" style="max-height:100%; max-width:100%; object-fit:contain; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.15)); mix-blend-mode: multiply;" /></div>',
    
    '<div class="gc-icon">📸</div>': '<div class="gc-img-wrap" style="height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; padding:5px;"><img src="../assets/drones/dji-air-3s.jpg" alt="Drones Fotografía" style="max-height:100%; max-width:100%; object-fit:contain; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.15)); mix-blend-mode: multiply;" /></div>',
    
    '<div class="gc-icon">⚡</div>': '<div class="gc-img-wrap" style="height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; padding:5px;"><img src="../assets/drones/dji-avata-2.jpg" alt="Drones FPV" style="max-height:100%; max-width:100%; object-fit:contain; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.15)); mix-blend-mode: multiply;" /></div>',
    
    '<div class="gc-icon">🌾</div>': '<div class="gc-img-wrap" style="height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; padding:5px;"><img src="../assets/drones/antarix-d50.jpg" alt="Drones Agrícolas" style="max-height:100%; max-width:100%; object-fit:contain; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.15)); mix-blend-mode: multiply;" /></div>',
    
    '<div class="gc-icon">📐</div>': '<div class="gc-img-wrap" style="height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; padding:5px;"><img src="../assets/drones/matrice-4e.jpg" alt="Drones Topografía" style="max-height:100%; max-width:100%; object-fit:contain; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.15)); mix-blend-mode: multiply;" /></div>',
    
    '<div class="gc-icon">🏭</div>': '<div class="gc-img-wrap" style="height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; padding:5px;"><img src="../assets/drones/dji-mavic-3-pro.jpg" alt="Drones Profesionales" style="max-height:100%; max-width:100%; object-fit:contain; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.15)); mix-blend-mode: multiply;" /></div>',
    
    '<div class="gc-icon">👜</div>': '<div class="gc-img-wrap" style="height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; padding:5px;"><img src="../assets/drones/dji-mini-4-pro.jpg" alt="Mini Drones" style="max-height:100%; max-width:100%; object-fit:contain; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.15)); mix-blend-mode: multiply;" /></div>',
    
    '<div class="gc-icon">👶</div>': '<div class="gc-img-wrap" style="height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; padding:5px;"><img src="../assets/drones/dji-tello.png" alt="Drones Niños" style="max-height:100%; max-width:100%; object-fit:contain; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.3));" /></div>'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(file_path, 'w') as f:
    f.write(html)

print("Icons replaced with images!")
