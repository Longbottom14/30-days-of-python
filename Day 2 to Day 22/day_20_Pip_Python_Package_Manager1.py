import requests
import re
#1
print('\n 1. Read this url and find the 10 most frequent words \n')
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet)
print(response)
print(response.status_code) # status code, success:200
#print(response.headers)     # headers information
#print(response.text)
romeo_text = response.text
print(type(romeo_text))
print('\n' in romeo_text)
text_list = romeo_text.split('\n')
for line in text_list[:10]:
    print(line,'\n')
def find_most_common_words(text_string):
        lines_list = text_string.split('\n')
        pattern2  = r'[^A-Za-z ]'
        """
            #cleaned = re.sub(pattern2 ,' ',lines_list[0] )
            #pattern2 = r'""+'
            #cleaned = cleaned.replace('  ',' ')
            #cleaned = cleaned.replace(' ',',')
            #cleaned= cleaned.replace(' ',',')
            #print('1st line cleaned : ',cleaned)
            #print('\n !st line crude : ',lines_list[0])
         """
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
        print('total words: ',sum(counts))
        print('different words: ',len(counts))
        print('Word Count : ',sort_list[:10],'\n')

find_most_common_words(romeo_text)