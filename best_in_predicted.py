import pandas as pd



class bestin2_class():
    def a_in_b_or_c(self,a,b,c):
        re=[]
        for i in range(len(a)):
            if a[i] == b[i] or a[i] ==c[i]:
                re.append(1)
            else:
                re.append(0)
        return re

df=pd.read_csv('predict.csv')

best2=bestin2_class()
re=best2.a_in_b_or_c(df.wins.values,df.best.values,df.sec_best.values)

print(sum(re)/(len(re)*1.0))
