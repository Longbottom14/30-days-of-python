"""total_count = 0
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
"""    
arr = [0,1,2,3,4,5,6,7,8,9,10]
print(arr[::-1])
print(arr[::-1][:5])
print(arr[-5:])
