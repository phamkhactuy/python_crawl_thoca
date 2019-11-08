import pandas as pd 
data = pd.read_csv("C:/Users/pktuy/Desktop/20191108_thoca.csv", delimiter = ';',prefix = 'T',header = 0) 
#print(data)
for index,row in data.iterrows():
    print(row['ABCD'])
