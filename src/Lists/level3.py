print('level 3')
'''Looping through lists :
    Lists can contain millions of items, so Python provides an efficient way to loop through all the items in a list. When you set up a loop,
    Python pulls each item from the list one at a time and stores it in a temporary variable, which you provide a name for. This name should be the
    singular version of the list name. The indented block of code makes up the body of the loop, where you can work with each individual item.
     Any lines that are not indented run after the loop is completed.
'''
users = ['aline','intel','nokia','lima','hp','kinaxis']
for user in users:
    print('well come to '+user+' ')

'''The range() function
we can use the range() function to work with a set of numbers efficiently. The range() function starts at 0 by default, and stops one number below
 the number passed to it. we can use the list() function to efficiently generate a large list of numbers.'''

for number in range(101):       #printing numbers from 0 t0 100
    print('number '+str(number))
for number in range(101,201):   #printing numbers from 101 to 200
    print('number '+str(number))

numbers = list(range(1,1001))   #making list of numbers
print('size of numbers '+str(len(numbers)))

'''Simple statistics  : there are number of simple statistics we can run on a list containing numerical data.'''
ages = [23,24,34,56,23,12,34,56,57,22]
youngest = min(ages)
oldest   = max(ages)
sum      = sum(ages)
print(youngest,oldest,sum)

'''
Slicing a list:
We can work with any set of elements from a list. A portion of a list is called a slice. To slice a list, start with the index of the first item you want,
then add a colon and the index after the last item we want. Leave off the first index to start at the beginning of the list, and leave off the last index
 to slice through the end of the list
'''
finishers = ['jadhav','dhoni','pandya','jadeja','rohit','kohli']
first_three = finishers[:3]
print('first three finishers '+str(first_three))
middle_three = finishers[1:4]
print('middle three finishers '+str(middle_three))
last_three = finishers[-3:]
print('last three finishers '+str(last_three))

'''Copying a list'''
finishers_copy = finishers[:]
print(finishers_copy)

'''List comprehensions'''
squares = []
for x in range(1,11):       #generating list squares using loop
    square = x**2
    squares.append(square)
print(squares)

cubes = [x**3 for x in range(1,11)] #generating list of cubes using comprehensions
print(cubes)

names = ['aline','intel','chennai','nokia']
print('names  '+str(names))
names = [name.upper() for name in names]    #using comphrehension to convert list of names to upper case
print('names '+str(names))

'''Tuples
A tuple is like a list, except we can't change the values in a tuple once it's defined. Tuples are good for storing information that shouldn't be changed 
throughout the life of a program. Tuples are designated by parentheses instead of square brackets. (We can overwrite an entire tuple, but we can't change
 the individual elements in a tuple.) 
'''
dimensions = (800,600)      #defining tuple
for dimension in dimensions:    #looping through tuple
    print('dimensions '+str(dimension))

print(dimensions)
dimensions = (1200,800)         #overwriting tuples
print(dimensions)

#Example
languages = []
languages.append('python')
languages.append('scala')
languages.append('java')
languages.append('sql')

for language in languages:
    print(language +' is a programming language')

primary_languages = languages[:2]
print('these are my primary programming languages ',end='')
for language in primary_languages:
    print(language+' ',end='')
print()
languages.remove('sql')
print(languages)
del languages[2]
print(languages)

