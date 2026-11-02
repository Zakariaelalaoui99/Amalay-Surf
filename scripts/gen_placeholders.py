import os
from xml.sax.saxutils import escape

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUT_DIR, exist_ok=True)

PALETTE = [
    ("#20403A", "#2E5951"),
    ("#2E5951", "#3E7269"),
    ("#5B5F55", "#8C8F82"),
    ("#181A17", "#24261F"),
]

def make_svg(name, width, height, label, sublabel, tone=0):
    c1, c2 = PALETTE[tone % len(PALETTE)]
    gid = f"g_{name.replace('.', '_')}"
    label = escape(label)
    sublabel = escape(sublabel)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="{gid}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#{gid})"/>
  <rect x="1" y="1" width="{width-2}" height="{height-2}" fill="none" stroke="#F4EEE3" stroke-opacity="0.25" stroke-width="2"/>
  <text x="50%" y="46%" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="{max(14, min(width, height)//18)}" fill="#F4EEE3" fill-opacity="0.9" font-weight="600">{label}</text>
  <text x="50%" y="54%" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="{max(11, min(width, height)//28)}" fill="#F4EEE3" fill-opacity="0.65">{sublabel}</text>
</svg>'''
    with open(os.path.join(OUT_DIR, name), "w") as f:
        f.write(svg)

placeholders = [
    ("hero.svg", 1920, 1080, "HERO PHOTO", "Sunset · coastline · palms · replace hero.svg", 0),
    ("intro-coastline.svg", 900, 1100, "COASTLINE PHOTO", "Aerial view of Tamraght bay · replace", 1),
    ("lesson-private.svg", 600, 760, "PRIVATE LESSONS", "Close-up hands-on teaching moment", 2),
    ("lesson-group.svg", 600, 760, "GROUP LESSONS", "Group of students in the water", 1),
    ("lesson-guiding.svg", 600, 760, "SURF GUIDING & TRIPS", "Coastline / surf spot scouting", 3),
    ("instructor.svg", 800, 1000, "INSTRUCTOR PORTRAIT", "Founder in wetsuit, board under arm", 0),
    ("contact-visual.svg", 800, 900, "CONTACT VISUAL", "Map or closing lifestyle shot", 3),
    ("gallery-1.svg", 500, 620, "GALLERY", "Lesson in progress", 1),
    ("gallery-2.svg", 500, 500, "GALLERY", "Wave close-up", 2),
    ("gallery-3.svg", 500, 380, "GALLERY", "Board rack / gear", 3),
    ("gallery-4.svg", 500, 620, "GALLERY", "Group photo on beach", 0),
    ("gallery-5.svg", 500, 500, "GALLERY", "Student catching wave", 1),
    ("gallery-6.svg", 500, 380, "GALLERY", "Sunset silhouette", 2),
    ("gallery-7.svg", 500, 620, "GALLERY", "Paddle out", 3),
    ("gallery-8.svg", 500, 500, "GALLERY", "Instructor coaching", 0),
    ("gallery-9.svg", 500, 380, "GALLERY", "High five / celebration", 1),
    ("gallery-10.svg", 500, 500, "GALLERY", "Boards lined up on sand", 2),
    ("gallery-11.svg", 500, 620, "GALLERY", "Portrait with board", 3),
]

for args in placeholders:
    make_svg(*args)

print(f"Generated {len(placeholders)} placeholder images in {os.path.abspath(OUT_DIR)}")
