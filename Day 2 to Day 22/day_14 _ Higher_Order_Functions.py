from functools import reduce
from os import remove


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('\n 7.Use map to create a new list by changing each country to uppercase in the countries list \n')
upper_case = map(lambda x : x.upper(),countries)
print("INput :",countries,'\n OUTput: ',list(upper_case))

print('\n 8. Use map to create a new list by changing each number to its square in the numbers list\n')
print("INput :",numbers,'\n OUTput: ',list(map(lambda x :x**2,numbers)))

print('\n 8.Use map to create a new list by changing each name to uppercase in the names list \n')
upper_case = map(lambda x : x.upper(),names)
print("INput :",names,'\n OUTput: ',list(upper_case))

print('\n 9. Use filter to filter out countries containing \'land\'.\n')
filter_land = filter(lambda x: 'land' in x,countries)
print("INput :",countries,'\n OUTput: ',list(filter_land))

print('\n 10. Use filter to filter out countries having exactly six characters.\n')
filter_6 = filter(lambda x: len(x)==6,countries)
print("INput :",countries,'\n OUTput: ',list(filter_6))

print('\n 11. Use filter to filter out countries having exactly six letters or more.\n')
filter_6_more = filter(lambda x: len(x)>=6,countries)
print("INput :",countries,'\n OUTput: ',list(filter_6_more))

print('\n 12. Use filter to filter out countries starting with letter\'E\'.\n')
filter_E = filter(lambda x: x.find('E')==0,countries)
print("INput :",countries,'\n OUTput: ',list(filter_E))

print('\n 13. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))\n')
#filter_E_upper = countries.filter(lambda x: x.find('E')==0,countries).map(lambda x : x.upper(),countries)
#print("INput :",countries,'\n OUTput: ',list(filter_E_upper))
#'dddd'.is
print(type('gggg'))
print('\n 14.Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.\n')
def string_decoarator(function):
    def wrapper(*args):
        get_list = function(*args)
        return list(filter(lambda x : type(x) == type('ddd'),get_list))
    return wrapper
@string_decoarator
def list_it(*args):
    return args
print("INput :",(1,2,3,'hhh',7,'ffff'),'\n OUTput: ',list_it(1,2,3,'hhh',7,'ffff'))

print('\n 15. Use reduce to sum all the numbers in the numbers list.\n')
def add_num(x,y):
    return x+y
total = reduce(add_num,numbers)
print('input: ',numbers ,'\n Output: ',total)
total2 = reduce((lambda x,y : x+y),numbers)
print('Output: ',total2)

print('\n 16. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries\n')
def country_string(x,y):
 return x+', '+y
cat_string =  reduce(country_string,countries) + ' are north European countries'
print('Output : ',cat_string)

print('\n 17. (eg \'land\', \'ia\', \'island\', \'stan\')).\n')
from day_5_lists2 import countries
countries_whole = countries
#print(type(countries_whole))
#print(countries_whole)
def categorize():
    aliases =  ['land', 'ia', 'island', 'stan']
    category = {}
    for alias in aliases:
        category[alias] = []
    for country in countries_whole: 
        for alias in aliases:
            idx_first = country.lower().rfind(alias[0])
            idx_last = country.lower().rfind(alias[-1])
            if (alias in country.lower()) and ( idx_last - idx_first) == len(alias)-1:
                category[alias].append(country)
    return category

grouped = categorize()
for key in grouped.keys():
    print(key)
    print(grouped[key],'\n')

print('\n 18. keys stand for starting letters of countries and values are the number of country names starting with that letter\n')
def categorize_with_first_letter():
    cat = {}
    for country in countries_whole:
        first_letter = country[0]
        if first_letter in cat.keys():
            cat[first_letter].append(country)
        else:
            cat[first_letter]=[]
            cat[first_letter].append(country)
    return cat
grouped_letter = categorize_with_first_letter()
for key in grouped_letter.keys():
    print(key)
    print(grouped_letter[key],'\n')

print('\n 19. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.\n')
def get_first_ten_countries():
    return countries[:10]
print(get_first_ten_countries())

print('\n 20. Declare a get_last_ten_countries function - it returns a list of last ten countries from the countries.\n')
def get_last_ten_countries():
    return countries[-10:]
print(get_last_ten_countries())

#22
#Use the countries_data.py 
#Sort countries by name, by capital, by population
#Sort out the ten most spoken languages by location.
#Sort out the ten most populated countries.

from countries_data import countries_data
countries_datas = countries_data
print('countries_data type :',type(countries_datas),'\n')
print('1st country data:\n',countries_datas[0],'\n')
print('1st_data type :',type(countries_datas[0]),'\n')
key_types = [ str(key)+':'+str(type(value))  for key,value in countries_datas[0].items() ]
print("KEYS and types")
[print(key_and_type) for key_and_type in key_types]
"""
name:<class 'str'>
capital:<class 'str'>
languages:<class 'list'>
population:<class 'int'>
flag:<class 'str'>
currency:<class 'str'>

"""
#test = [('a',4),('b',3),('d',5),('e',1),('c',6),('f',3)]
#test2 = [(4,'a'),(3,'b'),(5,'d'),(1,'e'),(6,'c'),(3,'f')]
#test2.sort()
#test.sort()
#print(test,test2)  ===[('a', 4), ('b', 3), ('c', 6), ('d', 5), ('e', 1), ('f', 3)] 
# [(1, 'e'), (3, 'b'), (3, 'f'), (4, 'a'), (5, 'd'), (6, 'c')]
def sort_languages_decorator(function):
    def wrapper(name_key,criteria,descending=False):
        sort_dict = function(name_key,criteria,descending=False)
        language_dict = {}
        for country_data in countries_datas:
            for language in country_data['languages']:
                if language in language_dict.keys():
                    language_dict[language] +=1
                else:
                    language_dict[language] = 1
        sort_list = [(value,key) for key,value in language_dict.items()]
        sort_list.sort(reverse=True)
        sort_dict['languages'] = [(tpl[1],tpl[0]) for tpl in sort_list]
        return sort_dict
    return wrapper

@sort_languages_decorator
def Sort_countries_by_name_by_capital_by_population(name_key,criteria,descending=False):
    sorter_dict={}
    for criterion in criteria:
        sorter = []
        for country_data in countries_datas: # country_data= dict
            sorter.append((country_data[criterion],country_data[name_key]))
        sorter.sort(reverse=descending)
        if criterion == name_key:
            sorter_dict[criterion] = [tpl[1] for tpl in sorter]
        else:
            sorter_dict[criterion] = [(tpl[1],tpl[0])for tpl in sorter]
    
    return sorter_dict
sorter_dict = Sort_countries_by_name_by_capital_by_population('name',['name','capital','population'])
print('\n Sort by name : \n',sorter_dict['name'])
print('\n Sort by Capital : \n',sorter_dict['capital'])
print('\n Sort by Population :  \n',sorter_dict['population'])

#Sort out the ten most spoken languages by location.


sorter_dict = Sort_countries_by_name_by_capital_by_population('name',['name','capital','population'])
print('\n Sort Languages : \n',sorter_dict['languages'])


                    
    
#Sort out the ten most populated countries.
sorter_dict = Sort_countries_by_name_by_capital_by_population('name',['name','capital','population'],descending=True)
top_10_populated = sorter_dict['population'][:10]  # list is in ascending order i.e reverse = Falsedescending ||
print('\n Top 1O populated countries : \n',top_10_populated)




