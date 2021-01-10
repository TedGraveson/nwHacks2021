import sqlite3

#line 5-26 is the cmd to create the databases, errors will occur 
# if ran more than once, but must be ran once to create the DB
# connect = sqlite3.connect("User_order.db")
# c = connect.cursor()
# c.execute("""CREATE TABLE user(
#                 first TEXT,
#                 last TEXT,
#                 driver INTEGER
#                 )""")

# c.execute("""CREATE TABLE ore(
#                 first TEXT,
#                 last TEXT,
#                 id INTEGER,
#                 item TEXT,
#                 time_start TEXT,
#                 time_end TEXT,
#                 address TEXT,
#                 tip INTEGER)
#         """)

# connect.commit()

# connect.close()

users = [{
                "firstName" : "Ted",
                "lastName" : "GStone",
                "driver" : True,
                "timeStart": {"09/01/21": "09:00"},
                "phoneNumber" : 1234567890,
                "orderID" : None
            },
            {
                "firstName" : "Brenda",
                "lastName" : "Woo",
                "driver" : False,
                "timeStart": {"09/01/21": "11:00"},
                "phoneNumber" : 1234567890,
                "orderID" : 123
            },

            {
                "firstName" : "Sally",
                "lastName" : "May",
                "driver" : True,
                "timeStart": {"09/01/21": "09:00"},
                "phoneNumber" : 1234567890,
                "orderID" : None
            }
        ]


def insert_user(user):
    conn = sqlite3.connect("User_order.db")
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO user VALUES(:first, :last, :driver)", 
        {'first':user["firstName"], 'last':user["lastName"],'driver':user["driver"]})
        c.execute("INSERT INTO ore VALUES(:first, :last, :id, :item, :time_start, :time_end,:address, :tip)",
        {'first':user["firstName"], 'last':user["lastName"],'id':1,'item':"", 'time_start': "", 'time_end':"", 'address':"",'tip':0})



# insert_user(users[1])
# insert_user(users[2])
# insert_user(users[0])