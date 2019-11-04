import pandas as pd

class eyeTracker_Subject:
    def __init__(self, filename:str):
        self.__inputfile = filename;
        self.__readfile()
    def __readfile(self):
        dfs = pd.read_excel(self.__inputfile, sheet_name=None)
        #print(dfs)

        for key, value in dfs.items():
            print(key)

