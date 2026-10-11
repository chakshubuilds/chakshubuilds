import math
import random
import numpy as np
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

def generate_banner(is_dark=True):
    # Palette
    if is_dark:
        bg_col = "#0A101F"
        card_bg = "#070b16"
        border_col = "#1c284a"
        portrait_col = "#A78BFA"
        ui_chrome = "#22D3EE"
        accent_col = "#10B981"
        text_primary = "#f8fafc"
        text_muted = "#94a3b8"
        leader_col = "rgba(34, 211, 238, 0.22)"
        pill_bg = "#0b1224"
        tab_bg = "#0d1428"
    else:
        bg_col = "#f1f5f9"
        card_bg = "#ffffff"
        border_col = "#cbd5e1"
        portrait_col = "#7C3AED"
        ui_chrome = "#0891B2"
        accent_col = "#059669"
        text_primary = "#0f172a"
        text_muted = "#475569"
        leader_col = "rgba(8, 145, 178, 0.25)"
        pill_bg = "#e2e8f0"
        tab_bg = "#e2e8f0"

    # Dithering Portrait
    im = Image.open('assets/portrait_clean.png').convert('RGBA')
    W_GRID, H_GRID = 300, 340
    im_resized = im.resize((W_GRID, H_GRID), Image.Resampling.LANCZOS)
    alpha = np.array(im_resized.split()[3])
    gray = np.array(im_resized.convert('L'))

    if is_dark:
        gray[alpha < 128] = 0
    else:
        # In light mode, transparent parts become white (255)
        gray[alpha < 128] = 255

    pil_gray = Image.fromarray(gray)
    enhancer = ImageEnhance.Contrast(pil_gray)
    pil_gray = enhancer.enhance(1.3)
    pil_gray = ImageOps.autocontrast(pil_gray, cutoff=1)
    pil_gray = pil_gray.filter(ImageFilter.UnsharpMask(radius=3, percent=140))

    arr = np.array(pil_gray, dtype=float)
    if is_dark:
        arr[alpha < 128] = 0.0

    binary = np.zeros((H_GRID, W_GRID), dtype=np.uint8)

    for y in range(H_GRID):
        if y % 2 == 0:
            xs = range(W_GRID)
            direction = 1
        else:
            xs = range(W_GRID - 1, -1, -1)
            direction = -1

        for x in xs:
            old_val = arr[y, x]
            if is_dark and alpha[y, x] < 128:
                new_val = 0
                err = 0
            else:
                if is_dark:
                    new_val = 255 if old_val >= 128 else 0
                else:
                    new_val = 0 if old_val < 128 else 255
                err = old_val - new_val

            if is_dark:
                binary[y, x] = 1 if new_val == 255 else 0
            else:
                binary[y, x] = 1 if new_val == 0 else 0

            # Distribute error
            if direction == 1:
                if x + 1 < W_GRID:
                    arr[y, x + 1] += err * 7 / 16
                if y + 1 < H_GRID:
                    if x - 1 >= 0:
                        arr[y + 1, x - 1] += err * 3 / 16
                    arr[y + 1, x] += err * 5 / 16
                    if x + 1 < W_GRID:
                        arr[y + 1, x + 1] += err * 1 / 16
            else:
                if x - 1 >= 0:
                    arr[y, x - 1] += err * 7 / 16
                if y + 1 < H_GRID:
                    if x + 1 < W_GRID:
                        arr[y + 1, x + 1] += err * 3 / 16
                    arr[y + 1, x] += err * 5 / 16
                    if x - 1 >= 0:
                        arr[y + 1, x - 1] += err * 1 / 16

    # Convert binary grid into path runs
    # Frame coordinates: x=34, y=72, w=400, h=505
    # Grid offset: x_off = 36, y_off = 100, dot_scale = 1.32 (width), 1.34 (height)
    sx = 1.32
    sy = 1.35
    ox = 38
    oy = 102

    # Group runs into 60 random interleaved groups for shimmer entrance
    random.seed(42)
    NUM_GROUPS = 60
    group_paths = {i: [] for i in range(NUM_GROUPS)}

    for y in range(H_GRID):
        row = binary[y]
        in_run = False
        start_x = 0
        for x in range(W_GRID):
            if row[x] == 1 and not in_run:
                in_run = True
                start_x = x
            elif row[x] == 0 and in_run:
                in_run = False
                run_len = x - start_x
                # Assign to random group
                grp = random.randint(0, NUM_GROUPS - 1)
                px = ox + start_x * sx
                py = oy + y * sy
                pw = run_len * sx
                group_paths[grp].append(f"M {px:.1f} {py:.1f} h {pw:.1f}")
        if in_run:
            run_len = W_GRID - start_x
            grp = random.randint(0, NUM_GROUPS - 1)
            px = ox + start_x * sx
            py = oy + y * sy
            pw = run_len * sx
            group_paths[grp].append(f"M {px:.1f} {py:.1f} h {pw:.1f}")

    # Build group path SVG elements with staggered opacity
    dots_svg_parts = []
    for grp_idx in range(NUM_GROUPS):
        if group_paths[grp_idx]:
            d_str = " ".join(group_paths[grp_idx])
            delay = (grp_idx / NUM_GROUPS) * 1.8
            dots_svg_parts.append(
                f'<path d="{d_str}" stroke="{portrait_col}" stroke-width="1.3" shape-rendering="crispEdges" '
                f'class="dither-grp" style="animation-delay: {delay:.2f}s;" />'
            )
    dots_svg = "\n    ".join(dots_svg_parts)

    # Info panel rows (Font-size 14, spacing 23px)
    rows_data = [
        ("Subject", "Chakshu Arora"),
        ("Role", "AI Agent Architect & Full-Stack Builder"),
        ("Origin", "New Delhi, India"),
        ("Education", "B.Tech CSE (AI) · VIPS-TC (CGPA 8.57)"),
        ("Status", "Building + Learning + Shipping"),
        ("ToolChain", "VS Code · Git · Docker · Linux · Postman"),
        ("Core.Lang", "Python · TypeScript · C++ · SQL"),
        ("Core.Frontend", "Next.js 15 · React · Tailwind CSS"),
        ("Core.Backend", "FastAPI · Node.js · Express · LangChain"),
        ("Core.Database", "PostgreSQL · Redis · Vector DB"),
        ("Core.Infra", "ESP32 · AWS (S3/EC2) · GitHub Actions"),
        ("Grid.Mail", "chakshuarora098@gmail.com"),
        ("Grid.Portfolio", "github.com/chakshubuilds"),
        ("Grid.LinkedIn", "in/chakshuarora716"),
        ("Grid.GitHub", "@chakshubuilds"),
        ("Grid.Community", "TechVerse Solutions (Founder)"),
    ]

    panel_rows_svg = []
    start_y = 126
    label_x = 478
    val_right_x = 1142

    for idx, (label, val) in enumerate(rows_data):
        cy = start_y + idx * 24.5
        # Computed dotted leader
        # Estimate label width roughly 8.5px per char for monospace 12.5px
        label_w = len(label) * 8.5 + 14
        val_w = len(val) * 7.6 + 14
        x1 = label_x + label_w
        x2 = val_right_x - val_w
        leader_svg = f'<line x1="{x1:.0f}" y1="{cy - 4:.0f}" x2="{x2:.0f}" y2="{cy - 4:.0f}" stroke="{leader_col}" stroke-width="1.2" stroke-dasharray="2 4" />'

        val_escaped = val.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        label_escaped = label.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        row_str = f'''<g>
      <text x="{label_x}" y="{cy}" class="mono label-txt" font-size="13" font-weight="600">{label_escaped}</text>
      {leader_svg}
      <text x="{val_right_x}" y="{cy}" text-anchor="end" class="mono val-txt" font-size="12.5" font-weight="500">{val_escaped}</text>
    </g>'''
        panel_rows_svg.append(row_str)

    rows_svg = "\n    ".join(panel_rows_svg)

    # Full SVG template (1180 x 610)
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Cascadia+Code:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap');
      .mono {{ font-family: 'Cascadia Code', monospace; }}
      .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }}

      @keyframes sh-shimmer {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
      }}
      .dither-grp {{
        opacity: 0;
        animation: sh-shimmer 1.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}

      @keyframes live-pulse {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(1.15); }}
      }}
      .pulse-beacon {{
        animation: live-pulse 1.8s ease-in-out infinite;
        transform-origin: 948px 84px;
      }}

      .label-txt {{ fill: {ui_chrome}; }}
      .val-txt {{ fill: {text_primary}; }}
    </style>

    <pattern id="dot-bg" x="0" y="0" width="18" height="18" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="{leader_col}" />
    </pattern>

    <linearGradient id="header-border" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{ui_chrome}" />
      <stop offset="100%" stop-color="{accent_col}" />
    </linearGradient>
  </defs>

  <!-- Window Container -->
  <rect width="1180" height="610" rx="16" fill="{bg_col}" stroke="{border_col}" stroke-width="1.5" />
  <rect width="1180" height="610" rx="16" fill="url(#dot-bg)" />

  <!-- Window Header Bar -->
  <g>
    <path d="M 0 16 Q 0 0 16 0 L 1164 0 Q 1180 0 1180 16 L 1180 44 L 0 44 Z" fill="{tab_bg}" />
    <line x1="0" y1="44" x2="1180" y2="44" stroke="{border_col}" stroke-width="1.2" />

    <!-- Window Control Dots -->
    <circle cx="24" cy="22" r="6" fill="#ff5f56" />
    <circle cx="44" cy="22" r="6" fill="#ffbd2e" />
    <circle cx="64" cy="22" r="6" fill="#27c93f" />

    <!-- Window Title -->
    <text x="590" y="27" text-anchor="middle" class="mono" font-size="13" font-weight="600" fill="{text_muted}">profile.sh --live</text>
  </g>

  <!-- Left ~38%: VISUAL.MAP Frame -->
  <g>
    <rect x="26" y="58" width="418" height="526" rx="10" fill="{card_bg}" stroke="{border_col}" stroke-width="1.2" />

    <!-- Frame Header -->
    <rect x="26" y="58" width="418" height="32" rx="10" fill="{tab_bg}" />
    <rect x="26" y="80" width="418" height="10" fill="{tab_bg}" />
    <line x1="26" y1="90" x2="444" y2="90" stroke="{border_col}" stroke-width="1" />
    <circle cx="42" cy="74" r="3.5" fill="{ui_chrome}" />
    <text x="54" y="78" class="mono" font-size="11.5" font-weight="700" fill="{ui_chrome}">VISUAL.MAP // DITHER_STREAM</text>
    <text x="428" y="78" text-anchor="end" class="mono" font-size="10.5" fill="{text_muted}">300x340 FS-1BIT</text>

    <!-- Dither Portrait Dots -->
    {dots_svg}

    <!-- Frame Bottom Status -->
    <rect x="42" y="546" width="386" height="24" rx="4" fill="{tab_bg}" stroke="{border_col}" stroke-width="0.8" />
    <text x="52" y="562" class="mono" font-size="10.5" fill="{ui_chrome}">HASH: 0x9842FDB7</text>
    <text x="416" y="562" text-anchor="end" class="mono" font-size="10.5" fill="{accent_col}">● STREAM SYNCHRONIZED</text>
  </g>

  <!-- Right: SYSTEM.INFO Panel -->
  <g>
    <rect x="458" y="58" width="696" height="526" rx="10" fill="{card_bg}" stroke="{border_col}" stroke-width="1.2" />

    <!-- Panel Header Bar -->
    <rect x="458" y="58" width="696" height="38" rx="10" fill="{tab_bg}" />
    <rect x="458" y="86" width="696" height="10" fill="{tab_bg}" />
    <line x1="458" y1="96" x2="1154" y2="96" stroke="{border_col}" stroke-width="1" />

    <!-- Header Label -->
    <text x="478" y="82" class="mono" font-size="13" font-weight="700" fill="{ui_chrome}">SYSTEM.INFO</text>

    <!-- Pulsing LIVE Badge -->
    <rect x="918" y="69" width="64" height="22" rx="4" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1" />
    <circle cx="930" cy="80" r="4" fill="#ef4444" class="pulse-beacon" />
    <text x="942" y="84" class="mono" font-size="11" font-weight="700" fill="#ef4444">LIVE</text>

    <!-- Coloured Handle Pill -->
    <rect x="996" y="69" width="144" height="22" rx="11" fill="{pill_bg}" stroke="{ui_chrome}" stroke-width="1.2" />
    <text x="1068" y="84" text-anchor="middle" class="mono" font-size="11.5" font-weight="700" fill="{ui_chrome}">@chakshubuilds</text>

    <!-- Rows with Dotted Leaders -->
    {rows_svg}
  </g>
</svg>'''

    return svg_content

# Generate dark.svg and light.svg
dark_content = generate_banner(is_dark=True)
with open('dark.svg', 'w', encoding='utf-8') as f:
    f.write(dark_content)
print("Generated dark.svg")

light_content = generate_banner(is_dark=False)
with open('light.svg', 'w', encoding='utf-8') as f:
    f.write(light_content)
print("Generated light.svg")
