import pandas as pd

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def summary_statistics(self):
        return self.df.describe()

    def correlation_matrix(self):
        return self.df.corr(numeric_only=True)

    def group_analysis(self, column):
        return self.df.groupby(column).mean(numeric_only=True)