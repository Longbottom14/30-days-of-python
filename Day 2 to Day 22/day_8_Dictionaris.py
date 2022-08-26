#Create an empty dictionary called dog
dog = {}

#Create a student dictionary 
# and add first_name, last_name, gender, age, marital status, skills, country, city and 
# address as keys for the dictionary

student = {
    'first_name' : 'Neville',
    'last_name' : "LongBottom",
    'gender' :'M',
    'age' : 22,
    'marital status':'Sad and Lonely',
    'skills': ['Python','C++','SQL',"PowerBI"],
    'country' :'Nigeria',
    'city' : 'LAgos',
    'address': {
        'street':'Adams Ajakaye',
        'NO':12,    
    }
}

print("dict : ",student)
print("Lenghth : ",len(student))
print("Skills: ",student['skills'],' type : ',type(student['skills']),'\n')

student['skills'].append('Excel')
print('Addding Excel:',student,'\n')

#Get the dictionary keys as a list
print("Keys : ",student.keys(),'\n')

#Get the dictionary values as a list
print('dictionary values as a list : ',student.values(),'\n')

#Change the dictionary to a list of tuples using items() method
print('dictionary to a list of tuples : ',student.items(),'\n')

#Delete one of the items in the dictionary
del student['address']

#delete dict
del student