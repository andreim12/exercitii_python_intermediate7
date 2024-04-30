# Decoratorul este o functie care imbraca o alta functie si ii extinde functionalitatea. Intotdeauna este precedat de @.
# O functie ia ca argument alta functie.
# Intr-o functie se poate crea alta functie: functii imbricate.

from datetime import datetime

def disable_at_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
    return wrapper

@disable_at_night
def ceva():
    print("Hhhhh")

ceva()


######### Built-In Decorator #########
from functools import lru_cache

@lru_cache(maxsize=100)  # lru - least recently used
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# cache miss, cache hit si locality (procesor)
#print(fibonacci(499))

@lru_cache(maxsize=50)
def print_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a)
        aux = a
        a = b
        b = aux + b

print_fibonacci(10)
'''
a,b = b, a+b  ==== aux = a, a=b, b= aux+b
a,b = b, a+b != a = b, b = a + b
'''
