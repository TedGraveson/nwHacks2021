
import json
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


orders = {
        "id" : 123,
        "items" : ["bread", "eggs", "milk", "batteries", "toaster"],
        "tip": 10,
        "address" : "8989 documentation lane"
    }


jsonUsers = json.dumps(users)
jsonOrders = json.dumps(orders)

testUsers = json.loads(jsonUsers)

for user in testUsers:
    print(user)

