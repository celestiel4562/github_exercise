import csv

Infn=r'\\putqc\學員上傳區\Train\Exercise\Exercise_5\input.csv'
Outfn=r'C:\Users\ASUS\Desktop\PYTHON\課堂練習\1090608\output_2.csv'
extralist=[['花茶',15],['蜜茶',10]]

with open(Infn) as csv_inFile:
    csvReader=csv.reader(csv_inFile)
    datalist=list(csvReader)
    
with open(Outfn,'w',newline="",encoding='utf-8') as csv_outFile:
    csvwriter=csv.writer(csv_outFile,delimiter="\t")
    for row in datalist:
        csvwriter.writerow(row)

    csvwriter.writerow(["-----------"])
    list_comb=datalist+extralist
    
    for row in list_comb:
        csvwriter.writerow(row)