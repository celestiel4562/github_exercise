# import pandas as pd

# data=pd.read_csv("nba.csv")
# print(data)

# mask=data["Age"]>=25 
# print(data[mask])

# mask2=data["Age"].between(25,27)
# print(data[mask2].head(3))

# df=data.groupby("Team")
# print(df.groups)
# print(df.get_group("Team"))


import pandas as pd
import numpy as ny

data=pd.DataFrame(
{"key1":["A","B","C","A","A","C"],
"key2":["ONE","TWO","ONE","ONE","TWO","ONE"],
"data1":ny.random.randn(6),
"data2":ny.random.randn(6)})

filter1=data.groupby("key1")
print(filter1)


























