print('level 1')
age = 23
if age>18:
    print('you are eligible to vote')

players = ['dAma']
if players:                                 #checking if list is empty
     for player in players:
         print('player : '+player)
         print('player : '+player)
else:
    print('we don not have players')


current_number = 1
while current_number<=5:
    print(current_number)
    current_number+=1

'''prompt = "\nTell me something, and I'll "  #let the user choose when to quit
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
msg = '''''

'''while msg != 'quit':
    msg = input(prompt)

    if msg != 'quit':
        print(msg)'''

'''flag = True                                         #using flag
while flag:
    msg = input(prompt)
    if msg !='quit':
        print(msg)
    else:
        flag = False'''

'''prompt = "\nWhat cities have you visited?"
prompt += "\nEnter 'quit' when you're done. "

while True:     #using break to exit loop
    city = input(prompt)
    if city =='quit':
        break
    else:
        print("I've been to "+city+" !")'''


#using continue in loop
'''banned_players = ['eve','jos','den','dag']
players = []
while True:
    player = input("enter your player name. Enter Quit to Exit")
    if(player=='quit'):
        break
    elif player in banned_players:
        print(player+' is banned')
        continue
    else:players.append(player)

print('your players')
for player in players:
    print(player)'''

