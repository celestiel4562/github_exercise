import csv

Infn=r'\\putqc\學員上傳區\Train\Exercise\Exercise_5\input.csv'
Outfn='output.csv'
extra_item=[['花茶',15],['蜜茶',10]]

with open(Infn) as csvFile:
    csvReader=csv.reader(csvFile)
    listReport=list(csvReader)
        
with open(Outfn,'w',newline='',encoding='utf8') as csvReFile:
    csvwriter=csv.writer(csvReFile,delimiter='\t')  
    for row in listReport:
        csvwriter.writerow(row)
    csvwriter.writerow(["---------------"])
    for row in listReport:
        csvwriter.writerow(row)
    for row in extra_item:
        csvwriter.writerow(row)
