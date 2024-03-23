import sqlite3
import pandas as pd

csv_data = pd.read_csv(r'C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\geography.uw.test.txt.csv')
records = csv_data.shape[0]

df = pd.DataFrame()

# Open the SQLite connection and cursor once
conn = sqlite3.connect(r'C:\Users\anark\Desktop\Capstone\SQLChatBot\backend\GeoQuery.db')
cursor = conn.cursor()

for record in range(records):
    golden_query = csv_data.iloc[record]['SQLQuery'] 
    golden_output = cursor.execute(golden_query)
    gold_result = golden_output.fetchall()
    if gold_result:
        final_result = gold_result[0]
    else:
        final_result = None
    
    new_record = {'Gold Result': final_result}
    df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    record = record+1
    #print(df)

# Close the SQLite connection and cursor
cursor.close()
conn.close()

print(df.head(15))
df.to_excel(r"C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\geography.gold.results.xlsx")
df.to_csv(r"C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\geography.gold.results.csv")