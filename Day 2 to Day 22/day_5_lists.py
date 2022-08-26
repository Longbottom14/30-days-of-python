#1
#Declare an empty list
empty_list=list()
print("empty: ",empty_list)

#2
#Declare a list with more than 5 item
items_5 = [1,2,3,4,5]
print('5 items: ',items_5)
print("lenght: ",len(items_5))
print(f'1st, middle ,last : {items_5[0]}, {items_5[(len(items_5)-1)//2]}, {items_5[-1]}')

#5
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['long', 22,6,'single','Degoba']
print(f' mixed_data_types : {mixed_data_types}')

#6
#Declare a list variable named it_companies and assign initial 
# values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']


print('it_companies: ',it_companies)
print("lenght: ",len(it_companies))
print(f'1st, middle ,last : {it_companies[0]}, {it_companies[(len(it_companies)-1)//2]}, {it_companies[-1]}')

it_companies[4] = 'world_bank'
print("modify ibm : ",it_companies)

it_companies.append('Tesla')
print("add Tesla : ",it_companies)

it_companies.insert(((len(it_companies)-1)//2),'Twitter')
print("imsert twitter in middle : ",it_companies)

it_companies[1]=it_companies[1].upper()
print("google Upper : ",it_companies)
print('jion with #:  ',' # '.join(it_companies))
print('facebook in the it_companies list: ','Facebook' in it_companies)

it_companies.sort()
print('sort list: ',it_companies)

it_companies.sort(reverse=True)
print('descending order: ',it_companies)

print('first 3 companies from the list: ',it_companies[:3])
print('last 3 companies from the list: ',it_companies[-3:])
print('middle :' ,it_companies[(len(it_companies)-1)//2])

it_companies.pop(0)
print('Remove the first IT company from the list: ',it_companies)

it_companies.pop((len(it_companies)-1)//2)
print('Remove the middle IT company from the list: ',it_companies)

it_companies.pop()
print('Remove the last IT company from the list: ',it_companies)

it_companies.clear()
print('Remove all IT companies from the list: ',it_companies)

del it_companies
#print('Remove all IT companies from the list: ',it_companies)

#26
#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

print(f'front_end : {front_end} \n backend: {back_end} \n full_package : {full_stack} \n')
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index+1,'Python')
full_stack.insert(redux_index+2,'SQL')
print('insert Python and SQL after Redux ',full_stack,'\n')

print("\"\"Exercises: Level 2\"\"\n")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sorting
ages.sort()
min_age = min(ages)
max_age = max(ages)
print('max age :',max_age,' ',ages[-1])
print('min age :',min_age,' ',ages[0])
#Add the min age and the max age again to the list
ages.insert(0,19)
ages.insert(-1,26)
print('Add the min age and the max age again to the list: ',ages)


#Find the median age (one middle item or two middle items divided by two)
print('lenghth: ',len(ages))
middle_from_start = ages[(len(ages)-1)//2]
reversed = ages.copy()
reversed.reverse()
middle_from_end = reversed[(len(reversed)-1)//2]
print('Ascending : ',middle_from_start,',  Descending: ',middle_from_end)
print('Median = ',(middle_from_end+middle_from_start)//2,'\n')

#Find the average age (sum of all items divided by their number )
mean = sum(ages)/len(ages)
print('mean = ',mean,'\n')

#RAnge
range_ages = ages[-1] - ages[0]
print('Range= ',range_ages,'\n')

#Compare the value of (min - average) and (max - average), use abs() method
min_avg= abs(ages[0]-mean)
max_avg = abs(ages[-1]-mean)
print('Compare the value of (min - average) and (max - average): ')
print('min_avg: ',min_avg)
print('max_avg: ',max_avg,'\n')


