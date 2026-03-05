from jinja2 import Environment, FileSystemLoader
import os

class ReportGenerator:
    def __init__(self, template_dir="templates"):
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def generate_html_report(self, context, output_file="reports/final_report.html"):
        template = self.env.get_template("report_template.html")
        html_content = template.render(context)

        os.makedirs("reports", exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        return output_file