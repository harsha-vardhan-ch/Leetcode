import math
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(math.ceil(sum(amount)/2), max(amount))
    
    
    '''
    Greedy Approach 
    - math.ceil(sum(amount)/2 => assuming there are multiple cups
    - max(amount) => assuming there is only one type of cup
    '''