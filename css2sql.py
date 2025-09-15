#!/usr/bin/env python3
import re
import sys

if len(sys.argv) < 2:
    print("Usage: css2sql.py <input.css>")
    sys.exit(1)

css_file = sys.argv[1]
with open(css_file, "r") as f:
    css = f.read()

# Extract --var: #HEX;
pairs = dict(re.findall(r'--([a-z0-9\-]+):\s*#?([0-9A-Fa-f]{6})', css))

# Build palette list
palette = []
for i in range(1, 22):  # up to 21
    key = f"palette-{i:02d}"
    if key in pairs:
        palette.append(pairs[key].upper())

# Build SQL string
sql = f"""UPDATE graph_theme
SET backgroundcolor     = '{pairs.get("background-color","282A36").upper()}',
    graphcolor          = '{pairs.get("graph-color","1E1F29").upper()}',
    gridcolor           = '{pairs.get("grid-color","282A36").upper()}',
    maingridcolor       = '{pairs.get("main-grid-color","6272A4").upper()}',
    gridbordercolor     = '{pairs.get("grid-border-color","6272A4").upper()}',
    textcolor           = '{pairs.get("text-color","F8F8F2").upper()}',
    highlightcolor      = '{pairs.get("highlight-color","BD93F9").upper()}',
    leftpercentilecolor = '{pairs.get("left-percentile-color","50FA7B").upper()}',
    rightpercentilecolor= '{pairs.get("right-percentile-color","FF5555").upper()}',
    nonworktimecolor    = '{pairs.get("nonworktime-color","232530").upper()}',
    colorpalette        = '{",".join(palette)}'
WHERE theme = 'naon-theme';
"""

print(sql)
