import pandas as pd
Data = pd.read_csv("D:\Python_OO\Historical Data.csv")
#print(data.head(10))
#print(data.tail(10))
#data_percentage_change= Data.loc[:,'Close']
#Data['% Change'] = data_percentage_change.pct_change()
#print(Data.head(10))
Data['% change'] = Data[['Open','Close']].pct_change(axis=1)['Close']
#print(Data)
Data.drop(['Date','Open','High','Low','Close','AdjClose','Volume'], axis=1, inplace=True)
print(Data)
#Historical_data = list(Data[0])
#print(Historical_data)
import csv
with open("D:\\Python_OO\location\\New4.csv", 'w') as f1:
  write = csv.writer(f1)
  write.writerow(Data)
  f1.close()


