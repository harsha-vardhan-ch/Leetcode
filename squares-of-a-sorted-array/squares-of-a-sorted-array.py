class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # s=0
        # e=len(nums)-1
        # r=[0]*len(nums)
        # n=e
        # for i in range(len(nums)):
        #     f=nums[s]*nums[s]
        #     k=nums[n]*nums[n]
        #     if f>k:
        #         r[e]=f
        #         s+=1
        #     else:
        #         r[e]=k
        #         n=n-1
        #     e=e-1
        #     #print(r)
        # return r
    
        result = [0]*len(A)
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[index] = A[left] ** 2
                left += 1
            else:
                result[index] = A[right] ** 2
                right -= 1
        return result