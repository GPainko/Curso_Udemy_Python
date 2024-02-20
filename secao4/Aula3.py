from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta


fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30',fmt)
data_fim = datetime.strptime('12/12/2024 08:20:20',fmt)
delta = timedelta(days=10,hours=2)
print(data_fim - delta)
print(data_fim + relativedelta(seconds=28,minutes=5))
# print(delta.days)
# print(delta.total_seconds())
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)