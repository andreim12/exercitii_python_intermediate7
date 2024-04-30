# Generators and Iterators

# a = [1, 2, 3, 4]
# for i in a:
#     print(i)
#
# b = "eu sunt andrei"
# for c in b:
#     print(c)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

from collections.abc import Iterable
class PrimeIterator(Iterable):
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()

iter = PrimeIterator(9)
for elem in iter:
    print(elem)



def prime_generator(n):
    number = 2
    generated_number = 0
    while generated_number != n:
        if is_prime(number):
            yield number  # yield salveaza in memorie, dar nu iese din functie.
            generated_number += 1
        number += 1

gen = prime_generator(100000)
for elem in gen:
    print(elem)
