#Create a Mapping of state to Abbreviation
states = {
    'TamilNadu': 'TN',
    'Karnataka': 'KA',
    'Kerala': 'KL',
    'Andhrapradesh': 'AP',
    'Westbengal': 'WB'
}


# Create a Basic set of states and cities in them

cities = {
    'TN': 'Salem',
    'KA': 'Bangalore',
    'KL': 'Thiruvanathapuram'
}

# add some more cities

cities['AP'] = 'Hyderabad'
cities['WB'] = 'Kolkata'

# Print out some cities

print('-' * 10)

print("TN state has: ", cities['TN'])
print("KA state has: ", cities['KA'])


# print some states

print('-' * 10)
print("Tamilnadu's abbreviation is: ", states['TamilNadu'])
print("Karnataka's abbreviation is: ", states['Karnataka'])


# Do it by using the state then cities dict

print('-' * 10)
print("Tamil Nadu has: ", cities[states['TamilNadu']])
print("Karnataka has: ", cities[states['Karnataka']])


# Print Every State Abbreviation

print('-' * 10)
for state, abbrev in list(cities.items()):
    print(f"{state} is abbreviated {abbrev}")

# Print Every City in State

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")


# Now do Both at the Same time 

print ('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print('-' * 10)
# Safely get a abbreviation by state that might not be there
state = states.get('Kashmir')

if not state:
    print("Sorry, no Kashmir.")

# Get a city with a Default value

city = cities.get('JK', 'Does Not Exist')
print(f"The city for the state 'JK' is: {city}")




      
