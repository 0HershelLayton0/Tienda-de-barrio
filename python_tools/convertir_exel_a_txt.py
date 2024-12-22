import os 
import pandas as pd


direc=os.getcwd()
direc=os.path.join(direc,'database')
direc=os.path.join(direc,'Data.csv')
print(direc)
data1=pd.read_csv(direc)

#print(data1)

direc=os.getcwd()
direc=os.path.join(direc,'database')
direc=os.path.join(direc,'text2.txt')
text2=open(direc,'w')

for i in range(15):
    for j in range(5):
        if(j!=2):
            text2.write(data1.iloc[i,j])
        else :
            text2.write(str(data1.iloc[i,j]))
        text2.write('#')
    text2.write('\n')

text2.close()