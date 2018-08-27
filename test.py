import sqlite3
def connect():
    try:
        # if os.path.isfile('db.sqlite3'): os.remove('db.sqlite3')
        conn = sqlite3.connect('database/db1.sqlite3')
        return conn
    except sqlite3.Error as e:
        print(e)


    


conn = connect()
with conn:   
    first_col_numbers =  [5,5]
    second_col_numbers = [5,5]
    print('no_sql:',sum(first_col_numbers)+sum(second_col_numbers))
    cur = conn.cursor()
    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS newone(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        first_col TEXT,
        second_col TEXT,
        third_col TEXT)
    """)
    # for x,y in zip(first_col_numbers,second_col_numbers):
    #     cur.execute(f""" 
    #     INSERT INTO newone(first_col,second_col)
    #     VALUES(?,?)
    #     """,(x,y))
    data = cur.execute(f'SELECT SUM(first_col+second_col) FROM newone')
    my_sum = data.fetchall()
    print(my_sum)