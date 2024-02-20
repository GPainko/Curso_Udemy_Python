from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('America/Sao_Paulo'))
data2 = datetime.now(timezone('Asia/Tokyo'))
data3 = datetime(2022,4,20,7,49,23, tzinfo=timezone('Asia/Tokyo'))
data4 = data.now()

print(data)
print(data2)
print(data3)
print(data4.timestamp())
print(datetime.fromtimestamp(1708448749.742608))