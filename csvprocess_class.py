import pandas as pd



class csvprocess_class():
	def __init__(self):
		pass

	#combine runtime together
	#combine a with b's bcol:
	def combine_a_bcol(self,afile,aindex,bfile,bindex,b_col,bnewname,saved_filename):
		dfa=pd.read_csv(afile)
		dfa=dfa.set_index(aindex)

		dfb=pd.read_csv(bfile)
		dfb=dfb.set_index(bindex)

		dfb_select=dfb[b_col]
		dfb_select.columns=bnewname

		dfa=dfa.join(dfb_select)
		print(dfa.shape)
		dfa=dfa.dropna()
		print(dfa.shape)

		dfa.sort_index()
		#dfa.to_csv(saved_filename)
		dfa.to_csv(saved_filename,index=False)

	def combine_acol_bcol(self,afile,aindex,a_col,anewname,bfile,bindex,b_col,bnewname,saved_filename):
		
		#read,set_index,select_col,set_col,join,dropna
		dfa=pd.read_csv(afile)
		dfa=dfa.set_index(aindex)

		dfa=dfa[a_col]
		dfa.columns=anewname

		dfb=pd.read_csv(bfile)
		dfb=dfb.set_index(bindex)

		dfb_select=dfb[b_col]
		dfb_select.columns=bnewname

		dfa=dfa.join(dfb_select)
		print(dfa.shape)
		dfa=dfa.dropna()
		print(dfa.shape)

		dfa.sort_index()
		#dfa.to_csv(saved_filename)
		dfa.to_csv(saved_filename,index=False)

#import os
#files=sorted(os.listdir("./input"))

#input enct1_result.csv:
#ins,model,time,groundsize


files='performance.csv,snake-mt_feature.csv,snake-vl-rc_feature.csv,\
snake_feature.csv,snake-rew_feature.csv,static_feature.csv'.split(',')
print(files)

b=files[0] #performance.csv
attrs='time_snake-mt,time_snake-rew,time_snake-vl-rc,time_snake,wins'.split(',')
b_col=attrs[-1] #wins

for i in range(1,3):
	a=files[i]
	saved_filename='classification1/'+a.split('_')[0]+'_traindata.csv'
	csvc=csvprocess_class()
	csvc.combine_a_bcol(a,'ins',b,'ins',[b_col],['y'],saved_filename)



