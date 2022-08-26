#1
print('Create an empty tuple: ',tuple(),' ',(),'\n')

#2
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
siblings = ('akk','skillz','bola','Ife')
print('names of your sisters and your brothers : ',siblings)
print('lenght: ',len(siblings),'\n')

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('pop',"Ma") 
print("family_member : ",family_members,'\n')

#Unpack siblings and parents from family_members
second ,first , soldier , prodigy , *Parents = family_members
print('parents: ',Parents,'\n')

#Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('mango','apple','orange','corn')
vegetables = ('efo','ewedu','ila')
animal_products = ('meat','milk','fish','egg')

food_stuff_tp = fruits + vegetables + animal_products
print('food_stuff_tp: ',food_stuff_tp,'\n')
#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('food_stuff_lt: ',food_stuff_lt,'\n')

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = (len(food_stuff_tp)-1)//2
print('middle: ',food_stuff_tp[middle_index], '\n')

#Slice out the first three items and the last three items from food_staff_lt list
print('first 3: ',food_stuff_lt[:3])
print('first 3: ',food_stuff_lt[-3:],'\n')

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('\'Estonia\' is a nordic country: ','Estonia' in nordic_countries)
print('\'Iceland\' is a nordic country: ','Iceland' in nordic_countries)




