a = [1,2,3,4,5]
print(a)
a.append(89)
print(a)

a.insert(2,20000) # first param is index, second value
print(a)

a.remove(2) #for removing value
print(a)

a.pop() #for removing last index 
print(a)
a.pop(2) #for removing the 2nd index
print(a)

# a.pop(8,99999) TypeError pop has only argument which should be a valid index for lists


b = {1:89,2:8,3:9090,4:289342}
for key,value in b.items():
    print(f'key : value =  {key} : {value}')
res = b.pop(189,'Value Not Found')
print(res)
c = {6:343,7:343}
d = {**b,**c}
print(d)

tup2 = (1,4,5,57,7,77,8676,454,8)
# tup2.pop() # AttributeError tuple object has no attribute pop

print(tup2[3])
tup3 = tup2[::2]
print(tup3)
