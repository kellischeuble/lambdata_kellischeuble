import pandas as pd


def separate_dates(df, column):
    df[column] = pd.to_datetime(df[column])
    df["day"] = df[column].dt.day
    df["month"] = df[column].dt.month
    df["year"] = df[column].dt.year
    return df


def add_list(df, list):
    series = pd.Series(list)
    df = df.append(series)
    return df
