import csv

fn="csvINPUT.csv"
with open('csvINPUT_2.csv','w',newline='') as csvFile:
    csvwriter=csv.writer(csvFile)
    csvwriter.writerow(['編號','用戶名','購買總金額','有無購買'])
    csvwriter.writerow(['01','Gina tang',1000,'TRUE'])
    csvwriter.writerow(['02','Katty Lin',0,'FALSE'])
    csvwriter.writerow(['03','Wang Wang',25285,True])
    