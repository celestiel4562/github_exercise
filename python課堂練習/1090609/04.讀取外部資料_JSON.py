import json

fn="C:\Users\ASUS\Desktop\PYTHON\課堂練習\opendata_samples\"
with open(fn,encoding="utf-8-sig") as jsFile:
    jsdata=json.load(jsFile)
    for item in jsdata:
        print(item["sno"],item["sarea"],item["sna"],item["tot"])
        
