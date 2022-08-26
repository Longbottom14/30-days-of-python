#1
"""
Declare your age as integer variable
Declare your height as a float variable
Declare a complex number variable
Write a script that prompts the user to enter base and height of the triangle 
and calculate an area of this triangle (area = 0.5 x b x h)
"""
age =22
height =6.2 # Chubby Engr
comlex_variable = 2+1j

b = float(input('Enter Base: ',))
h = float(input('Enter height: ',))
area = 0.5 * b * h
print('The area of the triangle is :',area)

#13
#Use and operator to check if 'on' is found in both 'python' and 'jargon'
word1 = 'python'
word2 ='jargon'
print('is found in both python and jargon :',('on' in word1) and ('on' in word2))

#14
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
print('check if jargon is in the sentence :','jargon' in sentence)

#15
#There is no 'on' in both dragon and python
w1 = 'dragon'
w2 ='python'
print('no on in both dragon and python : ', ('on' not in w1) and ('on' not in w2))


#16
#Find the length of the text python and convert the value to float and convert it to string
print('lenghth: ',len('python'))
print('float _lenghth: ',float(len('python')))
print('str_float _lenghth: ',str(float(len('python'))))

#18
#The floor division of 7 by 3 is equal to the int converted value of 2.7.
print('The floor division of 7 by 3 is equal to the int converted value of 2.7: ',(7//3)==int(2.7))

#19
#Check if type of '10' is equal to 10
print('type of \'10 \' is equal to 10: ',type('10')==type(10))

#20
#Check if int('9.8') is equal to 10
print('int(\'9.8\') is equal to 10 :',int(9.8)==10)

#23
#Write a python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print('1\t1\t1\t1\t1')
print('2\t1\t2\t4\t8')
print('3\t1\t3\t9\t27')
print('4\t1\t4\t16\t64')
print('5\t1\t5\t25\t125')