from abc import ABC, abstractmethod


# interfata Figura

# abstractmethod -> este un decorator specific unei clase abstracte
# definitia unei functii si declararea sa? (Intrebare de interviu)
# declaratia : semnatura functiei ( def add(a, b) )
# definitia : def add (a, b): return a + b
class Figura(ABC):
    @abstractmethod  # decoratorul : functie care "imbraca" alta functie. Functia care este "imbracata" extinde functionalitatile unei componente pe care
    def area(self):  # aplicam decoratorul
        pass
    @abstractmethod
    def draw(self):
        pass


class Cerc(Figura):
    def __init__(self, raza):
        self.raza = raza

    def area(self):
        return 3.14 * self.raza ** 2


class Patrat(Figura):
    def __init__(self, latura):
        self.latura = latura

    def area(self):
        return self.latura ** 2


class Dreptunghi(Figura):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def area(self):
        return self.lungime * self.latime


c1 = Cerc(5)
p1 = Patrat(4)
d1 = Dreptunghi(3, 5)

print(c1.area())
print(p1.area())
print(d1.area())

### Shape -> Cerc       -> area, draw
###       -> Patrat     -> area, draw
###       -> Dreptunghi -> area, draw

### abstractizam : luam trasaturi specifice si le extragem intr-o componenta; incapsularea logicii: functionalitatea si elementele de baza
### se aduna intr-o singura entitate; polymorphism : aceeasi interfata, dar mai multe forme