import os
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import sqlite3
class Gpt:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = ''
        self.db_path = "backend\GeoQuery.db"
        self.db = SQLDatabase.from_uri(f"sqlite:///{self.db_path}")
        self.llm = OpenAI(temperature = 0)
        self.db_chain = SQLDatabaseChain.from_llm(self.llm, self.db, return_sql = True, top_k = 0)
        self.prompt_template = "Summarize the {Question} in brief and share the detailed {Answer}."
        self.prompt_template = "Summarize the {Question} and {Answer}."
        self.prompt = PromptTemplate(input_variables=["query", "self.generated_sql_result"], template=self.prompt_template)
        self.chain = LLMChain(llm=OpenAI(), prompt= self.prompt)
        print("DB_chain successfull")

    def run_queries(self,query):
        self.query1 = query + " Do not change the condition asked by the user." + "Reply like you are interacting with a human in a json format."
        self.response = self.db_chain(self.query1)
        self.answer=self.response["result"]
        self.conn = sqlite3.connect(r'backend\GeoQuery.db')
        self.cursor = self.conn.cursor()
        self.generated_sql_output = self.cursor.execute(self.answer)
        self.generated_sql_result = self.generated_sql_output.fetchall()
        if len(self.generated_sql_result) == 0:
            self.generated_sql_result = "Error 404: Not found"
            self.answer1 = "The database does not contain any records matching your question."
        else:
            self.answer1 = self.chain({'Question': self.answer, 'Answer': self.generated_sql_result})
            self.answer1 = self.answer1['text'].replace('\n', '')
        return [self.answer, self.answer1, self.generated_sql_result]


        
        