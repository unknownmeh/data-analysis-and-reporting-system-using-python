from data_loader import DataLoader
from data_cleaner import DataCleaner
from analyzer import DataAnalyzer
from visualizer import DataVisualizer
from report_generator import ReportGenerator


import os

os.makedirs("data/raw", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("reports/figures", exist_ok=True)
os.makedirs("templates", exist_ok=True)

def run_pipeline(filepath):
    # Load
    loader = DataLoader()
    df = loader.load_data()

    # Clean
    cleaner = DataCleaner(df)
    df_clean = cleaner.clean()

    # Analyze
    analyzer = DataAnalyzer(df_clean)
    summary = analyzer.summary_statistics()
    correlation = analyzer.correlation_matrix()

    # Visualize
    visualizer = DataVisualizer(df_clean)
    heatmap_path = visualizer.plot_correlation_heatmap()

    # Report
    report = ReportGenerator()
    context = {
        "summary_table": summary.to_html(),
        "correlation_table": correlation.to_html(),
        "heatmap": heatmap_path
    }
    report.generate_html_report(context)

if __name__ == "__main__":
    run_pipeline('None')