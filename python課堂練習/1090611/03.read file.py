import pandas as pd

###
#用pd.read_csv讀取csv檔案
csv_data=pd.read_csv(r"C:\Users\ASUS\Desktop\PYTHON\課堂練習\1090611\csvsample.csv")
print(csv_data)
print("-"*10)
print("資料維度:",csv_data.ndim)   #資料維度
print("-"*10)
print("資料數:",csv_data.shape)  #資料數(欄數row,列數columes)
print("-"*10)
print("資料類型:\n",csv_data.dtypes) #資料類型(object物件/int數值)
print("-"*10)
print("顯示前5筆:\n",csv_data.head())
print("-"*10)
print("顯示最後5筆:\n",csv_data.tail())
print("-"*10)
print("顯示資料類型:\n",csv_data.info())
######

data=pd.read_csv(r"C:\Users\ASUS\Desktop\PYTHON\課堂練習\1090611\nba.csv")
print(data)
print(data["Name"][5:10])
print(data[["Name","Number","Position"]].head(5))
print("-"*10)
