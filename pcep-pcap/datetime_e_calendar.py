from datetime import date
from datetime import datetime
import time

data = date(2023, 7, 16)
data_iso = date.fromisoformat('2023-07-16')
print('Giorno della settimana (0..6): ' + str(data.weekday()))
print('Giorno della settimana in formato ISO (1..7): ' + str(data.isoweekday()))

print('Data attuale: '+ str(data.today()))
print('Data impostata: ' + str(data))
print('Data in formato ISO: ' + str(data_iso))

t_ts = time.time()
print('Timestamp attuale dell\'epoca Unix: ' + str(t_ts))
t_a = date.fromtimestamp(t_ts)
print('Data risultato della conversione di un Timestamp: ' + str(t_a))

dt = datetime(2023, 7, 16, 20, 30, 0)
print(dt)

from datetime import time

t = time(14, 53)
print(t.strftime("%H:%M:%S"))
#
import calendar

print(calendar.SUNDAY)
print(calendar.calendar(2024, 2, 1, 4, 3))
print(calendar.prcal(2024))
print(calendar.month(2023, 7))

cal = calendar.HTMLCalendar()
print(cal.cssclass_month)

calendar.prcal(1967)
calendar.prmonth(1967, 5)

calendar.setfirstweekday(4)
calendar.prmonth(1967, 5)

calendar.setfirstweekday(0)
calendar.prmonth(1967, 5)

if calendar.isleap(2019):
    print('2019, a leap year')

#
"""import os
os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('thumbnails')
os.chdir('thumbnails')
os.mkdir('tmp')
os.chdir('../')

print(os.getcwd())
"""
#

from datetime import datetime
d = datetime(2019, 11, 27, 11, 27, 22)
print(d.strftime('%y/%B/%d %H:$M:%S'))
#

from datetime import date
d_1 = date(1992, 1, 16)
d_2 = date(1991, 2, 5)
print(d_1 - d_2)
#

import random

random.seed()
print(random.random())

# La funzione choice() e il lancio dei dadi
s_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d = random.choice(s_l)
print(d)

# La funzione sample() è le disposizioni semplici di classe k di un iterabile
s_s = random.sample(s_l, 5)
print(s_s)
#

import platform

print(platform.platform(aliased=True, terse=True))
print(platform.platform())
print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.version())
print(platform.python_implementation())
print(platform.python_version_tuple())
#

import random
random.seed(0)
x = random.choice([0, 1])
print(x)
random.seed(0)
y = random.choice([0, 1])
print(y)
print(x - y)
#

try:
    1/0
except ZeroDivisionError as zero_division:
    print(zero_division.__str__())

