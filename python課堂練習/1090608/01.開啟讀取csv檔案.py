"""
import csv
fn=
with open("sample.csv",encoding="utf-8 sig") as csvFile: #開啟csv
    csvReader=csv.reader(csvFile) #讀取csv建立reader物件
    listReport=list(csvReader) #將資料轉成list(串列)
print(listReport)

"""


"""
#當csv檔案的編碼為UTF-8
import csv

fn=r"C:\Users\ASUS\Desktop\PYTHON\課堂練習\1090608\opendata106N0101.csv"
#fn="C:\\Users\\ASUS\\Desktop\\PYTHON\\課堂練習\\1090608\\opendata106N0101.csv"
#fn="C:/Users/ASUS/Desktop/PYTHON/課堂練習/1090608/opendata106N0101.csv"

with open(fn,encoding="utf-8 sig") as csv_file: 
    csv_reader=csv.reader(csv_file)
    csvlist=list(csv_reader)
print(csvlist)
"""


"""
#當csv檔案的編碼為ANSI
fn=r"C:\Users\ASUS\Desktop\PYTHON\課堂練習\1090608\sample_ansi.csv"
with open(fn) as csvFile:
    csvReader=csv.reader(csvFile)
    listReport=list(csvReader)

print(listReport)
"""