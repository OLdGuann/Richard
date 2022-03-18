import pandas as pd
import yfinance as yf
from yahoo_fin import stock_info as si
from tqdm import tqdm
import time



def get_closest_low_gap(df):
    for i in range(len(df)-1):
        prev_low = df.iloc[i,2]
        op = df.iloc[i+1,0]
        if op<prev_low:
            Low_gap=True
            index = i

    return index,Low_gap
def get_Island(stocklist,start,today):
    # 输出数据存放
    HighGapList = pd.DataFrame(columns=['Stock'])
    IslandList = pd.DataFrame(columns=['Stock'])

    for i in tqdm(range(len(stocklist))):

        # 读取股票代码
        stock=str(stocklist["Symbol"][i])
        # 读取股票数据
        df = yf.download(stock,start,today)
        if len(df) != 0:
            if df.iloc[-1,-1]>5000000:
                # 检查今天跳空高开
                op = df.iloc[-1,2] #今天的开盘价
                hi = df.iloc[-2,1] #昨天最高价

                # 如果高开
                if op>hi:
                    HighGapList = HighGapList.append({'Stock': stock},ignore_index=True)

                    #找最近的低开
                    index,Low_gap=get_closest_low_gap(df)

                    if Low_gap:

                        # 低开前一天的最低价格
                        gap_high = df.iloc[index,2]

                        # 除去今天，低开后所有天最高价
                        highest_price = max(df.iloc[index+1:-1,1])

                        if highest_price<=gap_high and df.iloc[-1,0]>highest_price:
                            print('岛型反转: '+stock)
                            IslandList = IslandList.append({'Stock': stock},ignore_index=True)
    return HighGapList,IslandList
