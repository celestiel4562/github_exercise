import json

dict1={"breakfast":50,"lunch":80,"dinner":100}
fn=r"C:\Users\ASUS\Desktop\PYTHON\課堂練習\1090609\jsonoutput.json"

with open (fn,"w") as objFile:
    json.dump(dict1,objFile,ensure_ascii=False)
    
with open (fn,"r") as objFile:
    objData=json.load(objFile)

print("早餐費用:{:d}元".format(objData["breakfast"]))
print("午餐費用:{:d}元".format(objData["lunch"]))
print("晚餐費用:{:d}元".format(objData["dinner"]))    



