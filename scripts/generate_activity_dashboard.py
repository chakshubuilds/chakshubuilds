import os

activity_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 310" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Cascadia+Code:wght@400;600;700&amp;family=Inter:wght@400;500;600;700;800&amp;display=swap');
      .font-mono { font-family: 'Cascadia Code', monospace; }
      .font-sans { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }

      @keyframes radar-ping {
        0% { transform: scale(1); opacity: 0.9; }
        50% { transform: scale(1.3); opacity: 0.3; }
        100% { transform: scale(1); opacity: 0.9; }
      }
      .beacon { animation: radar-ping 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; transform-origin: 22px 22px; }

      @keyframes wave-glow {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 1; }
      }
      .sparkline { animation: wave-glow 2.5s ease-in-out infinite; }

      @keyframes bar-fill-1 { from { width: 0px; } to { width: 148px; } }
      @keyframes bar-fill-2 { from { width: 0px; } to { width: 105px; } }
      @keyframes bar-fill-3 { from { width: 0px; } to { width: 63px; } }
      @keyframes bar-fill-4 { from { width: 0px; } to { width: 35px; } }
      .bar-1 { animation: bar-fill-1 1.6s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
      .bar-2 { animation: bar-fill-2 1.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
      .bar-3 { animation: bar-fill-3 2.0s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
      .bar-4 { animation: bar-fill-4 2.2s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
    </style>

    <pattern id="act-dots" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="rgba(36, 123, 255, 0.12)" />
    </pattern>

    <linearGradient id="act-top-bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#247bff" />
      <stop offset="50%" stop-color="#00f0ff" />
      <stop offset="100%" stop-color="#ff354f" />
    </linearGradient>

    <linearGradient id="spark-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#247bff" />
      <stop offset="50%" stop-color="#00f0ff" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>

    <linearGradient id="spark-area" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="rgba(0, 240, 255, 0.25)" />
      <stop offset="100%" stop-color="rgba(0, 240, 255, 0)" />
    </linearGradient>
  </defs>

  <!-- Container -->
  <rect width="920" height="310" rx="16" fill="#070b16" stroke="#1c284a" stroke-width="1.5" />
  <rect width="920" height="310" rx="16" fill="url(#act-dots)" />
  <path d="M 16 0 L 904 0" stroke="url(#act-top-bar)" stroke-width="2.5" />

  <!-- Header -->
  <g transform="translate(32, 24)">
    <rect x="0" y="0" width="176" height="24" rx="12" fill="#090f20" stroke="#182442" />
    <circle cx="12" cy="12" r="4.5" fill="#10b981" class="beacon" />
    <circle cx="12" cy="12" r="4.5" fill="#10b981" />
    <text x="24" y="16" class="font-mono" font-size="11" font-weight="700" fill="#10b981">LIVE_TELEMETRY</text>
    <text x="188" y="16" class="font-mono" font-size="11" fill="#5a7099">GITHUB RUNTIME TELEMETRY</text>
    <text x="0" y="52" class="font-sans" font-size="22" font-weight="800" fill="#f8fafc" letter-spacing="-0.3">Engineering Activity &amp; Velocity</text>
    <text x="0" y="70" class="font-sans" font-size="12.5" fill="#8ba0c8">Real-time metrics, commit velocity, autonomous agent handoffs, and domain distribution.</text>
  </g>

  <!-- 3 Dashboard Panels -->
  <g transform="translate(32, 108)">

    <!-- Panel 1: Activity Stats & Sprints -->
    <g transform="translate(0, 0)">
      <rect width="270" height="178" rx="12" fill="#0d1326" stroke="#1c284a" stroke-width="1.2" />
      <rect x="16" y="14" width="105" height="20" rx="4" fill="#090f20" stroke="#247bff" stroke-width="0.8" />
      <text x="24" y="28" class="font-mono" font-size="10" font-weight="700" fill="#247bff">01 // VELOCITY</text>

      <!-- Stat 1 -->
      <g transform="translate(16, 46)">
        <text x="0" y="20" class="font-mono" font-size="24" font-weight="800" fill="#f8fafc">100%</text>
        <text x="76" y="16" class="font-mono" font-size="10" font-weight="700" fill="#10b981">● OPERATIONAL</text>
        <text x="0" y="36" class="font-sans" font-size="11.5" fill="#8ba0c8">Active Continuous Builder Mode</text>
      </g>

      <!-- Stat 2 -->
      <g transform="translate(16, 96)">
        <text x="0" y="20" class="font-mono" font-size="24" font-weight="800" fill="#00f0ff">&gt;99.4%</text>
        <text x="96" y="16" class="font-mono" font-size="10" font-weight="700" fill="#00f0ff">HIGH PRECISION</text>
        <text x="0" y="36" class="font-sans" font-size="11.5" fill="#8ba0c8">Agent Tool Routing &amp; CI/CD Flow</text>
      </g>

      <!-- Status Footer -->
      <a href="https://github.com/chakshubuilds" target="_blank" style="text-decoration:none; cursor:pointer;">
        <rect x="16" y="142" width="238" height="22" rx="6" fill="#090f20" stroke="#182442" />
        <text x="24" y="157" class="font-mono" font-size="9.5" font-weight="600" fill="#247bff">STATUS: SHIPPING @ CHAKSHUBUILDS</text>
      </a>
    </g>

    <!-- Panel 2: Domain Breakdown (Visual Glowing Progress Bars) -->
    <g transform="translate(286, 0)">
      <rect width="284" height="178" rx="12" fill="#0d1326" stroke="#1c284a" stroke-width="1.2" />
      <rect x="16" y="14" width="135" height="20" rx="4" fill="#090f20" stroke="#00f0ff" stroke-width="0.8" />
      <text x="24" y="28" class="font-mono" font-size="10" font-weight="700" fill="#00f0ff">02 // DOMAIN_RATIO</text>

      <!-- Bar 1: AI & Agents -->
      <g transform="translate(16, 44)">
        <text x="0" y="12" class="font-sans" font-size="11.5" font-weight="600" fill="#f8fafc">AI Agents &amp; PyTorch</text>
        <text x="252" y="12" text-anchor="end" class="font-mono" font-size="11" font-weight="700" fill="#247bff">42%</text>
        <rect x="0" y="18" width="252" height="6" rx="3" fill="#090f20" />
        <rect x="0" y="18" width="105" height="6" rx="3" fill="#247bff" class="bar-1" />
      </g>

      <!-- Bar 2: Full-Stack -->
      <g transform="translate(16, 76)">
        <text x="0" y="12" class="font-sans" font-size="11.5" font-weight="600" fill="#f8fafc">Full-Stack &amp; Next.js 15</text>
        <text x="252" y="12" text-anchor="end" class="font-mono" font-size="11" font-weight="700" fill="#00f0ff">30%</text>
        <rect x="0" y="18" width="252" height="6" rx="3" fill="#090f20" />
        <rect x="0" y="18" width="75" height="6" rx="3" fill="#00f0ff" class="bar-2" />
      </g>

      <!-- Bar 3: IoT Edge -->
      <g transform="translate(16, 108)">
        <text x="0" y="12" class="font-sans" font-size="11.5" font-weight="600" fill="#f8fafc">IoT Edge &amp; Computer Vision</text>
        <text x="252" y="12" text-anchor="end" class="font-mono" font-size="11" font-weight="700" fill="#ff354f">18%</text>
        <rect x="0" y="18" width="252" height="6" rx="3" fill="#090f20" />
        <rect x="0" y="18" width="45" height="6" rx="3" fill="#ff354f" class="bar-3" />
      </g>

      <!-- Bar 4: Cloud & DevOps -->
      <g transform="translate(16, 140)">
        <text x="0" y="12" class="font-sans" font-size="11.5" font-weight="600" fill="#f8fafc">AWS, Docker &amp; CI/CD</text>
        <text x="252" y="12" text-anchor="end" class="font-mono" font-size="11" font-weight="700" fill="#10b981">10%</text>
        <rect x="0" y="18" width="252" height="6" rx="3" fill="#090f20" />
        <rect x="0" y="18" width="25" height="6" rx="3" fill="#10b981" class="bar-4" />
      </g>
    </g>

    <!-- Panel 3: Velocity Waveform Sparkline & Milestones -->
    <g transform="translate(586, 0)">
      <rect width="270" height="178" rx="12" fill="#0d1326" stroke="#1c284a" stroke-width="1.2" />
      <rect x="16" y="14" width="132" height="20" rx="4" fill="#090f20" stroke="#10b981" stroke-width="0.8" />
      <text x="24" y="28" class="font-mono" font-size="10" font-weight="700" fill="#10b981">03 // COMMIT_BURST</text>

      <!-- Mini Sparkline Waveform -->
      <g transform="translate(16, 42)">
        <path d="M 0 38 Q 20 10, 45 32 T 90 14 T 135 28 T 180 8 T 215 22 T 238 6 L 238 48 L 0 48 Z" fill="url(#spark-area)" />
        <path d="M 0 38 Q 20 10, 45 32 T 90 14 T 135 28 T 180 8 T 215 22 T 238 6" fill="none" stroke="url(#spark-grad)" stroke-width="2.2" class="sparkline" />
      </g>

      <!-- Verified Milestone Tags -->
      <g transform="translate(16, 102)">
        <rect width="238" height="20" rx="4" fill="#090f20" stroke="#182442" />
        <text x="8" y="14" class="mono" font-size="9" fill="#f8fafc">🏆 2nd Place / 8k+ Devs (Zero Limit)</text>
      </g>
      <g transform="translate(16, 126)">
        <rect width="238" height="20" rx="4" fill="#090f20" stroke="#182442" />
        <text x="8" y="14" class="mono" font-size="9" fill="#f8fafc">📜 1 Patent &amp; 1 IEEE Research Paper</text>
      </g>
      <g transform="translate(16, 150)">
        <rect width="238" height="20" rx="4" fill="#090f20" stroke="#182442" />
        <text x="8" y="14" class="mono" font-size="9" fill="#f8fafc">🚀 Founder @ TechVerse Solutions</text>
      </g>
    </g>

  </g>
</svg>'''

with open('assets/activity-dashboard.svg', 'w', encoding='utf-8') as f:
    f.write(activity_svg)

print("Generated assets/activity-dashboard.svg")
