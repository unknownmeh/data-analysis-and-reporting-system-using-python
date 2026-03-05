import pandas as pd
import seaborn as sns

class DataLoader:

    def load_data(self):
        # Load built-in dataset
        df = sns.load_dataset("tips")
        return df