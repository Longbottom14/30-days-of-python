from math import  *
from statistics import mean, median
import string

a=[1,2,3,4,5]
print(min(a))
print(max(a))
print(median(a))
print(mean(a))
import statistics as stat

#calculate standard deviation of list
print(stat.stdev(a))

b ={
    'a':1, 'c':2}

b['d'] = 3
print(b)

print(['annex'])
print(len([]))
a =[1,2,3]
print(len([1]))
import re
s = 'holes.mr.itd.umich.edu'
pattern_mail =r'.edu$' #r'[A-Za-z]*.edu'
match = re.findall(pattern_mail,s)
print(match)

a ={}
print(len(a))

a = [1,2,3]
print(*a)


