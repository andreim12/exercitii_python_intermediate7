import pickle
import csv

'''
modulul de pickle -> accepta orice obiect ( dict, lista, tuplu ... ) si il transforma in stream de bytes.

pickle.dump(object, file) -> converteste obiectul in stream de bytes, salvandu-l in file
pickle.load(file) -> deschide fisierul si converteste din stream de bytes inapoi in obiectul original

write_bytes -> wb
read_bytes -> rb
'''

# data = {
#     "a": [1, 2, 3, 4],
#     "b": ('string1', 'string2'),
#     "c": [False, True, True]
# }
#
# with open("data.pickle", "wb") as file:
#     pickle.dump(data, file)

with open("data.pickle", "rb")as file:
    data = pickle.load(file)
print(data)

with open("exemplu.csv") as file:
    continut = csv.reader(file)
    for rand in continut:
        print(rand)

with open("orice.csv", "a") as out_file:
    orice = csv.writer(out_file)
    orice.writerow(["nume", "varsta"])
    orice.writerow(["bogdan", "15"])