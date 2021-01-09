
import json
users = {   "user1" : {
                "firstName" : "Ted",
                "lastName" : "GStone",
                "driver" : True,
                "timeStart": {"09/01/21": "09:00"},
                "phoneNumber" : 1234567890,
                "orderID" : None
            },
            "user2" :  {
                "firstName" : "Brenda",
                "lastName" : "Woo",
                "driver" : False,
                "timeStart": {"09/01/21": "11:00"},
                "phoneNumber" : 1234567890,
                "orderID" : 123
            },

            "user3" : {
                "firstName" : "Sally",
                "lastName" : "May",
                "driver" : True,
                "timeStart": {"09/01/21": "09:00"},
                "phoneNumber" : 1234567890,
                "orderID" : None
            }
        }


orders = {
    "order1": {
        "id" : 123,
        "items" : ["bread", "eggs", "milk", "batteries", "toaster"],
        "tip": 10,
        "address" : "8989 documentation lane"
    }
}


jsonUsers = json.dumps(users)
jsonOrders = json.dumps(orders)

testUsers = json.loads(jsonUsers)
print(testUsers["user2"]["driver"])

