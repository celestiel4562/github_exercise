import pandas as pd

data=pd.read_csv("nba.csv") #讀取csv檔
print(data)
print("-"*5)

# 輸出指定欄及其列數的資料
print("↓↓輸出指定欄及其列數的資料↓↓")
print(data["Name"][5:10])
print("-"*5)
      
print("↓↓輸出複數指定欄的資料↓↓")
print(data[["Name","Number","Position"]].head())
print("-"*5)

print("↓↓在指定列插入新資料↓↓")
data.insert(1,column="sports",value="checked")
print(data)
print("-"*5)

print("↓↓刪除指定row的資料↓↓")
data=data.drop("sports",axis=1)
print(data)
print("-"*5)

print("↓↓刪除指定column的資料↓↓")
data=data.drop(0,axis=0)
print(data)
print("-"*5)

print("↓↓刪除空資料↓↓")
data=(data.dropna()) #dropna()裡為空
print(data)
print("-"*5)

print("↓↓填充空資料↓↓")
data=(data.fillna(100)) #fillna()裡可填任意資料
print(data)

print("↓↓資料排序↓↓")
print(data.head(6))
print("--"*35)
print(data.sort_values("Salary").head(6))
print("--"*35)
print(data.sort_values("Salary",ascending=False).head(6))





































