#1
"""
Python has the module called statistics 
and we can use this module to do all the statistical calculations.
 However, to learn how to make function and reuse function let us try to develop a program,
  which calculates the measure of central tendency of a sample (mean, median, mode)
   and measure of variability (range, variance, standard deviation).
    In addition to those measures, find the min, max, count, percentile,
     and frequency distribution of the sample.
      You can create a class called Statistics 
      and create all the functions that do statistical calculations 
      as methods for the Statistics class. Check the output below.

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist())
"""
class Stats():
    def __init__(self,numbers):
        self.numbers = numbers
    def count(self,):
        return len(self.numbers)
    def sum(self):
        return sum(self.numbers)
    def min(self):
        return min(self.numbers)
    def max(self):
        return max(self.numbers)
    def range(self):
        return self.max() -self.min()
    def mean(self):
        return self.sum()/self.count()
    
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Stats(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14    
print('Mean: ', data.mean()) # 30

#2
"""
Exercises: Level 2
Create a class called PersonAccount.
 It has firstname, lastname, incomes, expenses properties
  and it has total_income, total_expense, account_info, add_income, add_expense
   and account_balance methods.
    Incomes is a set of incomes and its description.
     The same goes for expenses.
"""
print('\n 2. Create a class called PersonAccount\n')
class PersonAccount():
    def __init__(self,firstname,lastname):
        self.firstname = firstname 
        self.lastname = lastname
        self.incomes = {} 
        self.expenses_properties = {}

    def total_income(self,):
        total_i = 0
        if len(self.incomes) !=0:
            for key,value in self.incomes.items():
                total_i+=int(value)
        return total_i

    def total_expense(self,):
        total_e = 0
        if len(self.expenses_properties) != 0:
            for key,value in self.expenses_properties.items():
                total_e+=int(value)
        return total_e


    def account_info(self,):
        print(f'\nAccount Info of {self.firstname}\n')
        print(f'Fullname:\t{self.firstname}\t{self.lastname}')
        print(f'Total Income:\t${self.total_income()}')
        print(f'Total Expense:\t${self.total_expense()}')

        
    def add_income(self,key,value):
        if key in self.incomes.keys(): # insurance
            self.incomes[key]+=value
        else:
            self.incomes[key] = value
        print(f'Income added sucessfully >>> {key} : {value}')
    
    def add_expense(self,key,value):
        if key in self.expenses_properties.keys(): # insurance
            self.expenses_properties[key]+=value
        else:
            self.expenses_properties[key] = value
        print(f'Expense added sucessfully >>> {key} : {value}')

    def account_balance(self):
        return self.total_income() - self.total_expense()

A = PersonAccount('Ridwan','Abdulkareem')
#print('type :',type(A),'\n')
A.account_info()
print('Account_Balance : ',A.account_balance(),'$')
A.add_income('skillz',50000)
A.add_income('Pops',10000)
A.add_income('sultana',20000)
A.add_income('salary',5000)
A.add_income('salary',5000)
A.add_expense('rent','2000')
A.add_expense('tax','2000')
A.add_expense('light','1000')
A.add_expense('hoes','1000')
A.add_expense('crypto','2000')
A.add_expense('USDT','2000')


print('\n<<< Incomes and Expenses Analysis >>>\n')
print(':::::::::Incomes:::::::')
for key,value in A.incomes.items():
    print(key,'\t:\t',value,'\n')
print(':::::::::Expenses:::::::')
for key,value in A.expenses_properties.items():
    print(key,'\t:\t',value,'\n')
A.account_info()
print('Account_Balance : ',A.account_balance(),'$')
