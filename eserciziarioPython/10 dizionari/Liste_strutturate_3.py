"""
Caricare una lista con 5 date casuali.
Dopo il riempimento della lista,
visualizzare quanti mesi di dicembre si trovano eventualmente presenti nella lista.
"""

import random
from datetime import timedelta, datetime
def generate_random_dates(start_date, end_date, k):
    random_dates = []
    date_range = end_date - start_date
    for _ in range(k):
        random_days = random.randint(0, date_range.days)
        random_date = start_date + timedelta(days=random_days)
        random_dates.append(random_date)
    return random_dates

start_date = datetime(1900, 5, 25)
end_date = datetime(2024, 5, 31)
random_dates = generate_random_dates(start_date, end_date, 5)

#print("The random dates generated are:")
date_list = []
for index, date in enumerate(random_dates):
    date_list.append((index, date.strftime('%Y-%m-%d')))
print(date_list)
    #print(f"{index+1}. {date.strftime('%Y-%m-%d')}")