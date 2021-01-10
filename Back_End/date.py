import datetime

date_time_str = '2018-06-29 08:15'

date_time_str1 = '2020-06-29 08:15'

date_time_obj1 = datetime.datetime.strptime(date_time_str1, '%Y-%m-%d %H:%M')

date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

#x = datetime.datetime(2018, 6, 1,5)
# print(date_time_obj)
# print(type(date_time_obj))


def date_to_string(date):
    ans = date.strftime('%Y-%m-%d %H:%M')
    return ans


def string_to_date(string):
    ans = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M')
    return ans

# x= string_to_date(date_time_str)
# print(x)
# print(type(x))

# y= date_to_string(x)

# print(y)
# print(type(y))

# z = string_to_date(y)
# print(z)
# print(type(z))