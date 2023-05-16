locations = {'North America': {'USA': ['Mountain View']}}
# NA = sorted(locations['North America']['USA'])
# print(NA[0])
# print(NA[1])
# AsianCountries = locations['Asia']
# SortedByCity = sorted(AsianCountries.items(), key=lambda x:x[1])
# print(SortedByCity[0][1][0]," - ",SortedByCity[0][0])
# print(SortedByCity[1][1][0]," - ",SortedByCity[1][0])
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India':['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt':['Cairo']}
# print(locations)
usa_cities = locations['North America']['USA']
for cities in sorted(usa_cities):
    print(cities)
asianCities = []
for countries, cities in locations['Asia'].items():
    city_country = cities[0] + ' - ' + countries
    asianCities.append(city_country)

for sac in sorted(asianCities):
    print(sac)
    print('\n')

# To find key from value in a dictionary
# my_dict ={"Java":100, "Python":112, "C":11}
# # one-liner
# print("One line Code Key value: ", list(my_dict.keys())[list(my_dict.values()).index(100)])