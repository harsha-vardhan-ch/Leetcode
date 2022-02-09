class Solution:
    def frequencySort(self, s: str) -> str:
        dic=Counter(s) 
        ans=""
        for k, v in dic.most_common():
            print(k,v)
            ans+=k*v
        return ans