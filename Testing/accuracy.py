import pandas as pd
import re

df = pd.read_csv(r'C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\geography.uw.test.txt.results.csv')

#print(df.head())

print(df.columns)

'''
Index(['Unnamed: 0', 'HumanQuery', 'Gold Query', 'Generated Query',
       'Gold Result', 'Generated Result', 'Generated Answer'],
      dtype='object')
'''

# Extracting columns for comparision & getting accuracy

GoldResult_df = df['Gold Result']
#print(GoldResult_df.head(14))

GeneratedResult_df = df['Generated Result']

Overlap = GoldResult_df.eq(GeneratedResult_df)

Overlap_Percentage = ((Overlap.sum())/len(GeneratedResult_df))*100

print("The accuracy is: ", Overlap_Percentage)