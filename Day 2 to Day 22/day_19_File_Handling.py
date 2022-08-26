#1
"""
    Write a function which count number of lines and number of words in a text.
    All the files are in the data the folder: 
    a) Read obama_speech.txt file and count number of lines and words 
    b) Read michelle_obama_speech.txt file and count number of lines and words 
    c) Read donald_speech.txt file and count number of lines and words 
    d) Read melina_trump_speech.txt file and count number of lines and words

    line Count :  66
    Word Count :  13276
"""
from functools import reduce
from genericpath import isdir
import os
import re
from turtle import title
import json
import csv

print('\n 1.count_number_of_lines_and_words \n')
def count_number_of_lines_and_words(path_):
    pp='i love'
    title =str(path_)
    title =  title.split('/')
    with open(path_) as f:
        all_lines = f.read().splitlines()
        #print(type(all_lines))
        #print(all_lines)
        #all_lines.remove('')
        no_lines = len(all_lines)
        word_count = 0
        for line in all_lines:
            word_count += len(line)
        print('Text: ',title[-1])
        print('Line Count : ',no_lines)
        print('Word Count : ',word_count,'\n')

path_obama = './Day_2/data/obama_speech.txt'
count_number_of_lines_and_words(path_obama)
text_paths = []
data_dir= './Day_2/data/' #'C:\\Users\\user\\Solo Dolo\\30 Days of Python\\Day_2\\data'
for entry in os.scandir(data_dir):
    #if  entry.isdir():
        text_paths.append(entry.path)
print(text_paths)
for path_ in text_paths:
    if '.txt' in path_:
        count_number_of_lines_and_words(path_)

#2
"""
    Read the countries_data.json data file in data directory, 
    create a function that finds the ten most spoken languages

    # Your output should look like this
    print(most_spoken_languages(filename='./data/countries_data.json', 10))
    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic'),
    (24, 'Spanish'),
    (9, 'Russian'),
    (9, 'Portuguese'),
    (8, 'Dutch'),
    (7, 'German'),
    (5, 'Chinese'),
    (4, 'Swahili'),
    (4, 'Serbian')]

    # Your output should look like this
    print(most_spoken_languages(filename='./data/countries_data.json', 3))
    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic')]
"""
print('\n 2. most_spoken_languages \n')
def most_spoken_languages(file_name,number):
    with open(file_name,'r',encoding='utf-8') as f:
        json_dict = json.load(f)
        #def wrapper(name_key,criteria,descending=False):
            #sort_dict = function(name_key,criteria,descending=False)
        language_dict = {}
        for country_data in json_dict:
            for language in country_data['languages']:
                if language in language_dict.keys():
                    language_dict[language] +=1
                else:
                    language_dict[language] = 1
        sort_list = [(value,key) for key,value in language_dict.items()]
        sort_list.sort(reverse=True)
        output_list = [(tpl[1],tpl[0]) for tpl in sort_list]
        return output_list[:number]
print(most_spoken_languages(file_name='./Day_2/data/countries_data.json', number=10),'\n')
print(most_spoken_languages(file_name='./Day_2/data/countries_data.json', number=3),'\n')

#3
"""
    Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

    # Your output should look like this
    print(most_populated_countries(filename='./data/countries_data.json', 10))

    [
    {'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000},
    {'country': 'Indonesia', 'population': 258705000},
    {'country': 'Brazil', 'population': 206135893},
    {'country': 'Pakistan', 'population': 194125062},
    {'country': 'Nigeria', 'population': 186988000},
    {'country': 'Bangladesh', 'population': 161006790},
    {'country': 'Russian Federation', 'population': 146599183},
    {'country': 'Japan', 'population': 126960000}
    ]

    # Your output should look like this

    print(most_populated_countries(filename='./data/countries_data.json', 3))
    [
    {'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000}
    ]
"""
print('\n 3. most_populated_countries \n')
def most_populated_countries(filename,number):
   with open(filename,'r',encoding='utf-8') as f:
        json_dict = json.load(f)
        sorter = []
        for country_data in json_dict: # country_data= dict
            sorter.append((country_data['population'],country_data['name']))
        sorter.sort(reverse=True)
        output = [{'country': tpl[1],'population': tpl[0]}for tpl in sorter]
        return output[:number]
print(most_populated_countries(filename='./Day_2/data/countries_data.json', number=10),'\n')
print(most_populated_countries(filename='./Day_2/data/countries_data.json', number=3),'\n')

#Exercises: Level 2
#4
print('\n 5. Extract all incoming email addresses as a list \n')
"""Extract all incoming email addresses as a list from the email_exchange_big.txt file."""
def Extract_all_incoming_email_addresses(filename):
    with open(filename) as f:
        all_lines = f.read().splitlines()
        print('Printing lines:\n')
        for line in all_lines[:10]:
                print(line,'\n')
        current_line = 0
        pattern_mail = r'.edu$'
        brackets = r'(|)'
        outside=[]
        for line in all_lines:
            tokens = line.split(' ')
            for token in tokens:
                match = re.findall(pattern_mail,token)
                if match != []:
                    no_bracket = re.sub('[()]','',token)
                    outside.append(no_bracket)
        outside = set(outside)
        """
        for mail in outside:
            print(mail,'\n')
        """
        print(outside)
        

emails_junk = './Day_2/data/email_exchange_big.txt'
Extract_all_incoming_email_addresses(filename=emails_junk)




#5
print('\n 5. find_most_common_words \n')
'''
    Find the most common words in the English language.
    Call the name of your function find_most_common_words, 
    it will take two parameters - a string or a file and a positive integer, 
    indicating the number of words. 
    Your function will return an array of tuples in descending order. 
    Check the output:
    # Your output should look like this
        print(find_most_common_words('sample.txt', 10))
        [(10, 'the'),
        (8, 'be'),
        (6, 'to'),
        (6, 'of'),
        (5, 'and'),
        (4, 'a'),
        (4, 'in'),
        (3, 'that'),
        (2, 'have'),
        (2, 'I')]

        # Your output should look like this
        print(find_most_common_words('sample.txt', 5))

        [(10, 'the'),
        (8, 'be'),
        (6, 'to'),
        (6, 'of'),
        (5, 'and')]
'''
def find_most_common_words(filename, number):
    with open(filename) as f:
        lines_list = f.read().splitlines()
        pattern2  = r'[^A-Za-z ]'
        """
        #cleaned = re.sub(pattern2 ,' ',lines_list[0] )
        #pattern2 = r'""+'
        #cleaned = cleaned.replace('  ',' ')
        #cleaned = cleaned.replace(' ',',')
        #cleaned= cleaned.replace(' ',',')
        #print('1st line cleaned : ',cleaned)
        """#print('\n !st line crude : ',lines_list[0])
        word_count = {}
        for line in lines_list:
            cleaned = re.sub(pattern2 ,' ',line )
            cleaned = cleaned.replace('  ',' ')
            cleaned = cleaned.replace(' ',',')
            words = cleaned.split(',')
            for word in words:
                word = word.lower()
                if word == '':
                    continue
                elif word in word_count.keys():
                    word_count[word]+=1
                else:
                    word_count[word]=1
        sort_list = [(value,key) for key,value in word_count.items()]
        counts = [int(value) for key,value in word_count.items()]
        sort_list.sort(reverse=True)
        title =str(filename)
        title =  title.split('/')
        print('Text: ',title[-1])
        print('total words: ',sum(counts))
        print('different words: ',len(counts))
        print('Word Count : ',sort_list[:number],'\n')
#find_most_common_words(path_obama,10)
for path_ in text_paths:
    if '.txt' in path_:
        find_most_common_words(path_,10)

"""
    total words:  2401
    different words:  887 #with lower

    total words:  2401
    different words:  923 #without lower
"""

#6
"""
Write a python application that checks similarity between two texts. 
It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
You may need a couple of functions:,
 function to clean the text(clean_text),
  function to remove support words(remove_support_words)
   and finally to check the similarity(check_text_similarity). 
   List of stop words are in the data directory
"""
def clean_text(filename):
    with open(filename) as f:
        lines_list = f.read().splitlines()
        pattern2  = r'[^A-Za-z ]'
        line_list_cleaned = []
        word_count = {}
        #word_list_cleaned = []
        for line in lines_list:
            cleaned = re.sub(pattern2 ,' ',line )
            cleaned = cleaned.replace('  ',' ')
            cleaned = cleaned.replace(' ',',')
            words = cleaned.split(',')
            if words != ['']:
                while '' in words:
                    words.remove('') #used wile loop because .remove() removs only the first occurence
                line_list_cleaned.append([ word.lower() for word in words])
        for clean_line in line_list_cleaned:
            for word in clean_line:
                if word == '':
                    continue
                elif word in word_count.keys():
                    word_count[word]+=1
                else:
                    word_count[word]=1
        word_list_cleaned = [(int(value),key) for key,value in word_count.items()]

        #for line in line_list_cleaned:
            #print(line,'\n')
        #print(word_list_cleaned[0])
        cleaned_dict ={
            'lines': line_list_cleaned,
            'words':word_list_cleaned
        }

        return cleaned_dict

stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

cleaned_dict  = clean_text(path_obama)

def remove_support_words(cleaned_dict):
    lines = cleaned_dict['lines']
    words = cleaned_dict['words']
    line_no_stop = []
    no_stop ={}
    def is_not_stop_word(word):
        if word not in stop_words:
            return True
        return False
    def add_sentences(a,b):
        return a + b
    for line in lines:
        # i used filter instead of remove  function
        """for curse in stop_words:
            while curse in line:
                line.remove(curse)
        """
        line = list(filter(is_not_stop_word,line))
        line_no_stop.append(line)
    words_no_stop = reduce(add_sentences,line_no_stop) 
    no_stop['lines'] = line_no_stop
    no_stop['words'] = words_no_stop
    return no_stop

def check_text_similarity(text1,text2):
    total_count = 0
    total_count2 = 0
    set_text1 = set(text1)
    set_text2 = set(text2)
    common_words = set_text1.intersection(set_text2)
    similarity_word_dict ={}
    similarity_word_dict2 ={}
    for word1 in text1:
        if word1 in common_words:
            total_count+=1
            if word1 in similarity_word_dict.keys():
                similarity_word_dict[word1]+=1
            else:
                similarity_word_dict[word1]=1
    sort_list1 = [(int(value),key) for key,value in similarity_word_dict.items()]
    sort_list1.sort(reverse=True)
        
    for word2 in text2:
        if word2 in common_words:
            total_count2 +=1
            if word2 in similarity_word_dict2.keys():
                similarity_word_dict2[word2]+=1
            else:
                similarity_word_dict2[word2]=1
    sort_list2 = [(int(value),key) for key,value in similarity_word_dict2.items()]
    sort_list2.sort(reverse=True)
    
    print("No of common words: ",len(common_words),'\n')
    print('ratio of common words to total words of first text: ',(total_count/len(text1))*100,'%','\n')
    print('ratio of common words to total words of second text: ',(total_count2/len(text2))*100,'%','\n')
    #print("common words: ",common_words,'\n')
    print('Top 10 common words in text 1 :',sort_list1[:10],'\n')
    print('Top 10 common words in text 2 :',sort_list2[:10],'\n')
    




melina_path = './Day_2/data/melina_trump_speech.txt'
mitchell_path = './Day_2/data/michelle_obama_speech.txt' 

cleaned_dict_melina  = clean_text(melina_path)
cleaned_dict_mitchell = clean_text(mitchell_path)

no_stop_melina = remove_support_words(cleaned_dict_melina)
no_stop_mitchell = remove_support_words(cleaned_dict_mitchell)

melina_words = no_stop_melina['words']
mitchell_words = no_stop_mitchell['words']

check_text_similarity(text1=melina_words,text2=mitchell_words)

#9
"""
Read the hacker news csv file and find out:
 a) Count the number of lines containing python or Python
  b) Count the number lines containing JavaScript, javascript or Javascript 
  c) Count the number lines containing Java and not JavaScript
"""
print('\n 9. Read the hacker news csv file\n')
import csv
hacker_csv_path = './Day_2/data/hacker_news.csv'
def read_hacker_news(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        no_of_lines =0
        python_regex = r'Python|python'
        JavaScript_regex = r'JavaScript|javascript|Javascript'
        Java_regex = r'Java'

        python_matches =[]
        Javascript_matches =[]
        Java_matches =[]

        for row in csv_reader:
            no_of_lines+=1
            match_python = re.findall(python_regex,row[1])
            if match_python!= []:
                python_matches.append(row[1])

            match_javascript = re.findall(JavaScript_regex,row[1])
            if match_javascript != []:
                Javascript_matches.append(row[1])

            sub_Javascript = re.sub(JavaScript_regex,'',row[1])# remove anything javascript
            match_Java = re.findall(Java_regex,sub_Javascript)
            if match_Java != []:
                Java_matches.append(row[1])
        print('Total Number of Lines: ',no_of_lines,'\n')
        print('number of lines containing python or Python: ',len(python_matches),'\n')
        print('number lines containing JavaScript, javascript or Javascript: ',len(Javascript_matches),'\n')
        print('number lines containing Java and not JavaScript: ',len(Java_matches),'\n')
        """
        print('\n Python matches\n')
        for match in python_matches:
            print(match,'\n')

        print('\n Java matches\n')
        for match in Javascript_matches:
            print(match,'\n')
        
        print('\n Java matches\n')
        for match in Java_matches:
            print(match,'\n')"""
        

read_hacker_news(filename=hacker_csv_path)    





"""
    print('#######################')
    print('crude _stop : ',cleaned_dict['lines'][0],'\n')
    no_stop_word = filter(is_not_stop_word,cleaned_dict['lines'][0])
    print('no stop : ',list(no_stop_word))
    print('++++++++++++++++++++++++++++++++++++++++')

cl = remove_support_words(cleaned_dict)
print('lenghth : ',len(cl['lines']))
for sw in stop_words[:5]:
    print(sw in cl['lines'],'\n')
#print(cl['lines'])
"""
"""
Find the 10 most repeated words in the romeo_and_juliet.txt
Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
Exercises: Level 3
"""



        
        
    
