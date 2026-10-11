import base64
from PIL import Image

def generate_about():
    with open('assets/portrait_highres.png', 'rb') as f:
        p_b64 = base64.b64encode(f.read()).decode('utf-8')
    with open('assets/desk_perfect.png', 'rb') as f:
        d_b64 = base64.b64encode(f.read()).decode('utf-8')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1020 545" width="100%" height="100%" xml:space="preserve">
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
      .btn-hover:hover {{ filter: brightness(1.18) drop-shadow(0 0 16px rgba(56,189,248,0.6)); }}
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
      <rect x="0" y="0" width="130" height="138" rx="14" />
    </clipPath>

    <clipPath id="bento-container-clip">
      <rect x="0" y="0" width="533" height="182" rx="14" />
    </clipPath>

    <linearGradient id="desk-edge-fade" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0b1329" stop-opacity="1" />
      <stop offset="35%" stop-color="#0b1329" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#0b1329" stop-opacity="0" />
    </linearGradient>

    <pattern id="dot-grid" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="rgba(56, 189, 248, 0.05)" />
    </pattern>
  </defs>

  <!-- Canvas Background -->
  <rect width="1020" height="545" rx="16" fill="#040714" />
  <rect width="1020" height="545" rx="16" fill="url(#dot-grid)" />

  <!-- ================= HEADER ================= -->
  <g transform="translate(24, 36)">
    <!-- Orange Lightning Bolt -->
    <path d="M 6 -12 L -4 1 L 2 1 L -2 12 L 8 -1 L 2 -1 Z" fill="#ff6b35" transform="translate(6, 0) scale(1.1)" />
    <text x="24" y="5" font-size="22" font-weight="800" fill="#ffffff" letter-spacing="0.4">01. About &amp;<tspan dx="8" fill="url(#cyan-purple)">Engineering Matrix</tspan></text>
    
    <!-- Right Tracker -->
    <line x1="680" y1="-2" x2="745" y2="-2" stroke="#1e293b" stroke-width="1.2" />
    <text x="760" y="2" font-size="10.5" font-weight="600" fill="#64748b" letter-spacing="2.5">PEOPLE  ×  PRODUCTS  ×  IMPACT</text>
  </g>

  <!-- ================= LEFT IDENTITY CARD ================= -->
  <g transform="translate(20, 68)">
    <!-- Main Card Body -->
    <rect width="395" height="460" rx="16" fill="#080e1e" stroke="#1c284a" stroke-width="1.2" />

    <!-- Avatar with ambient backlight glow -->
    <g transform="translate(22, 22)">
      <rect x="-4" y="-4" width="138" height="146" rx="18" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1.5" />
      <g clip-path="url(#avatar-clip)">
        <image href="data:image/png;base64,{p_b64}" x="0" y="0" width="130" height="138" preserveAspectRatio="xMidYMid slice" />
      </g>
      <rect x="0" y="0" width="130" height="138" rx="14" fill="none" stroke="#1e293b" stroke-width="1" />
    </g>

    <!-- Profile Info (Right of Avatar) -->
    <g transform="translate(166, 22)">
      <text x="0" y="12" font-size="9" font-weight="700" fill="#64748b" letter-spacing="1.8">AI &amp; SYSTEMS BUILDER</text>
      
      <text x="0" y="36" font-size="21" font-weight="800" fill="#ffffff" letter-spacing="0.4">Chakshu<tspan dx="8" fill="url(#cyan-purple)">Arora</tspan></text>
      
      <text x="0" y="56" font-size="12" font-weight="700" fill="#38bdf8" letter-spacing="0.3">AI Developer</text>
      
      <!-- Institution & CGPA -->
      <g transform="translate(0, 68)">
        <path d="M 0 8 L 6 3 L 12 8 M 2 8 L 2 13 M 5 8 L 5 13 M 7 8 L 7 13 M 10 8 L 10 13 M 0 13 L 12 13" stroke="#38bdf8" stroke-width="1" fill="none" />
        <text x="16" y="11" font-size="10" font-weight="500" fill="#64748b" letter-spacing="0.2">VIPS-TC (2024 – 2028) <tspan fill="#334155" dx="2">|</tspan> <tspan fill="#38bdf8" font-weight="600" dx="2">CGPA: 8.65 / 10</tspan></text>
      </g>

      <!-- Bio Text -->
      <text x="0" y="96" font-size="10.5" fill="#94a3b8" letter-spacing="0.2">
        <tspan x="0" dy="0">Building <tspan fill="#38bdf8" font-weight="600">AI-powered products</tspan>, scalable</tspan>
        <tspan x="0" dy="16">systems and communities that create</tspan>
        <tspan x="0" dy="16"><tspan fill="#e2e8f0" font-weight="600">real-world impact.</tspan></tspan>
      </text>

      <!-- 4 Filter Pills -->
      <g transform="translate(0, 142)">
        <!-- AI -->
        <rect x="0" y="0" width="30" height="19" rx="9.5" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
        <text x="15" y="13" font-size="9" font-weight="600" fill="#94a3b8" text-anchor="middle" letter-spacing="0.3">AI</text>
        
        <!-- Systems -->
        <rect x="36" y="0" width="56" height="19" rx="9.5" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
        <text x="64" y="13" font-size="9" font-weight="600" fill="#94a3b8" text-anchor="middle" letter-spacing="0.3">Systems</text>

        <!-- Community (highlighted cyan) -->
        <rect x="98" y="0" width="70" height="19" rx="9.5" fill="#083344" stroke="#06b6d4" stroke-width="1" />
        <text x="133" y="13" font-size="9" font-weight="700" fill="#22d3ee" text-anchor="middle" letter-spacing="0.3">Community</text>

        <!-- Impact -->
        <rect x="174" y="0" width="48" height="19" rx="9.5" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
        <text x="198" y="13" font-size="9" font-weight="600" fill="#94a3b8" text-anchor="middle" letter-spacing="0.3">Impact</text>
      </g>
    </g>

    <!-- ================= 4 MILESTONE TILES ================= -->
    <!-- Tile 1 (Col 1, Row 1): 3rd Year / Undergraduate -->
    <g transform="translate(20, 206)">
      <rect width="170" height="48" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Purple icon box: Graduation Cap -->
      <rect x="8" y="8" width="32" height="32" rx="8" fill="#2e1065" stroke="#7c3aed" stroke-width="0.8" />
      <path d="M 16 23 L 24 19 L 32 23 L 24 27 Z M 18 25 L 18 29 C 18 31 30 31 30 29 L 30 25" fill="none" stroke="#c084fc" stroke-width="1.2" />
      <text x="48" y="23" font-size="12" font-weight="700" fill="#ffffff" letter-spacing="0.3">3rd Year</text>
      <text x="48" y="36" font-size="9.5" font-weight="500" fill="#64748b" letter-spacing="0.2">Undergraduate</text>
    </g>

    <!-- Tile 2 (Col 2, Row 1): AI Developer / Autonomous & Edge -->
    <g transform="translate(202, 206)">
      <rect width="173" height="48" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Cyan icon box: Code symbol -->
      <rect x="8" y="8" width="32" height="32" rx="8" fill="#083344" stroke="#06b6d4" stroke-width="0.8" />
      <path d="M 19 20 L 16 24 L 19 28 M 29 20 L 32 24 L 29 28 M 26 19 L 22 29" fill="none" stroke="#22d3ee" stroke-width="1.2" stroke-linecap="round" />
      <text x="48" y="23" font-size="12" font-weight="700" fill="#ffffff" letter-spacing="0.3">AI Developer</text>
      <text x="48" y="36" font-size="9.5" font-weight="500" fill="#64748b" letter-spacing="0.2">Autonomous &amp; Edge</text>
    </g>

    <!-- Tile 3 (Col 1, Row 2): 8.65 / 10 / CGPA -->
    <g transform="translate(20, 264)">
      <rect width="170" height="48" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Blue icon box: Score Chart -->
      <rect x="8" y="8" width="32" height="32" rx="8" fill="#172554" stroke="#3b82f6" stroke-width="0.8" />
      <path d="M 16 28 L 20 24 L 24 26 L 30 20 M 27 20 H 30 V 23" fill="none" stroke="#60a5fa" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
      <text x="48" y="23" font-size="12" font-weight="700" fill="#ffffff" letter-spacing="0.3">8.65 / 10</text>
      <text x="48" y="36" font-size="9.5" font-weight="500" fill="#64748b" letter-spacing="0.3">CGPA</text>
    </g>

    <!-- Tile 4 (Col 2, Row 2): Founder / TechVerse Solutions -->
    <g transform="translate(202, 264)">
      <rect width="173" height="48" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Teal icon box: Rocket / Company -->
      <rect x="8" y="8" width="32" height="32" rx="8" fill="#042f2e" stroke="#14b8a6" stroke-width="0.8" />
      <path d="M 26 18 C 23 18 20 21 20 24 C 20 27 22 29 26 29 C 26 25 29 23 29 20 C 28 19 27 18 26 18 Z M 19 25 L 17 27 M 24 30 L 24 32" fill="none" stroke="#2dd4bf" stroke-width="1.2" stroke-linecap="round" />
      <text x="48" y="23" font-size="12" font-weight="700" fill="#ffffff" letter-spacing="0.3">Founder</text>
      <text x="48" y="36" font-size="9" font-weight="500" fill="#64748b" letter-spacing="0.2">TechVerse Solutions</text>
    </g>

    <!-- ================= META LINKS ================= -->
    <g transform="translate(24, 340)">
      <!-- Location (Informational - not a link) -->
      <g transform="translate(0, 0)">
        <path d="M 5 0 C 2.2 0 0 2.2 0 5 C 0 8.5 5 13 5 13 C 5 13 10 8.5 10 5 C 10 2.2 7.8 0 5 0 Z M 5 6.5 C 4.2 6.5 3.5 5.8 3.5 5 C 3.5 4.2 4.2 3.5 5 3.5 C 5.8 3.5 6.5 4.2 6.5 5 C 6.5 5.8 5.8 6.5 5 6.5 Z" fill="#38bdf8" transform="scale(0.85)" />
        <text x="13" y="9" font-size="10" font-weight="500" fill="#94a3b8" letter-spacing="0.3">New Delhi, India</text>
      </g>
      
      <!-- LinkedIn -->
      <a href="https://www.linkedin.com/in/chakshuarora716/" target="_blank" style="text-decoration:none; cursor:pointer;">
        <g transform="translate(116, 0)">
          <rect x="0" y="0" width="11" height="11" rx="2" fill="#0a66c2" />
          <text x="2.5" y="8" font-size="7.5" font-weight="800" fill="#ffffff">in</text>
          <text x="15" y="9" font-size="10" font-weight="600" fill="#38bdf8" letter-spacing="0.3">LinkedIn</text>
        </g>
      </a>

      <!-- GitHub -->
      <a href="https://github.com/chakshubuilds" target="_blank" style="text-decoration:none; cursor:pointer;">
        <g transform="translate(194, 0)">
          <path d="M 6 0 C 2.7 0 0 2.7 0 6 C 0 8.7 1.7 10.9 4.1 11.7 C 4.4 11.8 4.5 11.6 4.5 11.4 L 4.5 10.4 C 2.8 10.8 2.5 9.6 2.5 9.6 C 2.2 8.9 1.8 8.7 1.8 8.7 C 1.3 8.3 1.9 8.3 1.9 8.3 C 2.5 8.3 2.8 8.9 2.8 8.9 C 3.3 9.8 4.2 9.5 4.5 9.4 C 4.6 9 4.7 8.7 4.9 8.6 C 3.6 8.4 2.2 7.9 2.2 5.7 C 2.2 5.1 2.4 4.5 2.8 4.1 C 2.7 3.9 2.5 3.3 2.9 2.4 C 2.9 2.4 3.4 2.2 4.5 3 C 5 2.8 5.5 2.8 6 2.8 C 6.5 2.8 7 2.8 7.5 3 C 8.6 2.2 9.1 2.4 9.1 2.4 C 9.5 3.3 9.3 3.9 9.2 4.1 C 9.6 4.5 9.8 5.1 9.8 5.7 C 9.8 7.9 8.4 8.4 7.1 8.6 C 7.3 8.8 7.5 9.1 7.5 9.6 L 7.5 11.4 C 7.5 11.6 7.6 11.8 7.9 11.7 C 10.3 10.9 12 8.7 12 6 C 12 2.7 9.3 0 6 0 Z" fill="#22d3ee" />
          <text x="16" y="9" font-size="10" font-weight="600" fill="#22d3ee" letter-spacing="0.3">GitHub</text>
        </g>
      </a>

      <!-- Email -->
      <a href="mailto:chakshuarora098@gmail.com" style="text-decoration:none; cursor:pointer;">
        <g transform="translate(266, 0)">
          <path d="M 0 1 C 0 0.4 0.4 0 1 0 L 11 0 C 11.6 0 12 0.4 12 1 L 12 9 C 12 9.6 11.6 10 11 10 L 1 10 C 0.4 10 0 9.6 0 9 Z M 1 2 L 6 5.5 L 11 2" fill="none" stroke="#10b981" stroke-width="1.1" />
          <text x="16" y="9" font-size="10" font-weight="600" fill="#10b981" letter-spacing="0.3">Email</text>
        </g>
      </a>
    </g>

    <!-- ================= CTA BUTTON ================= -->
    <a href="mailto:chakshuarora098@gmail.com" style="text-decoration:none; cursor:pointer;">
      <g transform="translate(20, 386)" class="btn-hover">
        <rect width="355" height="48" rx="14" fill="url(#btn-grad)" />
        <text x="177" y="29" font-size="13.5" font-weight="700" fill="#ffffff" text-anchor="middle" letter-spacing="0.6">Let's Build Something Meaningful  →</text>
      </g>
    </a>
  </g>

  <!-- ================= RIGHT TOP: CORE CAPABILITIES ================= -->
  <g transform="translate(435, 68)">
    <!-- Container -->
    <rect width="565" height="215" rx="16" fill="#080e1e" stroke="#1c284a" stroke-width="1.2" />

    <!-- Header -->
    <g transform="translate(20, 24)">
      <!-- Gear Cog Icon -->
      <circle cx="9" cy="9" r="8" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 2" />
      <circle cx="9" cy="9" r="3.5" fill="#38bdf8" />
      
      <text x="25" y="14" font-size="16" font-weight="800" fill="#ffffff" letter-spacing="0.4">Core<tspan dx="8" fill="url(#cyan-purple)">Capabilities</tspan></text>
      <text x="525" y="12" font-size="9" font-weight="700" fill="#64748b" text-anchor="end" letter-spacing="2">WHAT I WORK ON</text>
    </g>

    <!-- 4 Capability Cards (2x2 Grid) -->
    <!-- Card 1 (Top Left) -->
    <g transform="translate(20, 48)">
      <rect width="255" height="70" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Robot icon box -->
      <rect x="10" y="15" width="36" height="40" rx="8" fill="#2e1065" stroke="#7c3aed" stroke-width="0.8" />
      <path d="M 23 28 H 33 V 38 H 23 Z M 21 33 H 23 M 33 33 H 35 M 28 25 V 28 M 26 32 H 27 M 29 32 H 30" stroke="#c084fc" stroke-width="1.2" fill="none" />
      <text x="54" y="27" font-size="10.5" font-weight="700" fill="#ffffff" letter-spacing="0.2">Autonomous Multi-Agent Platforms</text>
      <text x="54" y="43" font-size="8.5" fill="#94a3b8" letter-spacing="0.1">
        <tspan x="54" dy="0">LangChain, memory streams, agentic tools,</tspan>
        <tspan x="54" dy="13">sub-50ms handoffs &amp; Orchestra AI</tspan>
      </text>
    </g>

    <!-- Card 2 (Top Right) -->
    <g transform="translate(290, 48)">
      <rect width="255" height="70" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- 3D Cube Edge IoT icon box -->
      <rect x="10" y="15" width="36" height="40" rx="8" fill="#042f2e" stroke="#14b8a6" stroke-width="0.8" />
      <path d="M 28 25 L 35 29 L 35 37 L 28 41 L 21 37 L 21 29 Z M 28 25 V 33 M 21 29 L 28 33 L 35 29" fill="none" stroke="#2dd4bf" stroke-width="1.2" stroke-linejoin="round" />
      <text x="54" y="27" font-size="10.5" font-weight="700" fill="#ffffff" letter-spacing="0.2">Edge Computer Vision &amp; IoT</text>
      <text x="54" y="43" font-size="8.5" fill="#94a3b8" letter-spacing="0.1">
        <tspan x="54" dy="0">YOLOv8 real-time detection, ESP32 sensor</tspan>
        <tspan x="54" dy="13">mesh, IEEE paper &amp; municipal patent</tspan>
      </text>
    </g>

    <!-- Card 3 (Bottom Left) -->
    <g transform="translate(20, 126)">
      <rect width="255" height="70" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Globe icon box -->
      <rect x="10" y="15" width="36" height="40" rx="8" fill="#451a03" stroke="#f59e0b" stroke-width="0.8" />
      <circle cx="28" cy="35" r="7" fill="none" stroke="#fbbf24" stroke-width="1.2" />
      <ellipse cx="28" cy="35" rx="3.5" ry="7" fill="none" stroke="#fbbf24" stroke-width="1" />
      <line x1="21" y1="35" x2="35" y2="35" stroke="#fbbf24" stroke-width="1" />
      <text x="54" y="27" font-size="10.5" font-weight="700" fill="#ffffff" letter-spacing="0.2">Full-Stack Web &amp; Event Systems</text>
      <text x="54" y="43" font-size="8.5" fill="#94a3b8" letter-spacing="0.1">
        <tspan x="54" dy="0">Next.js 15, TypeScript, WebSockets, real-time</tspan>
        <tspan x="54" dy="13">queues &amp; leaderboards (TechVerse)</tspan>
      </text>
    </g>

    <!-- Card 4 (Bottom Right) -->
    <g transform="translate(290, 126)">
      <rect width="255" height="70" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
      <!-- Analytics icon box -->
      <rect x="10" y="15" width="36" height="40" rx="8" fill="#4c0519" stroke="#f43f5e" stroke-width="0.8" />
      <rect x="23" y="36" width="2.5" height="6" fill="#fb7185" />
      <rect x="27.5" y="31" width="2.5" height="11" fill="#fb7185" />
      <rect x="32" y="26" width="2.5" height="16" fill="#fb7185" />
      <text x="54" y="27" font-size="10.5" font-weight="700" fill="#ffffff" letter-spacing="0.2">Data, Analytics &amp; ML Systems</text>
      <text x="54" y="43" font-size="8.5" fill="#94a3b8" letter-spacing="0.1">
        <tspan x="54" dy="0">Python, PyTorch, TensorFlow, Power BI,</tspan>
        <tspan x="54" dy="13">predictive models &amp; high-impact datasets</tspan>
      </text>
    </g>
  </g>

  <!-- ================= RIGHT BOTTOM: CURRENTLY BUILDING ================= -->
  <g transform="translate(435, 288)">
    <!-- Main Card Body -->
    <rect width="565" height="240" rx="16" fill="#080e1e" stroke="#1c284a" stroke-width="1.2" />

    <!-- Header (shifted up, builder button removed) -->
    <g transform="translate(20, 18)">
      <!-- Folder Icon -->
      <path d="M 3 5 H 8 L 10 7 H 17 V 15 H 3 Z" fill="none" stroke="#38bdf8" stroke-width="1.4" stroke-linejoin="round" />
      <text x="25" y="14" font-size="16" font-weight="800" fill="#ffffff" letter-spacing="0.4">Currently<tspan dx="8" fill="url(#cyan-purple)">Building</tspan></text>
    </g>

    <!-- Inner Bento Container -->
    <g transform="translate(16, 40)">
      <!-- Card background -->
      <rect width="533" height="182" rx="14" fill="#0b1329" />

      <!-- Clipped Image touching top, right, and bottom boundaries of the container -->
      <g clip-path="url(#bento-container-clip)">
        <image href="data:image/png;base64,{d_b64}" x="305" y="0" width="228" height="182" preserveAspectRatio="xMidYMid slice" />
        <rect x="305" y="0" width="55" height="182" fill="url(#desk-edge-fade)" />
      </g>

      <!-- Card container border -->
      <rect width="533" height="182" rx="14" fill="none" stroke="#1e293b" stroke-width="1" />

      <!-- Left Text Content -->
      <g transform="translate(18, 18)">
        <!-- Green NOW Pill -->
        <rect x="0" y="0" width="38" height="18" rx="9" fill="#059669" />
        <text x="19" y="12.5" font-size="8.5" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="0.8">NOW</text>
        
        <!-- Heading -->
        <text x="46" y="13" font-size="12" font-weight="800" fill="#ffffff">2:47 AM <tspan dx="4" fill="#38bdf8">·</tspan><tspan dx="4">Deep Work Sprints &amp; Flow State</tspan></text>

        <!-- Paragraph Description -->
        <text x="0" y="42" font-size="10.5" fill="#94a3b8" letter-spacing="0.15">
          <tspan x="0" dy="0">Thriving in midnight flow sessions where complex agent</tspan>
          <tspan x="0" dy="17">architectures crystalize. Guided by Clean Code &amp; Pragmatic</tspan>
          <tspan x="0" dy="17">Programming principles.</tspan>
        </text>

        <!-- 5 Hashtag Pills (Clean Two-Row Grid with ample spacing) -->
        <g transform="translate(0, 105)">
          <!-- Row 1 -->
          <rect x="0" y="0" width="76" height="19" rx="9.5" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="38" y="13" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle" letter-spacing="0.3">#DeepWork</text>

          <rect x="84" y="0" width="94" height="19" rx="9.5" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="131" y="13" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle" letter-spacing="0.3">#SystemDesign</text>

          <rect x="186" y="0" width="76" height="19" rx="9.5" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="224" y="13" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle" letter-spacing="0.3">#ShipCraft</text>

          <!-- Row 2 -->
          <rect x="0" y="24" width="108" height="19" rx="9.5" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="54" y="37" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle" letter-spacing="0.3">#ZeroDistractions</text>

          <rect x="116" y="24" width="116" height="19" rx="9.5" fill="#0f172a" stroke="#1e293b" stroke-width="0.8" />
          <text x="174" y="37" font-size="8.5" font-weight="600" fill="#38bdf8" text-anchor="middle" letter-spacing="0.3">#ContinuousBuilder</text>
        </g>
      </g>
    </g>
  </g>
</svg>'''

    with open('assets/about-life.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Successfully generated assets/about-life.svg (size: %d bytes)" % len(svg))

if __name__ == '__main__':
    generate_about()
