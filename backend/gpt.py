import os
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
#from langchain.chains import create_sql_query_chain
#from langchain_community.chat_models import ChatOpenAI
import sqlite3
class Gpt:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = ''
        self.db_path = "C:/Users/anark/Desktop/Capstone/Implementation/Modulated_code/backend/GeoQuery.db"
        self.db = SQLDatabase.from_uri(f"sqlite:///{self.db_path}")
        self.llm = OpenAI(temperature = 0)
        self.db_chain = SQLDatabaseChain.from_llm(self.llm, self.db, return_sql = True, top_k = 0)
        #self.db_chain1 = SQLDatabaseChain.from_llm(self.llm, self.db, return_intermediate_steps = True, top_k = 0)
        #Add code to give the query and the db chain answer to get the result[1]
        # better - self.prompt_template = "Condense {Question}'s essence into a single sentence encapsulating {Answer}."
        self.prompt_template = "Summarize the {Question} in brief and share the detailed {Answer}."
        self.prompt = PromptTemplate(input_variables=["query", "self.generated_sql_result"], template=self.prompt_template)
        self.chain = LLMChain(llm=OpenAI(), prompt= self.prompt)
        print("DB_chain successfull")

    def run_queries(self,query):
        #self.query1 = query + " " + "Reply like you are interacting with a human in a json format."
        self.query1 = query + " Do not change the condition asked by the user." + "Reply like you are interacting with a human in a json format."
        self.response = self.db_chain(self.query1)
        self.answer=self.response["result"]
        #self.response1 = self.db_chain1(query)
        #self.answer1 = self.response1["result"]
        #return [self.answer, self.answer1]
        self.conn = sqlite3.connect(r'C:\Users\anark\Desktop\Capstone\SQLChatBot\backend\GeoQuery.db')
        self.cursor = self.conn.cursor()
        self.generated_sql_output = self.cursor.execute(self.answer)
        self.generated_sql_result = self.generated_sql_output.fetchall()
        #print("Here")
        #print(self.generated_sql_result)
        if len(self.generated_sql_result) == 0:
            self.generated_sql_result = "Error 404: Not found"
            self.answer1 = "The database does not contain any records matching your question."
        else:
            #self.answer1 = self.chain({'Question': query, 'Answer': self.generated_sql_result})
            self.answer1 = self.chain({'Question': self.answer, 'Answer': self.generated_sql_result})
            self.answer1 = self.answer1['text'].replace('\n', '')
        return [self.answer, self.answer1, self.generated_sql_result]


        
        