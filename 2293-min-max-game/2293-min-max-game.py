class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n=len(nums)
        while n!=1:
            ch=True
            i=0
            while i<=(n//2)-1:
                if ch:
                    if nums[i]>nums[i+1]:
                        del nums[i]
                    else:
                        del nums[i+1]
                    # del max(nums[i],nums[i+1])
                    ch=False
                else:
                    if nums[i]>nums[i+1]:
                        del nums[i+1]
                    else:
                        del nums[i]
                    # del min(nums[i],nums[i+1])
                    ch=True
                i+=1
            # print(nums)
            n=len(nums)
            
        return nums[0]