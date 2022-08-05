import sqlalchemy as db 
import youtube_api_search as c


def create_database(limit, duration, key, order):
    
    dataframe = c.convert_data_to_dataframe(limit, duration, key, order)
    engine = db.create_engine('sqlite:///youtube_search_results.db')
    dataframe.to_sql('table_name', con=engine, if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM table_name;").fetchall()
    return query_result


