class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            # print(i,ch)
            for other in strs:
                # print(other)
                if other[i] != ch:
                    return shortest[:i]
        return shortest 