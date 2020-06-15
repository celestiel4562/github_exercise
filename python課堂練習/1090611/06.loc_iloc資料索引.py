import pandas as pd
import numpy as np

frame=pd.DataFrame(np.random.rand(5,5),index=list("12345"),columns=list("abcde"))
print(frame)
print(frame.loc["1","a"])
print(frame.loc["2","a"])
print(frame.loc["1","b"])
print(frame.loc["1":"2","a":"d"])
print(frame.loc["3":"5",:])
print(frame.loc[["2","4"],["b","d"]])

print("\n"+"-"*10)
print(frame.iloc[0,0])

print("\n"+"-"*10)
print(frame.iloc[0,3])

print("\n"+"-"*10)
print(frame.iloc[1:3,2:4])