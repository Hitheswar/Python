"""
A list stores a series of items in a particular order. lists allows you to store sets of information in one place,whether you have just few items or millions of
items. Lists are one of python most powerful features readily accessible for new programmers. And they tie together many important concepts in python programming.

Defining a list :
1. use square brackets to define a list.
2. use commas to separate individual items in lists.
3. use plural names for lists, to make your code easier to read.
"""
users = ['nokia', 'intel','aline', 'edh', 'hp']
print(users)
#Accessing elements : individual elements in a list are accessed according to their position, called the index.
first_user  = users[0]
second_user = users[1]
last_user   = users[-1]
print(first_user,second_user,last_user)
#Modifying individual items by referring to the index of the item.
users[-2] = 'lima'
print(users)

#Adding items to the end of the list, or we can insert any wherever we like
users.append('pdi') #adding item to the end of the list
print(users)

states = [] #empty list
states.append('AP')
states.append('TG')
states.append('TN')
states.append('NJK')
print("states ",end='')
print(states)

states.insert(1,'KT') # inserting elements at a particular position
states.insert(2,'KL')
states.insert(2,'KL')
print(states)

#Removing elements from the list
del states[2]           #removing element by index
print(states)
states.remove('NJK')    #removin element by value
print(states)

