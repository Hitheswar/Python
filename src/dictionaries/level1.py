print('dictionaries level 1')
'''
Python's dictionaries allow you to connect pieces of related information. Each piece of information in a dictionary is stored as a key-value pair. 
When you provide a key, Python returns the value associated with that key. You can loop through all the key-value pairs, all the keys, or all the values

Defining dictionaries   :
1. use curly braces to define dictionary.
2. use colons to connect keys and values.
3. use commas to separate individual key value pairs.
'''
#defining dictionary
alien = {'colour':'green','height':7,'eye_colour':'blue','points':7}
print(alien)
#Accessing values
print('alien colour '+alien['colour'])
print('alien points '+str(alien['points'])) #getting the value associated with the key

#Adding new key-value pairs:
'''
You can store as many key-value pairs as you want in a dictionary, until your computer runs out of memory. To add a new key-value pair to an existing dictionary
give the name of the dictionary and the new key in square brackets, and set it equal to the new value. This also allows you to start with an empty dictionary 
and add key-value pairs as they become relevant. '''

alien['speed'] = '12.5kmph' #Adding a new key-value pair to dictionary
print(alien)

mi_note7 = {}               #defining a empty dictionary
mi_note7['ram'] = '3gb'     #Adding items to dictionary
mi_note7['rom'] = '32gb'
mi_note7['battery'] = '4000mah'
mi_note7['camera']  = '16mp'
print(mi_note7)


#Modifying values in dictionary
mi_note7['camera'] = '12mp'
mi_note7['display'] = '5inch'
print(mi_note7)

#Removing key value pairs
del mi_note7['display']
print(mi_note7)

#Looping through a dictionary:
'''You can loop through a dictionary in three ways: you can loop through all the key-value pairs, all the keys, or all the values.     
A dictionary only tracks the connections between keys and values; it doesn't track the order of items in the dictionary. If you want to process the information 
in order, you can sort the keys in your loop'''

#looping through key-values
fav_languages = {'spark':'scala','spring':'java','db':'sql','ML':'python'}
for name,language in fav_languages.items():
    print(name+' favorite language is '+language)
#looping through keys:
for name in fav_languages.keys():
    print(name)
#looping through values
for language in fav_languages.values():
    print(language)

#looping through all keys in order
for name in sorted(fav_languages.keys()):
    print(name)

#Dictionary length:
print(len(fav_languages))