import pandas as pd



class interleave_class():
    def __init__(self):
        pass
    #input list, cap_runtime
    #return solve percentage, avg time
    def solve_perc_avg_time(self,input_list,cap_runtime):
        leng=len(input_list)*1.0
        sov=sum([i<cap_runtime for i in input_list])
        time=sum(input_list)
        return sov/leng,time/leng


    #input: list of runtime, time_each,total_time
    #for example [10,3,13], 4, 20
    #1,2,3,1,2,3,...
    #return runtime of interleave_runing
    def interleave_runing(self,list_solver_time,time_each,total_time):
        timeout=False
        index=0
        used_time_list=[0 for i in list_solver_time]

        #init: all time set 0, start from index 0
        #continue solving, until one's time < time_each+ his used time
        #then he uses his time in total. other use the used time.
        while not timeout:
            if list_solver_time[index]<=time_each+used_time_list[index]:
                solved=index 
                break
            else:
                used_time_list[index]+=time_each
                index+=1
                if index==len(list_solver_time):
                    index=0

            if sum(used_time_list)>=total_time:
                timeout=True
        
        if timeout:
            return total_time

        re=0
        for i in range(len(list_solver_time)):
            if i==solved:
                re+=list_solver_time[i]
            else:
                re+=used_time_list[i]
        return re


    def interleave_run_four_lists(self,la,lb,lc,ld,time_each=20,total_time=400):
        re=[]
        for i in range(len(la)):
            list_time=[la[i],lb[i],lc[i],ld[i]]
            r=self.interleave_runing(list_time,time_each,total_time)
            re.append(r)
        return re

    def interleave_run_three_lists(self,la,lb,lc,time_each=20,total_time=400):
        re=[]
        for i in range(len(la)):
            list_time=[la[i],lb[i],lc[i]]
            r=self.interleave_runing(list_time,time_each,total_time)
            re.append(r)
        return re

    def interleave_run_two_lists(self,la,lb,time_each=20,total_time=400):
        re=[]
        for i in range(len(la)):
            list_time=[la[i],lb[i]]
            r=self.interleave_runing(list_time,time_each,total_time)
            re.append(r)
        return re

    #input 4 lists, time range, time each
    def interleave_diff_tm_n_ord_4list_(self,input_la,input_lb,input_lc,input_ld,rs,re,r,time_each=20,total_time=400):
        #print(column)
        alldata=[input_la,input_lb,input_lc,input_ld]
        for time_each in range(rs,re,r):
            allfour=[]
            size=4
            for i in range(size):
                for j in range(size):
                    for a in range(size):
                        for b in range(size):
                            if not (i==j or i==a or i==b or j==a or j==b or a==b):
                                la,lb,lc,ld=alldata[i],alldata[j],alldata[a],alldata[b]
                                re_list=self.interleave_run_four_lists(la,lb,lc,ld,time_each,total_time)
                                s,t=self.solve_perc_avg_time(re_list,total_time)
                                si,sj,sa,sb=str(i),str(j),str(a),str(b)
                                allfour.append((s,t,'_'.join([si,sj,sa,sb])))
            allfour=sorted(allfour)
            #time, best result and order in the time
            print(time_each,allfour[-1])



    def interleave_diff_tm_n_ord_3list_(self,input_la,input_lb,input_lc,rs,re,r,time_each=20,total_time=400):
        #print(column)
        alldata=[input_la,input_lb,input_lc]
        for time_each in range(rs,re,r):
            allthree=[]
            size=3
            for i in range(size):
                for j in range(size):
                    for a in range(size):
                            if not (i==j or i==a or j==a ):
                                la,lb,lc=alldata[i],alldata[j],alldata[a]

                                re_list=self.interleave_run_three_lists(la,lb,lc,time_each,total_time)
                                s,t=self.solve_perc_avg_time(re_list,total_time)

                                si,sj,sa=str(i),str(j),str(a)
                                allthree.append((s,t,'_'.join([si,sj,sa])))

            allthree=sorted(allthree)
            print(time_each,allthree[-1])       


    def interleave_diff_tm_n_ord_2list_(self,input_la,input_lb,rs,re,r,time_each=20,total_time=400):
        #print(column)
        alldata=[input_la,input_lb]
        for time_each in range(rs,re,r):
            allret=[]
            size=2
            for i in range(size):
                for j in range(size):
                            if not (i==j):
                                la,lb=alldata[i],alldata[j]
                                re_list=self.interleave_run_two_lists(la,lb,time_each,total_time)
                                s,t=self.solve_perc_avg_time(re_list,total_time)
                                si,sj=str(i),str(j)
                                allret.append((s,t,'_'.join([si,sj])))

            allret=sorted(allret)
            print(time_each,allret[-1])       


df=pd.read_csv('snake_performance.csv')
df=df.set_index('ins')
column=df.columns.values
input_la,input_lb,input_lc,input_ld=df[column[0]],df[column[1]],df[column[2]],df[column[3]]


intlv=interleave_class()
#intlv.interleave_diff_tm_n_ord_4list_(input_la,input_lb,input_lc,input_ld,10,70,5,time_each=20,total_time=400)


input_la,input_lb,input_lc=df[column[0]],df[column[1]],df[column[2]]
#intlv.interleave_diff_tm_n_ord_3list_(input_la,input_lb,input_lc,10,70,5,time_each=20,total_time=400)


input_la,input_lb=df[column[0]],df[column[1]]
intlv.interleave_diff_tm_n_ord_2list_(input_la,input_lb,10,70,5,time_each=20,total_time=400)

exit()