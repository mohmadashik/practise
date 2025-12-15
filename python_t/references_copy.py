import copy
#deep copy
print('deep copy')
a = [[1,2,3],[4,5,6]]

b = copy.deepcopy(a)

b[0][0] = 898

print(a)
print(b)  
#deep copy creates completely independent object including all the nested elements
'''
nested elements of the original list are recursively duplicated to ensure even 
deeply nested objects are entirely independent in the copied set
'''

print('shallow copy')

#shallow copy
c = copy.copy(a)

c[0][0] = 565

print(a)
print(c)
'''
shallow copy only copies the outer structure of the list to the new list and
retains the original nested elements in the second list. so any changes to the nested elements 
in the copied list will also affect the original list
'''
print('what if we change the structure of the copied list in shallow copy? copy.copy()')

c.append([8,8,8])

print(a)
print(c)
'''
so when we change the structure the newly added elements are not original nested elements
of the original list. so those new elements are not added in the original list.
'''
print('''what if we change the nested elements now in shallow copied object after some new elements 
have been added to it?)
''')
c[0][1] = 9999
print(a)
print(c)
'''
even though we have altered the structure of the copied list, the existing inner elements are 
still having the reference of the original list nested objects/elements.
so the changes to the nested objects in duplicated list(even after its structure is different from original list)
are affecting the nested elements of the original list
'''

print('lets do the copies without the copy.deepcopy() or copy.copy()')

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
arr3 = arr1
arr4 = arr2
arr3[0]=89
arr4.append(89)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print('currently there are no nested elements. this copy is working as shallow copy.')

arr1.append([89898,9839453])
print(arr1)
print(arr3)
print('still the arr1 and arr3 are in sync. the arr3 is getting the new values added to the arr1. let us reverse this')
arr3.append([1000,12345])
print(arr1)
print(arr3)
print('even the changes to the structure of arr3 are also affecting the structure of arr1.')
print('this cannot be copy.copy() or copy.deepcopy(). what copy is this ?')
print('this is not a copy at all, this is just a reference assignment. using = operator we are just assigning the reference of arr1 to arr3')
'''
In a reference assignment, both variables refer to the same object in memory,
meaning they are not independent. Any changes made to one variable will directly affect the other.
This differs from shallow or deep copies, where new objects are created, and changes to one do not affect the other.
'''


print('\n\n\n\n\n\nlet us see the working in dict')
d1 = {1:'hello',2:'red'}
d2 = d1
d2[3] = 'yellow'
print(d1)
print(d2) #same behaviour as list.

print("let's see new code snippets ")
a = [1, 2, 3]
b = a
b[1] = 999
a.append(4)
b.append(5)
print(a)
print(b)
print("i'm guessing both a,b are going to be the same")
#i'm correct
print("let's see code 2")
x = [10, 20]
y = x
x = [30, 40]  # Reassigning x
y.append(50)
print(x)
print(y)
print('here y should be [10,20,50] and x should be [30,40]')
#i'm correct. why ? because x reference has entirely changed in this code snippet
# so the y maintained the reference of y as it is.

print('code 3')
p = [[1, 2], [3, 4]]
q = p
q[0][1] = 999
p[1] = [5, 6]
q.append([7, 8])
print(' i think p and q should differ now')
print(p)
print(q)
# p should be [ [1,999],[5,6]]
# q should be [[1,999],[3,4],[7,8]]
# because whenever we are assigning the p[1] = [5,6], the reference to [3,4] is detached
# from p and I think it should force python to create the separate copied object for q. now q has became independent
#let's see whether i'm correct or not
print("I'M WRONG... if you don't use copy.copy() or copy.deepcopy() whatever you do will affect both lists \
      because this is just a reference assignment. except in the case we are totally changing the reference of the root object")

print('\n\n\n code 4')
u = [100, 200]
v = u
v = v + [300]  # This creates a new object for v
print('so u and v should be different now')
u.append(400)
print(u)
print(v)
print("we are correct")

print('\n\n\n code 5')
m = [1, 2, 3]
n = m
n += [4, 5]  # This modifies n in place
print("I think n and m should be the same")
print(m)
print(n)

# correct again
"""
why ? n+= [4,5] here it is adding [4,5] to n without creating a new object . += operator object modifies the object in place , 
v = v + [300] here it is adding v+ [300] by creating a new object and assigning this to v. + operator creates a new object entirely
so, the v no longer is pointing to the  reference of u.
"""

