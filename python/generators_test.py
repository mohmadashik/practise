#write a generator function to generate fibonacci sequence

def fibonacci(n):
    a,b= 0,1
    print('1 : ',0)
    i = 1
    while i<n:
        a,b = b,a+b
        print(i+1, ' : ',b)
        i+=1

fibonacci(20)

def gen_fibonacci(n):
    a,b = 0,1
    i=1
    while i<n:
        yield a+b
        a,b = b,a+b
        i+=1
for num in gen_fibonacci(20):
    print("""Now i'm in between the time of called function gen_fibonacci, so usually when you call the function again
          you will not start from the old state. since you have kept yield instead of return,
          it is starting from the old values of a,b in their last called state and continuing with them only.
          this is called state retention
          I may not see memory efficiency or faster performance here for 20 fib but you know... this will help in larger 
          pipelines of streams of data processing.""")
    print(num)