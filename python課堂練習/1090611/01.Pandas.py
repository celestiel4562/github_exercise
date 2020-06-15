import pandas as pd

ss1=pd.Series([1,3,5,7,"數字"])  #pd.Series中的S必須為大寫
print(ss1)  #輸出陣列
print(ss1.values)  #輸出Series中的值
print(ss1.index)   #輸出Series索引
print(ss1[0])  #輸出對應索引[i]的值
print('#索引0有無在陣列中:','0' in ss1)  #索引0有無在Series中
print("#內容7有無於陣列中:",7 in ss1.values)  #內容7有無於Series中
print("-"*10)
print(ss1*2) #內容*2
print("-"*20)

ss2=pd.Series(["ABC","ㄅㄆㄇ","あいう",100],index=["I","II","III","IV"])#自訂索引
print(ss2)
print(ss2.values)
print(ss2.index)
print('#索引[I]有無在陣列中:','I' in ss2)  #索引0有無在陣列中
print("#內容ABC(str)有無於陣列中:","ABC" in ss2.values)  #內容有無於陣列中
print("#內容100(int)有無於陣列中:",100 in ss2.values)  #內容有無於陣列中
print("-"*20)

#串列轉Series
print("↓↓串列轉陣列↓↓")
list_sample=["a",1,"b",3,"c",5,"d",7,"e","數字"]
list_to_series=pd.Series(list_sample)
print(list_to_series)
print("-"*20)

#字典轉Series
print("↓↓字典轉陣列↓↓")
dict_sample={"a":1,"b":3,"c":5,"d":7,"e":"數字"}
dict_to_series=pd.Series(dict_sample)
print(dict_to_series)
print("-"*20)
