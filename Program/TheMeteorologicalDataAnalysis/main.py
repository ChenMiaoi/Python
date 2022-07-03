import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas
import pandas as pd
from dateutil import parser

def Distance() :
    '''
        为了方便，我们采取了用一个城市到一个沿海城市的距离近似作为距海距离
        本次，我们选取意大利的Comacchio作为参考城市
        同时，直接使用城市名代表距离(km)
    '''
    dis = {
        "Ferrara"   : 47,
        "Torino"    : 358,
        "Mantova"   : 121,
        "Milano"    : 251,
        "Ravenna"   : 31,
        "Asti"      : 316,
        "Bologna"   : 71,
        "Piacenza"  : 200,
        "Cesena"    : 62,
        "Faenza"    : 52
    }
    return dis

def Asti() :
    df = pd.read_csv("WeatherData/asti_270615.csv")
    temp = df[:]["temp"]
    time = df[:]["day"]
    dtime = []
    for i in range(0, 20) :
        dtime.append(time[i][10:13])
    dtime = pd.Series(dtime)
    print(dtime)
    plt.plot(dtime, temp)
    plt.title("Asti One Day Temp", fontsize = 16)
    plt.xlabel("time")
    plt.ylabel("temp")
    plt.axhline(y=25, ls='--', c='red')
    plt.show()

if __name__ == "__main__" :
    dis = Distance()
    temp = []
    time = []
    Asti()

