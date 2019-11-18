class HelloWorld:
    print("Hello World!")
    msg = "Aline"
    print(msg)
    first_name = 'Andhra'
    last_name  = "Pradesh"
    print(first_name+' '+last_name)

#making list and looping
bikes = ['yamaha','bajaj','hero']
print('first_bike '+bikes[0])
print('last_bike '+bikes[-1])
bikes[-1] = 'honda' #replacing item inside list
for bike in bikes:
    print(bike)

#Adding elements to list
cars = []
cars.append("Land Rover")
cars.append('volvo')
cars.append("Range Rover")
print(cars)
for car in cars:
    print("name of car "+car)

#making numerical lists
squares = []
for x in range (1,5):
    squares.append(x**2)
print(squares)

#List comprehensions
cubes =[x**3 for x in range(1,10)]
print(cubes) #[1, 8, 27, 64, 125, 216, 343, 512, 729]

#slicing lists
cube_slice = cubes[:2]
print(cube_slice) #[1, 8]
cube_slice_last = cubes[:-2]
print(cube_slice_last) #[1, 8, 27, 64, 125, 216, 343]

#Coping list
cube_copy = cubes[:]
print(cube_copy) #[1, 8, 27, 64, 125, 216, 343, 512, 729]

#Tuples (Similar to lists, but items in tuples can't be modified)
dimensions = (123,124)
print(dimensions[0])

#if statements
if(5<10):
    print('yes')

#Conditional tests with lists
squares = [x**2 for x in range(1,10)]
range =[x for x in  range(1,10)]
print(squares)
print(range)
if(5 in range):
    print("is there in given range")

if(18 not in range):
    print("not there in given range")

age  = 23
if(age>18):
    print("you are eligible to vote")
else:
    print('you are not eligible to vote')

#if-elif-else
if(age>21):
    print("eleigible to valte and marrage")
elif(age>18):
    print("eligible to vote")
else:
    print("Not eligible")

#Dictionaries - Dictionaries store connections between pieces of information. Each item in a dictionary is a key value pair.
alien = {'colour':'green','points':5}
print('Alies colour is '+alien['colour'])#Alies colour is green
alien['eyes'] = 'blue'
print(alien) #{'colour': 'green', 'points': 5, 'eyes': 'blue'}
alien['points'] = 6 #updating items in a dictionary
print(alien)

#Looping through all key value pairs
for item in alien.items():
    print(item)
for key in alien.keys():
    print(key)
for value in alien.values():
    print(value)

for x,y in alien.items():
    print(x+" " +str(y))

fav_numbers = {'eric': 17, 'ever': 4}
for name,number in fav_numbers.items():
    print(name + ' loves '+str(number))

#User Input (program can prompt user for input. All input is stored as string)
name  = input("What's your name")
print("Hello "+name)

pi = input("What's the value of pi")
pi = float(pi)
print(pi)


