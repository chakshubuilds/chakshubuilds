import math
import random
import numpy as np
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageDraw, ImageFont

def build_banner(is_dark=True):
    # Palette
    if is_dark:
        bg_col = "#0A101F"
        card_bg = "#070b16"
        border_col = "#1c284a"
        portrait_col = "#A78BFA"
        code_col = "#00f0ff"
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
        code_col = "#0891B2"
        ui_chrome = "#0891B2"
        accent_col = "#059669"
        text_primary = "#0f172a"
        text_muted = "#475569"
        leader_col = "rgba(8, 145, 178, 0.25)"
        pill_bg = "#e2e8f0"
        tab_bg = "#e2e8f0"

    W_GRID, H_GRID = 300, 340
    sx = 1.32
    sy = 1.35
    ox = 38
    oy = 102
    NUM_GROUPS = 50

    # 1. GENERATE PORTRAIT DOTS
    im = Image.open('assets/portrait_clean.png').convert('RGBA')
    im_resized = im.resize((W_GRID, H_GRID), Image.Resampling.LANCZOS)
    alpha = np.array(im_resized.split()[3])
    gray = np.array(im_resized.convert('L'))
    gray[alpha < 128] = 0 if is_dark else 255

    pil_gray = Image.fromarray(gray)
    enhancer = ImageEnhance.Contrast(pil_gray)
    pil_gray = enhancer.enhance(1.3)
    pil_gray = ImageOps.autocontrast(pil_gray, cutoff=1)
    pil_gray = pil_gray.filter(ImageFilter.UnsharpMask(radius=3, percent=140))

    arr = np.array(pil_gray, dtype=float)
    if is_dark:
        arr[alpha < 128] = 0.0

    p_binary = np.zeros((H_GRID, W_GRID), dtype=np.uint8)
    for y in range(H_GRID):
        xs = range(W_GRID) if y % 2 == 0 else range(W_GRID - 1, -1, -1)
        direction = 1 if y % 2 == 0 else -1
        for x in xs:
            old_val = arr[y, x]
            if is_dark and alpha[y, x] < 128:
                new_val = 0
                err = 0
            else:
                new_val = 255 if old_val >= 128 else 0
                err = old_val - new_val
            p_binary[y, x] = 1 if new_val == 255 else 0

            # Error diffusion
            if direction == 1:
                if x + 1 < W_GRID: arr[y, x + 1] += err * 7 / 16
                if y + 1 < H_GRID:
                    if x - 1 >= 0: arr[y + 1, x - 1] += err * 3 / 16
                    arr[y + 1, x] += err * 5 / 16
                    if x + 1 < W_GRID: arr[y + 1, x + 1] += err * 1 / 16
            else:
                if x - 1 >= 0: arr[y, x - 1] += err * 7 / 16
                if y + 1 < H_GRID:
                    if x + 1 < W_GRID: arr[y + 1, x + 1] += err * 3 / 16
                    arr[y + 1, x] += err * 5 / 16
                    if x - 1 >= 0: arr[y + 1, x - 1] += err * 1 / 16

    # 2. GENERATE ONLY BIG </> CODE SYMBOL DOTS
    code_img = Image.new('L', (W_GRID, H_GRID), 0)
    c_draw = ImageDraw.Draw(code_img)

    # Bold, clean, iconic centered </> symbol
    # Left bracket <
    c_draw.line([(100, 105), (42, 170), (100, 235)], fill=255, width=16, joint='round')
    # Center slash /
    c_draw.line([(172, 90), (128, 250)], fill=255, width=16)
    # Right bracket >
    c_draw.line([(200, 105), (258, 170), (200, 235)], fill=255, width=16, joint='round')

    c_arr = np.array(code_img)
    c_binary = np.where(c_arr > 120, 1, 0).astype(np.uint8)

    # 3. BUILD SCATTER PATHS & KEYFRAMES
    random.seed(1337)
    p_group_paths = {i: [] for i in range(NUM_GROUPS)}
    c_group_paths = {i: [] for i in range(NUM_GROUPS)}
    group_vectors = []

    for i in range(NUM_GROUPS):
        angle = (i / NUM_GROUPS) * 2 * math.pi + random.uniform(-0.2, 0.2)
        dist = random.uniform(45, 95)
        dx = math.cos(angle) * dist
        dy = math.sin(angle) * dist
        group_vectors.append((dx, dy))

    # Convert portrait binary to runs
    for y in range(H_GRID):
        row = p_binary[y]
        in_run = False
        start_x = 0
        for x in range(W_GRID):
            if row[x] == 1 and not in_run:
                in_run = True
                start_x = x
            elif row[x] == 0 and in_run:
                in_run = False
                run_len = x - start_x
                grp = random.randint(0, NUM_GROUPS - 1)
                px = ox + start_x * sx
                py = oy + y * sy
                pw = run_len * sx
                p_group_paths[grp].append(f"M {px:.1f} {py:.1f} h {pw:.1f}")
        if in_run:
            run_len = W_GRID - start_x
            grp = random.randint(0, NUM_GROUPS - 1)
            px = ox + start_x * sx
            py = oy + y * sy
            pw = run_len * sx
            p_group_paths[grp].append(f"M {px:.1f} {py:.1f} h {pw:.1f}")

    # Convert code binary to runs
    for y in range(H_GRID):
        row = c_binary[y]
        in_run = False
        start_x = 0
        for x in range(W_GRID):
            if row[x] == 1 and not in_run:
                in_run = True
                start_x = x
            elif row[x] == 0 and in_run:
                in_run = False
                run_len = x - start_x
                grp = random.randint(0, NUM_GROUPS - 1)
                px = ox + start_x * sx
                py = oy + y * sy
                pw = run_len * sx
                c_group_paths[grp].append(f"M {px:.1f} {py:.1f} h {pw:.1f}")
        if in_run:
            run_len = W_GRID - start_x
            grp = random.randint(0, NUM_GROUPS - 1)
            px = ox + start_x * sx
            py = oy + y * sy
            pw = run_len * sx
            c_group_paths[grp].append(f"M {px:.1f} {py:.1f} h {pw:.1f}")

    # Build keyframes for each group
    keyframes_css = []
    portrait_svg_paths = []
    code_svg_paths = []

    for i in range(NUM_GROUPS):
        dx, dy = group_vectors[i]
        kf_p = f'''
      @keyframes p-scat-{i} {{
        0%, 30% {{ transform: translate(0px, 0px); opacity: 1; }}
        42%, 78% {{ transform: translate({dx:.1f}px, {dy:.1f}px); opacity: 0; }}
        88%, 100% {{ transform: translate(0px, 0px); opacity: 1; }}
      }}
      .p-grp-{i} {{
        animation: p-scat-{i} 14s cubic-bezier(0.4, 0, 0.2, 1) infinite;
      }}
      @keyframes c-scat-{i} {{
        0%, 30% {{ transform: translate({-dx:.1f}px, {-dy:.1f}px); opacity: 0; }}
        42%, 78% {{ transform: translate(0px, 0px); opacity: 1; }}
        88%, 100% {{ transform: translate({-dx:.1f}px, {-dy:.1f}px); opacity: 0; }}
      }}
      .c-grp-{i} {{
        animation: c-scat-{i} 14s cubic-bezier(0.4, 0, 0.2, 1) infinite;
      }}'''
        keyframes_css.append(kf_p)

        if p_group_paths[i]:
            d_p = " ".join(p_group_paths[i])
            portrait_svg_paths.append(
                f'<path d="{d_p}" stroke="{portrait_col}" stroke-width="1.3" shape-rendering="crispEdges" class="p-grp-{i}" />'
            )
        if c_group_paths[i]:
            d_c = " ".join(c_group_paths[i])
            code_svg_paths.append(
                f'<path d="{d_c}" stroke="{code_col}" stroke-width="1.3" shape-rendering="crispEdges" class="c-grp-{i}" />'
            )

    all_css_kf = "\n".join(keyframes_css)
    p_paths_svg = "\n    ".join(portrait_svg_paths)
    c_paths_svg = "\n    ".join(code_svg_paths)

    # 4. INFO PANEL ROWS
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

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Cascadia+Code:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap');
      .mono {{ font-family: 'Cascadia Code', monospace; }}
      .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }}

      {all_css_kf}

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

  <rect width="1180" height="610" rx="16" fill="{bg_col}" stroke="{border_col}" stroke-width="1.5" />
  <rect width="1180" height="610" rx="16" fill="url(#dot-bg)" />

  <g>
    <path d="M 0 16 Q 0 0 16 0 L 1164 0 Q 1180 0 1180 16 L 1180 44 L 0 44 Z" fill="{tab_bg}" />
    <line x1="0" y1="44" x2="1180" y2="44" stroke="{border_col}" stroke-width="1.2" />
    <circle cx="24" cy="22" r="6" fill="#ff5f56" />
    <circle cx="44" cy="22" r="6" fill="#ffbd2e" />
    <circle cx="64" cy="22" r="6" fill="#27c93f" />
    <text x="590" y="27" text-anchor="middle" class="mono" font-size="13" font-weight="600" fill="{text_muted}">profile.sh --live</text>
  </g>

  <!-- Left ~38%: VISUAL.MAP Frame with Morphing Dots -->
  <g>
    <rect x="26" y="58" width="418" height="526" rx="10" fill="{card_bg}" stroke="{border_col}" stroke-width="1.2" />
    <rect x="26" y="58" width="418" height="32" rx="10" fill="{tab_bg}" />
    <rect x="26" y="80" width="418" height="10" fill="{tab_bg}" />
    <line x1="26" y1="90" x2="444" y2="90" stroke="{border_col}" stroke-width="1" />
    <circle cx="42" cy="74" r="3.5" fill="{ui_chrome}" />
    <text x="54" y="78" class="mono" font-size="11.5" font-weight="700" fill="{ui_chrome}">VISUAL.MAP // DITHER_STREAM</text>
    <text x="428" y="78" text-anchor="end" class="mono" font-size="10.5" fill="{text_muted}">SCATTER_MORPH</text>

    <!-- Layer 1: Portrait Dots (Scatters then reforms) -->
    {p_paths_svg}

    <!-- Layer 2: Code Image Dots (Assembles then scatters) -->
    {c_paths_svg}

    <!-- Bottom Status -->
    <rect x="42" y="546" width="386" height="24" rx="4" fill="{tab_bg}" stroke="{border_col}" stroke-width="0.8" />
    <text x="52" y="562" class="mono" font-size="10.5" fill="{ui_chrome}">HASH: 0x9842FDB7</text>
    <text x="416" y="562" text-anchor="end" class="mono" font-size="10.5" fill="{accent_col}">● CONTINUOUS MORPH ACTIVE</text>
  </g>

  <!-- Right: SYSTEM.INFO Panel -->
  <g>
    <rect x="458" y="58" width="696" height="526" rx="10" fill="{card_bg}" stroke="{border_col}" stroke-width="1.2" />
    <rect x="458" y="58" width="696" height="38" rx="10" fill="{tab_bg}" />
    <rect x="458" y="86" width="696" height="10" fill="{tab_bg}" />
    <line x1="458" y1="96" x2="1154" y2="96" stroke="{border_col}" stroke-width="1" />
    <text x="478" y="82" class="mono" font-size="13" font-weight="700" fill="{ui_chrome}">SYSTEM.INFO</text>
    <rect x="918" y="69" width="64" height="22" rx="4" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1" />
    <circle cx="930" cy="80" r="4" fill="#ef4444" class="pulse-beacon" />
    <text x="942" y="84" class="mono" font-size="11" font-weight="700" fill="#ef4444">LIVE</text>
    <rect x="996" y="69" width="144" height="22" rx="11" fill="{pill_bg}" stroke="{ui_chrome}" stroke-width="1.2" />
    <text x="1068" y="84" text-anchor="middle" class="mono" font-size="11.5" font-weight="700" fill="{ui_chrome}">@chakshubuilds</text>
    {rows_svg}
  </g>
</svg>'''

    return svg_content

dark_content = build_banner(is_dark=True)
with open('dark.svg', 'w', encoding='utf-8') as f:
    f.write(dark_content)
print("Updated dark.svg with continuous scatter & morph!")

light_content = build_banner(is_dark=False)
with open('light.svg', 'w', encoding='utf-8') as f:
    f.write(light_content)
print("Updated light.svg with continuous scatter & morph!")
