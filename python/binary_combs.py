from itertools import product
def hasAllCodes( s: str, k: int) -> bool:
    binary_combs = {''.join(bits):1 for  bits in product('01',repeat=k)}
    total_combs = len(binary_combs)
    print('total_combs ',total_combs)
    cur_str = s[:k]
    res= binary_combs.pop(cur_str,None)
    num_pops =0
    if res:
        num_pops+=1
    for i in range(1,len(s)):
        binary_combs.pop(s[i:i+k],None)
        if res:
            num_pops+=1
        if num_pops == total_combs:
            return True
    return len(binary_combs) == 0

s = '0110'
k =2
print(hasAllCodes(s,k))
