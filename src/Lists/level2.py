#Popping elements :
cities  = ['tpt','skht','bnk','spt','nlr']
last_city = cities.pop()    #Pop the last element from the list (default)
print(last_city)
print(cities)

pop_element = cities.pop(2) #Pop element based on index position
print(pop_element)
print(cities)

#List length
cities_length = len(cities) # len() returns number of items in a list
print('cities length is '+str(cities_length))

#Sorting List

list_data = ['aaa','bbb','ccc','ddd','eee','abb','bcc']
print(list_data)
list_data.sort()    #sorting list permanently
print(list_data)

list_data.sort(reverse=True)    # sorting lists permanently in reverse order
print(list_data)

print(sorted(list_data)) #sorting list temporarily (sorted() returns copy of the list, leaving the original list)
print(list_data)
print(sorted(list_data,reverse=True))

list_data.reverse() #reversing the order of the list

#Looping through a list



