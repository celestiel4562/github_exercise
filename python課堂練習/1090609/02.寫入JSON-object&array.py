import json

dictobject={"x":100,"y":100.01,"z":"壹零零"}
fn="pythontojsonobject.json"
with open(fn,"w") as objfile:
    json.dump(dictobject,objfile,ensure_ascii=False)
    ###無ensure_ascii=False的話，寫入字元顯示為unicode
    
    
arraylist=[123,100.01,{"A":"一三五","B":246,"C":True},{"a":135,"b":"二四六","C":False}]
fn="pythontojsonarray.json"
with open(fn,"w") as aryfile:
    json.dump(arraylist,aryfile,ensure_ascii=False)