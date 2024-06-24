import pymysql
import pandas as pd

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",  # Your password here if any
    database="mybook",
    charset="utf8"
)
sql = "SELECT * FROM book"
df = pd.read_sql(sql, con=conn)
print(df.head())
conn.close() 
