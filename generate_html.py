import os

html_file = "index.html"
folder_path = "."  # current folder

# Get all .txt files and sort them
txt_files = [f for f in os.listdir(folder_path) if f.startswith("slip") and f.endswith(".txt")]
txt_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))  # slip1, slip2 ... क्रमाने

# HTML content
html_content = """<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <title>माझ्या Text Files</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #2c3e50; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
        a { text-decoration: none; color: #2980b9; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>माझ्या Text Files</h1>
    <ul>
"""

for file in txt_files:
    html_content += f'        <li><a href="{file}" target="_blank">{file}</a></li>\n'

html_content += """    </ul>
</body>
</html>"""

# Write HTML file
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ {html_file} तयार झाले! {len(txt_files)} text files add केल्या आहेत.")
