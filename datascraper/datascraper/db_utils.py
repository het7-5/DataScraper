import os 
import mysql.connector


def create_db_conncection():
    try:
        k= os.getenv("DATABASE")
        connection = mysql.connector.connect(
            host="localhost",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DATABASE"),
        )

        return connection
    except Exception as err:
        print("Error while connecting to MySQL", err)
        return None

def readurls_from_db():
    connection = create_db_conncection()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute("SELECT url FROM crawl_urls")
    urls = cursor.fetchall()
    connection.close()

    return [url[0] for url in urls]