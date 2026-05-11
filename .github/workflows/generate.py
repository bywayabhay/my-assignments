import os, re

folders = sorted([
    f for f in os.listdir('.')
    if os.path.isdir(f) and re.match(r'^assignment-\d+$', f)
], key=lambda x: int(x.split('-')[1]))

# Generate index.html
cards = ""
for f in folders:
    num = f.split('-')[1]
    cards += f'''
    <div class="card">
      <h2>Assignment {num}</h2>
      <a href="{f}/">View Live →</a>
    </div>'''

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Assignments</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>📚 My Assignments</h1>
  <div class="grid">{cards}
  </div>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(html)

# Generate README.md
rows = ""
for f in folders:
    num = f.split('-')[1]
    url = f"https://bywayabhay.github.io/my-assignments/{f}/"
    rows += f"| {num} | Assignment {num} | [View Live →]({url}) |\n"

readme = f"""# 📚 My Assignments

| # | Assignment | Live URL |
|---|------------|----------|
{rows}
"""

with open("README.md", "w") as f:
    f.write(readme)

print(f"Generated index.html and README.md with {len(folders)} assignments")