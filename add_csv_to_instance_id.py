import sys
import pandas as pd

filename=sys.argv[1]
df=pd.read_csv(filename)
#df=df.set_index('ins')

insts=df['ins']
instscsv=[i+'.csv' for i in insts]
df=df.set_index('ins')
df['ins']=instscsv
df=df.set_index('ins')

df.to_csv("new/"+filename)


