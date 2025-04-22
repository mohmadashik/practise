"""
Given a string S, find the longest substring P that is lexicographically greater than S. 
Sample:  
"banana" -> "nana" 
"apple" -> "pple" 

"""

line = "banana"
line = 'apple'
line = 'asdfaa'
line = 'thgyfh'
line = 'acbcbcacbda'

start = None
for i in range(len(line)) :
    if ord(line[i]) > ord(line[0]):
        start =i 
        break 

occurences = [0,start]
for i in range(start+1,len(line)):
    if line[i] == line[start]:
        occurences.append(i)

print(occurences)
result_start = start 

result_start = occurences[0]
max_string  = ''
for i in range(len(occurences)) :
    if line[occurences[i]:] >= max_string:
        result_start = occurences[i]
        max_string = line[occurences[i]:]

print(line[result_start:])




# for left in range(len(occurences)-1):
#     right = left + 1 
#     i = occurences[left] 
#     j = occurences[right]

#     while i < len(line) and j < len(line):
#         if line[i]>= line[j]:
#             i+=1
#             j+=1
#             result_start = left 
#         else :
#             result_start = right 
#             break 

# print(line[result_start:])






# print(line[start:])