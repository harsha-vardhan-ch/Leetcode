class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''
        App 1 - BruteForce
        T.C - O(m.n)
        S.C - O(1)
        '''
        # res=[]
        # for i in nums1:
        #     suc=0
        #     k=nums2.index(i)
        #     for j in range(k,len(nums2)):
        #         if nums2[j]>i:
        #             res.append(nums2[j])
        #             suc=1
        #             break
        #     if suc==0:
        #         res.append(-1)
        # return res
        
        '''
        App 2 - Better BruteForce
        T.C - O(m.n)
        S.C - O(n)
        '''
        # d={}
        # for ind,val in enumerate(nums2):
        #     d[val]=ind
        # # print(d)
        # res=[]
        # for i in nums1:
        #     suc=0
        #     k=d[i]     // Optimized retrieval here
        #     for j in range(k,len(nums2)):
        #         if nums2[j]>i:
        #             res.append(nums2[j])
        #             suc=1
        #             break
        #     if suc==0:
        #         res.append(-1)
        # return res
    
        '''
        App 3 - Stack
        '''
        r=[-1]
        d={}
        for i in range(len(nums2)):
            # print(r[-1],nums2[i])
            while len(r)>0 and nums2[i]>r[-1]:
                d[r.pop()]=nums2[i]
            r.append(nums2[i])
        while len(r)>0:
            d[r.pop()]=-1
        # print(d)
        res=[]
        for i in nums1:
            res.append(d[i])
        return res