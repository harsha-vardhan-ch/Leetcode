class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, ans, suffix_prod = len(nums), [1]*len(nums), 1
        pre=[1]*len(nums)
        post=[1]*len(nums)
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i]
        post[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            post[i]=post[i+1]*nums[i]

            #ans[i] *= suffix_prod
            #suffix_prod *= nums[i]
        for i in range(1,n-1):
            ans[i]=pre[i-1]*post[i+1]
        ans[0]=post[1]
        ans[-1]=pre[-2]
        print(pre,post)
        return ans
        