def find_most_common_words(filename, number):
    with open(filename) as f:
        lines_list = f.read().splitlines()
        pattern2  = r'[^A-Za-z ]'
        #cleaned = re.sub(pattern2 ,' ',lines_list[0] )
        #pattern2 = r'""+'
        #cleaned = cleaned.replace('  ',' ')
        #cleaned = cleaned.replace(' ',',')
        #cleaned= cleaned.replace(' ',',')
        #print('1st line cleaned : ',cleaned)
        #print('\n !st line crude : ',lines_list[0])
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
