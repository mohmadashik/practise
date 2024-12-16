#SET 1
# import os
# print(os.curdir)
# print(os.listdir())
# for file in os.listdir():
#     if file.split('.')[1] =='py':
#         print(file)
# #file name, characters length, Capitalised sentence, extension in a dic
# def read_data(filename):
#     with open(filename,'r') as f:
#         data = f.read()
#     return data.capitalize()

# txt_details = []
# for file in os.listdir():
#     # if file.split('.')[1] =='txt':
#     if file.endswith('.txt'):
#         txt_details.append({
#                             'name':file,
#                             'ext':'txt',
#                             'data': read_data(file)
#                             })
# print(txt_details)

##################### SET 2###############
# print('Factorial of a number'.center(50))
# n = int(input('give me a number : '))
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
# print(f'factorial of {n} : {factorial(n)}')
# print('*'*50)
# print()
# print()
# print()

# print('*'*50)
# print('Reverse a number'.center(50))

# n = int(input('give me a number : '))

# def reverse(n):
#     rev = 0
#     while n > 0:
#         rem = n%10
#         rev = rev*10 + rem
#         n//=10
#     return rev 
# print(f'reverse of {n} is : {reverse(n)}')
# print('*'*50)

######### Set 3 ##################
#functional programming 
# map,filter, reduce, lambda funtions
# # join
# a = ['apple','gouva','mango','cherry','banana']
# all_fruits = ','.join(a)
# print('all_fruits are : ',all_fruits)

# #lambda 
# check_5_char = lambda x : x if len(x)==5 else None

# #filter
# five_letter_fruites = [x for x in filter(check_5_char,a)]
# print('fruits with five letters are : ',five_letter_fruites)

# #lambda multiple parameters
# big_number = lambda a,b,c : a if a > b and a > c else b if b>c and b>a else c
# print(big_number(1,2,3))
# print(big_number(14,2,3))
# print(big_number(14,22,3))

# #map
# def add_prefix(name):
#     return f'Star_{name}'

# names = list(map(add_prefix,input('give me a list of names : (separated by commas) \n').split(',')))
# print(names)
# #reduce
# import functools
# nums = [5,76,44,7,8,99]
# #find bigger number 
# big_number = functools.reduce(lambda a,b: a if a>b else b , nums)
# print(f'big number is : {big_number}')

##################### SET 4 ########################
#decorators
# from functools import wraps

# def check_for_zero(func):
#     @wraps(func)
#     def inner_fun(*args,**kwargs):
#         a = args[0]
#         b = args[1]
#         print(f'given numbers : {a},{b}')
#         if b ==0 :
#             print('0 cannot be used as a divider')
#             # return
#         else:
#             print('calling function ',func.__name__)
#             func(*args,**kwargs)
#     return inner_fun

# @check_for_zero
# def divider_fun(a,b):
#     print(f'{a}/{b} = {a//b}')

# divider_fun(2,0)
# divider_fun(44,3)

##################### SET 5 ########################
#date handling
# from datetime import datetime
#change 10-11-2024 to 10 November 2024

# c_date = '10-11-2024'
# input_date = datetime.strptime(c_date,'%d-%m-%Y')
# print(input_date)
# print(input_date.strftime('%d %B %Y'))


# #change 10-11-2024 to 10 Nov 2024
# c_date = '10-11-2024'
# i_date = datetime.strptime(c_date,'%d-%m-%Y')
# print(i_date)
# print(i_date.strftime('%d %b %Y'))
# #change 10-11-2024 to 11 October 2024
# c_date = '10-11-2024'
# i_date = datetime.strptime(c_date,'%m-%d-%Y')
# print(i_date)
# print(i_date.strftime('%d %B %Y'))

# #change 10-11-2024 to 11/10/24
# print(i_date.strftime('%d/%m/%y'))

# #change 10-11-2024 to 11-Oct-24
# print(i_date.strftime('%d-%b-%y'))


##################### SET 6 ########################
#list comprehension
a = [1,2,3,3,4,6,5,5,5,55,66,64]
unique_list = [x for x in a if a.count(x)==1]
print(unique_list)

#string slice

#how are you - print in reverse

s1 = 'how are you'
print(s1[-1::-1])

