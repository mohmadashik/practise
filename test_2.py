def even_numbers():
    for i in range(2,10,2):
        yield i 

number = iter(even_numbers())
print(next(number))
print(next(number))
print(next(number))
# Write a function to multiply 2 numbers without using loops and * , /
# print(eval('+4'*5))

x,y = 3,-5 
x,y = -5,3 

# x,y = -5,-3

def multiply(a,b):
    if a ==0 or b == 0:
        return 0
    negative_result = 1
    if a<0 or b< 0:
        negative_result = -1
        if a<0:
            a = a* -1
        if b < 0:
            b = b* -1
   
    if b == 1:
        return a
    else:
        return negative_result*(multiply(a,b-1)+a)

print(multiply(x,y))