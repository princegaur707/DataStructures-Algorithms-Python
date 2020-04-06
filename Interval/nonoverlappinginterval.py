# https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def overlap(self,a,b):
        return b[0]<=a[1]
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == []:
            return 0
        intervals.sort(key=lambda x:x[0])
        cnt = 0
        prev = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0]<prev:
                cnt = cnt + 1
                prev = min(prev,interval[1])
            else:
                prev = interval[1]
                
        return cnt 
        
        
        
        
