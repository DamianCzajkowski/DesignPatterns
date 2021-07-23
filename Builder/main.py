from typing import List
from .director import Director

data = [
    ['Jan', 'Kowalski', 27, '111-222-333', 'Poland'],
    ['John', 'Smith', 33, '333-222-111', 'England'],
    ['Martin', 'Aub', 7, None, 'France']
]

data2 = [
    {'imię': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 27,
        'telefon': '111-222-333', 'kraj': 'Poland'},
    {'imię': 'John', 'nazwisko': 'Smith', 'wiek': 33,
        'telefon': '333-222-111', 'kraj': 'England'},
    {'imię': 'Martin', 'nazwisko': 'Aub', 'wiek': 7,
        'telefon': None, 'kraj': 'France'}
]

director = Director()
director.set_data(data2)
director.create_csv()
