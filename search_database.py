import sqlalchemy as db 
import youtube_api_search as c
import pandas as pd 

dataframe = c.convert_data_to_dataframe(3, 'short', "hello")

engine = db.create_engine('sqlite:///youtube_search_results.db')

dataframe.to_sql('table_name', con=engine, if_exists='replace', index=False)

query_result = engine.execute("SELECT * FROM table_name;").fetchall()



print(pd.DataFrame(query_result))