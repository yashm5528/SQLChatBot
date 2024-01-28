import sqlite3
import pandas as pd
from backend import Gpt
mygpt = Gpt()

csv_data = pd.read_csv(r'C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\Book1.csv')
records = csv_data.shape[0]

df = pd.DataFrame()

for record in range(records):
    conn = sqlite3.connect(r'C:\Users\anark\Desktop\Capstone\SQLChatBot\backend\GeoQuery.db')
    cursor = conn.cursor()
    query = csv_data.iloc[record]['HumanQuery']
    golden_query = csv_data.iloc[record]['SQLQuery'] 
    try:
        result = mygpt.run_queries(query)
        golden_output = cursor.execute(golden_query)
        gold_result = golden_output.fetchall()
        #normalized_gold_result = ', '.join(str(item[0]) for item in gold_result)
        generated_sql_output = cursor.execute(result[0])
        generated_sql_result = generated_sql_output.fetchall()
        #normalized_generated_sql_result = ', '.join(str(item[0]) for item in generated_sql_result)

    except:
        print("This question cannot be answered by this database")
        print("Please ask questions related to GeoQuery database")
    new_record = {'HumanQuery': query, 'Gold Query': golden_query, 'Generated Query': result[0], 'Gold Result': gold_result,'Generated Result':generated_sql_result, 'Generated Answer': result[1]}
    df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    record = record+1

print(df)
print('------------------------')
print(df.iloc[:1])
print('------------------------')
df.to_excel(r"C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\Book1_results.xlsx")
df.to_csv(r"C:\Users\anark\Desktop\Capstone\SQLChatBot\Testing\Book1_results.csv")

