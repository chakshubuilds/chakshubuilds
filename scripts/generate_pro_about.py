import base64
from PIL import Image

def generate_about():
    with open('assets/portrait_highres.png', 'rb') as f:
        p_b64 = base64.b64encode(f.read()).decode('utf-8')
    with open('assets/desk_setup_clean.png', 'rb') as f:
        d_b64 = base64.b64encode(f.read()).decode('utf-8')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1020 480" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@500;700&amp;display=swap');
      * {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
      .mono {{ font-family: 'JetBrains Mono', monospace; }}
      
      @keyframes pulse-green {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(0.85); }}
      }}
      .green-pulse {{ animation: pulse-green 2s ease-in-out infinite; transform-origin: 10px 6px; }}

      .card-hover {{ transition: transform 0.25s ease, stroke 0.25s ease; }}
      .card-hover:hover {{ stroke: #38bdf8; }}
      .btn-hover {{ transition: transform 0.2s ease, filter 0.2s ease; cursor: pointer; }}
      .btn-hover:hover {{ filter: brightness(1.15) drop-shadow(0 0 14px rgba(56,189,248,0.55)); }}
    </style>

    <linearGradient id="cyan-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>

    <linearGradient id="btn-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="45%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#9333ea" />
    </linearGradient>

    <clipPath id="avatar-clip">
      <rect x="0" y="0" width="126" height="130" rx="14" />
    </clipPath>

    <clipPath id="desk-clip">
      <rect x="0" y="0" width="176" height="114" rx="10" />
    </clipPath>

    <pattern id="dot-grid" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="rgba(56, 189, 248, 0.05)" />
    </pattern>
  </defs>

  <!-- Canvas Background -->
  <rect width="1020" height="480" rx="16" fill="#040714" />
  <rect width="1020" height="480" rx="16" fill="url(#dot-grid)" />

  <!-- ================= HEADER ================= -->
  <g transform="translate(24, 34)">
    <!-- Orange Lightning Bolt -->
    <path d="M 6 -12 L -4 1 L 2 1 L -2 12 L 8 -1 L 2 -1 Z" fill="#ff6b35" transform="translate(6, 0) scale(1.1)" />
    <text x="24" y="5" font-size="22" font-weight="800" fill="#ffffff" letter-spacing="-0.5">01. About &amp; <tspan fill="url(#cyan-purple)">Engineering Matrix</tspan></text>
    
    <!-- Right Tracker -->
    <line x1="680" y1="-2" x2="745" y2="-2" stroke="#1e293b" stroke-width="1.2" />
    <text x="760" y="2" font-size="10.5" font-weight="600" fill="#64748b" letter-spacing="2">PEOPLE  ×  PRODUCTS  ×  IMPACT</text>
  </g>

  <!-- ================= LEFT IDENTITY CARD ================= -->
  <g transform="translate(20, 65)">
    <!-- Main Card Body -->
    <rect width="395" height="395" rx="16" fill="#080e1e" stroke="#1c284a" stroke-width="1.2" />

    <!-- Avatar with ambient backlight glow -->
    <g transform="translate(24, 22)">
      <rect x="-4" y="-4" width="134" height="138" rx="18" fill="none" stroke="rgba(56, 189, 248, 0.18)" stroke-width="1.5" />
      <g clip-path="url(#avatar-clip)">
        <image href="data:image/png;base64,{p_b64}" x="0" y="0" width="126" height="130" preserveAspectRatio="xMidYMid slice" />
      </g>
      <rect x="0" y="0" width="126" height="130" rx="14" fill="none" stroke="#1e293b" stroke-width="1" />
    </g>

    <!-- Profile Info (Right of Avatar) -->
    <g transform="translate(164, 22)">
      <text x="0" y="11" font-size="9" font-weight="700" fill="#64748b" letter-spacing="1.5">AI &amp; SYSTEMS BUILDER</text>
      
      <text x="0" y="34" font-size="20.5" font-weight="800" fill="#ffffff" letter-spacing="-0.5">Chakshu <tspan fill="url(#cyan-purple)">Arora</tspan></text>
      
      <text x="0" y="52" font-size="11" font-weight="500" fill="#94a3b8">B.Tech CSE (AI)</text>
      
      <!-- Institution & CGPA -->
      <g transform="translate(0, 62)">
        <path d="M 0 8 L 6 3 L 12 8 M 2 8 L 2 13 M 5 8 L 5 13 M 7 8 L 7 13 M 10 8 L 10 13 M 0 13 L 12 13" stroke="#38bdf8" stroke-width="1" fill="none" />
        <text x="16" y="11" font-size="10" font-weight="500" fill="#64748b">VIPS-TC (2024 – 2028) <tspan fill="#334155">|</tspan> <tspan fill="#38bdf8" font-weight="600">CGPA: 8.65 / 10</tspan></text>
      </g>

      <!-- Bio Text -->
      <text x="0" y="88" font-size="10.5" fill="#94a3b8">
        <tspan x="0" dy="0">Building <tspan fill="#38bdf8" font-weight="600">AI-powered products</tspan>, scalable</tspan>
        <tspan x="0" dy="14">systems and communities that create</tspan>
        <tspan x="0" dy="14"><tspan fill="#e2e8f0" font-weight="600">real-world impact.</tspan></tspan>
      </text>

      <!-- 4 Filter Pills -->
      <g transform="translate(0, 130)">
        <!-- AI -->
        <rect x="0" y="0" width="30" height="18" rx="9" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
        <text x="15" y="12.5" font-size="9" font-weight="600" fill="#94a3b8" text-anchor="middle">AI</text>
        
        <!-- Systems -->
        <rect x="36" y="0" width="54" height="18" rx="9" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
        <text x="63" y="12.5" font-size="9" font-weight="600" fill="#94a3b8" text-anchor="middle">Systems</text>

        <!-- Community (highlighted cyan) -->
        <rect x="96" y="0" width="68" height="18" rx="9" fill="#083344" stroke="#06b6d4" stroke-width="1" />
        <text x="130" y="12.5" font-size="9" font-weight="700" fill="#22d3ee" text-anchor="middle">Community</text>

        <!-- Impact -->
        <rect x="170" y="0" width="46" height="18" rx="9" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
        <text x="193" y="12.5" font-size="9" font-weight="600" fill="#94a3b8" text-anchor="middle">Impact</text>
      </g>
    </g>

    <!-- ================= 4 MILESTONE TILES ================= -->
    <!-- Tile 1 (Col 1, Row 1): 3rd Year / Undergraduate -->
    <g transform="translate(20, 186)" class="card-hover">
      <rect width="170" height="42" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Purple icon box: Graduation Cap -->
      <rect x="7" y="6" width="30" height="30" rx="7" fill="#2e1065" stroke="#7c3aed" stroke-width="0.8" />
      <path d="M 14 20 L 22 16 L 30 20 L 22 24 Z M 16 22 L 16 26 C 16 28 28 28 28 26 L 28 22" fill="none" stroke="#c084fc" stroke-width="1.2" />
      <text x="44" y="20" font-size="11.5" font-weight="700" fill="#ffffff">3rd Year</text>
      <text x="44" y="31" font-size="9" font-weight="500" fill="#64748b">Undergraduate</text>
      <path d="M 154 18 L 158 21 L 154 24" fill="none" stroke="#475569" stroke-width="1.2" stroke-linecap="round" />
    </g>

    <!-- Tile 2 (Col 2, Row 1): AI Developer / Autonomous & Edge -->
    <g transform="translate(202, 186)" class="card-hover">
      <rect width="173" height="42" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Cyan icon box: Code symbol -->
      <rect x="7" y="6" width="30" height="30" rx="7" fill="#083344" stroke="#06b6d4" stroke-width="0.8" />
      <path d="M 18 18 L 15 21 L 18 24 M 26 18 L 29 21 L 26 24 M 23 17 L 21 25" fill="none" stroke="#22d3ee" stroke-width="1.2" stroke-linecap="round" />
      <text x="44" y="20" font-size="11.5" font-weight="700" fill="#ffffff">AI Developer</text>
      <text x="44" y="31" font-size="9" font-weight="500" fill="#64748b">Autonomous &amp; Edge</text>
      <path d="M 157 18 L 161 21 L 157 24" fill="none" stroke="#475569" stroke-width="1.2" stroke-linecap="round" />
    </g>

    <!-- Tile 3 (Col 1, Row 2): 8.65 / 10 / CGPA -->
    <g transform="translate(20, 236)" class="card-hover">
      <rect width="170" height="42" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Blue icon box: Score Chart -->
      <rect x="7" y="6" width="30" height="30" rx="7" fill="#172554" stroke="#3b82f6" stroke-width="0.8" />
      <path d="M 15 25 L 19 21 L 23 23 L 28 17 M 25 17 H 28 V 20" fill="none" stroke="#60a5fa" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
      <text x="44" y="20" font-size="11.5" font-weight="700" fill="#ffffff">8.65 / 10</text>
      <text x="44" y="31" font-size="9" font-weight="500" fill="#64748b">CGPA</text>
      <path d="M 154 18 L 158 21 L 154 24" fill="none" stroke="#475569" stroke-width="1.2" stroke-linecap="round" />
    </g>

    <!-- Tile 4 (Col 2, Row 2): Founder / TechVerse Solutions -->
    <g transform="translate(202, 236)" class="card-hover">
      <rect width="173" height="42" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Teal icon box: Rocket / Company -->
      <rect x="7" y="6" width="30" height="30" rx="7" fill="#042f2e" stroke="#14b8a6" stroke-width="0.8" />
      <path d="M 24 16 C 21 16 18 19 18 22 C 18 25 20 27 24 27 C 24 23 27 21 27 18 C 26 17 25 16 24 16 Z M 17 23 L 15 25 M 22 28 L 22 30" fill="none" stroke="#2dd4bf" stroke-width="1.2" stroke-linecap="round" />
      <text x="44" y="20" font-size="11.5" font-weight="700" fill="#ffffff">Founder</text>
      <text x="44" y="31" font-size="9" font-weight="500" fill="#64748b">TechVerse Solutions</text>
      <path d="M 157 18 L 161 21 L 157 24" fill="none" stroke="#475569" stroke-width="1.2" stroke-linecap="round" />
    </g>

    <!-- ================= META LINKS ================= -->
    <g transform="translate(24, 298)">
      <!-- Location -->
      <g transform="translate(0, 0)">
        <path d="M 5 0 C 2.2 0 0 2.2 0 5 C 0 8.5 5 13 5 13 C 5 13 10 8.5 10 5 C 10 2.2 7.8 0 5 0 Z M 5 6.5 C 4.2 6.5 3.5 5.8 3.5 5 C 3.5 4.2 4.2 3.5 5 3.5 C 5.8 3.5 6.5 4.2 6.5 5 C 6.5 5.8 5.8 6.5 5 6.5 Z" fill="#38bdf8" transform="scale(0.85)" />
        <text x="13" y="9" font-size="10" font-weight="500" fill="#94a3b8">New Delhi, India</text>
      </g>
      
      <!-- LinkedIn -->
      <g transform="translate(112, 0)">
        <rect x="0" y="0" width="11" height="11" rx="2" fill="#0a66c2" />
        <text x="2.5" y="8" font-size="7.5" font-weight="800" fill="#ffffff">in</text>
        <text x="15" y="9" font-size="10" font-weight="500" fill="#94a3b8">LinkedIn</text>
      </g>

      <!-- GitHub -->
      <g transform="translate(186, 0)">
        <path d="M 6 0 C 2.7 0 0 2.7 0 6 C 0 8.7 1.7 10.9 4.1 11.7 C 4.4 11.8 4.5 11.6 4.5 11.4 L 4.5 10.4 C 2.8 10.8 2.5 9.6 2.5 9.6 C 2.2 8.9 1.8 8.7 1.8 8.7 C 1.3 8.3 1.9 8.3 1.9 8.3 C 2.5 8.3 2.8 8.9 2.8 8.9 C 3.3 9.8 4.2 9.5 4.5 9.4 C 4.6 9 4.7 8.7 4.9 8.6 C 3.6 8.4 2.2 7.9 2.2 5.7 C 2.2 5.1 2.4 4.5 2.8 4.1 C 2.7 3.9 2.5 3.3 2.9 2.4 C 2.9 2.4 3.4 2.2 4.5 3 C 5 2.8 5.5 2.8 6 2.8 C 6.5 2.8 7 2.8 7.5 3 C 8.6 2.2 9.1 2.4 9.1 2.4 C 9.5 3.3 9.3 3.9 9.2 4.1 C 9.6 4.5 9.8 5.1 9.8 5.7 C 9.8 7.9 8.4 8.4 7.1 8.6 C 7.3 8.8 7.5 9.1 7.5 9.6 L 7.5 11.4 C 7.5 11.6 7.6 11.8 7.9 11.7 C 10.3 10.9 12 8.7 12 6 C 12 2.7 9.3 0 6 0 Z" fill="#94a3b8" />
        <text x="16" y="9" font-size="10" font-weight="500" fill="#94a3b8">GitHub</text>
      </g>

      <!-- Email -->
      <g transform="translate(254, 0)">
        <path d="M 0 1 C 0 0.4 0.4 0 1 0 L 11 0 C 11.6 0 12 0.4 12 1 L 12 9 C 12 9.6 11.6 10 11 10 L 1 10 C 0.4 10 0 9.6 0 9 Z M 1 2 L 6 5.5 L 11 2" fill="none" stroke="#38bdf8" stroke-width="1.1" />
        <text x="16" y="9" font-size="10" font-weight="500" fill="#94a3b8">Email</text>
      </g>
    </g>

    <!-- ================= CTA BUTTON ================= -->
    <g transform="translate(20, 332)" class="btn-hover">
      <rect width="355" height="42" rx="12" fill="url(#btn-grad)" />
      <text x="177" y="26" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle" letter-spacing="0.2">Let's Build Something Meaningful  →</text>
    </g>
  </g>

  <!-- ================= RIGHT TOP: CORE CAPABILITIES ================= -->
  <g transform="translate(435, 65)">
    <!-- Container -->
    <rect width="565" height="195" rx="16" fill="#080e1e" stroke="#1c284a" stroke-width="1.2" />

    <!-- Header -->
    <g transform="translate(20, 24)">
      <!-- Gear Cog Icon -->
      <circle cx="9" cy="9" r="8" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 2" />
      <circle cx="9" cy="9" r="3.5" fill="#38bdf8" />
      
      <text x="25" y="14" font-size="16" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Core <tspan fill="url(#cyan-purple)">Capabilities</tspan></text>
      <text x="525" y="12" font-size="9" font-weight="700" fill="#64748b" text-anchor="end" letter-spacing="1.5">WHAT I WORK ON</text>
    </g>

    <!-- 4 Capability Cards (2x2 Grid) -->
    <!-- Card 1 (Top Left) -->
    <g transform="translate(20, 48)" class="card-hover">
      <rect width="255" height="62" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Robot icon box -->
      <rect x="10" y="12" width="36" height="38" rx="8" fill="#2e1065" stroke="#7c3aed" stroke-width="0.8" />
      <path d="M 23 25 H 33 V 35 H 23 Z M 21 30 H 23 M 33 30 H 35 M 28 22 V 25 M 26 29 H 27 M 29 29 H 30" stroke="#c084fc" stroke-width="1.2" fill="none" />
      <text x="54" y="27" font-size="11.5" font-weight="700" fill="#ffffff">Autonomous Multi-Agent Platforms</text>
      <text x="54" y="41" font-size="8.5" fill="#94a3b8">
        <tspan x="54" dy="0">LangChain, context-preserving memory</tspan>
        <tspan x="54" dy="11">streams, sub-50ms tool handoffs (Orchestra AI)</tspan>
      </text>
      <path d="M 242 30 L 246 33 L 242 36" fill="none" stroke="#475569" stroke-width="1.2" stroke-linecap="round" />
    </g>

    <!-- Card 2 (Top Right) -->
    <g transform="translate(290, 48)" class="card-hover">
      <rect width="255" height="62" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- 3D Cube Edge IoT icon box -->
      <rect x="10" y="12" width="36" height="38" rx="8" fill="#042f2e" stroke="#14b8a6" stroke-width="0.8" />
      <path d="M 28 22 L 35 26 L 35 34 L 28 38 L 21 34 L 21 26 Z M 28 22 V 30 M 21 26 L 28 30 L 35 26" fill="none" stroke="#2dd4bf" stroke-width="1.2" stroke-linejoin="round" />
      <text x="54" y="27" font-size="11.5" font-weight="700" fill="#ffffff">Edge Computer Vision &amp; IoT</text>
      <text x="54" y="41" font-size="8.5" fill="#94a3b8">
        <tspan x="54" dy="0">YOLOv8 real-time detection, ESP32 sensor</tspan>
        <tspan x="54" dy="11">mesh, IEEE paper &amp; municipal patent</tspan>
      </text>
      <path d="M 242 30 L 246 33 L 242 36" fill="none" stroke="#475569" stroke-width="1.2" stroke-linecap="round" />
    </g>

    <!-- Card 3 (Bottom Left) -->
    <g transform="translate(20, 118)" class="card-hover">
      <rect width="255" height="62" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Globe icon box -->
      <rect x="10" y="12" width="36" height="38" rx="8" fill="#451a03" stroke="#f59e0b" stroke-width="0.8" />
      <circle cx="28" cy="31" r="7" fill="none" stroke="#fbbf24" stroke-width="1.2" />
      <ellipse cx="28" cy="31" rx="3.5" ry="7" fill="none" stroke="#fbbf24" stroke-width="1" />
      <line x1="21" y1="31" x2="35" y2="31" stroke="#fbbf24" stroke-width="1" />
      <text x="54" y="26" font-size="11" font-weight="700" fill="#ffffff">
        <tspan x="54" dy="0">Resilient Full-Stack Web &amp; Event</tspan>
        <tspan x="54" dy="12">Platforms</tspan>
      </text>
      <text x="54" y="49" font-size="8.5" fill="#94a3b8">
        <tspan x="54" dy="0">Next.js 15, TypeScript, WebSockets,</tspan>
        <tspan x="54" dy="10">real-time queues &amp; leaderboards (TechVerse)</tspan>
      </text>
      <path d="M 242 30 L 246 33 L 242 36" fill="none" stroke="#475569" stroke-width="1.2" stroke-linecap="round" />
    </g>

    <!-- Card 4 (Bottom Right) -->
    <g transform="translate(290, 118)" class="card-hover">
      <rect width="255" height="62" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Analytics icon box -->
      <rect x="10" y="12" width="36" height="38" rx="8" fill="#4c0519" stroke="#f43f5e" stroke-width="0.8" />
      <rect x="23" y="32" width="2" height="6" fill="#fb7185" />
      <rect x="27" y="27" width="2" height="11" fill="#fb7185" />
      <rect x="31" y="23" width="2" height="15" fill="#fb7185" />
      <text x="54" y="27" font-size="11.5" font-weight="700" fill="#ffffff">Data, Analytics &amp; ML Systems</text>
      <text x="54" y="41" font-size="8.5" fill="#94a3b8">
        <tspan x="54" dy="0">Python, PyTorch, TensorFlow, Power BI,</tspan>
        <tspan x="54" dy="11">predictive models &amp; real-world datasets</tspan>
      </text>
      <path d="M 242 30 L 246 33 L 242 36" fill="none" stroke="#475569" stroke-width="1.2" stroke-linecap="round" />
    </g>
  </g>

  <!-- ================= RIGHT BOTTOM: CURRENTLY BUILDING ================= -->
  <g transform="translate(435, 272)">
    <!-- Main Card Body -->
    <rect width="565" height="188" rx="16" fill="#080e1e" stroke="#1c284a" stroke-width="1.2" />

    <!-- Header -->
    <g transform="translate(20, 24)">
      <!-- Folder Icon -->
      <path d="M 3 5 H 8 L 10 7 H 17 V 15 H 3 Z" fill="none" stroke="#38bdf8" stroke-width="1.4" stroke-linejoin="round" />
      <text x="25" y="14" font-size="16" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Currently <tspan fill="url(#cyan-purple)">Building</tspan></text>
      
      <!-- Builder Pill Badge -->
      <g transform="translate(440, 2)">
        <rect x="0" y="-3" width="105" height="18" rx="9" fill="#042f2e" stroke="#059669" stroke-width="0.8" />
        <circle cx="10" cy="6" r="3.5" fill="#10b981" class="green-pulse" />
        <text x="18" y="9.5" font-size="8.5" font-weight="700" fill="#34d399" letter-spacing="1">BUILDER // 2026</text>
      </g>
    </g>

    <!-- Inner Bento Container -->
    <g transform="translate(16, 42)">
      <rect width="533" height="130" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1" />

      <!-- Left Text Content -->
      <g transform="translate(18, 16)">
        <!-- Green NOW Pill -->
        <rect x="0" y="0" width="38" height="17" rx="8.5" fill="#059669" />
        <text x="19" y="12" font-size="8.5" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">NOW</text>
        
        <!-- Heading -->
        <text x="48" y="13" font-size="13" font-weight="800" fill="#ffffff" letter-spacing="-0.2">2:47 AM  Deep Work Sprints &amp; Flow State</text>

        <!-- Paragraph Description -->
        <text x="0" y="38" font-size="10.5" fill="#94a3b8">
          <tspan x="0" dy="0">Thriving in midnight flow sessions where complex agent</tspan>
          <tspan x="0" dy="16">architectures crystalize. Guided by Clean Code &amp; Pragmatic</tspan>
          <tspan x="0" dy="16">Programming principles.</tspan>
        </text>

        <!-- 4 Hashtag Pills -->
        <g transform="translate(0, 78)">
          <!-- #DeepWork -->
          <rect x="0" y="0" width="66" height="18" rx="9" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="33" y="12" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle">#DeepWork</text>

          <!-- #SystemDesign -->
          <rect x="72" y="0" width="82" height="18" rx="9" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="113" y="12" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle">#SystemDesign</text>

          <!-- #ZeroDistractions -->
          <rect x="160" y="0" width="94" height="18" rx="9" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="207" y="12" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle">#ZeroDistractions</text>

          <!-- #ShipCraft -->
          <rect x="260" y="0" width="64" height="18" rx="9" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="292" y="12" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle">#ShipCraft</text>
        </g>
      </g>

      <!-- Right Visual: Midnight Desk Setup -->
      <g transform="translate(345, 8)">
        <rect x="-2" y="-2" width="180" height="118" rx="12" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1.2" />
        <g clip-path="url(#desk-clip)">
          <image href="data:image/png;base64,{d_b64}" x="0" y="0" width="176" height="114" preserveAspectRatio="xMidYMid slice" />
        </g>
        <rect x="0" y="0" width="176" height="114" rx="10" fill="none" stroke="#1e293b" stroke-width="1" />
      </g>
    </g>
  </g>
</svg>'''

    with open('assets/about-life.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Successfully generated assets/about-life.svg (size: %d bytes)" % len(svg))

if __name__ == '__main__':
    generate_about()
