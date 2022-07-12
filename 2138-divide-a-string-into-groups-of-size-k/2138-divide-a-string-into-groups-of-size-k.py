class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s)%k!=0:
            s=s+ fill * (k-(len(s)%k)) 
        h = [s[i:i+k] for i in range(0,len(s),k)]
        return h