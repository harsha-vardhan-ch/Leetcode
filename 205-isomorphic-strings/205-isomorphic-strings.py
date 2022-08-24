class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i, key in enumerate(s):
            print(i,key)
            d1[key] = d1.get(key, []) + [i]
        for i, key in enumerate(t):
            d2[key] = d2.get(key, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())