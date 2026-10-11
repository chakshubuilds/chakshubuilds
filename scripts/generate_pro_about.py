from PIL import Image
import io, base64

img = Image.open('assets/portrait_clean.png')
img.thumbnail((260, 280), Image.Resampling.LANCZOS)
buf = io.BytesIO()
img.save(buf, format='PNG', optimize=True)
clean_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 460" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Cascadia+Code:wght@400;600;700&amp;family=Inter:wght@400;500;600;700;800&amp;display=swap');
      .mono {{ font-family: 'Cascadia Code', monospace; }}
      .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }}

      /* 3 Progress Bars (12s cycle, 4s each) */
      @keyframes bar-prog-1 {{
        0% {{ width: 0px; }}
        28% {{ width: 140px; }}
        33.3%, 100% {{ width: 140px; }}
      }}
      @keyframes bar-prog-2 {{
        0%, 33.3% {{ width: 0px; }}
        61% {{ width: 140px; }}
        66.6%, 100% {{ width: 140px; }}
      }}
      @keyframes bar-prog-3 {{
        0%, 66.6% {{ width: 0px; }}
        94% {{ width: 140px; }}
        100% {{ width: 140px; }}
      }}
      .pfill-1 {{ animation: bar-prog-1 12s cubic-bezier(0.16, 1, 0.3, 1) infinite; }}
      .pfill-2 {{ animation: bar-prog-2 12s cubic-bezier(0.16, 1, 0.3, 1) infinite; }}
      .pfill-3 {{ animation: bar-prog-3 12s cubic-bezier(0.16, 1, 0.3, 1) infinite; }}

      /* 3 Carousel Slides */
      @keyframes cslide-1 {{
        0%, 28% {{ opacity: 1; transform: translateY(0); }}
        33.3%, 96% {{ opacity: 0; transform: translateY(6px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes cslide-2 {{
        0%, 28% {{ opacity: 0; transform: translateY(6px); }}
        33.3%, 61% {{ opacity: 1; transform: translateY(0); }}
        66.6%, 100% {{ opacity: 0; transform: translateY(6px); }}
      }}
      @keyframes cslide-3 {{
        0%, 61% {{ opacity: 0; transform: translateY(6px); }}
        66.6%, 94% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 0; transform: translateY(6px); }}
      }}
      .cslide-item-1 {{ animation: cslide-1 12s infinite; }}
      .cslide-item-2 {{ animation: cslide-2 12s infinite; }}
      .cslide-item-3 {{ animation: cslide-3 12s infinite; }}

      @keyframes radar-pulse {{
        0%, 100% {{ transform: scale(1); opacity: 0.9; }}
        50% {{ transform: scale(1.2); opacity: 0.4; }}
      }}
      .pulse-dot {{ animation: radar-pulse 2s ease-in-out infinite; transform-origin: 22px 22px; }}
    </style>

    <pattern id="abt-dots-2" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="rgba(36, 123, 255, 0.12)" />
    </pattern>

    <linearGradient id="abt-neon-bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#247bff" />
      <stop offset="50%" stop-color="#00f0ff" />
      <stop offset="100%" stop-color="#ff354f" />
    </linearGradient>

    <linearGradient id="avatar-frame-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#247bff" />
      <stop offset="50%" stop-color="#00f0ff" />
      <stop offset="100%" stop-color="#ff354f" />
    </linearGradient>

    <clipPath id="abt-avatar-clip">
      <rect x="0" y="0" width="86" height="102" rx="12" />
    </clipPath>
  </defs>

  <!-- Container -->
  <rect width="920" height="460" rx="16" fill="#070b16" stroke="#1c284a" stroke-width="1.5" />
  <rect width="920" height="460" rx="16" fill="url(#abt-dots-2)" />
  <path d="M 16 0 L 904 0" stroke="url(#abt-neon-bar)" stroke-width="2.5" />

  <!-- Main Grid: Left Identity Card (width 320) + Right Matrix (width 536) -->
  <g transform="translate(28, 28)">

    <!-- ================= LEFT IDENTITY CARD ================= -->
    <g transform="translate(0, 0)">
      <rect width="324" height="404" rx="14" fill="#090f20" stroke="#1c284a" stroke-width="1.2" />

      <!-- Card Top Bar -->
      <g transform="translate(18, 16)">
        <rect width="134" height="20" rx="4" fill="#070b16" stroke="#247bff" stroke-width="0.8" />
        <circle cx="10" cy="10" r="3.5" fill="#10b981" class="pulse-dot" />
        <text x="18" y="14" class="mono" font-size="9.5" font-weight="700" fill="#247bff">IDENTITY_MATRIX</text>
        <text x="288" y="14" text-anchor="end" class="mono" font-size="9.5" fill="#5a7099">BUILDER // 2026</text>
      </g>

      <!-- Avatar + Name Header Row -->
      <g transform="translate(18, 48)">
        <!-- Photo Frame -->
        <g>
          <rect x="-2" y="-2" width="90" height="106" rx="14" fill="none" stroke="url(#avatar-frame-grad)" stroke-width="1.5" />
          <g clip-path="url(#abt-avatar-clip)">
            <rect width="86" height="102" fill="#050811" />
            <image x="-6" y="-4" width="98" height="110" preserveAspectRatio="xMidYMid slice" href="data:image/png;base64,{clean_b64}" />
          </g>
        </g>

        <!-- Name & Bio -->
        <g transform="translate(102, 6)">
          <text x="0" y="20" class="sans" font-size="19" font-weight="800" fill="#f8fafc">Chakshu Arora</text>
          <text x="0" y="38" class="mono" font-size="11" font-weight="600" fill="#247bff">AI &amp; Systems Builder</text>
          <text x="0" y="56" class="sans" font-size="11.5" fill="#8ba0c8">B.Tech AI Scholar @ VIPS-TC</text>
          <rect x="0" y="68" width="168" height="20" rx="5" fill="#070b16" stroke="#10b981" stroke-width="0.8" />
          <circle cx="8" cy="78" r="3" fill="#10b981" />
          <text x="16" y="82" class="mono" font-size="9" font-weight="700" fill="#10b981">STATUS: ACTIVE RESEARCH</text>
        </g>
      </g>

      <!-- 4 Verified Highlights Tiles -->
      <g transform="translate(18, 172)">
        <!-- Tile 1 -->
        <g transform="translate(0, 0)">
          <rect width="288" height="48" rx="8" fill="#0d1428" stroke="#182442" />
          <circle cx="18" cy="24" r="10" fill="rgba(36, 123, 255, 0.15)" />
          <text x="14" y="28" class="mono" font-size="12" fill="#247bff">🎓</text>
          <text x="36" y="20" class="sans" font-size="12" font-weight="700" fill="#f8fafc">B.Tech CSE (AI) · CGPA: 8.57 / 10</text>
          <text x="36" y="36" class="sans" font-size="10.5" fill="#8ba0c8">VIPS-TC (2024–2028) Undergraduate</text>
        </g>

        <!-- Tile 2 -->
        <g transform="translate(0, 56)">
          <rect width="288" height="48" rx="8" fill="#0d1428" stroke="#182442" />
          <circle cx="18" cy="24" r="10" fill="rgba(255, 53, 79, 0.15)" />
          <text x="14" y="28" class="mono" font-size="12" fill="#ff354f">🏆</text>
          <text x="36" y="20" class="sans" font-size="12" font-weight="700" fill="#f8fafc">2nd Place / 8,000+ Developers</text>
          <text x="36" y="36" class="sans" font-size="10.5" fill="#8ba0c8">Zero Limit Hackathon · CodeChrono Platform</text>
        </g>

        <!-- Tile 3 -->
        <g transform="translate(0, 112)">
          <rect width="288" height="48" rx="8" fill="#0d1428" stroke="#182442" />
          <circle cx="18" cy="24" r="10" fill="rgba(0, 240, 255, 0.15)" />
          <text x="14" y="28" class="mono" font-size="12" fill="#00f0ff">🔬</text>
          <text x="36" y="20" class="sans" font-size="12" font-weight="700" fill="#f8fafc">1 Patent &amp; 1 IEEE Research Paper</text>
          <text x="36" y="36" class="sans" font-size="10.5" fill="#8ba0c8">Edge AI Sensor IoT Analytics · IIIT-Delhi</text>
        </g>

        <!-- Tile 4 -->
        <g transform="translate(0, 168)">
          <rect width="288" height="48" rx="8" fill="#0d1428" stroke="#182442" />
          <circle cx="18" cy="24" r="10" fill="rgba(16, 185, 129, 0.15)" />
          <text x="14" y="28" class="mono" font-size="12" fill="#10b981">🚀</text>
          <text x="36" y="20" class="sans" font-size="12" font-weight="700" fill="#f8fafc">Founder @ TechVerse Solutions</text>
          <text x="36" y="36" class="sans" font-size="10.5" fill="#8ba0c8">Scaling 500+ Student Developer Community</text>
        </g>
      </g>
    </g>

    <!-- ================= RIGHT COLUMN (width 526) ================= -->
    <g transform="translate(340, 0)">

      <!-- Top: 3 Core Capabilities Matrix -->
      <g transform="translate(0, 0)">
        <rect width="524" height="194" rx="14" fill="#090f20" stroke="#1c284a" stroke-width="1.2" />

        <g transform="translate(18, 16)">
          <rect width="144" height="20" rx="4" fill="#070b16" stroke="#00f0ff" stroke-width="0.8" />
          <text x="8" y="14" class="mono" font-size="9.5" font-weight="700" fill="#00f0ff">CORE_CAPABILITIES</text>
          <text x="488" y="14" text-anchor="end" class="mono" font-size="9.5" fill="#5a7099">PRODUCTION DOMAINS</text>
        </g>

        <!-- Pillar 1 -->
        <g transform="translate(18, 44)">
          <rect width="488" height="42" rx="7" fill="#0d1428" stroke="#182442" />
          <circle cx="18" cy="21" r="8" fill="rgba(36, 123, 255, 0.18)" />
          <text x="14" y="25" class="mono" font-size="10" fill="#247bff">⚡</text>
          <text x="34" y="18" class="sans" font-size="12" font-weight="700" fill="#f8fafc">Autonomous Multi-Agent Platforms</text>
          <text x="34" y="32" class="sans" font-size="10.5" fill="#8ba0c8">LangChain, context-preserving memory streams, sub-50ms tool handoffs (Orchestra AI)</text>
        </g>

        <!-- Pillar 2 -->
        <g transform="translate(18, 92)">
          <rect width="488" height="42" rx="7" fill="#0d1428" stroke="#182442" />
          <circle cx="18" cy="21" r="8" fill="rgba(255, 53, 79, 0.18)" />
          <text x="14" y="25" class="mono" font-size="10" fill="#ff354f">🔬</text>
          <text x="34" y="18" class="sans" font-size="12" font-weight="700" fill="#f8fafc">Edge Computer Vision &amp; Connected IoT</text>
          <text x="34" y="32" class="sans" font-size="10.5" fill="#8ba0c8">YOLOv8 real-time detection, ESP32 sensor mesh, IEEE paper &amp; municipal patent</text>
        </g>

        <!-- Pillar 3 -->
        <g transform="translate(18, 140)">
          <rect width="488" height="42" rx="7" fill="#0d1428" stroke="#182442" />
          <circle cx="18" cy="21" r="8" fill="rgba(0, 240, 255, 0.18)" />
          <text x="14" y="25" class="mono" font-size="10" fill="#00f0ff">🌐</text>
          <text x="34" y="18" class="sans" font-size="12" font-weight="700" fill="#f8fafc">Resilient Full-Stack Web &amp; Event Platforms</text>
          <text x="34" y="32" class="sans" font-size="10.5" fill="#8ba0c8">Next.js 15, TypeScript, WebSockets, real-time queues &amp; leaderboards (TechVerse)</text>
        </g>
      </g>

      <!-- Bottom: 3-Slide Auto-Rotating Philosophy Carousel -->
      <g transform="translate(0, 206)">
        <rect width="524" height="198" rx="14" fill="#090f20" stroke="#1c284a" stroke-width="1.2" />

        <!-- Header + 3 Segment Progress Bars -->
        <g transform="translate(18, 16)">
          <text x="0" y="12" class="mono" font-size="10.5" font-weight="700" fill="#ff354f">PHILOSOPHY &amp; EXPEDITIONS</text>

          <!-- 3 Progress Segments -->
          <g transform="translate(230, 6)">
            <rect x="0" y="0" width="76" height="4" rx="2" fill="#141e36" />
            <rect x="0" y="0" width="0" height="4" rx="2" fill="#247bff" class="pfill-1" />

            <rect x="88" y="0" width="76" height="4" rx="2" fill="#141e36" />
            <rect x="88" y="0" width="0" height="4" rx="2" fill="#00f0ff" class="pfill-2" />

            <rect x="176" y="0" width="76" height="4" rx="2" fill="#141e36" />
            <rect x="176" y="0" width="0" height="4" rx="2" fill="#ff354f" class="pfill-3" />
          </g>
        </g>

        <!-- Slide 1 -->
        <g class="cslide-item-1" transform="translate(18, 42)">
          <rect width="488" height="138" rx="10" fill="#0d1428" stroke="#182442" />
          <rect x="14" y="14" width="138" height="20" rx="4" fill="#070b16" stroke="#247bff" stroke-width="0.8" />
          <text x="20" y="28" class="mono" font-size="10" font-weight="700" fill="#247bff">01 // NOCTURNAL DEV</text>
          <text x="14" y="58" class="sans" font-size="15" font-weight="700" fill="#f8fafc">2:47 AM Deep Work Sprints &amp; Flow State</text>
          <text x="14" y="80" class="sans" font-size="12" fill="#94a3b8">Thriving in midnight flow sessions where complex agent architectures</text>
          <text x="14" y="98" class="sans" font-size="12" fill="#94a3b8">crystallize. Guided by Clean Code &amp; Pragmatic Programmer principles.</text>
          <text x="14" y="122" class="mono" font-size="10.5" fill="#247bff">TAGS: #DeepWork #SystemDesign #ZeroDistractions #ShipCraft</text>
        </g>

        <!-- Slide 2 -->
        <g class="cslide-item-2" transform="translate(18, 42)">
          <rect width="488" height="138" rx="10" fill="#0d1428" stroke="#182442" />
          <rect x="14" y="14" width="155" height="20" rx="4" fill="#070b16" stroke="#00f0ff" stroke-width="0.8" />
          <text x="20" y="28" class="mono" font-size="10" font-weight="700" fill="#00f0ff">02 // ECOSYSTEM LEAD</text>
          <text x="14" y="58" class="sans" font-size="15" font-weight="700" fill="#f8fafc">TechVerse Founder &amp; Community Building</text>
          <text x="14" y="80" class="sans" font-size="12" fill="#94a3b8">Empowering 500+ student developers across university campuses</text>
          <text x="14" y="98" class="sans" font-size="12" fill="#94a3b8">with hands-on AI workshops, hackathons, and builder incubators.</text>
          <text x="14" y="122" class="mono" font-size="10.5" fill="#00f0ff">TAGS: #CommunityFounder #Hackathons #Mentorship #OpenLearning</text>
        </g>

        <!-- Slide 3 -->
        <g class="cslide-item-3" transform="translate(18, 42)">
          <rect width="488" height="138" rx="10" fill="#0d1428" stroke="#182442" />
          <rect x="14" y="14" width="168" height="20" rx="4" fill="#070b16" stroke="#ff354f" stroke-width="0.8" />
          <text x="20" y="28" class="mono" font-size="10" font-weight="700" fill="#ff354f">03 // HARDWARE HACKING</text>
          <text x="14" y="58" class="sans" font-size="15" font-weight="700" fill="#f8fafc">Soldering Iron, ESP32 &amp; Silicon Circuits</text>
          <text x="14" y="80" class="sans" font-size="12" fill="#94a3b8">Connecting software to the physical edge. Soldering circuits, tuning</text>
          <text x="14" y="98" class="sans" font-size="12" fill="#94a3b8">I2C sensors, and compiling embedded C++ for low-power edge compute.</text>
          <text x="14" y="122" class="mono" font-size="10.5" fill="#ff354f">TAGS: #IoT #ESP32 #HardwarePrototyping #EdgeSensors</text>
        </g>

      </g>
    </g>
  </g>
</svg>'''

with open('assets/about-life.svg', 'w', encoding='utf-8') as f:
    f.write(about_svg)

print("Generated new assets/about-life.svg")
