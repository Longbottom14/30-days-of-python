print([x for  x in range(10,-1,-1)])

w=10
while w >=0:
    print(w)
    w=w-1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
 
for row in range(6):
    print('#'*row)

#Use nested loops to create the following:
# # # # # # # #  (0,0) ,(0,1),(0,2),(0,3)....(0,col)
# # # # # # # #   (1,0)
# # # # # # # #    (2,0)
# # # # # # # #     .
# # # # # # # #     .
# # # # # # # #     .
# # # # # # # #     .
# # # # # # # #     (row,0)
print("\n nested \n")
rows =8
cols = 6
for row in range(rows):
    #for col in range(cols):
        print('#'*cols)
#5
print('\n pattern \n')
x=10
y=10
for x_ in range(x):
    print(f'{x_} x {x_} = {x_*x_}')

#6
print('\n skillz \n')
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)

#7
print('\n Use for loop to iterate from 0 to 100 and print only even numbers \n')
for i in range(101):
    if i%2 == 0 and i > 0:
        print('even no : ',i)

#9
print("\n Use for loop to iterate from 0 to 100 and print the sum of all numbers. \n")
total_all=0
for i in range(101):
    total_all=total_all+i
print('Total sum : ',total_all)

#10
print('\n Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.\n')
total_even=0
total_odd=0
for i in range(101):
    if i%2 == 0 and i > 0:
        total_even+=i
    else:
        total_odd +=i
print('Even : ',total_even,"  odd: ",total_odd)

#12
print('\n This is a fruit list, [banana, orange, mango, lemon] reverse the order using loop \n')
fruits = ['banana', 'orange', 'mango', 'lemon']
reverse = []
for i in range(len(fruits)-1,-1,-1):
    reverse.append(fruits[i])
print('reversed with for :',reverse)
r = fruits.reverse()
print('with function:',r)

