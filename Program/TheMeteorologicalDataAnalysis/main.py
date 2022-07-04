import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
    plt.savefig("Asti.png")
    plt.show()

def sort(x) :
    '''
        字典进行排序，查看距离最近的三个以及距离最远的三个
        可以知道：
            最近的三个城市：Ravenna、Ferrara、Faenza
            最远的三个城市：Milano、Asti、Torino
    '''
    sort_list = zip(x.values(), x.keys())
    sort_list = sorted(sort_list, reverse=False)
    return sort_list

def compareWeather() :
    '''
        探究三个最远的城市和三个最近的城市天气
    '''
    # 三个最近的城市
    ravenna = pd.read_csv("WeatherData/ravenna_270615.csv")
    temp1 = ravenna[:]["temp"]
    time1 = ravenna[:]["day"]
    dtime1 = []
    for i in range(0, 17):
        dtime1.append(time1[i][10:13])
    dtemp1 = temp1[0:17]
    dtime1 = pd.Series(dtime1)

    ferrara = pd.read_csv("WeatherData/ferrara_270615.csv")
    temp2 = ferrara[:]["temp"]
    time2 = ferrara[:]["day"]
    dtime2 = []
    for j in range(1, 19):
        dtime2.append(time2[j][10:13])
    dtemp2 = temp2[1:19]
    dtime2 = pd.Series(dtime2)

    faenza  = pd.read_csv("WeatherData/faenza_270615.csv")
    temp3 = faenza[:]["temp"]
    time3 = faenza[:]["day"]
    dtime3 = []
    for k in range(0, 19):
        dtime3.append(time3[k][10:13])
    dtemp3 = temp3[0:19]
    dtime3 = pd.Series(dtime3)

    # 因为数据集问题，如果采用原数据集数据会导致图像错误，因此将ferrara的08删除
    # 且将另外两个数据集的第一个03改为02
    # 绘制对应的图像，最近的用红色，最远的用绿色
    plt.plot(dtime1, dtemp1, color = 'red', label = 'r')
    plt.plot(dtime2, dtemp2, color = 'r')
    plt.plot(dtime3, dtemp3, color = 'r')

    # 三个最远的城市
    milano = pd.read_csv("WeatherData/milano_270615.csv")
    temp1 = milano[:]["temp"]
    time1 = milano[:]["day"]
    dtime1 = []
    for i in range(0, 17):
        dtime1.append(time1[i][10:13])
    dtemp1 = temp1[0:17]
    dtime1 = pd.Series(dtime1)

    asti = pd.read_csv("WeatherData/asti_270615.csv")
    temp2 = asti[:]["temp"]
    time2 = asti[:]["day"]
    dtime2 = []
    for i in range(0, 19):
        dtime2.append(time2[i][10:13])
    dtemp2 = temp2[0:19]
    dtime2 = pd.Series(dtime2)

    torino = pd.read_csv("WeatherData/torino_270615.csv")
    temp3 = torino[:]["temp"]
    time3 = torino[:]["day"]
    dtime3 = []
    for i in range(0, 17):
        dtime3.append(time3[i][10:13])
    dtemp3 = temp3[0:17]
    dtime3 = pd.Series(dtime1)

    # 绘制对应的图像，最近的用红色，最远的用绿色
    plt.plot(dtime1, dtemp1, color='green', label = 'g')
    plt.plot(dtime2, dtemp2, color='g')
    plt.plot(dtime3, dtemp3, color='g')
    plt.title("Six City Trend of Temp", fontsize = 16)
    plt.xlabel("time")
    plt.ylabel("temp")
    plt.legend(loc = 'upper right')
    plt.savefig("SixCityTrendofTemp.png")
    plt.show()

def CityHighTemp(path) :
    temp = pd.read_csv(path)
    temp = temp.sort_values(by="temp", ascending=False)
    temp = temp[:]["temp"]
    temp = temp.iloc[0:1] # 取出特定行
    return temp

def highTemp(x) :
    x = dict(sort(x))
    dis = pd.Series(x.keys())
    rank = pd.Series(x.values())
    print(rank)

    # 此时应该按照rank的远近顺序来提取出各自的温度最大值
    # 由于相似代码太多，直接封装函数，传入csv文件路径即可
    temp1 = CityHighTemp("WeatherData/ravenna_270615.csv")
    temp2 = CityHighTemp("WeatherData/ferrara_270615.csv")
    temp3 = CityHighTemp("WeatherData/faenza_270615.csv")
    temp4 = CityHighTemp("WeatherData/cesena_270615.csv")
    temp5 = CityHighTemp("WeatherData/bologna_270615.csv")
    temp6 = CityHighTemp("WeatherData/mantova_270615.csv")
    temp7 = CityHighTemp("WeatherData/piacenza_270615.csv")
    temp8 = CityHighTemp("WeatherData/milano_270615.csv")
    temp9 = CityHighTemp("WeatherData/asti_270615.csv")
    temp10 = CityHighTemp("WeatherData/torino_270615.csv")
    temp = [temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10]
    dis = list(dis)
    print(temp)
    print(dis)
    plt.plot(dis, temp, 'ro')
    plt.title("Highest Temp of City", fontsize = 16)
    plt.xlabel("distance")
    plt.ylabel("temp")
    plt.grid()
    plt.savefig("HighestTemOfCity.png")
    plt.show()



if __name__ == "__main__" :
    dis = Distance()
