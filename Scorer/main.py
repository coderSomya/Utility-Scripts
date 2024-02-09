import pandas as pd


sheet1 = pd.read_csv('1-result.csv')


sheet2 = pd.read_csv('2-result.csv')


sheet1['Score'] = pd.to_numeric(sheet1['Score'], errors='coerce')
sheet2['Score'] = pd.to_numeric(sheet2['Score'], errors='coerce')


merged = pd.merge(sheet1, sheet2, on='Team Id', suffixes=('_round1', '_round2'), how='outer')

merged['Score_round1'].fillna(0, inplace=True)
merged['Score_round2'].fillna(0, inplace=True)


merged['Total Score'] = merged['Score_round1'] + merged['Score_round2']


merged = merged[['Team Id', 'Team Name_round1', 'Total Score', 'Score_round1', 'Score_round2']]

merged = merged.sort_values(by='Total Score', ascending=False)


merged.to_csv('merged_result.csv', index=False)
