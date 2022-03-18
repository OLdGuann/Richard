import time
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from pandas import ExcelWriter
from datetime import datetime,timedelta
import HighGap_Island

yf.pdr_override()
# 今天
today = dt.datetime.now()
# today = dt.datetime(2022,3,17)
# 年初开始
start =dt.datetime(2022,1,1)

# root = Tk()
# ftypes = [(".xlsm","*.xlsx",".xls")]
# ttl  = "Title"
# dir1 = 'C:\\'
# filePath = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
filePath=r"StockTick.xlsx"

stocklist = pd.read_excel(filePath)
#stocklist=stocklist.head()

HighGapList,IslandList = HighGap_Island.get_Island(stocklist,start,today)



    #Ma13 = (sum(df.iloc[-13:-1,4])+df.iloc[-1,4])/13
    # if df.size>100:
    #     zuida21 = max(df.iloc[-21:-1,4])
    #     zuixiao21 = min(df.iloc[-21:-1,4])
    #     jintian = df.iloc[-1,4]
    #     MAX21 = max(zuida21,jintian)
    #     MIN21 = min(zuixiao21,jintian)
    #     WR21 = (MAX21-jintian)/(MAX21-MIN21)*100

    #     zuida42 = max(df.iloc[-42:-1,4])
    #     zuixiao42 = min(df.iloc[-42:-1,4])
    #     jintian = df.iloc[-1,4]
    #     MAX42 = max(zuida42,jintian)
    #     MIN42 = min(zuixiao42,jintian)
    #     WR42 = (MAX42-jintian)/(MAX42-MIN42)*100

    #     if WR21>80 and WR42>80 and df.iloc[-1,5]>5000000:
    #         exportList = exportList.append({'Stock': stock},ignore_index=True)


# print(exportList)

# newFile=os.path.dirname(filePath)+"/ScreenOutput.xlsx"

# writer= ExcelWriter(newFile)
# exportList.to_excel(writer,"Sheet1")
# writer.save()





















    
