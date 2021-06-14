import datetime

# print(datetime.timedelta(days=7))

# print(datetime.datetime.today() - datetime.timedelta(days=30))

# stats = []

# for i in range(1,8):
#     days = datetime.timedelta(days=i)
#     print(datetime.datetime.today() - days)

today = datetime.date.today()
day = datetime.timedelta(days=1)
date = datetime.datetime.strftime(today + day, '%Y-%m-%d')
print(date)