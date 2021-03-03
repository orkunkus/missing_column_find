# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:20:48 2021

@author: orkun
"""

from tkinter import filedialog
import tkinter as tk
import pandas as pd

root = tk.Tk()
root.wm_attributes('-topmost', 1)
root.withdraw()


class file_read(object):
    def __init__(self, file_path, miss_format, delimiter):
        self.file_path = file_path
        self.miss_format = miss_format
        self.delimiter = delimiter


class miss_columns(file_read):
    def __init__(self, file_path, miss_format, delimiter):
        super().__init__(file_path, miss_format, delimiter)

    def missing_cols_get(self):
        df = pd.read_csv(self.file_path, delimiter=self.delimiter, na_values=self.miss_format)
        missing_col_list = [column for column in df.columns if df[column].isnull().any()]
        return missing_col_list


if __name__ == '__main__':
    # ---Read File Path
    file_path = filedialog.askopenfilename(parent=root, initialdir="/", title='Please select a file')
    missing_formats = ["NA", "nan", "NAN", ""]
    delimeter = ";"
    missing_object = miss_columns(file_path, missing_formats, delimeter)
    missing_columns = missing_object.missing_cols_get()
    print(file_path + " has missing columns : " + ",".join(missing_columns))
