import pandas as pd

class eyeTracker_Subject:
    def __init__(self, filename:str):
        self.__inputfile = filename;
        self.__readfile()
    def __readfile(self):
        dfs = pd.read_excel(self.__inputfile, sheet_name="TETSimpleGaze_Order1-999-1")
        #print(type(dfs))
        x = 0
        #print(dfs.columns)
        #print(dfs['Subject'])
        #for i in dfs.index:
            #print(dfs['Subject'][i])

        for i in dfs.index:
            for j in dfs.columns:
                print(j,i)
                print(dfs[j][i])