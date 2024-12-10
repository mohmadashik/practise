def sum(a=5,b=8):
    # second()

    print(b)

def second():
    print('second')

# sum(b=23)

try:
    print(0/0)
    sum(b=90)
except Exception as err:
    print('error')
    raise

sum(b=37439)