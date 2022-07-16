class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: 
            return False
        left = 0
        right = len(arr) - 1
        # while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]: 
        #     l += 1
        # while r - 1 > 0 and arr[r] < arr[r - 1]: 
        #     r -= 1
        # return l == r
    
        
        while left < right:
            if arr[left] < arr[left + 1]:
                left += 1
            elif arr[right - 1] > arr[right]:
                right -= 1
            else:
                break
            
        if left==right and (left>0 and right<len(arr)-1):
            return True
        return False
            