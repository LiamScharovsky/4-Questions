places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']
newPlaces = [locations for locations in places if locations.strip()]

print(newPlaces)
