class Solution:
    def countAsterisks(self, s: str) -> int:
        if '|' not in s:
            return s.count('*')
        s = s.split('|')
        # print(s[0::2])
        return sum([i.count('*') for i in s[0::2]])