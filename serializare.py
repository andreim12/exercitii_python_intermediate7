# Serializare : presupune salvarea unui obiect de orice tip in memorie/baza de date
# A lua un obiect si a-l salva intr-un fisier/baza de date/... ( intr-o maniera structurata )
# Serializarea unei clase : presupune salvarea intr-un json/obiect structurat a intregii structuri a clasei cu tot ce contine
# Un dictionar si un json sunt fundamental aceleasi.

from contextlib import contextmanager
import json

data = {
    'name': 'Razvan',
    'age': 20
}
json_data = json.dumps(data)
print(json_data)

@contextmanager
def serializeaza_in_json(fisier, date):
    try:
        yield
    finally:
        with open(fisier, 'w') as f:
            json.dump(date, f)

with serializeaza_in_json('data.json', data):
    pass




class Exemplu:
    def __init__(self, atribut_clasa):
        self.atribut_clasa = atribut_clasa

    def to_dict(self):
        return {
            'atribut_clasa': self.atribut_clasa
        }

o = Exemplu('Ceva')

clasa_serializata = json.dumps(o.to_dict())
print(clasa_serializata)
