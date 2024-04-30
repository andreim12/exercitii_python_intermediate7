# Se da un dictionar care contine configuratia unei aplicatii web
# dictionarul are urmatoarele chei: 'host', 'port', 'debug'
# cream o functie care valideaza configuratia : trebuie sa contina cheile date si valori valide
# daca nu contine valori valide, se vor arunca exceptii


# def valideaza_config(config):
#     try:
#         if not all(key in config for key in ('host', 'port', 'debug')):
#             raise ValueError('Missing required configuration keys.')
#         if not isinstance(config['host'], str):
#             raise TypeError("'host' should be a string!")
#         if not isinstance(config['port'], int):
#             raise TypeError("'port' should be a integer!")
#         if not isinstance(config['debug'], bool):
#             raise TypeError("'debug' should be a boolean!")
#         print("Configuratia este valida.")
#     except (ValueError, TypeError) as e:
#         print(f'Invalid config: {e}')

class ConfigurationError(Exception):

    def __init__(self, message):
        super().__init__(message)

def valideaza_config(config):
    required_keys = ['host', 'port', 'debug']
    for key in required_keys:
        if key not in config:
            raise ConfigurationError(f'Missing required key: {key}')
        if key not in config:
            raise ConfigurationError(f'Missing required key" {key}')
        if key not in config:
            raise ConfigurationError(f'Missing required key: {key}')
    print('Configuratia este valida.')

config_ex = {
    'host': 'localhost',
    'port': 8080,
    'debug': True
}
try:
    valideaza_config(config_ex)
except ConfigurationError as e:
    print(e)


# TEMA

# ADAUGATI VERIFICARI DE TIP

# Titlu: Simulator simplu de testare a conexiunii la o baza de date
# Creati exceptii customizate pentru urmatoarele scenarii:
# 1. NetworkError
# 2. AuthenticationError
# 3. SQLError
# 4. MaxRetriesExceededError
# Conditiile de "ridicare" a erorilor este la latitudinea voastra: fie sa aiba o logica, fie sa contina date random
# Implementati un mecanism de retry cu maxim 10 incercari
# Fiecare incercare de conectare este logata (printata) si se arunca eroarea
# Daca totusi conexiunea are loc cu succes, afisati un mesaj de bun venit!
# 2 functii : def simulare_conexiune() si def conectare_baza_de_date(max_retries=10);