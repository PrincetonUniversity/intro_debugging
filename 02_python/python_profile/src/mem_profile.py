
import pandas as pd
from time import time
from memory_profiler import profile
from functools import reduce

@profile
def concatenate_samples(sample1_file,sample2_file,sample3_file):
    df_1 = pd.read_csv(sample1_file,sep='\t', header=None)
    df_2 = pd.read_csv(sample2_file,sep='\t', header=None)
    df_3 = pd.read_csv(sample3_file,sep='\t', header=None)
    frames = [df_1, df_2, df_3]
    df_All = pd.concat(frames)
    return df_All

@profile
def concatenate_samples_better(sample1_file,sample2_file,sample3_file):
    df_1 = pd.read_csv(sample1_file,sep='\t', header=None)
    df_2 = pd.read_csv(sample2_file,sep='\t', header=None)
    df_3 = pd.read_csv(sample3_file,sep='\t', header=None)
    df_All = df_1.append(df_2, ignore_index=True)
    df_All = df_All.append(df_3, ignore_index=True)
    return df_All

@profile
def concatenate_samples_even_better(sample1_file,sample2_file,sample3_file):
    df_All = pd.concat([pd.read_csv(sample1_file,sep='\t', header=None),
                        pd.read_csv(sample2_file,sep='\t', header=None),
                        pd.read_csv(sample3_file,sep='\t', header=None)], axis=0)
    return df_All

@profile
def three_merge_1(sample1_file,sample2_file,sample3_file):
    df_1 = pd.read_csv(sample1_file,sep='\t', header=None)
    df_1.drop(df_1.columns[3:], axis=1, inplace=True)
    df_1.columns = ["ID", "start", "end"]
    df_2 = pd.read_csv(sample2_file,sep='\t', header=None)
    df_2.drop(df_2.columns[3:], axis=1, inplace=True)
    df_2.columns = ["ID", "start", "end"]
    df_3 = pd.read_csv(sample3_file,sep='\t', header=None)
    df_3.drop(df_3.columns[3:], axis=1, inplace=True)
    df_3.columns = ["ID", "start", "end"]
    df_All = pd.merge(pd.merge(df_1,df_2,on=['ID','start']),df_3,on=['ID','start'])
    return df_All

@profile
def three_merge_2(sample1_file,sample2_file,sample3_file):
    df_1 = pd.read_csv(sample1_file,sep='\t', header=None)
    df_1.drop(df_1.columns[3:], axis=1, inplace=True)
    df_1.columns = ["ID", "start", "end"]
    df_2 = pd.read_csv(sample2_file,sep='\t', header=None)
    df_2.drop(df_2.columns[3:], axis=1, inplace=True)
    df_2.columns = ["ID", "start", "end"]
    df_3 = pd.read_csv(sample3_file,sep='\t', header=None)
    df_3.drop(df_3.columns[3:], axis=1, inplace=True)
    df_3.columns = ["ID", "start", "end"]
    dfs = [df_1, df_2, df_3]
    df_All = reduce(lambda left,right: pd.merge(left,right,on=['ID','start']), dfs)
    return df_All

@profile
def three_merge_3(sample1_file,sample2_file,sample3_file):
    df_1 = pd.read_csv(sample1_file,sep='\t', header=None)
    df_1.drop(df_1.columns[3:], axis=1, inplace=True)
    df_1.columns = ["ID", "start", "end"]
    df_2 = pd.read_csv(sample2_file,sep='\t', header=None)
    df_2.drop(df_2.columns[3:], axis=1, inplace=True)
    df_2.columns = ["ID", "start", "end"]
    df_3 = pd.read_csv(sample3_file,sep='\t', header=None)
    df_3.drop(df_3.columns[3:], axis=1, inplace=True)
    df_3.columns = ["ID", "start", "end"]
    df_All = pd.merge(df_1,df_2,on=['ID','start'])
    df_All = pd.merge(df_All,df_3,on=['ID','start'])
    return df_All

if __name__ == '__main__':
    start = time()
    df_All = concatenate_samples('../metadata/sample_1.bed', '../metadata/sample_2.bed', '../metadata/sample_3.bed')
    end = time()
    print(f'Time taken {round(end - start,4)} seconds.')