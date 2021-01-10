import requests
from mapping import distance

#the code for formatting the date that will be passed from front. 
#You said the date will have to be passed in a specific way so this
#is a quick function to return a fixed verison of the string, we can
#copy paste this into the date.py file later i think
def date_fix(date):
    string = date.split('T')
    ans = string[0] + " " + string[1]
    return ans


#this code is gonna be messy like REALLY messy but this will eventually
#go into splite_storage and this solution was using my 3am brain lvl 
#so this might get really messy. I added one extra function down in sqlite_storage
#as well as some test code thats pre much just returning all of our dbs.
#the length comparing works by first checking whether we want a driver or a list
#user, then it begins taking the address passed and calling the length matrix
#on the target group, it'll then store all the times 

#the function i added directly to sqlite_storage (btw res_user and res_order will be tuples)
# def query_user_and_order():
#     conn = sqlite3.connect("User_order.db")
#     c=conn.cursor()
#     with conn:
#         c.execute("SELECT * FROM user")
#         res_user = c.fetchall()
#         c.execute("SELECT * FROM ore")
#         res_order = c.fetchall()

#     return res_user, res_order


def take_first(lis):
    return lis[0]

def distance_compare(address, fName, lName, res_user, res_order,is_driver ):
    valid = []
    for i in range(len(res_order)):
        if(is_driver != res_user[i][2]) and ((fName != res_order[i][0]) and (lName != res_order[i][1])):
            dist = distance(address, res_order[i][6])
            fir = res_order[i][0]
            las = res_order[i][1]
            res = [dist, fir, las]
            valid.append(res)
    
    valid.sort(key=take_first)
    #at this point there should be a list of of people that are of the opposite is_Driver bool
    #and do not have the exact same name as the person we are checking (this could imply) a repeat
    #order if the aforementioned statement were true. The final thing we do is sort the list based
    #on the distance, so now the first index will be the lowest distance away (by extension we can
    # later call the person since the list also stores the person's first and last name).
    # this means that index 0 in valid is the closest possible person to the address passed in.

    return valid 


#okay i kinda got lazy but like for the unique id think I still think the global counter
#could work despite python being a pain to deal with with the global vars. Hopefully this
#work will be semi useful (???)

