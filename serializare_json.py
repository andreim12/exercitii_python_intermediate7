'''
JSON : JavaScript Object Notation

API : Application Programming Interface -> expunere de metode, clase, variabile catre cineva.
endpoint: URL
comunicare/transfer informatii : JSON

Standardul REST
get
set
'''


import json


with open("fisier.json")as file:
    data = json.load(file)

print(data['incaltaminte'][0])