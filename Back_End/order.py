class Order:
    id = 0
    def __init__(self, dict):
        self.items = dict["items"]
        self.address = dict["address"]
        self.tip = dict["tip"] 
        self.note = dict["note"]
        self.id = id + 1

