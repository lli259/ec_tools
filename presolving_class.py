import pandas as pd



class presolving():
    def __init__(self):
        pass

    def presolving_3_encodings(self,pre_time,lists_3):      
        allpss=0
        c1,c2,c3=lists_3[0],lists_3[1],lists_3[2]
        for i in range(len(c1)):
            if c1[i]<=pre_time or c2[i]<=pre_time or c3[i]<=pre_time:
                allpss+=1

        print(allpss*1.0/len(df))


pre_run_time=20
filename='snake_performance.csv'
df=pd.read_csv(filename)
column=df.columns.values
best_index=[1,2,3]
c1=df[column[best_index[0]]].values
c2=df[column[best_index[1]]].values
c3=df[column[best_index[2]]].values

pres=presolving()
pres.presolving_3_encodings(pre_run_time,[c1,c2,c3])