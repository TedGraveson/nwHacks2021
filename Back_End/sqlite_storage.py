import sqlite3
import datetime
import sys
sys.path.append("Back_end/")
import mapping
# line 5-26 is the cmd to create the databases, errors will occur 
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
#                 orderID INTEGER,
#                 items TEXT,
#                 time_start TEXT,
#                 timeEnd TEXT,
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

orders = [
        {
            "orderID" : 123,
            "items" : ["bread", "eggs", "milk", "batteries", "toaster"],
            "tip": 10,
            "address" : "8989 documentation lane",
            "timeEnd" : "9:00"

        },
        {   "orderID" : 456,
            "items" : ["eggs", "milk", "batteries"],
            "tip": 1000,
            "address" : "8989 documentation lane",
            "timeEnd" : "9:00"
        }
]

def format_order(list_post):
    order = {}
    order['orderID'] = 123
    order['items'] = list_post['items']
    order['tip'] = list_post['tip']
    order['address'] = list_post['address']
    order['time_start'] = "lmao"
    order['timeEnd'] = date_fix(list_post['date'])
    return order

def insert_user(user):
    conn = sqlite3.connect("User_order.db")
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO user VALUES(:first, :last, :driver)", 
        {'first':user["firstName"], 'last':user["lastName"],'driver':user["driver"]})
        c.execute("INSERT INTO ore VALUES(:first, :last, :orderID, :items, :time_start, :timeEnd,:address, :tip)",
        {'first':user["firstName"], 'last':user["lastName"],'orderID':1,'items':"", 'time_start': "", 'timeEnd':"", 'address':"",'tip':0})

def date_fix(date):
    string = date.split('T')
    ans = string[0] + " " + string[1]
    return ans

def list_to_string(lis):
    string = ""
    for obj in lis:
        string += (obj + " ")
    return string

def update_order(order, first, last):
    x = datetime.datetime.now()
    lis = list_to_string(order["items"])
    conn = sqlite3.connect("User_order.db")
    c=conn.cursor()
    with conn:
        c.execute("""UPDATE ore SET 'orderID'= :orderID, items = :items, time_start = :time_start,
        timeEnd = :timeEnd, address = :address, tip = :tip WHERE first = :first AND last = :last""",
        {'first':first, 'last':last, 'items':lis, 'time_start':x.strftime("%Y-%m-%d %H:%M"), 
        'timeEnd':order["timeEnd"], 'address':order["address"], 'tip':order["tip"], 'orderID':order["orderID"]})

def query_user_and_order():
    conn = sqlite3.connect("User_order.db")
    c=conn.cursor()
    with conn:
        c.execute("SELECT * FROM user")
        res_user = c.fetchall()
        c.execute("SELECT * FROM ore")
        res_order = c.fetchall()

    return res_user, res_order

def query_driver(first, last):
    conn = sqlite3.connect("User_order.db")
    c=conn.cursor()
    with conn:
        c.execute("SELECT * FROM user WHERE first = :first AND last = :last", {'first':first, 'last': last})
        tup = c.fetchone()
    return tup[2]

def query_names(address):
    conn = sqlite3.connect("User_order.db")
    c=conn.cursor()
    with conn:
        c.execute("SELECT * FROM ore WHERE address = :address", {'address':address})
        tup = c.fetchone()
        first = tup[0]
        last = tup[1]
    return first, last

def take_first(lis):
    return lis[0]

def distance_compare(address, fName, lName, res_user, res_order):
    valid = []
    for i in range(len(res_order)):
        if((fName != res_order[i][0]) and (lName != res_order[i][1])):
            timeE = res_order[i][5]
            tip = res_order[i][7]
            dist = mapping.distance(address, res_order[i][6])
            fir = res_order[i][0]
            las = res_order[i][1]
            res = [dist, fir, las, timeE, tip]
            valid.append(res)

    valid.sort(key=take_first)

    return valid

#okay i kinda got lazy but like for the unique id think I still think the global counter
#could work despite python being a pain to deal with with the global vars. Hopefully this
#work will be semi useful (???)
# test = list_to_string(orders[0]["items"])
# print(test)
# print(type(test))
# insert_user(users[1])
# insert_user(users[2])                                          
# insert_user(users[0])

# update_order(orders[0],'Ted', 'GStone')
# update_order(orders[1],'Brenda', 'Woo')
# che_use, che_ore = query_user_and_order()
# print(che_use)
# print(che_ore)
# print(len(che_ore))