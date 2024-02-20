from datetime import datetime

data_str = '2022-04-20 07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(data_str,data_str_fmt)
#data = datetime(2022,4,20,13,45,23)
print(data)