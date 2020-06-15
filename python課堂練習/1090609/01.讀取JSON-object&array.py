import json  #導入JSON模組

fn="jsonobject.json"
with open(fn) as file:  #讀取JSON 物件(json.load)
    data=json.load(file)
    print(data)
    print(type(data))
    
fn2="jsonsarray.json"
with open(fn2) as file2: #讀取JSON 陣列(json.load)
    data2=json.load(file2)
    print(data2)
    print(type(data2))