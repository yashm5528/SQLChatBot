import sqlite3
import pandas as pd
from backend import Gpt
mygpt = Gpt()
#geography.uw.test.txt
csv_data = pd.read_csv(r"C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\geography.uw.test.txt - Copy.csv")
records = csv_data.shape[0]

df = pd.DataFrame()
conn = sqlite3.connect(r'C:\Users\anark\Desktop\Capstone\SQLChatBot\backend\GeoQuery.db')
cursor = conn.cursor()
conn1 = sqlite3.connect(r'C:\Users\anark\Desktop\Capstone\SQLChatBot\backend\GeoQuery.db')
cursor1 = conn1.cursor()
for record in range(records):
    query = csv_data.iloc[record]['HumanQuery']
    query = query + " " + "Reply like you are interacting with a human"
    golden_query = csv_data.iloc[record]['SQLQuery'] 
    try:
        result = mygpt.run_queries(query)
        golden_output = cursor.execute(golden_query)
        gold_result = golden_output.fetchall()
        generated_sql_output = cursor1.execute(result[0])
        generated_sql_result = generated_sql_output.fetchall()
        new_record = {'HumanQuery': query, 'Gold Query': golden_query, 'Generated Query': result[0], 'Gold Result': gold_result,'Generated Result': generated_sql_result, 'Generated Answer': result[1]}
        print(new_record)
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    except:
        print("This question cannot be answered by this database")
        print("Please ask questions related to GeoQuery database")
        record = record+1
cursor.close()
conn.close()
cursor1.close()
conn1.close()
print(df)
print('------------------------')
print(df.iloc[:1])
print('------------------------')
df.to_excel(r"C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\geography.uw.test.txt.results.xlsx")
df.to_csv(r"C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\geography.uw.test.txt.results.csv")

