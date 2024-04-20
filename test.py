import sqlite3
import pandas as pd
from backend import Gpt
import re
import pickle

mygpt = Gpt()
#geography.uw.test.txt - Copy
csv_data = pd.read_csv(r"Testing\geography.uw.test.txt.csv")
records = csv_data.shape[0]

df = pd.DataFrame()
conn = sqlite3.connect(r'backend\GeoQuery.db')
cursor = conn.cursor()
for record in range(records):
    query = csv_data.iloc[record]['HumanQuery']
    prompt = query
    golden_query = csv_data.iloc[record]['SQLQuery'] 
    try:
        result = mygpt.run_queries(prompt)
        golden_output = cursor.execute(golden_query)
        gold_result = golden_output.fetchall()
        new_record = {'HumanQuery': query, 'Gold Query': golden_query, 'Generated Query': result[0], 'Gold Result': gold_result,'Generated Result': result[2], 'Generated Answer': result[1]}
        print(new_record)
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    except:
        print("This question cannot be answered by this database")
        print("Please ask questions related to GeoQuery database")
        new_record = {'HumanQuery': query, 'Gold Query': golden_query, 'Generated Query': 
                      "This question cannot be answered by this database", 'Gold Result': gold_result,'Generated Result': 
                      "[(NA,)]", 'Generated Answer': "NA"}
        print(new_record)
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        record = record+1
cursor.close()
conn.close()
print(df)
print('------------------------')
print(df.iloc[:1])
print('------------------------')
df.to_excel(r"Testing\geography.uw.test.txt.results.xlsx")
df.to_csv(r"Testing\geography.uw.test.txt.results.csv")

with open('geography.uw.test.txt.results.pkl', 'wb') as f:
    pickle.dump(df, f)

df.head(10)