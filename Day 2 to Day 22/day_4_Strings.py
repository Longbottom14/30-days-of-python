#1
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
space=' '
print('Concatenate : ','Thirty' + space + 'Days' + space  +'Of' + space  + 'Python')

#2
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Concatenate: ', 'Coding'+ space+ 'For' + space + 'All')

#3
#Declare a variable named company and assign it to an initial value "Coding For All"
company = 'Coding'+ space+ 'For' + space + 'All'
print(company)

#4
#Print the length of the company string using len() method and print()
print('lenght: ',len(company))
print("upper: ",company.upper())
print('lower: ',company.lower())

#8
#capitalize(), title(), swapcase()
print("capitalize: ",company.capitalize())
print('title: ',company.title())
print('Swapcase: ',company.swapcase())

#9
#Cut(slice) out the first word of Coding For All string
print("Cut(slice) out the first word: ",company[:6])

#10
#Check if Coding For All string contains a word Coding using the method index, find or other methods
print("Index_method_contains a word Coding: ",company.index('Coding'))
print("Index_method_contains a word Coding: ",company.find('Coding'))
print("other_method \'in\'contains a word Coding: ",'Coding' in company)

#11
#Replace the word coding in the string 'Coding For All' to Python.
print("Replace the word coding to Python: ",company.replace('Coding','Python'))

#13
#Split the string 'Coding For All' using space as the separator (split()) .
print('Split the string \'Coding For All\': ',company.split(' '))

#14
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print("Split 2: ","Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(" "))

#15
#What is the character at index 0 in the string Coding For All
print('the character at index 0 : ',company[0])

#16
#What is the last index of the string Coding For All
print("last index of the string: ",len(company)-1)

#17
#What character is at index 10 in "Coding For All" string.
print("character is at index 10: ",company[10])

#18
#Create an acronym or an abbreviation for the name 'Python For Everyone'
print('Acronym: ','Python For Everyone'[0],'Python For Everyone'[7],'Python For Everyone'[11])

#20
#Use index to determine the position of the first occurrence of C in Coding For All
print("index of C: ",'Coding For All'.index('C'))
print("index of F: ",'Coding For All'.index('F'))
print("index of A: ",'Coding For All'.index('A'))

#22
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("rfind position of \'l\': ",'Coding For All People'.rfind('l'))

#23
#Use index or find to find the position of the first occurrence of the word 'because'
#  in the following sentence:
#  'You cannot end a sentence with because because because is a conjunction'
print("first occuence of because using index mtd: ",
'You cannot end a sentence with because because because is a conjunction'.index('because'))
print("first occuence of because using find mtd: ",
'You cannot end a sentence with because because because is a conjunction'.find('because'))

#24
#last occurrence of the word because

print("last occurrence of the word \'because\': ",
'You cannot end a sentence with because because because is a conjunction'.rindex('because'))
#25
#Slice out the phrase 'because because because'
print("Slice out phrase: ",
'You cannot end a sentence with because because because is a conjunction'[31:(47+len('because'))])

#28
#Does ''Coding For All' start with a substring Coding?
#Does 'Coding For All' end with a substring coding?
print("Does \'Coding For All\' start with a substring Coding? ",'Coding For All'.startswith('Coding'))
print("Does \'Coding For All\' end with a substring coding? ",'Coding For All'.endswith('coding'))

#30
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("Remove trailing spaces \'   Coding For All      \':",('   Coding For All      '.strip(' ')),'.')

#31
#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
print("30DaysOfPython is identifier(): ",'30DaysOfPython'.isidentifier())
print("thirty_days_of_python is isidentifier(): ",'thirty_days_of_python'.isidentifier())

#32
#['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print('join() method: ','#'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

#33
#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print('newline sequence : \n I am enjoying this challenge.\n I just wonder what is next.')

#34
#Use a tab escape sequence to write the following lines.
#Name      Age     Country
#Asabeneh  250     Finland
print('tab sequence: \n Name\t\tAge\tCountry\n Asabebeh\t250\tFinland')

#35
#Use the string formating method to display the following:
radius = 10
area = 3.14 * radius ** 2
#The area of a cricle with radius 10 is 314 meters square.
print(f'the area of a cricle with radius 10 is {area} meters square')