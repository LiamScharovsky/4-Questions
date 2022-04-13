#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
newPlaces = []
for place in map(lambda place : (place[0], place[1] *9/5 + 32), places):
    newPlaces.append(place)



print(newPlaces)
# HINT: KEEP IN MIND PEMDAS. USE THE CELCIUS - FAHRENHEIT CONVERSION
# F = C * 9/5 + 32