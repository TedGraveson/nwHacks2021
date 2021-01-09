import requests

#please don't steal my key :(
#auth key for G.maps
api_key = "AIzaSyBsiUB5LFI3bYXjUjoIlkMQJXtIxu8PImE"

#start point for matrix
begin = "4266 Gilpin Crescent, Burnaby, BC V5G 2K2, Canada"

#end point for matrix
finish = "3711 Wakefield Court, Burnaby, BC"

#base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

#get request
r = requests.get(url + "origins=" + begin + "&destinations=" + finish + "&key=" + api_key) 

#time of travel between locations
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]   
cap = r.json()

timer = time.split()
fin = int(timer[0])
print("Time to teddy G's place " + time)

# print(fin)
# print(type(fin))
def distance(start, end):
    req = requests.get(url + "origins=" + start + "&destinations=" + end + "&key=" + api_key) 
    time = req.json()["rows"][0]["elements"][0]["duration"]["text"]
    piece = time.split()
    ans = int(piece[0])
    return ans

print(distance(begin, finish))
print(type(distance(begin, finish)))