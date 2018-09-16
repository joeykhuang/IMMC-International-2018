
import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv('../../Dat/HospitalInformation.csv')
df.sort_values('P', ascending = False)
df['MortalityRanked'] = 0
df['PatientRanked'] = 0
df['PSIRanked'] = 0
df['SpendingRanked'] = 0
l_mort_min = df['Mortality'].min()
l_mort_max = df['Mortality'].max()
l_mort_range = l_mort_max - l_mort_min
l_patient_min = df['P'].min()
l_patient_max = df['P'].max()
l_patient_range = l_patient_max - l_patient_min
l_psi_min = df['PSI'].min()
l_psi_max = df['PSI'].max()
l_psi_range = l_psi_max - l_psi_min
l_spending_min = df['Spending'].min()
l_spending_max = df['Spending'].max()
l_spending_range = l_spending_max - l_spending_min
for row in df.itertuples():
    df.loc[row.Index, 'MortalityRanked'] = 10*(float(row[7]) - l_mort_min)/l_mort_range
    df.loc[row.Index, 'PatientRanked'] = 10*(float(row[8]) - l_patient_min)/l_patient_range
    df.loc[row.Index, 'PSIRanked'] = -10*(float(row[9]) - l_psi_max)/l_psi_range
    df.loc[row.Index, 'SpendingRanked'] = -10*(float(row[10]) - l_spending_max)/l_spending_range
gf = df.drop(['Mortality', 'P', 'PSI', 'Spending'], axis = 1)
gf.to_csv('RankedHospitalInfo.csv')
gf['TotalRanking'] = 0
for row in gf.itertuples():
    gf.loc[row.Index, 'TotalRanking'] = row[7]*0.375 + row[9]*0.15 + row[10]*0.10
gf['TotalRankingReranked'] = 0
l_min = gf['TotalRanking'].min()
l_max = gf['TotalRanking'].max()
l_range = l_max - l_min
for row in gf.itertuples():
    gf.loc[row.Index, 'TotalRankingReranked'] = 10*(float(row[11]) - l_min)/l_range
gf.sort_values(by='TotalRankingReranked', ascending = False)
gf.to_csv('FinalRankingsSens.csv')
