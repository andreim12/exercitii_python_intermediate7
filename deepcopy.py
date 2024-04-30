# Deep Copy vs Shallow Copy ( Copiere Adanca VS Copiere Superficiala )


# Shallow Copy -> retine referintele la elementele originale ( dar nu si pe cele adaugate dupa )
# Deep Copy -> copiaza recursiv toate elementele originale, dar fara referinte ( pastreaza o copie a obiectului original, un back-up)

import copy

class Ceva:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):  # dunder method pentru REPRESENTATION IN TERMINAL.
        return f'{self.a!r}, {self.b!r}'  # !r este specific doar pentru __repr__

