import os
os.environ["OPENAI_API_KEY"] = ''
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
db_path = "C:/Users/anark/Desktop/Capstone/Implementation/Modulated_code/backend/GeoQuery.db"
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
llm = OpenAI(temperature=0)
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
print("DB_chain successful")
db_chain.run("what mountains are in alaska")