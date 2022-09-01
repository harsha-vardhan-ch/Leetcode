class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # r=[]
        # d={}
        # d[nums2[-1]]=-1
        # for i in range(len(nums2)-2,-1,-1):
        #     if nums2[i]<nums2[i+1]:
        #         d[nums2[i]]=nums2[i+1]
        #     else:
        #         d[nums2[i]]=d[nums2[i+1]]
        # #print(d)
        # for i in nums1:
        #     r.append(d[i])
        # return r
        res=[]
        for i in nums1:
            suc=0
            k=nums2.index(i)
            for j in range(k,len(nums2)):
                if nums2[j]>i:
                    res.append(nums2[j])
                    suc=1
                    break
            if suc==0:
                res.append(-1)
        return res