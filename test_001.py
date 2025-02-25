# import threading
# import request

# end_point = 'www.google.com'

# response = request.get(url=end_point,headers=[],timeout=30)

# data = response.json()
# # 
a = list(range(1,11))
# usb for 3, 5 device, usbdevice for both 3&5

def generate(start,end):
    arr = list(range(start,end))
    result = []
    for i in a:
        if i%3 ==0 and i%5==0:
            result.append(f'usbdevice {3}&{5}')
        elif i%5==0:
            result.append(f'device {5}')
        elif i%3==0:
            result.append(f'usb {3}')
    return result

def test_output():
    result = generate(0,11)
    for i in result:
        if i =='usbdevice':
           assert i.split()[1] == '3&5'
        elif i =='device':
            assert i.split()[1] =='5'
        elif i =='usb':
            assert i.split()[1]=='3'
test_output()

word = 'abc'
line = 'hlljkjlsdfabclkjlfscd'
# if word in line:
#     print('yes')

# left = 0
# right = len(line)-1

for i in range(len(line)-2):
    if line[i] == word[0] and line[i+1]==word[1] and line[i+2]==word[2]:
        print('yes')

# O(1) space complexity
# O(n) time complexity


