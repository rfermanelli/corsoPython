"""
Data la lista stutturata Corso con i campi
Nomin, Tel, Residenza, Datanascita, Luogonascita, Sesso,
visualizzare tutte le informazioni relative ai corsisti residenti a Roma e visualizzare quanti sono.
"""

corsisti = [{
        "Nomin": "Mario Rossi",
        "Tel": "1234567890",
        "Residenza": "Roma",
        "Datanascita": "1980-01-01",
        "Luogonascita": "Milano",
        "Sesso": "M"},{
        "Nomin": "Luigi Bianchi",
        "Tel": "0987654321",
        "Residenza": "Roma",
        "Datanascita": "1975-05-12",
        "Luogonascita": "Roma",
        "Sesso": "M"}, {
        "Nomin": "Anna Verdi",
        "Tel": "1122334455",
        "Residenza": "Roma",
        "Datanascita": "1988-09-23",
        "Luogonascita": "Genova",
        "Sesso": "F" },{
        "Nomin": "Carla Neri",
        "Tel": "6677889900",
        "Residenza": "Roma",
        "Datanascita": "1990-11-15",
        "Luogonascita": "Napoli",
        "Sesso": "F"},{
        "Nomin": "Giovanni Blu",
        "Tel": "4433221100",
        "Residenza": "Roma",
        "Datanascita": "1982-03-18",
        "Luogonascita": "Firenze",
        "Sesso": "M" }]
corsisti_residenti_roma=[]
for i in corsisti:
    if i["Residenza"]=="Roma":
        corsisti_residenti_roma.append(i)
print(corsisti_residenti_roma)


