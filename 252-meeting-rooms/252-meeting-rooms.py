class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        '''
        App 1
        T.C - O(nlogn)
        S.C - O(1)
        '''
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
    
        