# class Solution:
#     def findAnagrams(self, s: str, p: str):
#         result = []
#         k = len(p)
#         n = len(s)
#         p_set = set(p)
#         for i in range(n-k+1):
#             cur_set = set(s[i:i+k])
#             if cur_set == p_set:
#                 result.append(i)
#         return result

class Solution:
    def findAnagrams(self, s: str, p: str):
        result = []
        k = len(p)
        n = len(s)
        p_map = {}
        for i in p:
            p_map[i]= 1+p_map.get(i,0)

            # if i in p_map:
            #     p_map[i]+=1
            # else:
            #     p_map[i]=1
        print('p_map',p_map)
        print()
        cur_s_map = {} 
        for i in range(n-k+1):
            print(f's[i-1({i-1})] {s[i-1]}')
            cur_s_map.pop(s[i-1],None)

            for j in range(k):
                if s[i+j] in cur_s_map:
                    cur_s_map[s[i+j]]+=1
                else:
                    cur_s_map[s[i+j]]=1
            print(cur_s_map)
            if cur_s_map == p_map :
                result.append(i)
        return result
    
sol_obj = Solution()
s = 'cbaebabacd'
p='abc'
res = sol_obj.findAnagrams(s,p)
print(res)
