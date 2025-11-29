from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def render_report(context: dict, template_path: Path, out_html: Path):
    env = Environment(loader=FileSystemLoader(str(template_path.parent)))
    tmpl = env.get_template(template_path.name)
    html = tmpl.render(**context)
    out_html.write_text(html, encoding='utf-8')
    # WeasyPrint conversion can be added when system deps are available
