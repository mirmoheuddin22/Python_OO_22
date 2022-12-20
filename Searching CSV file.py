import csv
with open("D:\Python_OO\Historical Data.csv", 'r') as f1:
    CSV_data = csv.reader(f1)
    header = next(CSV_data) #read first row & skip first row (header).
    Historical_data = list(CSV_data)
    f1.close()
    #for row in Historical_data:
        #[int(i) for i in row]
    #print(Historical_data)
    list = []
    for row in Historical_data:
        change = ((((int(col[4])-int(col[1]))/int(col[1]))*100) for col in row)
        #print(change)
        list.append(change)
    print(list)
with open("D:\\Python_OO\location\\New.csv", 'w') as f2:
    write = csv.writer(f2)
    write.writerow(list)
    f2.close()


