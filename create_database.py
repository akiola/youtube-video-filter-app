import sqlalchemy as db 
import youtube_api_search as c
import pandas as pd 

def create_database(limit, duration, key, order):

    dataframe = c.convert_data_to_dataframe(limit, duration, key, order)
    engine = db.create_engine('sqlite:///youtube_search_results.db')
    dataframe.to_sql('video_database', con=engine, if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM video_database;").fetchall()
    return query_result



