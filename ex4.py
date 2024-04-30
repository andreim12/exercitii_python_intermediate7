# Sa se creeze o clasa abstracta numita "Vehicul" , cu metodele abstracte viteza_maxima si tip_vehicul.
# Luati 2 subclase, care sa mosteneasca din Vehicul ( Masina, Autobuz ). Adaugati o variabila membra in clasa vehicul,
# care va tine cont de toate instantele claselor mostenite.

# KISS - keep it simple stupid ( idiot proof )

from abc import ABC, abstractmethod

class Vehicul(ABC):

    vehicule = []

    def __init__(self):
        Vehicul.vehicule.append(self)

    @abstractmethod
    def viteza_maxima(self):
        pass

    @abstractmethod
    def tip_vehicul(self):
        pass

class Masina(Vehicul):

    def viteza_maxima(self):
        return 180

    def tip_vehicul(self):
        return "Dacia"

class Autobuz(Vehicul):

    def viteza_maxima(self):
        return 80

    def tip_vehicul(self):
        return "Mercedes"

m1 = Masina()
a1 = Autobuz()

print(m1.viteza_maxima())
print(a1.tip_vehicul())
print(Vehicul.vehicule)

