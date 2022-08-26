#1
age = int(input('Enter your age : ',))
print('You are old enough to learn to drive' if age >= 18 
else f'You need {18 - age} more years to learn to drive')

#3
number_one = int(input('Enter number one:',))
number_two = int(input('Enter number two:',))

if number_one > number_two:
    print(f'{number_one} is greater than {number_two}')

elif number_one < number_two:
    print(f'{number_one} is less than {number_two}')

else:
    print(f'{number_one} is equal {number_two}')

#6
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter fruit:',)
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
    
#7
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#If the person is married and if he lives in Finland, print the information in the following format:
    # Asabeneh Yetayeh lives in Finland. He is married.
print('subset:',set(['React', 'Node' ,'MongoDB']).issubset(set(person['skills'])))
print('All:',all(['React', 'Node' ,'MongoDB']) in person['skills'])
for s in ['React', 'Node' ,'MongoDB']:
    print(s,'in skills : ',s in person['skills'])
if 'skills' in person.keys():
    print('Middle skill: ',person['skills'][(len(person['skills'])-1)//2])
    if 'Python' in person['skills']:
        print('Pythonista')
        if person['skills'] == ['JavaScript', 'React']:
            print('He is a front end developer')
        elif person['skills'] == [ 'Node', 'Python', 'MongoDB']:
             print('He is a backend developer')
        elif set(['React', 'Node' ,'MongoDB']).issubset(set(person['skills'])):
             print('He is a fullstack developer')
        else:
         print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print(person['first_name'],person['last_name'], ' lives in ',person['country'])


    



