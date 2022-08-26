# Day 2 : 30 Days of python programming 

#Exercise Level 1
#print([1,2,3,4].all() is int)
first_name = 'Ridwan'
last_name ='Abdulkareem'
full_name = ' Abdulkareem Ridwan'
Country = 'Nigeria'
City = 'Lagos'
Age = 22
Year = 2000
is_married = False
is_true = True
is_light_on = True
mul_x,mul_y,mul_z = 1,2,3


# Exercise Level 2

#1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(Country))
print(type(City))
print(type(Age))
print(type(Year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type([mul_x,mul_y,mul_z]))

#2
print(len(first_name))

#3
print('first_name = ',len(first_name),' , lastname = ',len(last_name))

#4
num_one = 5
print('num_one =',num_one)
num_two = 4
print('num_two = ',num_two)
#i
variable_total = num_one + num_two
print('total  ',variable_total)
#ii
variable_diff = num_one - num_two
print('diff ', variable_diff)
#iii
variable_product = num_one * num_two
print('product  ',variable_product )
#iv
variable_division = num_one / num_two 
print('Divisoin ',variable_division)
#v
variable_remainder = num_two%num_one
print('remainder ',variable_remainder)
#vi
variable_exp = num_one**num_two
print('exponential ',variable_exp)
#vii
variable_floor_division = num_one// num_two
print('florr division ',variable_floor_division)


#5
#i
radius = 30.0 
print('radius = ',radius)
pi = 3.143
area_of_circle = pi*(radius**2)
print("Area ",area_of_circle)

#ii
circum_of_circle = 2*pi*radius
print("Circumference ",circum_of_circle)

#iii
#print("Radius = ")
radius = float(input("Radius = ",))
area_of_circle = pi*(radius**2)
print("Area_2 ",area_of_circle)


#6
first_name = input(" first name : ",)

last_name =input(" last name : ",)

Country = input(" Country : ",)

Age = input(" Age : ",)


#7
print(help())

