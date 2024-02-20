from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2024,2,20,14,27)
data = datetime.strptime('2024-02-20 13:27','%Y-%m-%d %H:%M')
print(data.strftime(fmt),data.year)
print(data.strftime(fmt),data.day)