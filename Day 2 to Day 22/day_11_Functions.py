print(' 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum\n')
def add_two_numbers(x,y):
    return x+y
print('add_two_numbers(4,5): ',add_two_numbers(4,5))

#3
#Write a function called add_all_nums which takes arbitrary number of arguments 
# and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
print("\n 3.add_all_nums which takes arbitrary number of arguments \n")
def add_all_nums(*nums):
    total=0
    index = 1
    for num in nums:
        if str(num).isdigit():
            total+=num
        else:
            print("Invalid value")
            return
    print("total: ",total)

add_all_nums(1,2,'s') 

#Temperature in °C can be converted to °F using this formula:
#  °F = (°C x 9/5) + 32. Write a function which converts °C to °F,
#  convert_celcius_to-fahrenheit.
print(" \n 4. function which converts °C to °F \n")
def convert_celcius_to_fahrenheit(C):
    F = (C * 9/5) + 32
    print(f'{C} degree Celsius is {F} degrees in Fahrenheit')
convert_celcius_to_fahrenheit(100)

#Write a function called calculate_slope which return the slope of a linear equation
print("\n 6. calculate_slope which return the slope of a linear equation \n")
def calculate_slope():
    y1= float(input("Enter initial value of y:",))
    y2= float(input("Enter final value of y:",))
    x1= float(input("Enter initial value of x:",))
    x2= float(input("Enter final value of y:",))
    slope = (y2 -y1)/(x2 -x1)
    print(f'slope of line moving from: y2 = {y2} to y1 = {y1} \n and x2 = {x2} to {x1} \n Slope = {slope}')

calculate_slope()

#Quadratic equation is calculated as follows: 
# ax² + bx + c = 0.
#  Write a function which calculates solution set of a quadratic equation, 
# solve_quadratic_eqn.
print('\n 7. function which calculates solution set of a quadratic equation\n')
def solve_quadratic_eqn():
    print(" Equation in form of  ax² + bx + c = 0")
    a= float(input("Enter initial value of a:",))
    b= float(input("Enter final value of b:",))
    c= float(input("Enter initial value of c:",))
    r1 = (-b + (b*2-(4*a*c))*0.5)/(2*a)
    r2 = (-b - (b*2-(4*a*c))*0.5)/(2*a)
    print(f'The roots of Quadratic Equation : {a}x² + {b}x + {c} = 0 \n\t\tr1 = {r1} \t r2 = {r2}')
solve_quadratic_eqn()

#Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
print('\n 8. returns the reverse of the array \n ')
def reverse_list(array):
    max_index =  len(array)-1
    #print('max index :',max_index)
    reversed_list =[]
    while max_index > -1:
        #print(max_index)
        reversed_list.append(array[max_index])
        max_index-=1
    print("INPUT ARRAY : ",array,)
    return reversed_list
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]

#9. Declare a function named capitalize_list_items.
#  It takes a list as a parameter and it returns a capitalized list of items
print('\n 9.returns a capitalized list of items \n')
def capitalize_list_items(array):
    output=[]
    for item in array:
        output.append(str(item).upper())
    print("INPUT ARRAY: ",array)
    del array
    return output
print(capitalize_list_items(['nba','uefa','nepa','phcn']))

#10
#Declare a function named add_item. 
# It takes a list and an item parameters. It returns a list with the item added at the end.
print('\n 10. returns a list with the item added at the end \n')
def add_item(array,new_item):
    print("INPUT ARRAY : ",array)
    array.append(new_item)
    return array
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(  add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))     # [2, 3, 7, 9, 5]

#12
#Declare a function named remove_item. 
# It takes a list and an item parameters. It returns a list with the item removed from it.
print('\n 12.  returns a list with the item removed from it\n')
def remove_item(array,new_item):
    print("INPUT ARRAY : ",array)
    array.remove(new_item)
    return array
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

#!7
#Call your function factorial, it takes a whole number as a parameter and
#  it return a factorial of the number
print('\n 10.  return a factorial of the number \n')
def factorial(number):
    get_range = range(1,number+1)
    fact=1
    for num in get_range:
        fact = fact*num
    print(f"The factorial of {number}! is {fact}")
factorial(number=4)
factorial(number=5)

#18
#Call your function is_empty, it takes a parameter and it checks if it is empty or not
print('\n 10.  takes a parameter and it checks if it is empty or not \n')
def is_empty(array):
    print("INPUT ARRAY : ",array)
    return len(array)==0
print(is_empty([1,2,3,4]))
print(is_empty([])) 

#20
#Write a function called is_prime, which checks if a number is prime.
print('\n 20.  checks if a number is prime \n')
def is_prime(number):
    print(f"Is {number} a prime number ?")
    possible_divisor = range(2,number) # number not included
    if number == 2:
        return True
    else:
        for div in possible_divisor:
            if number%div == 0: # divisible by another number
                return False
        return True
print(is_prime(2))
print(is_prime(3))
print(is_prime(7))
print(is_prime(10))
print(is_prime(15))

#21
#Write a functions which checks if all items are unique in the list.
print('\n 21. functions which checks if all items are unique in the list \n')
def is_all_items_unique(array):
    set_array = set(array) # array contains only unique
    print("INPUT ARRAY : ",array)
    return len(array) == len (set_array) # if lenghth is not equal ; array contains duplicates
print(is_all_items_unique([1,2,3,4,5]))  
print(is_all_items_unique([1,2,3,4,4,5]))

#22
#Write a function which checks if all the items of the list are of the same data type
print('\n 21. checks if all the items of the list are of the same data type\n')
def is_same_type(array):
    first_item_type = type(array[0])
    print("INPUT ARRAY : ",array)
    for item in range(1,len(array)):
        if type(array[item]) != first_item_type:
            return False
    else:
        return True
print(is_same_type([1,2,3,4]))
print(is_same_type([1,2,'3',4]))
print(is_same_type([True,2,True,4]))

#23
#Write a function which check if provided variable is a valid python variable
print('\n  23. check if provided variable is a valid python variable\n')
def is_valid_var(variable):
    print(f"is {variable} an identifier ?")
    return str(variable)[0].isalpha()
print(is_valid_var('3Kings'))
print(is_valid_var('_KingJames'))
print(is_valid_var('KingJames'))

