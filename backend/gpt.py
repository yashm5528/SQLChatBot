import os
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import create_sql_query_chain
from langchain_community.chat_models import ChatOpenAI
class Gpt:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = ''
        self.db_path = "C:/Users/anark/Desktop/Capstone/Implementation/Modulated_code/backend/GeoQuery.db"
        self.db = SQLDatabase.from_uri(f"sqlite:///{self.db_path}")
        self.llm = OpenAI(temperature = 0)
        self.db_chain = SQLDatabaseChain.from_llm(self.llm, self.db, return_sql = True, top_k = 1)
        self.db_chain1 = SQLDatabaseChain.from_llm(self.llm, self.db, return_intermediate_steps = True, top_k = 1)
        print("DB_chain successfull")

    def run_queries(self,query):
        self.response = self.db_chain(query)
        self.answer=self.response["result"]
        self.response1 = self.db_chain1(query)
        self.answer1 = self.response1["result"]
        return [self.answer, self.answer1]



        
        