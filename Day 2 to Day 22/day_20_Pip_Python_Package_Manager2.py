#2
"""
Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
    1. the min, max, mean, median, standard deviation of cats' weight in metric units.
    2. the min, max, mean, median, standard deviation of cats' lifespan in years.
    3. Create a frequency table of country and breed of cats
"""
from itertools import count
from operator import concat
import requests
import re
import json
from math import *
import statistics as stat


print('\n 2. Read this api and perform escriptive analysis \n')
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
print(response)
print(response.status_code) # status code, success:200
#print(response.headers)     # headers information
#print(response.text)
cat_json = response.json()
def descriptive_analysis(extracted_json):
    weight_list = []
    life_span_list =[]
    for cat_dict in extracted_json:
        weight_dict =  cat_dict['weight']
        metric_range = weight_dict['metric']
        lower_limit , upper_limit = metric_range.split('-')
        average_metric_weight = (int(lower_limit) +int(upper_limit))/2
        weight_list.append(average_metric_weight)

        life_span_range = cat_dict['life_span']
        lower_limit , upper_limit = life_span_range.split('-')
        average_life_span = (int(lower_limit) +int(upper_limit))/2
        life_span_list.append(average_life_span)

    print('\tDescriptive Analysis of Cat metric weight \n')
    print('\t\t\tCat MIN metri_weight : ',min(weight_list),'\n')
    print('\t\t\tCat MAX metri_weight : ',max(weight_list),'\n')
    print('\t\t\tCat MEAN metri_weight : ',stat.mean(weight_list),'\n')
    print('\t\t\tCat MEDIAN metri_weight : ',stat.median(weight_list),'\n')
    print('\t\t\tCat STD metri_weight : ',stat.stdev(weight_list),'\n')

    
    print('\tDescriptive Analysis of Cat life span \n')
    print('\t\t\tCat MIN life_span : ',min(life_span_list),'\n')
    print('\t\t\tCat MAX life_span : ',max(life_span_list),'\n')
    print('\t\t\tCat MEAN life_span : ',stat.mean(life_span_list),'\n')
    print('\t\t\tCat MEDIAN life_span : ',stat.median(life_span_list),'\n')
    print('\t\t\tCat STD life_span : ',stat.stdev(life_span_list),'\n')
descriptive_analysis(extracted_json=cat_json)

print('==============================================================')

print('\n Create a frequency table of country and breed of cats \n')

def Create_frequency_table(extracted_json):
    #country
    #       (breed1,freq)
    #       (breed2,freq)
    country_list = []
    breed_list =[]
    country_key_breed_list = {}
    country_concate_breed = []
    count=0
    for cat_dict in extracted_json:
        cat_country = cat_dict["origin"]
        cat_breed = cat_dict["name"]
        concat_c_b = cat_country+'_'+cat_breed
        country_concate_breed.append(concat_c_b)
        country_list.append(cat_country)
        if cat_country in country_key_breed_list.keys():
            country_key_breed_list[cat_country] += []+[cat_breed]#','+cat_breed
        else:
                country_key_breed_list[cat_country]=[cat_breed]#cat_breed
        count+=1
        breed_list.append(cat_breed)
    country_list = set(country_list)
    breed_list = set(breed_list)
    """for concated in country_concate_breed:
        if concated  in country_key_breed_list.keys():
            country_key_breed_list[concated] += 1
        else:
            country_key_breed_list[concated]=1
            """
    
    print('No of cats:',count,'\n')
    print('Total Number of Countries: ',len(country_list),'\n')
    print('Total Number of breeds: ',len(breed_list),'\n')
    print('Concat list :',country_concate_breed[:10],'\n')
    print('con  brreed list: ',country_key_breed_list)
    print('country\tbred_list\tNumber of breeds\n')
    for key in country_key_breed_list.keys():
        print(f'{key}\t{country_key_breed_list[key]}\t{len(country_key_breed_list[key])}\n')
Create_frequency_table(extracted_json=cat_json)       
        


