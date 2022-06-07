import pandas as pd

import numpy as np

import sys

import matplotlib.pyplot as plt

import datetime

from matplotlib import dates

import warnings

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")

    df = pd.read_excel('수도권_5호선_3사_파이썬.xlsx', engine="openpyxl")

    df3 = pd.read_excel('SMAP raw file.xlsx', engine="openpyxl")

    df0 = pd.read_excel('DM raw file.xlsx', engine="openpyxl")

    df1 = pd.read_excel('파이썬용 칼럼(SMAP).xlsx', engine="openpyxl")

    df2 = pd.read_excel('파이썬용 칼럼(DM).xlsx', engine="openpyxl")

df_dm_suc = df0[df0['Result'] == 'Success']

df_dm_low = df0[df0['Result'] == 'Low Throughput']

df_dm = pd.concat([df_dm_suc, df_dm_low])

df_smap_suc = df3[df3['Result'] == 'Success']

df_smap_low = df3[df3['Result'] == 'Low Throughput']

df_smap = pd.concat([df_smap_suc, df_smap_low])

df_dm = df_dm.replace(' ', np.nan)

df_smap = df_smap.replace(' ', np.nan)

dfSKT = df_dm[df_dm['[Smart Phone] Android Mobile SP Name'] == 'SK Telecom']

dfKT = df_dm[df_dm['[Smart Phone] Android Mobile SP Name'] == 'KT']

dfLG = df_dm[df_dm['[Smart Phone] Android Mobile SP Name'] == 'LGU+']

dfSKTD = dfSKT[dfSKT['[SKT Speed Test App Info] Call Type'] == 'FTP DL']

dfSKTU = dfSKT[dfSKT['[SKT Speed Test App Info] Call Type'] == 'FTP UL']

dfSKTP = dfSKT[dfSKT['[SKT Speed Test App Info] Call Type'] == 'Ping']

dfKTD = dfKT[dfKT['[SKT Speed Test App Info] Call Type'] == 'FTP DL']

dfKTU = dfKT[dfKT['[SKT Speed Test App Info] Call Type'] == 'FTP UL']

dfKTP = dfKT[dfKT['[SKT Speed Test App Info] Call Type'] == 'Ping']

dfLGD = dfLG[dfLG['[SKT Speed Test App Info] Call Type'] == 'FTP DL']

dfLGU = dfLG[dfLG['[SKT Speed Test App Info] Call Type'] == 'FTP UL']

dfLGP = dfLG[dfLG['[SKT Speed Test App Info] Call Type'] == 'Ping']

dm_final = pd.DataFrame()

a0 = dfSKT['5G-NR Network Ratio'].mean(axis=0)

a1 = dfKT['5G-NR Network Ratio'].mean(axis=0)

a2 = dfLG['5G-NR Network Ratio'].mean(axis=0)

a3 = a0 - max(a1, a2)

b0 = dfSKTP['[SKT Speed Test App Info] Ping Avg Result'].mean(axis=0)

b1 = dfKTP['[SKT Speed Test App Info] Ping Avg Result'].mean(axis=0)

b2 = dfLGP['[SKT Speed Test App Info] Ping Avg Result'].mean(axis=0)

b3 = b0 - max(b1, b2)

c0 = len(dfSKTD)

c1 = len(dfKTD)

c2 = len(dfLGD)

d0 = dfSKTD['Result'].value_counts('Low Throughput')

d1 = dfKTD['Result'].value_counts('Low Throughput')

d2 = dfLGD['Result'].value_counts('Low Throughput')

temp = '임시'

e0 = dfSKTD['[SKT Speed Test App Info] Download APP Throughput[Mbps]'].mean(axis=0)

e1 = dfKTD['[SKT Speed Test App Info] Download APP Throughput[Mbps]'].mean(axis=0)

e2 = dfLGD['[SKT Speed Test App Info] Download APP Throughput[Mbps]'].mean(axis=0)

e3 = e0 - max(e1, e2)

f0 = dfSKTD['[5G-NR Qualcomm] Total MAC DL Throughput [Mbps]'].mean(axis=0)

f1 = dfKTD['[5G-NR Qualcomm] Total MAC DL Throughput [Mbps]'].mean(axis=0)

f2 = dfLGD['[5G-NR Qualcomm] Total MAC DL Throughput [Mbps]'].mean(axis=0)

f3 = f0 - max(f1, f2)

g0 = e2 * 1.25

g1 = e0 - g0

if g1 < 0:

    g2 = '열위'

else:

    g2 = '우위'

dm_final.loc[:, '5G 점유율 SKT'] = [a0]

dm_final.insert(1, '5G 점유율 KT', a1, True)

dm_final.insert(2, '5G 점유율 LG', a2, True)

dm_final.insert(3, '5G 점유율 Gap', a3, True)

dm_final.insert(4, 'RTT SKT', b0, True)

dm_final.insert(5, 'RTT KT', b1, True)

dm_final.insert(6, 'RTT LG', b2, True)

dm_final.insert(7, 'RTT Gap', b3, True)

dm_final.insert(8, '시도호 SKT', c0, True)

dm_final.insert(9, '시도호 KT', c1, True)

dm_final.insert(10, '시도호 LG', c2, True)

dm_final.insert(11, '속도저조 SKT', d0, True)

dm_final.insert(12, '속도저조 KT', d1, True)

dm_final.insert(13, '속도저조 LG', d2, True)

dm_final.insert(14, '성공률 SKT', temp, True)

dm_final.insert(15, '성공률 KT', temp, True)

dm_final.insert(16, '성공률 LG', temp, True)

dm_final.insert(17, '성공률 Gap', temp, True)

dm_final.insert(18, 'APP T/P SKT', e0, True)

dm_final.insert(19, 'APP T/P KT', e1, True)

dm_final.insert(20, 'APP T/P LG', e2, True)

dm_final.insert(21, 'APP T/P Gap', e3, True)

dm_final.insert(22, '5G MAC T/P SKT', f0, True)

dm_final.insert(23, '5G MAC T/P KT', f1, True)

dm_final.insert(24, '5G MAC T/P LG', f2, True)

dm_final.insert(25, '5G MAC T/P Gap', f3, True)

dm_final.insert(26, '', f3, True)

dm_final