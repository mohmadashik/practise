def generate_numbers(n):
    for i in range(n):
        yield i

iter_obj = iter(generate_numbers(5))

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
# print(next(iter_obj))
print('why are generators used? 1. memory efficiency, 2. state retention , 3. calculating the values at runtime, 4. faster performance while large pipeline of data processing ')

a = [1,2,3,4,5,6,7,8,9,10]
iter_a = iter(a)
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))
