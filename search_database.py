
import sqlalchemy as db 
import youtube_api_search as c


def create_database(limit, duration, key):
    
    dataframe = c.convert_data_to_dataframe(3, 'short', "hello")
    engine = db.create_engine('sqlite:///youtube_search_results.db')
    dataframe.to_sql('table_name', con=engine, if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM table_name;").fetchall()
    return query_result

if __name__ == "__main__":
    limit = int(input("Enter your search limit: "))
    duration = input("Enter long or short: ")
    key = input("Enter the search term: ")
    print(create_database(limit, duration, key))
     
