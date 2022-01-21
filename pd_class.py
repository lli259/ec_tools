import pandas as pd
class pd_class():
    def __init__(self):
        self.self_pd=None
    
    #get_df and set first col as index
    def get_df(self,file_name):
        df=pd.read_csv(file_name)
        df=df.set_index(df.columns.values[0])
        return df    

    #combine two df when all set first col as index
    def join_df(self,file_namea,file_nameb):
        adf=self.get_df(file_namea)
        bdf=self.get_df(file_nameb)
        self.self_pd=adf.join(bdf)
        self.self_pd=self.self_pd.dropna()

    #add 'xxx' to index, and set it as new index
    #add_chars_to_index(df,'inst','.csv')
    def add_chars_to_index(self,pd_in,colname,chars):
        cols=pd_in[colname]
        cols_chars=[i+chars for i in cols]
        pd_in=pd_in.set_index(colname)
        pd_in[colname]=cols_chars
        pd_in=pd_in.set_index(colname)
        return pd_in
   
if __name__ == "__main__":
    print('pd_class main')
