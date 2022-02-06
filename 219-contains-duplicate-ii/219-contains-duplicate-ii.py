class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        '''for i in range(len(nums)):
            print(nums[i],d)
            if nums[i] not in d:
                d[nums[i]]=i
            else:
                j=d[nums[i]]
                if abs(i-j) <=k:
                    return True
                else:
                    d[nums[i]]=i
        '''           
        for i,v in enumerate(nums):
            if v in d and abs(i-d[v])<=k:
                return True
            d[v]=i
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''index_dict = {}

        for i in range(len(nums)):

            
            if nums[i] not in index_dict:
                index_dict[nums[i]] = i

            # If the element is present in the dict,
            # then the current one is a duplicate
            else:

                # Return true if the diff between the
                # current and stored indices is less than k
                if i - index_dict[nums[i]] <=k:
                    return True

                # Otherwise update stored index to latest index of the element
                else:
                    index_dict[nums[i]] = i

        
        return False'''