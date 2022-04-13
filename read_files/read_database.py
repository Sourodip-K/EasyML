import pandas as pd
import sqlite3

def read(path):
    # open engine connection
    con = sqlite3.connect(path)
    # create a cursor object
    cur = con.cursor()
    # Perform query: rs
    rs = cur.execute('select * from TEST')
    # Save results of the query to DataFrame: df
    df = pd.DataFrame(rs.fetchall())
    # Close connection
    con.commit()
    # Print head of DataFrame df
    return df