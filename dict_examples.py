
airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports, '\n')

for code in 'EWR', 'ORF', 'YOW', 'IAD', 'PHX':
    print(airports.get(code, 'NOPE'))
print()

for code in 'EWR', 'ORF', 'YOW', 'IAD', 'PHX':
    print(airports.setdefault(code, 'NOPE'))

print(airports)
