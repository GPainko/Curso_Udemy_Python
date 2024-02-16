from typing import Any


class CallMe:
    def __init__(self,phone):
        self.phone = phone

    def __call__(self, *args, **kwds):
        print('Chamando',self.phone)


call1 = CallMe('234567890')
call1(1,2,3)