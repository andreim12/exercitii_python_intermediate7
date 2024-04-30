# Se cere un script python care traverseaza un director, listeaza toate fisierele de tip text!
# Printand numele fisierului si prima linie cu continutul acesteia
import linecache
import os

def traverse_directory(path):  # NE PLIMBA PRIN TOT PATH-UL
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                print(f'{file}')
                with open(os.path.join(root, file), 'r') as f:
                    print(f'Prima linie este: {f.readline()}')

traverse_directory("/Users/andreimusceleanu12/python class/pythonIntermediate")


def traverse_directory_non_recursive(path):  # AICI DOAR INTR-UN FISIER ANUME ( NON-RECURSIV )
    with os.scandir(path) as entries:
        for entry in entries:
            if(entry.is_file() and entry.name.endswith('.txt')):
                print(f'Fisierul: {entry.name}')

traverse_directory_non_recursive("/Users/andreimusceleanu12/python class/pythonIntermediate")



# def read_multiple_lines(path):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith(".txt"):
#                 print(f'{file}')
#                 with open(os.path.join(root, file), 'r') as f:
#                     while True:
#                         line = f.readline()
#                         if not line:
#                             break
#                         print(line.strip())
#
# read_multiple_lines("/Users/andreimusceleanu12/python class/pythonIntermediate")


def read_multiple_lines(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                print(f'{file}')
                with open(os.path.join(root, file), 'r') as f:
                    # for _ in range(2):
                    #     print(f.readline().strip())
                    linia_2 = linecache.getline(f.name, 2).strip()
                    print(linia_2)
                    # lines = f.readlines()
                    # for line in lines:
                    #     print(line.strip())

read_multiple_lines("/Users/andreimusceleanu12/python class/pythonIntermediate")



# Dat fiind un fisier, de orice tip, care contine mai multe linii
# Se cere crearea unei clase ce introduce fiecare linie intr-o structura de date aleasa de voi
# lista sau dictionar
# Astfel incat atunci cand vrem sa accesam o linie, sa o putem face dupa index/cheie
# Tratati posibilele exceptii
