#1
#Writ a function which generates a six digit/character random_user_id
from array import array
import string
from random import random,randint,randrange
from turtle import color
import time

#print(string.ascii_lowercase)
#print(string.digits)
#print(string.ascii_lowercase+string.digits)
print('\n 1. function which generates a six digit/character\n')
def  random_user_id():
    length = 6
    possible_characters= str(string.ascii_lowercase+string.digits)
    id='#'
    while length>0:
        random_index = randint(0,len(possible_characters)-1)
        #print(random_index)
        char = possible_characters[random_index]
        #print(char)
        id=id+str(char)
        length-=1
    return id
print("User ID: ",random_user_id())

#2
#Modify the previous task. Declare a function named user_id_gen_by_user.
#  It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and 
# the second input is the number of IDs which are supposed to be generated.
print('\n 2. number of IDs which are supposed to be generated\n')
r = list(range(5))
#print(r)
def user_id_gen_by_user():
    length = int(input("length of chracters:"),)
    no_IDs = int(input("Number of IDs:"),)
    possible_characters= str(string.ascii_lowercase+string.digits)
    array_out = list()
    while no_IDs>0:
        id='#'
        itr= length # after the while conditions runs out..it reset itr to the length again
        while itr>0:
            random_index = randint(0,len(possible_characters)-1)
            #print(random_index)
            char = possible_characters[random_index]
            id = id + char
            itr=itr-1
        array_out.append(id)
        no_IDs= no_IDs-1
    return ' '.join(array_out)
print(user_id_gen_by_user())
print(user_id_gen_by_user())

#3
#Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).
print("\n 3. It will generate rgb colors (3 values ranging from 0 to 255 each) \n")
def rgb_color_gen():
    color_array = []
    for i in range(3):
        random_no = randrange(0,255)
        color_array.append(str(random_no))
    rgb = ','.join(color_array)
    return 'rgb('+ rgb + ')'
print(rgb_color_gen())

#4
#Write a function list_of_hexa_colors 
# which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #.
#Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet,a-f. 
print('\n 4. returns any number of hexadecimal colors in an array \n')
def list_of_hexa_colors(no_hexa_colors):
    possible_characters= str(string.digits+'ABCDEF') #string.hexdigits=0123456789abcdefABCDEF
    hex_color_list = list()
    for i in range(no_hexa_colors):
        hex_color ='#'
        for i in range(6):
            random_index = randrange(0,len(possible_characters)-1)
            char = possible_characters[random_index]
            hex_color+=char
        hex_color_list.append(hex_color)
    return hex_color_list
print(list_of_hexa_colors(3))

#5
#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print('\n 5. returns any number of RGB colors in an array\n')
def list_of_rgb_colors(no_rgb_colors):
    rgb_colors_list = list()
    for i in range(no_rgb_colors):
        color_array = []
        for i in range(3):
            random_no = randrange(0,255)
            color_array.append(str(random_no))
            rgb = ','.join(color_array)
        new_rgb  = 'rgb('+ rgb + ')'
        rgb_colors_list.append(new_rgb)
    return rgb_colors_list
print(list_of_rgb_colors(5))

#6
#Write a function generate_colors which can generate any number of hexa or rgb colors
print('\n 6. generate any number of hexa or rgb colors \n')
def generate_colors(color_type,no_of_type):
    print(f'Generating {no_of_type} {color_type} colors :')
    if color_type == 'hexa':
        possible_characters= str(string.digits+'ABCDEF') #string.hexdigits=0123456789abcdefABCDEF
        hex_color_list = list()
        for i in range(no_of_type):
            hex_color ='#'
            for i in range(6):
                random_index = randrange(0,len(possible_characters)-1)
                char = possible_characters[random_index]
                hex_color+=char
            hex_color_list.append(hex_color)
        return hex_color_list
    elif color_type == 'rgb':
        rgb_colors_list = list()
        for i in range(no_of_type):
            color_array = []
            for i in range(3):
                random_no = randrange(0,255)
                color_array.append(str(random_no))
                rgb = ','.join(color_array)
            new_rgb  = 'rgb('+ rgb + ')'
            rgb_colors_list.append(new_rgb)
        return rgb_colors_list
    else:
        print("Invalid colortype")

print(generate_colors('hexa', 3) )
print(generate_colors('hexa', 1) )
print(generate_colors('rgb', 3) ) 
print(generate_colors('rgb', 1) ) 

#7.
#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
#from math import perm
import random
print('\n 7. takes a list as a parameter and it returns a shuffled list\n ')
def shuffle_list(array):
    print("INPUT ARRAY: ",array)
    print("Shuffle: ")
    random.shuffle(array)
    return  array
print(shuffle_list(['Ridwan',"khadijah",'Skillz']))

#8.
#Write a function which returns an array of seven random numbers in a range of 0-9.
# All the numbers must be unique.
print("\n  8. function which returns an array of seven random numbers in a range of 0-9\n")
def Unique_Numbers():
    start = time.time()
    not_found  = True
    set_number = set() #stored in set to select only unique values
    no_iteration =0
    while not_found:
        a_number = randrange(0,10)
        set_number.add(a_number)
        if len(set_number) == 7:
            not_found = False
        no_iteration+=1
    print(f'Number of Epochs : {no_iteration} iterations')
    end = time.time()
    print(f'Runtime of the program is : {end - start}')
    return set_number
print(Unique_Numbers())

def Unique_Numbers2():
    start = time.time()
    not_found  = True
    set_number = set() #stored in set to select only unique values
    no_iteration =0
    range_list = list(range(0,10))
    while not_found:
        an_index = randint(0,len(range_list)-1)
        number_from_range_list = range_list[an_index]
        set_number.add(number_from_range_list)
        if len(set_number) == 7:
            not_found = False
        range_list.pop(an_index)
        no_iteration+=1
    print(f'Number of Epochs Optimized function: {no_iteration} iterations')
    end = time.time()
    print(f'Runtime of the program is : {end - start}')
    return set_number
    
print(Unique_Numbers2())

def Unique_Numbers2():
    start = time.time()
    not_found  = True
    set_number = list() #stored in set to select only unique values
    no_iteration =0
    range_list = list(range(0,10))
    while not_found:
        an_index = randint(0,len(range_list)-1)
        number_from_range_list = range_list[an_index]
        set_number.append(number_from_range_list)
        if len(set_number) == 7:
            not_found = False
        range_list.pop(an_index)
        no_iteration+=1
    print(f'Number of Epochs  SuperOptimized function: {no_iteration} iterations')
    end = time.time()
    print(f'Runtime of the program is : {end - start}')
    return set_number
print(Unique_Numbers2())









