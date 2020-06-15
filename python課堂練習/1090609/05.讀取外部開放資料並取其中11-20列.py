import json

fn=r"C:\Users\ASUS\Desktop\PYTHON\課堂練習\opendata_samples\drugstore.json"
with open(fn,encoding="utf-8-sig") as jsFile:
    jsdata=json.load(jsFile)
    
    n=0
    for x in jsdata:
        if x["地址縣市別"]=="新北市" and x["機構狀態"]=="開業":
            n+=1
            if n>=0 and n<=10:
                print(x["機構名稱"])
                print(x["地址縣市別"]+x["地址鄉鎮市區"]+x["地址街道巷弄號"])
            if n>=11:
                break