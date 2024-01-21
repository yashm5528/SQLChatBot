import pandas as pd
from backend import Gpt
mygpt = Gpt()

csv_data = pd.read_csv(r"C:\Users\anark\Desktop\Capstone\Implementation\Modulated_code\Testing\Book1.csv")
records = csv_data.shape[0]
structure = {
    "Human Query": [],
    "Gold Query": [],
    "Generated Query": [],
    "Generated Answer": []
}
df = pd.DataFrame(structure)
nr = {
    "Human Query": 1,
    "Gold Query": 2,
    "Generated Query": 3,
    "Generated Answer": 4
}
new_record_df = pd.DataFrame(nr, index=[0])
df = pd.concat([df, new_record_df], ignore_index=True)
print(df)
'''
for record in range(records):
    query = csv_data.iloc[record]['HumanQuery']
    golden_query = csv_data.iloc[record]['SQLQuery'] 
    try:
        result = mygpt.run_queries(query)
    except:
        print("This question cannot be answered by this database")
        print("Please ask questions related to GeoQuery database")
    new_record = {'HumanQuery': query, 'Gold Query': golden_query, 'Generated Query': result[0], 'Generated Answer': result[1]}
    df = df.append(new_record, ignore_index=True)
    record = record+1

print(df)
'''
'''
from frontend import App
ui = App()
'''
# ADD Buttons