class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Invariant: The over-lap occurs when starting time is same for intervals
        # state: sorted intervals, common starting and end time of 2nd intervals
        # violation: when there is overlap of starting time
        # pattern: intervals, range

        if not intervals:
            return []

        # sort by starting time
        intervals.sort(key=lambda a:a[0])
        print(intervals)

        # 1     3
        # 1         5
        #               6 7

        merged = [intervals[0]] # 1,5

        for interval in intervals[1:]:
            last_interval = merged[-1]      # append

            # [start, old, new]
            if last_interval[1] >= interval[0]:
                merged[-1][1] = max(last_interval[1], interval[1])
            else:
                merged.append(interval)
        
        return merged


        