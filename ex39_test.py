import hashmap

def divider():
    print '-' * 10

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Orgeon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan,' 'MI')
hashmap.set(states, 'Massachusetts', 'MA')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')
hashmap.set(cities, 'MA', 'Boston')

# print out some cities
divider()
print 
