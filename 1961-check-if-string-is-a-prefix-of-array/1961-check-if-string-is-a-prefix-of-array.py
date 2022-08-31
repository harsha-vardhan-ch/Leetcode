class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        t=''
        n=len(s)
        for i in words:
            t=t+i
            if len(t)==n and t==s:
                return True
            elif len(t)>n:
                return False
        