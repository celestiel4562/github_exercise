import pandas as pd

#自建DataFrame
pf_data=[["asuka","00546",True],["mika","00550",False],["riko","00551",True]]
pf=pd.DataFrame(pf_data,columns=["name","id","Y/N"],index=["1","2","3"])
print(pf)
print("-"*10)
print("▼ 資料維度:",pf.ndim)   #資料維度
print("-"*10)
print("▼ 資料數:",pf.shape)  #資料數(欄數row,列數columes)
print("-"*10)
print("▼ 資料類型:\n",pf.dtypes) #資料類型(object物件/int數值)
print("-"*10)
print("▼ 顯示資料類型:",pf.info())