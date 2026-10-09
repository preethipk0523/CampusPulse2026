
from pathlib import Path
import markdown
from weasyprint import HTML

source = Path("submission/implementation_report.md")
output = Path("submission/implementation_report.pdf")

if not source.exists():
    raise SystemExit(f"Report not found: {source.resolve()}")

text = source.read_text(encoding="utf-8")
html_body = markdown.markdown(
    text,
    extensions=["tables", "fenced_code", "toc"]
)

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page { size: A4; margin: 20mm 18mm; }
body { font-family: Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #222; }
h1 { font-size: 22pt; color: #17365d; }
h2 { font-size: 16pt; color: #24527a; margin-top: 20px; }
h3 { font-size: 12pt; margin-top: 16px; }
table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 9pt; }
th, td { border: 1px solid #999; padding: 6px; text-align: left; }
th { background: #eaf0f6; }
pre, code { font-family: Consolas, monospace; font-size: 9pt; overflow-wrap: anywhere; }
blockquote { border-left: 3px solid #999; padding-left: 10px; color: #555; }
</style>
</head>
<body>
""" + html_body + """
</body>
</html>
"""

HTML(string=html, base_url=str(Path.cwd())).write_pdf(str(output))
print(f"PDF created: {output.resolve()}")
