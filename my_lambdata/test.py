from my_lambdata.module import Wrangle
import unittest
import pandas as pd

class TestWrangle(unittest.TestCase):

    def test_separate_dates(self):
        df = pandas.DataFrame({"date": ["3-22-1939", "11-23-1953", "5-30-2001"]})
        df = separate_dates(df, "date")
        self.assertTrue('month' in df.columns.tolist())