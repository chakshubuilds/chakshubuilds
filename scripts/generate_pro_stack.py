import os

# Precise SVG icons
# Dimensions: 18x18 viewBox="0 0 24 24"

PYTHON_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <path d="M11.9 1.5c-4.4 0-4.1 1.9-4.1 1.9l.01 2h4.2v.6H6.1S3.5 5.7 3.5 10.1c0 4.4 2.3 4.2 2.3 4.2h1.4v-2s-.1-2.3 2.3-2.3h4.1s2.2.04 2.2-2.2V3.7s.3-2.2-3.9-2.2zm-2.4 1.3a.8.8 0 110 1.6.8.8 0 010-1.6z" fill="#387eb8"/>
  <path d="M12.1 22.5c4.4 0 4.1-1.9 4.1-1.9l-.01-2h-4.2v-.6h5.9s2.6.3 2.6-4.1c0-4.4-2.3-4.2-2.3-4.2h-1.4v2s.1 2.3-2.3 2.3h-4.1s-2.2-.04-2.2 2.2v4.1s-.3 2.2 3.9 2.2zm2.4-1.3a.8.8 0 110-1.6.8.8 0 010-1.6z" fill="#ffe052"/>
</svg>'''

TS_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <rect width="24" height="24" rx="4" fill="#3178C6"/>
  <path d="M11.5 8.5H5v2.2h2.1V18h2.3v-7.3h2.1V8.5zm7.3 3.8c-.5-.4-1.2-.7-2-.9-.6-.2-1-.4-1-.7 0-.3.2-.5.6-.5.4 0 .9.2 1.4.5l.8-1.7c-.7-.4-1.5-.6-2.4-.6-2 0-3.1 1.1-3.1 2.6 0 1.2.7 2 2.1 2.5.7.2 1.1.4 1.1.8 0 .4-.3.6-.8.6-.6 0-1.2-.3-1.8-.7l-.8 1.8c.8.5 1.7.8 2.7.8 2.2 0 3.3-1.1 3.3-2.7 0-1.4-.7-2.1-2.1-2.6z" fill="#FFFFFF"/>
</svg>'''

JS_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <rect width="24" height="24" rx="4" fill="#F7DF1E"/>
  <path d="M7 16.5c.5.8 1.2 1.4 2.2 1.4 1.1 0 1.8-.6 1.8-1.9v-6.5h-2.1v6.5c0 .4-.2.6-.5.6-.3 0-.5-.2-.7-.5l-.7.4zm8.2-.1c.6 0 1.1-.3 1.1-.8 0-.5-.4-.7-1.3-1.1-.9-.4-2-.9-2-2.1 0-1.2 1-2 2.5-2 1.2 0 1.9.4 2.3 1.2l-1.3.8c-.3-.5-.6-.7-1-.7-.5 0-.8.3-.8.6 0 .4.3.6 1.2 1 1.1.5 2.1 1 2.1 2.2 0 1.4-1.1 2.2-2.7 2.2-1.5 0-2.3-.6-2.8-1.5l1.4-.8c.4.6.9.9 1.4.9z" fill="#000000"/>
</svg>'''

CPP_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <path d="M12 2L2 7.8v11.5L12 25l10-5.7V7.8L12 2z" fill="#00599C"/>
  <circle cx="12" cy="13.5" r="4.5" fill="#FFFFFF"/>
  <circle cx="12" cy="13.5" r="3" fill="#00599C"/>
  <path d="M18.5 12h-1v1.5H16v1h1.5V16h1v-1.5H20v-1h-1.5V12zm3 0h-1v1.5H19v1h1.5V16h1v-1.5H23v-1h-1.5V12z" fill="#FFFFFF"/>
</svg>'''

SQL_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <ellipse cx="12" cy="6" rx="8" ry="3.5" fill="#336791"/>
  <path d="M4 6v5c0 1.9 3.6 3.5 8 3.5s8-1.6 8-3.5V6" stroke="#336791" stroke-width="2" fill="none"/>
  <path d="M4 11v5c0 1.9 3.6 3.5 8 3.5s8-1.6 8-3.5V11" stroke="#336791" stroke-width="2" fill="none"/>
</svg>'''

PYTORCH_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <path d="M13.2 2.5l-.8.8 3.2 3.2c1.7 1.7 2.7 4 2.7 6.4 0 5-4.1 9.1-9.1 9.1s-9.1-4.1-9.1-9.1c0-4.6 3.4-8.4 7.9-9l.5 1.4C5 6 2.3 9.2 2.3 12.9c0 3.8 3.1 6.9 6.9 6.9s6.9-3.1 6.9-6.9c0-1.8-.7-3.6-2-4.9l-3.2 3.2-.8-.8 3.2-3.2-.8-.8z" fill="#EE4C2C"/>
  <circle cx="17" cy="4.5" r="1.5" fill="#EE4C2C"/>
</svg>'''

LANGCHAIN_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <rect width="24" height="24" rx="5" fill="#1C3C3C"/>
  <path d="M6 12a4 4 0 014-4h4a4 4 0 014 4 4 4 0 01-4 4h-4a4 4 0 01-4-4z" stroke="#10B981" stroke-width="2" fill="none"/>
  <circle cx="10" cy="12" r="2" fill="#10B981"/>
  <circle cx="14" cy="12" r="2" fill="#22D3EE"/>
</svg>'''

FASTAPI_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <circle cx="12" cy="12" r="10" fill="#05998B"/>
  <path d="M13 3L6 14h5l-1 7 8-11h-5l1-7z" fill="#FFFFFF"/>
</svg>'''

OPENCV_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <circle cx="12" cy="7" r="4" fill="#EA4335"/>
  <circle cx="6.5" cy="16.5" r="4" fill="#34A853"/>
  <circle cx="17.5" cy="16.5" r="4" fill="#4285F4"/>
  <circle cx="12" cy="7" r="2" fill="#070b16"/>
  <circle cx="6.5" cy="16.5" r="2" fill="#070b16"/>
  <circle cx="17.5" cy="16.5" r="2" fill="#070b16"/>
</svg>'''

VECTORDB_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <path d="M12 2L3 7v10l9 5 9-5V7l-9-5z" stroke="#A78BFA" stroke-width="2" fill="#090f20"/>
  <path d="M12 12L3 7m9 5l9-5m-9 5v10" stroke="#A78BFA" stroke-width="1.5"/>
</svg>'''

NEXTJS_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <circle cx="12" cy="12" r="11" fill="#000000" stroke="#FFFFFF" stroke-width="1.2"/>
  <path d="M8 7v10m4.5-10l5.5 8" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
  <path d="M16 7v4" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
</svg>'''

REACT_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <ellipse cx="12" cy="12" rx="3.5" ry="9" stroke="#61DAFB" stroke-width="1.5" transform="rotate(30,12,12)"/>
  <ellipse cx="12" cy="12" rx="3.5" ry="9" stroke="#61DAFB" stroke-width="1.5" transform="rotate(90,12,12)"/>
  <ellipse cx="12" cy="12" rx="3.5" ry="9" stroke="#61DAFB" stroke-width="1.5" transform="rotate(150,12,12)"/>
  <circle cx="12" cy="12" r="1.8" fill="#61DAFB"/>
</svg>'''

NODE_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <path d="M12 2L3 7.2v10.4L12 23l9-5.4V7.2L12 2z" fill="#5FA04E"/>
  <path d="M12 6.5L6.5 9.7v5.4l5.5 3.2 5.5-3.2V9.7L12 6.5z" fill="#FFFFFF"/>
</svg>'''

TAILWIND_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <path d="M6.5 10c1.5-3 3.5-3.5 5.5-2.5 1.2.6 2 1.5 3 2.5 1.5 1.5 3.3 2 5.5 1-1.5 3-3.5 3.5-5.5 2.5-1.2-.6-2-1.5-3-2.5-1.5-1.5-3.3-2-5.5-1zm-4 5c1.5-3 3.5-3.5 5.5-2.5 1.2.6 2 1.5 3 2.5 1.5 1.5 3.3 2 5.5 1-1.5 3-3.5 3.5-5.5 2.5-1.2-.6-2-1.5-3-2.5-1.5-1.5-3.3-2-5.5-1z" fill="#06B6D4"/>
</svg>'''

ESP32_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <rect x="5" y="5" width="14" height="14" rx="2" fill="#1e2c50" stroke="#00f0ff" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="3" fill="#00f0ff"/>
  <path d="M2 8h3m-3 4h3m-3 4h3m14-8h3m-3 4h3m-3 4h3M8 2v3m4-3v3m4-3v3M8 19v3m4-3v3m4-3v3" stroke="#22D3EE" stroke-width="1.2"/>
</svg>'''

DOCKER_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <rect x="4" y="10" width="3" height="3" fill="#2496ED" rx="0.5"/>
  <rect x="8" y="10" width="3" height="3" fill="#2496ED" rx="0.5"/>
  <rect x="12" y="10" width="3" height="3" fill="#2496ED" rx="0.5"/>
  <rect x="8" y="6" width="3" height="3" fill="#2496ED" rx="0.5"/>
  <rect x="12" y="6" width="3" height="3" fill="#2496ED" rx="0.5"/>
  <path d="M22 13c-.4-1.2-1.4-1.8-2.5-1.7-.3-1.6-1.5-2.8-3.1-2.9-1.2 0-2.3.6-2.9 1.6H3c-.6 0-1 .4-1 1 0 4.4 3.6 8 8 8 5.5 0 10.3-3.4 12-6z" fill="#2496ED"/>
</svg>'''

AWS_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <path d="M19.5 16.5c-3.2 2-7.5 2.5-11.5 1.2-1-.3-1.9-.8-2.8-1.4-.2-.1-.4.1-.3.3 1.2 1.4 3.4 2.5 5.8 2.8 3.5.4 7-.3 10-2.4.3-.2.1-.6-.2-.5z" fill="#FF9900"/>
  <path d="M20.2 14.8c-.3-.4-1.8-.2-2.5-.1-.2 0-.3.2-.1.3.7.5 1.5.3 2 .2.2-.1.7-.1.6-.4z" fill="#FF9900"/>
  <path d="M7 8l-2 5h1.5l.5-1.3h2l.5 1.3H11L9 8H7zm.3 2.5l.6-1.6.6 1.6h-1.2zm6.2-2.5l-1.5 5h1.2l.8-2.8.8 2.8h1.2l.8-2.8.8 2.8h1.2L17 8h-1.2l-.9 3.2L14 8h-1.2z" fill="#f8fafc"/>
</svg>'''

GIT_ICON = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none">
  <path d="M21.6 10.9L13.1 2.4c-.6-.6-1.5-.6-2.1 0L8.6 4.8l2.7 2.7c.6-.2 1.3-.1 1.8.4.5.5.7 1.2.5 1.8l2.6 2.6c.6-.2 1.3-.1 1.8.4.8.8.8 2.1 0 2.9-.8.8-2.1.8-2.9 0-.6-.6-.7-1.4-.4-2.1L12.1 11v5.1c.3.2.6.5.7.8.8.8.8 2.1 0 2.9-.8.8-2.1.8-2.9 0-.8-.8-.8-2.1 0-2.9.3-.3.6-.5.9-.6V9.8c-.3-.1-.7-.3-.9-.6-.6-.6-.7-1.4-.4-2.1L6.7 4.3 2.4 8.6c-.6.6-.6 1.5 0 2.1l8.5 8.5c.6.6 1.5.6 2.1 0l8.5-8.5c.6-.6.6-1.6.1-2.1v.3z" fill="#F05032"/>
</svg>'''

# Generate HTML / SVG for each badge pill
def make_pill(x, y, w, h, icon_svg, label, badge_border="#1c284a", text_col="#f8fafc"):
    return f'''<g transform="translate({x}, {y})">
      <rect width="{w}" height="{h}" rx="8" fill="#090f20" stroke="{badge_border}" stroke-width="1" />
      <g transform="translate(10, 7)">{icon_svg}</g>
      <text x="36" y="21" class="font-sans" font-size="12" font-weight="600" fill="{text_col}">{label}</text>
    </g>'''

# Bento Categories
cat_1_pills = [
    (14, 44, 120, 32, PYTHON_ICON, "Python", "#387eb8"),
    (144, 44, 134, 32, TS_ICON, "TypeScript", "#3178C6"),
    (288, 44, 126, 32, JS_ICON, "JavaScript", "#F7DF1E"),
    (14, 86, 105, 32, CPP_ICON, "C / C++", "#00599C"),
    (129, 86, 95, 32, SQL_ICON, "SQL", "#336791"),
    (234, 86, 180, 32, PYTHON_ICON, "MicroPython", "#387eb8"),
]

cat_2_pills = [
    (14, 44, 125, 32, PYTORCH_ICON, "PyTorch", "#EE4C2C"),
    (149, 44, 135, 32, LANGCHAIN_ICON, "LangChain", "#10B981"),
    (294, 44, 120, 32, FASTAPI_ICON, "FastAPI", "#05998B"),
    (14, 86, 120, 32, OPENCV_ICON, "OpenCV", "#4285F4"),
    (144, 86, 115, 32, OPENCV_ICON, "YOLOv8", "#EA4335"),
    (269, 86, 145, 32, VECTORDB_ICON, "Vector DBs", "#A78BFA"),
]

cat_3_pills = [
    (14, 44, 125, 32, NEXTJS_ICON, "Next.js 15", "#f8fafc"),
    (149, 44, 115, 32, REACT_ICON, "React.js", "#61DAFB"),
    (274, 44, 140, 32, NODE_ICON, "Node.js", "#5FA04E"),
    (14, 86, 140, 32, TAILWIND_ICON, "Tailwind CSS", "#06B6D4"),
    (164, 86, 115, 32, FASTAPI_ICON, "REST APIs", "#22D3EE"),
    (289, 86, 125, 32, TS_ICON, "WebSockets", "#00f0ff"),
]

cat_4_pills = [
    (14, 44, 120, 32, ESP32_ICON, "ESP32", "#00f0ff"),
    (144, 44, 115, 32, DOCKER_ICON, "Docker", "#2496ED"),
    (269, 44, 145, 32, AWS_ICON, "AWS Cloud", "#FF9900"),
    (14, 86, 115, 32, GIT_ICON, "Git CI/CD", "#F05032"),
    (139, 86, 110, 32, ESP32_ICON, "Arduino", "#00878F"),
    (259, 86, 155, 32, DOCKER_ICON, "Linux Servers", "#f8fafc"),
]

def render_pills(pills):
    res = []
    for x, y, w, h, icon, label, col in pills:
        res.append(make_pill(x, y, w, h, icon, label, badge_border="rgba(36, 123, 255, 0.25)", text_col="#f8fafc"))
    return "\\n      ".join(res)

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 450" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Cascadia+Code:wght@400;600;700&amp;family=Inter:wght@400;500;600;700;800&amp;display=swap');
      .font-mono {{ font-family: 'Cascadia Code', monospace; }}
      .font-sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }}

      @keyframes glow-pulse {{
        0%, 100% {{ opacity: 0.8; }}
        50% {{ opacity: 0.3; }}
      }}
      .pulse-line {{ animation: glow-pulse 3s ease-in-out infinite; }}
    </style>

    <pattern id="stk-dot-grid" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="rgba(36, 123, 255, 0.12)" />
    </pattern>

    <linearGradient id="top-neon-bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#247bff" />
      <stop offset="50%" stop-color="#00f0ff" />
      <stop offset="100%" stop-color="#ff354f" />
    </linearGradient>
  </defs>

  <!-- Container -->
  <rect width="920" height="450" rx="16" fill="#070b16" stroke="#1c284a" stroke-width="1.5" />
  <rect width="920" height="450" rx="16" fill="url(#stk-dot-grid)" />
  <path d="M 16 0 L 904 0" stroke="url(#top-neon-bar)" stroke-width="2.5" />

  <!-- Header -->
  <g transform="translate(32, 26)">
    <rect x="0" y="0" width="182" height="24" rx="12" fill="#090f20" stroke="#182442" />
    <circle cx="12" cy="12" r="4.5" fill="#247bff" />
    <text x="24" y="16" class="font-mono" font-size="11" font-weight="700" fill="#247bff">STACK_ARCHITECTURE</text>
    <text x="194" y="16" class="font-mono" font-size="11" fill="#5a7099">VERIFIED TOOLING &amp; RUNTIMES</text>
    <text x="0" y="54" class="font-sans" font-size="22" font-weight="800" fill="#f8fafc" letter-spacing="-0.3">Engineering Stack &amp; Technologies</text>
    <text x="0" y="74" class="font-sans" font-size="13" fill="#8ba0c8">High-concurrency systems, autonomous AI agents, and embedded edge devices with real official toolchains.</text>
  </g>

  <!-- 4 Bento Cards (2x2 Grid) -->
  <g transform="translate(32, 116)">
    <!-- Card 1: Core Languages -->
    <g transform="translate(0, 0)">
      <rect width="420" height="142" rx="12" fill="#0d1326" stroke="#1c284a" stroke-width="1.2" />
      <circle cx="22" cy="22" r="5" fill="#247bff" />
      <text x="36" y="26" class="font-sans" font-size="13.5" font-weight="700" fill="#f8fafc">Core Languages</text>
      <text x="404" y="26" text-anchor="end" class="font-mono" font-size="10.5" fill="#5a7099">01 // LANG</text>
      {render_pills(cat_1_pills)}
    </g>

    <!-- Card 2: AI & Agents -->
    <g transform="translate(436, 0)">
      <rect width="420" height="142" rx="12" fill="#0d1326" stroke="#1c284a" stroke-width="1.2" />
      <circle cx="22" cy="22" r="5" fill="#ff354f" />
      <text x="36" y="26" class="font-sans" font-size="13.5" font-weight="700" fill="#f8fafc">AI, Agents &amp; Computer Vision</text>
      <text x="404" y="26" text-anchor="end" class="font-mono" font-size="10.5" fill="#5a7099">02 // AI_ML</text>
      {render_pills(cat_2_pills)}
    </g>

    <!-- Card 3: Web & Full-Stack -->
    <g transform="translate(0, 156)">
      <rect width="420" height="142" rx="12" fill="#0d1326" stroke="#1c284a" stroke-width="1.2" />
      <circle cx="22" cy="22" r="5" fill="#00f0ff" />
      <text x="36" y="26" class="font-sans" font-size="13.5" font-weight="700" fill="#f8fafc">Web &amp; Full-Stack Systems</text>
      <text x="404" y="26" text-anchor="end" class="font-mono" font-size="10.5" fill="#5a7099">03 // WEB</text>
      {render_pills(cat_3_pills)}
    </g>

    <!-- Card 4: IoT & DevOps -->
    <g transform="translate(436, 156)">
      <rect width="420" height="142" rx="12" fill="#0d1326" stroke="#1c284a" stroke-width="1.2" />
      <circle cx="22" cy="22" r="5" fill="#10b981" />
      <text x="36" y="26" class="font-sans" font-size="13.5" font-weight="700" fill="#f8fafc">IoT Edge &amp; Cloud DevOps</text>
      <text x="404" y="26" text-anchor="end" class="font-mono" font-size="10.5" fill="#5a7099">04 // INFRA</text>
      {render_pills(cat_4_pills)}
    </g>
  </g>
</svg>'''

with open('assets/stack.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("Generated new assets/stack.svg with official vector logos!")
