
import pandas as pd
from backend import Gpt
from frontend import App

def get_query(query):
    print(query)
    query = query + " " + "Reply like you are interacting with a human"
    try:
        mygpt = Gpt()
        request = mygpt.run_queries(query)
        print(request[0], "\n", request[1])
        ui.query_out(request[0])
        ui.result_out(request[1])
    except:
        ui.query_out("An error has occured.")
        ui.result_out("Please contact the development team for assistance.")
ui = App(get_query)
ui.app.mainloop()