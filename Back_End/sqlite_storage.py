import sqlite3

connect = sqlite3.connect("User_order.db")

c = connect.cursor()

c.execute("""CREATE TABLE user(
                first TEXT,
                last TEXT,
                driver INTEGER)


    """)

c.execute("INSERT INTO user VALUES('Ted','Graveson',1)")

c.execute("INSERT INTO user VALUES('Brenden','Wu',0)")
connect.commit()

connect.close()

# def insert_emp(conn, user):
#     c=conn.cursor()
#     with conn:
#         c.