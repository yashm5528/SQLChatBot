import os
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import create_sql_query_chain
from langchain_community.chat_models import ChatOpenAI
class Gpt:
    def __init__(self):
        print("in init")
        os.environ["OPENAI_API_KEY"] = ''
        self.db_path = "C:/Users/anark/Desktop/Capstone/Implementation/Modulated_code/backend/GeoQuery.db"
        self.db = SQLDatabase.from_uri(f"sqlite:///{self.db_path}")
        self.llm = OpenAI(temperature=0)
        self.chain = create_sql_query_chain(self.llm, self.db)
        self.db_chain = SQLDatabaseChain.from_llm(self.llm, self.db , return_intermediate_steps=True)
        print("DB_chain successfull")

    def run_queries(self,query):
        self.response = self.db_chain(query)
        self.intermediateSteps=self.response["intermediate_steps"]
        self.answer=self.response["result"]
        self.response1 = self.chain.invoke({"question": f"{query}"})
        print("query = ",self.response1)
        #print("self.response  = ",self.response)
        #print("self.intermediateSteps = ",self.intermediateSteps)
        print(self.answer)
        return [self.response1, self.answer]

        '''
        self.response = self.chain.invoke({"question": f"{query}"})
        print("query = ",self.response)
        #print("solution = ",self.result)
        print(self.db.run(self.response))
        self.db_chain.run(query)
        '''

        
        