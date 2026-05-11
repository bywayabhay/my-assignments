import os, re

folders = sorted([
    f for f in os.listdir('.')
    if os.path.isdir(f) and re.match(r'^assignment-\d+$', f)
], key=lambda x: int(x.split('-')[1]))

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

print(f"Generated index.html with {len(folders)} assignments")