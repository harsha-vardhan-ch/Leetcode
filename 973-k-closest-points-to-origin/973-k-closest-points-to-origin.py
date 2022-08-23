class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # d = { point: distance, ... }
        # sort based on distances [ values ]
        # return k points
        
        points.sort( key = lambda point: (point[0]**2 + point[1]**2) )
        
        return points[:k]
        