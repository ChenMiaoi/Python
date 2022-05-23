import pandas as pd

# 对于外部数据，pandas内置了一些接口
# 比如对于csv文件，直接pd.read_csv()
# 比如对于mysql, 直接pd.read_sql()
# 比如对于html, 直接pd.read_html()
FILE_PATH = "./dogNames2.csv"
df = pd.read_csv(FILE_PATH)
print(df)
