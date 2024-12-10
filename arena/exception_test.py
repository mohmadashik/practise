def abc ():
    print('enter into abc')
    raise Exception('manual exception')
    print('how are you')

print('hello')
abc()
print('after the abc function')