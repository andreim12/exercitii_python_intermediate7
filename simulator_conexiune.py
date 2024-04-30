import time
class NetworkError(Exception):
    pass

class AuthenticationError(Exception):
    pass

class SQLError(Exception):
    pass

class MaxRetriesExceededError(Exception):
    pass

config_ex = {
    'Ethernet_cable': 'Disconnected',
    'is_authentication': False,
    'adresa_sql': 'localhost',
}

def simulare_conexiune(config):
    required_keys = ['Ethernet_cable', 'is_authentication', 'adresa_sql']
    for key in required_keys:
        if key not in config:
            raise NetworkError(f'Connection is unstable: {key}')
        if key not in config:
            raise AuthenticationError(f'User or password is not correct: {key}')
        if key not in config:
            raise SQLError(f'SQL Error: {key}')
    print('Connection is established! Welcome!')


def conectare_baza_de_date(max_retries=10):

    for incercare in range(1, max_retries + 1):
        try:
            print(f"Incercarea {incercare}: Conectare la baza de date...")
            simulare_conexiune(config_ex)
            break
        except (NetworkError, AuthenticationError, SQLError) as e:
            print(f"Incercarea cu nr {incercare} a esuat cu eroarea {e}.")
            time.sleep(1)
        if(incercare == max_retries):
            raise MaxRetriesExceededError("Prea multe incercari!")


try:
    conectare_baza_de_date()
except MaxRetriesExceededError as e:
    print(e)


# sanitizarea input-ului : verificam ca ceea ce primim de la user (input) este valid si putem lucra cu el.
