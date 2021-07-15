'''
- 해시문제 데이터분석으로 풀어보기
- 해시를 이용한 해결책 제시하기
'''

import pandas as pd
import numpy as np
def solution(genres, plays):
    result=[]
    df=pd.DataFrame({
        'genres':genres,
        'plays':plays
    })
    print(df)
    print(df.groupby(df['genres']).sum())
    df1=df.groupby(df['genres']).sum().sort_values(by='plays',ascending=False)
    for i in df1.index:
        #print(i)
        print(df[df['genres']==i].sort_values(by='plays',ascending=False)[:2])
        rank_idx=df[df['genres']==i].sort_values(by='plays',ascending=False)[:2].index
        rank_idx=list(rank_idx) #list로 변환
        result.extend(rank_idx) #list 병합
    return df