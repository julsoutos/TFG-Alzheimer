import datetime

print(datetime.timedelta(days=7))

print(datetime.datetime.today() - datetime.timedelta(days=30))

stats = []

for i in range(1,8):
    days = datetime.timedelta(days=i)
    print(datetime.datetime.today() - days)