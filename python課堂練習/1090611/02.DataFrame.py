import pandas as pd
#dict轉為
data={"name":["asuka","mika","riko"],"id":["00546","00550","00551"],"Y/N":[True,False,True]}
df1=pd.DataFrame(data)
print(df1)
print('-'*30)

df2=pd.DataFrame(data,columns=["id","name","Y/N","abc"],index=["I","II","III"])
print(df2)

ss1=pd.Series(data)
print(ss1)