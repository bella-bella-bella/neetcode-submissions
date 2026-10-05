class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval[0], newInterval[1]

        cur_i = 0
        while cur_i < len(intervals) and intervals[cur_i][1] < new_start:
            res.append(intervals[cur_i])
            cur_i += 1
        
        if (len(res) == len(intervals)):
            # case 1: we've appended all intervals
            res.append(newInterval)
        elif intervals[cur_i][0] > new_end:
            # case 2: we've reached an interval whose start value is 
            # greater than the new interval's end
            res.append(newInterval)
            while cur_i < len(intervals):
                res.append(intervals[cur_i])
                cur_i += 1
        else:
            # case 3: we have an overlapping interval
            start = min(intervals[cur_i][0], new_start)
            end = new_end

            while cur_i < len(intervals) and intervals[cur_i][0] <= new_end:
                end = max(end, intervals[cur_i][1])
                cur_i += 1

            res.append([start, end])

            while cur_i < len(intervals):
                res.append(intervals[cur_i])
                cur_i += 1

        return res

