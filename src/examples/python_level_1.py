#while loop     - repeats a block of code as long as a certain code is true
current_value = 1
while current_value <=5:
    print(current_value,end=' ')    #printing values in the same line
    current_value +=1
print()

'''msg = ''                         #letting user choose when to quit
while msg!='quit':
    msg = input('enter your message = ')
    print(msg)'''

'''Functions      - Functionas are named blocks of code, designed to do one specific job. Information passesd to a function is called an argument.
                  Information received by a funcion is called a parameter'''
def greet_user(name):               #calling function with argument
    """Display a simple greeting"""
    print('Hello '+name)
greet_user("Hithesh")

def make_pizza(topping='bacon'):    #default values as parameters
    """make a single topping pizza"""
    print('have a '+topping+' pizza')
make_pizza('pepper_onion')
make_pizza()

def add_numbers(x,y):               #return a value
    """"Add two numbers and return the sum"""
    return x+y
sum = add_numbers(2,3)
print('sum '+str(sum))


'''Classes    - A class defines the behavior of an object and the kind of information an object can store. The information in class is stored in attributes
                 and functions belongs to class are called as methods. A child class inherits methods and attributes from it's parent class'''
#Creating parrot class
class Parrot():
    """Representing Parrot class"""
    def __init__(self,name):
        """initializing parrot object"""
        self.name = name
    def play(self):
        """simulate sitting"""
        print(self.name +" is playing")

my_parrot = Parrot('chiluka')
print(my_parrot.name+" is a good parrot")
my_parrot.play()


#Exceptions
prompt = "How many tickets you need? "
num_tickets = input(prompt)
try:
    num_tickets = int(num_tickets)
except ValueError:
    print("please try again")
else:
    print("your tickets are printing")