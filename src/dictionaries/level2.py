# Nesting - a list of dictionaries
mobiles = [] #empty list
mi_note7 = {'ram':'3gb','hd':'32gb','camera':'16mp','screen':'5inch','os':'mi'}
nokia9 = {'ram':'2gb','hd':'32gb','camera':'12mp','screen':'4.9inch','os':'windows'}
google_pixel2 = {'ram':'6gb','hd':'128gb','camera':'32mp','os':'android'}

mobiles.append(mi_note7) #adding dictionary to list
mobiles.append(nokia9)
mobiles.append(google_pixel2)
print(mobiles)
print('looping list of dictionaries    --------------------------------->')
for mobile in mobiles:
    for infomation in mobile.items():
        print(infomation)
for mobile in mobiles:
    for key,value in mobile.items():
        print(key,' : ',value)
        print('\n')

#Nesting - lists in a dictionary
fav_languages = {'jon':['python','scala'],'den':['c'],'sara':['java','shell']}
for name,languages in fav_languages.items():
    print(name+' : ',end=' ')
    for language in languages:
        print(language,end=',')
    print()

#Nesting - A dictionary of dictionaries
users = {'aline':{'name':'aline','location':'chennai','pincode':600032},'intel':{'name':'intel','location':'usa','pincode':123456}}
print(users)
for name,details in users.items():
    print(details)
    for key,value in details.items():
        print(key+'  :  '+str(value))

#Using an ordered dict
'''Standard Python dictionaries don't keep track of the order in which keys and values are added; they only preserve the association between 
each key and its value. If you want to preserve the order in which keys and values are added, use an OrderedDict'''

from collections import OrderedDict

students = {} #defining empty dictionary

students['Manoj'] = ['yes','B.Tech']
students['Buvan'] = ['yes','Inter']
students['Anil']  = ['yes','3']
print('students '+str(students))

#Generating a million dictionaries
alien = []
for alien_num in range(1000000):
    new_alien = {}
    new_alien['height'] = 7.5
    new_alien['colour'] = 'blue'
    new_alien['eye_colour'] = 'green'
    new_alien['id'] = alien_num
    alien.append(new_alien)
print(len(alien))

