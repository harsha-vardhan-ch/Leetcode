class Solution:
    def calPoints(self, ops: List[str]) -> int:
        r = []
        for op in ops:
            if op == 'C':
                r.pop()
            elif op == 'D':
                r.append(r[-1] * 2)
            elif op == '+':
                r.append(r[-1] + r[-2])
            else:
                r.append(int(op))
        return sum(r)