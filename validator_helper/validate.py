#!/usr/bin/env python

import pandas as pd


class Column(object):

    def __init__(self, column_name, column_type='Categorical', acceptable_range=None):
        self.column_name = column_name
        self.column_type = column_type
        self.acceptable_range = acceptable_range


class Validator(object):
    def __init__(self, reference_csv, test_csv, column_list):
        self.reference_csv = reference_csv
        self.test_csv = test_csv
        self.column_list = column_list
        self.reference_headers = list(pd.read_csv(self.reference_csv).columns)
        self.test_headers = list(pd.read_csv(self.test_csv).columns)

    def check_columns_in_ref_and_test(self):
        pass


