class CustomException(Exception):

    def __init__(self):
        message = 'Divizorul nu poate fi 0!'
        Exception.__init__(self, message)


a = 4
b = [1, 0, 2]

for element in b:
    try:
        rezultat = a / element
    except ZeroDivisionError:
        # continue
        print('ATENTIE! Ai incerat sa imparti la 0!') # sau comanda continue
    print(rezultat)


for element in b:
    if element == 0:
        raise CustomException()
    rezultat = a / element
    print(rezultat)