from collections import defaultdict
freq = defaultdict(int)
print(freq)
freq['s'] = 534
print(freq)
freq['s'] = '534'
print(freq)
freq['h']= freq.get('h',0)+1
print(freq)
