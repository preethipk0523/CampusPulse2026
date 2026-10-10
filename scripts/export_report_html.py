from pathlib import Path
import markdown

source = Path("submission/implementation_report.md")
output = Path("submission/implementation_report.html")

text = source.read_text(encoding="utf-8")
html_body = markdown.markdown(
    text,
    extensions=["tables", "fenced_code", "toc"]
)

# Embed architecture SVG image tag cleanly
html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>CampusPulse 2026 — Implementation Report</title>
<style>
@page { size: A4; margin: 20mm 18mm; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; font-size: 11pt; line-height: 1.6; color: #1e293b; max-width: 960px; margin: 40px auto; padding: 0 20px; }
h1 { font-size: 22pt; color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 32px; }
h2 { font-size: 16pt; color: #1d4ed8; margin-top: 24px; }
h3 { font-size: 13pt; color: #334155; margin-top: 18px; }
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 9.5pt; }
th, td { border: 1px solid #cbd5e1; padding: 8px 10px; text-align: left; }
th { background: #f1f5f9; color: #0f172a; font-weight: 600; }
pre { background: #0f172a; color: #f8fafc; padding: 14px; border-radius: 6px; overflow-x: auto; }
code { font-family: Consolas, 'Courier New', monospace; font-size: 9.5pt; }
p code, td code { background: #f1f5f9; color: #0f172a; padding: 2px 5px; border-radius: 4px; border: 1px solid #e2e8f0; }
blockquote { border-left: 4px solid #3b82f6; padding-left: 14px; color: #475569; margin: 16px 0; font-style: italic; }
img { max-width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0; }
hr { border: 0; height: 1px; background: #e2e8f0; margin: 30px 0; }
</style>
</head>
<body>
""" + html_body + """
</body>
</html>
"""

output.write_text(html, encoding="utf-8")
print(f"HTML Report generated: {output.resolve()} ({output.stat().st_size} bytes)")
