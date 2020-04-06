# https://leetcode.com/problems/merge-intervals/
# T.C O(nlogn) S.C O(1) or O(n)
class Solution:
    def overlap(self,a,b):
        return a[0] <= b[1] and b[0] <= a[1]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if self.overlap(res[-1],interval):
                res[-1][1] = max(res[-1][1],interval[1])
            else:
                res.append(interval)
        return res
