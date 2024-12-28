import sqlite3 as sq3
import pandas.io.sql as pd

path = './exp-9_read_sql_data/classic_rock.db'
conn = sq3.Connection(path)

query = '''
SELECT *
FROM rock_songs where PlayCount>100 ;
'''

observations = pd.read_sql(query, conn)
print(observations.head(50))