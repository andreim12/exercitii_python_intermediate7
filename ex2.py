### OOP - object oriented programming : Python (totul este un obiect)
### functionale: Lisp, Haskell > aproape toate operatiile sunt functii
### high-level, strongly typed : C, C++ ( a = 5 -> int a = 5; )

# OOP - mostenirea
class Persoana:  # clasa de baza
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"{self.nume} are varsta {self.varsta} ani"


class Angajat(Persoana):  # clasa mostenita ( clasa copil ) -> mosteneste init si str
    def __init__(self, nume, varsta, salariu, ore_lucrate):
        Persoana.__init__(self, nume, varsta)  # super() -> adica superclass : clasa din care mostenim
        self.salariu = salariu
        self.ore_lucrate = ore_lucrate

    def arata_finante(self):
        return self.salariu * self.ore_lucrate


class Student(Persoana):  # clasa copil > mosteneste init si str
    def __init__(self, nume, varsta, bursa):
        Persoana.__init__(self, nume, varsta)
        self.bursa = bursa

    def arata_finante(self):
        return self.bursa

    @classmethod
    def create_from_string(cls, sablon: str):   # cls este instanta clasei curente
        # Student.create_from_string("Ana 15 700")
        nume, varsta, bursa = sablon.split()
        varsta, bursa = int(varsta), int(bursa)  # type casting
        if cls.is_name_correct(nume):
            return cls(nume, varsta, bursa)  # echivalent cu a zice asta :  __init__(self, nume, varsta, bursa)

    @staticmethod
    def is_name_correct(nume):
        if nume[0].isupper() and len(nume) > 2:
            return True
        return False

class StudentMuncitor(Angajat, Student):  # Conteaza ordinea mostenirii ! Primul mostenit este Student, apoi Angajat
    def __init__(self, nume, varsta, bursa, salariu, ore_lucrate):
        Student.__init__(self, nume, varsta, bursa)                     # Student.__ -> Instantiere anonima
        Angajat.__init__(self, nume, varsta, salariu, ore_lucrate)

    def arata_finante(self):
        return self.ore_lucrate * self.salariu + self.bursa

    def __str__(self):
        return f"{self.nume} a lucrat {self.ore_lucrate} ore si a castigat {self.salariu} RON"


o1 = Persoana("George", 25)
o2 = Angajat("Andrei", 26, 1000, 40)
o3 = Student("Ion", 15, 800)
o4 = StudentMuncitor("Geo", 30, 800, 1200, 20)
print(o1)
print(o2)
print(o3)
print(o4)

o5 = Student.create_from_string("Razvan 30 1000")
print(o5)


# dunder methods : __dunder__

# __init__ self e null; __str__: null; __add__

# Persoana.__init__(self, nume, varsta) VS super().__init__(nume,varsta)
# super() -> Persoana -> self -> stie automat
# Persoana.__init__(self, nume, varsta) -> trebuie specificat

# DECORATOR "@"
# @classmethod -> Este o functie, dar se apeleaza pentru intreaga instanta a clasei, poate modifica membrii sai (ai clasei), cls
# @staticmethod -> Este o functie, dar care e doar asociata clasei, nu este necesara instantierea unui obiect pentru a o folosi. NU MODIFICA MEMBRII CLASEI.

class Matematica:

    @staticmethod
    def integrare():
        pass

Matematica.integrare()





#####################
# DataClasses
#####################

from dataclasses import dataclass

@dataclass
class Cineva:
    nume : str
    prenume : str
    #dataclass va creeaza automat dunder methods : __str__, __init__, __add__
    def afisare_nume_complet(self):
        return f"Eu sunt {self.nume} {self.prenume}!"

c1 = Cineva("Ion", "Gheorghe")
print(c1.afisare_nume_complet())
c2 = Cineva("Ion", "Gheorghe")
print(c1 == c2)
