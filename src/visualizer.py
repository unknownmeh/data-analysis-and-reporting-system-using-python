import matplotlib.pyplot as plt
import seaborn as sns
import os

class DataVisualizer:
    def __init__(self, df, output_dir="reports/figures"):
        self.df = df
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def plot_histogram(self, column):
        plt.figure()
        sns.histplot(self.df[column], kde=True)
        path = f"{self.output_dir}/{column}_hist.png"
        plt.savefig(path)
        plt.close()
        return path

    def plot_correlation_heatmap(self):
        plt.figure(figsize=(10,8))
        sns.heatmap(self.df.corr(numeric_only=True), annot=True, cmap="coolwarm")
        path = f"{self.output_dir}/correlation_heatmap.png"
        plt.savefig(path)
        plt.close()
        return path