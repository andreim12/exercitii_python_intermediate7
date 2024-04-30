import requests
import json

# se da API endpoint de la spaceX: "https://api.spacexdata.com/v4/launches"
# se cere: sa se faca get asupra acestui endpoint returnand datele obtinute (daca e cu succes)
# sa se creeze un iterator custom pentru aceste "lansari"


class SpaceXLaunchIterator:

    def __init__(self, launches):
        self.launches = launches
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.launches):
            launch = self.launches[self.index]
            self.index += 1
            return launch
        else:
            raise StopIteration


def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch launches: {response.status_code}')
        return None

def display_launch_data():
    launches = fetch_spacex_launches()
    if launches:
        launch_iterator = SpaceXLaunchIterator(launches)
        for launch in launch_iterator:
            print(f"Flight Number: {launch['flight_number']}")
            print(f"Mission Name: {launch['name']}")
            print(f"Rocket Type: {launch['rocket']}")
            print(f"Launch Date: {launch['date_utc']}")
            print("-" * 20)

def main():
    display_launch_data()

if __name__ == "__main__":
    main()