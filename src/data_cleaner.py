class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean(self):

        # remove duplicates
        self.df = self.df.drop_duplicates()

        # fill missing values
        self.df = self.df.ffill()

        return self.df