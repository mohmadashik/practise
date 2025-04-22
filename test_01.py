"""
program to count the occurrences of each word in a given sentence
For ex: the quick brown fox jumps over the brown box.
"""

line = "the quick brown fox jumps over the brown box"
counter = {}
for word in line.split():
    if word in counter:
        counter[word]+=1
    else :
        counter[word] = 1
# print(counter)

counter = {}
for letter in line:
    ltr = letter.lower()
    if ltr.isalpha():
        if ltr in counter:
            counter[ltr]+=1
        else :
            counter[ltr] = 1
# print(counter)

"""
i/p my $arr = (1,2,3,4,5,6,7,8,9) and o/p should be  (9,2,7,4,5,6,3,8,1)
reverse the odd indexed values and leave the even values as it is.
"""
arr = [1,2,3,4,5,6,7,8,9]
left = 1
right = len(arr)-1
output = []
while left < len(arr) or right > -1:
    output.append(arr[right])
    right-=2
    if left < len(arr):
        output.append(arr[left])
        left+=2
# print(output)


"""
Try to print Diamond of stars for n. Say if n=4 then print like below
 
"""
n = 4
i = 1
stars = 1
spaces = n - 1
while i <= n :
    # print(' '*spaces+stars*'*')
    i+=1
    stars= i*2 -1
    spaces-=1

word = 'ashik'
# print(word[-1::-1])

fruit_count  = {}
fruits = ['apple','mango','grapes']
colors = ['red','yellow','green']
for i in range(len(fruits)):
    fruit_count[fruits[i]] = colors[i]
print(fruit_count)

a = [43,5343,63534,64353,3436,43,5]
# a.sort()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j] :
            a[i],a[j] = a[j],a[i]
# print(a)
# print(a[1])

# emp
select * from 