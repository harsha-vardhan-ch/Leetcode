class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bin(h):
            bit=0
            while h>0:
                bit+=h%2
                h=h//2
            return bit
        
        return sorted(arr,key=lambda x:(count_bin(x), x))