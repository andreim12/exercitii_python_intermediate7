# Orice operatie pe fisier reprezinta un management de resure ( resursa este chiar fisierul )
# ORICE RESURSA TREBUIE INITIALIZATA SI ELIBERATA CAND ESTE FOLOSITA. ( Daca deschidem un fisier trebuie sa il si inchidem )

f = open("exemplu.txt", "w")
try:
    f.write("Ceva")
except IOError:
    print("Error occured")
finally:
    f.close()

# Context manager : with

with open("exemplu.txt", "w") as fisier:
    fisier.write("Altceva")

# Crearea propriului context manager ( with )
class FileManager:
    # def __init__, __enter__, __exit__
    def __init__(self, file_name, mod):
        self.file_name = file_name
        self.file = None
        self.mod = mod

    def __enter__(self):
        self.file = open(self.file_name, self.mod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):  # exc_type -> tipul de fisier, exc_value -> valoarea curenta, exc_tb -> traceback
        self.file.close()

with FileManager("exemplu1.txt", "w") as fisier2:
    fisier2.write("Example")

with FileManager("exemplu1.txt", "r") as fisier3:
    content = fisier3.read()
    print(content)