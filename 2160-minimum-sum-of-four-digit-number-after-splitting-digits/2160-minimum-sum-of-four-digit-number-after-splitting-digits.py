class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(map(int,str(num)))
        num.sort(reverse=True)
        print(num)
        return num[0] + num[1] + num[2]*10 + num[3]*10
        