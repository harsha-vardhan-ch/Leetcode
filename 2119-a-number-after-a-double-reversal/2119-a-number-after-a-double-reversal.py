class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s1 = str(num).rstrip("0")
        if s1=="":
            return True
        # print(s1)
        return s1 == str(num)