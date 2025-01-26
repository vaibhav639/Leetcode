class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals = sorted(intervals)

        for i in range(len(intervals)):
            if not merged:
                merged.append(intervals[i])
            elif merged[-1][-1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][-1] = max(merged[-1][-1],intervals[i][-1])
        return merged
        