
import pandas as pd
import math
import numpy as np
df = pd.read_csv('../Data/Hospital_Revised_Flatfiles/Deaths.csv')
df = df.drop(['Provider ID', 'Address', 'City', 'ZIP Code', 'County Name', 'Phone Number', 'Compared to National', 'Lower Estimate', 'Higher Estimate','Footnote', 'Measure Start Date', 'Measure End Date'], axis = 1)
df['Ranking'] = 0
pdf = pd.read_csv('../Data/Hospital_Mortality.csv')
for row in df.itertuples():
    for row2 in pdf.itertuples():
        if row[2] == row2[1] and row[3] == row2[2]:
            if row[6] != 'Not Available':
                df.loc[row.Index, 'Ranking'] = float(row[6])*float(row2[9])
            else:
                if row[3] == 'Acute Myocardial Infarction (AMI) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = 13.6*float(row2[9])
                elif row[3] == 'Death rate for chronic obstructive pulmonary disease (COPD) patients':
                    df.loc[row.Index, 'Ranking'] = 8*float(row2[9])
                elif row[3] == 'Death rate for stroke patients':
                    df.loc[row.Index, 'Ranking'] = 14.6*float(row2[9])
                elif row[3] == 'Heart failure (HF) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = 11.9*float(row2[9])
                elif row[3] == 'Pneumonia (PN) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = 15.9*float(row2[9])
        elif row[2] not in row2 and row[3] == row2[2]:
            if row[6] != 'Not Available':
                if row[3] == 'Acute Myocardial Infarction (AMI) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = float(row[6])*0.23435
                elif row[3] == 'Death rate for chronic obstructive pulmonary disease (COPD) patients':
                    df.loc[row.Index, 'Ranking'] = float(row[6])*0.05117
                elif row[3] == 'Death rate for stroke patients':
                    df.loc[row.Index, 'Ranking'] = float(row[6])*0.33798
                elif row[3] == 'Heart failure (HF) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = float(row[6])*0.19212
                elif row[3] == 'Pneumonia (PN) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = float(row[6])*0.18437
            else:
                if row[3] == 'Acute Myocardial Infarction (AMI) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = 13.6*0.23435
                elif row[3] == 'Death rate for chronic obstructive pulmonary disease (COPD) patients':
                    df.loc[row.Index, 'Ranking'] = 8*0.05117
                elif row[3] == 'Death rate for stroke patients':
                    df.loc[row.Index, 'Ranking'] = 14.6*0.33798
                elif row[3] == 'Heart failure (HF) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = 11.9*0.19212
                elif row[3] == 'Pneumonia (PN) 30-Day Mortality Rate':
                    df.loc[row.Index, 'Ranking'] = 15.9*0.18437
ef = pd.read_csv('1_Prime.csv')
ef = ef.drop(['Unnamed: 0', 'Provider ID', 'Address', 'City', 'ZIP Code', 'County Name', 'Phone Number', 'Unnamed: 16', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24' ], axis = 1)
ef = ef.drop(['Compared to National', 'Unnamed: 13', 'Lower Estimate', 'Higher Estimate', 'Footnote', 'Measure Start Date', 'Measure End Date'], axis = 1)
ef = ef.replace(np.nan, 'Not Available', regex=True)
for row in ef.itertuples():
    if row[7] != 'Not Available':
        ef.loc[row.Index, 'Score'] = row[7]
ef = ef.drop('Unnamed: 15', axis = 1)
df.loc[:, 'Score'] = ef.loc[:, 'Score']
for row in df.itertuples():
    if row[6] != 'Not Available':
        if row[3] == 'Death rate for CABG':
            df.loc[row.Index, 'Ranking'] = float(row[6])*0.4
        if row[3] == 'Serious blood clots after surgery':
            df.loc[row.Index, 'Ranking'] = float(row[6])*0.35
        if row[3] == 'Deaths among Patients with Serious Treatable Complications after Surgery':
            df.loc[row.Index, 'Ranking'] = float(row[6])*0.025
    else:
        if row[3] == 'Death rate for CABG':
            df.loc[row.Index, 'Ranking'] = 3.24*0.4
        if row[3] == 'Serious blood clots after surgery':
            df.loc[row.Index, 'Ranking'] = 4.35*0.35
        if row[3] == 'Deaths among Patients with Serious Treatable Complications after Surgery':
df['Category'] = hosList
df.to_csv('HosCateData.csv')
gf = df.pivot_table(values='Ranking', index=['State', 'Hospital Name'], columns=['Category'], aggfunc=np.sum)
hf = df.set_index('State')
