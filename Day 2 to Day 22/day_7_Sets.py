it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('length IT companies: ',len(it_companies),'\n')

it_companies.add('Twitter')
print("Added Twitter: ",it_companies,'\n')

new_it = ['Tesla','Bitcoin','Ali Baba']
it_companies.update(new_it)
print('added new it comapnies: ',it_companies,'\n')

it_companies.remove("Ali Baba")
print('removed Ali Baba: ',it_companies,'\n')

print('Discard: ',it_companies.discard("Kowope"),'\n')

print('A :',A)
print("B :",B)
print('Join A nd B: ',A.union(B),'\n')

print(' A intersection B: ',A.intersection(B),'\n')

print('Is A subset of B: ',A.issubset(B),'\n')

print('Are A and B disjoint sets: ',A.isdisjoint(B),'\n')


print('A :',A)
print("B :",B)
print('What is the symmetric difference between A and B: ',A.symmetric_difference(B),'\n')

del A,B

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print('Ages:',age)
print("lenght age_list :",len(age))
print('lenght age_set: ',len(set(age)),'\n')

#I am a teacher and I love to inspire and teach people.
#  How many unique words have been used in the sentence?
#  You did not learn loops yet you can do it manually
sentence ='I am a teacher and I love to inspire and teach people.'
sentence = sentence.strip('.')
sentence = sentence.split(' ')

print('Sentence : ',sentence)
print("Unique :",set(sentence))
print('lenght of sentence: ',len(set(sentence)),'\n')


