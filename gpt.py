import os
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
class Gpt:
    def __init__(self):
        print("in init")
        os.environ["OPENAI_API_KEY"] = ''
        self.db_path = "C:/Users/anark/Desktop/Capstone/Implementation/Modulated_code/backend/GeoQuery.db"
        self.db = SQLDatabase.from_uri(f"sqlite:///{self.db_path}")
        self.llm = OpenAI(temperature=0)
        self.db_chain = SQLDatabaseChain(llm=self.llm, database=self.db)
        print("DB_chain successfull")

    def run_queries(self,query):
        self.db_chain.run(query)
        
        