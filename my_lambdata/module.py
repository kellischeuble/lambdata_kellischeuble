import pandas as pd


class Wrangle:  

    def __init__(self, df):
        self.df = df

    def separate_dates(self, column):
        """
        Parameter df is a dataframe
        Parameter column is a column with date values
        Returns dataframe with split columns for day, month, year
        """
        self.df[column] = pd.to_datetime(self.df[column])
        self.df["day"] = self.df[column].dt.day
        self.df["month"] = self.df[column].dt.month
        self.df["year"] = self.df[column].dt.year
        return self.df


    def add_list(self, list):
        """
        Returns a dataframe with the paramater list added as a column
        Param list must have number of values as columns in dataframe
        """
        self.series = pd.Series(list)
        self.df = self.df.append(series)
        return self.df
