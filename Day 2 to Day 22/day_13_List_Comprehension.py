#1.
#Filter only negative and zero in the list using list comprehension
print('\n 1. Filter only negative and zero in the list using list comprehension\n')
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
sol1 = [i for i in numbers if i>0]
print(f'input: {numbers} \n output : {sol1}')

#2.
#Flatten the following list of lists of lists to a one dimensional list :
print('\n 2. Flatten the following list of lists of lists to a one dimensional list \n')
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#[
# [
# [1, 2, 3
# 
# ]], 

# [[4, 5, 6]],
#  [[7, 8, 9]]]
sol2 = [no for box1  in list_of_lists for box2 in box1 for no in box2  ]
print(f'input: {list_of_lists} \n output : {sol2}')

#3.
#Using list comprehension create the following list of tuples:
print('\n 3.Using list comprehension create the following list of tuples: \n')
sol3=[(i,1,i,i**2,i**3,i**4,i**5) for i in range(11) ]
print(f'input: \n output : {sol3} \n')
for tp in sol3:
    print(tp)

#4.
#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#countries = 
# [
# [
# (
# 'Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print('\n 4.Flatten the following list to a new list: \n')
sol5 = [location for country_city_array  in countries for country_city_tp in country_city_array for location in country_city_tp  ]
print(f'input: {countries} \n output : {sol5}')

#5
#Change the following list to a list of dictionaries:
print('\n 5. Change the following list to a list of dictionaries:\n')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]
sol5 = [{'country': country_city_tp[0] ,'city':country_city_tp[1]} for country_city_array  in countries for country_city_tp in country_city_array  ]
print(f'input: {countries} \n output : {sol5}')

#6
#Change the following list of lists to a list of concatenated strings:
print('\n 6. Change the following list of lists to a list of concatenated strings: \n')
names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
sol6 = [ names_tp[0]+' '+names_tp[1] for names_array  in names for names_tp in names_array ]
print(f'input: {names} \n output : {sol6}')

#7
#Write a lambda function which can solve a slope or y-intercept of linear functions.
print('\n 7. Write a lambda function which can solve a slope or y-intercept of linear functions.\n')
slope = lambda y1,y0,x1,x0 : (y1-y0)/(x1-x0)
print('slope of : (0,2) to (1,4) is ',slope(4,2,1,0))
