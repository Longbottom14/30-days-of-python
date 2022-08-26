#from ast import pattern
from itertools import count
import re

#What is the most frequent word in the following paragraph?
print('\n 1. What is the most frequent word in the following paragraph?\n')
word_count = []
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph_list = paragraph.strip('.').split(' ')
for string in paragraph_list:
    matches = re.findall(string,paragraph,re.I)
    word_count.append((string,len(matches)))
print(set(word_count))

#2
sentence = 'The position of some particles on the horizontal x-axis -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
print(f'\n 2. {sentence}\n ')
regex_pattern = r'[+-]\d+|\d+'
matches = re.findall(regex_pattern,sentence)
matches=[int(i) for i in matches]
print('points :',matches)
matches.sort()
print('sorted list : ',matches)
print('distance : ',matches[-1]-matches[0])

#3
print('\n 3. Write a pattern which identifies if a string is a valid python variable\n')
def is_valid_variable(variable):
    pattern = r'^[A-Za-z_]' # variable must not be a number
    pattern2 = r'-' #hyphen
    match = re.match(pattern,variable)
    if match == None:
        return False
    else:
        match = re.findall(pattern2,variable)
        return match == []

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname'))

#4
print('\n 4. Clean the following text. After cleaning, count three most frequent words in the string.\n')
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(sentence):
    pattern2  = r'[^A-Za-z ]'
    cleaned = re.sub(pattern2 ,'',sentence )
    return cleaned
print(clean_text(sentence))

def most_frequent_words(clean_text):
    clean_text_list = clean_text.split(' ')
    count_list = []
    for word in clean_text_list:
        match = re.findall(word,clean_text,re.I)
        tpl = (len(match),word)
        if tpl in count_list:
            continue
        else:
            count_list.append(tpl)
    count_list.sort(reverse=True)
    return count_list[:3]
cleaned_text = clean_text(sentence)
print(most_frequent_words(cleaned_text))