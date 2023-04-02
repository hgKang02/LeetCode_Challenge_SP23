class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = [] 
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x:x[0])
        arr = intervals
        for num in arr:
            if not sol or sol[-1][1] < num[0]:
                sol.append(num)
            else:
                sol[-1][1] = max(sol[-1][1], num[1])
        return sol