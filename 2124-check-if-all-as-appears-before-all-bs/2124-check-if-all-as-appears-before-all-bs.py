class Solution:
    def checkString(self, s: str) -> bool:
        rs = s.rstrip('b')
        for i in rs:
            if i == 'b':
                return False
            
        return True