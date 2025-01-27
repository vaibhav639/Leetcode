class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = []
        after = []
        final = []
        merged = []
        if not intervals:
            return [newInterval]

        for lst in intervals:
            if lst[-1] < newInterval[0]:
                before.append(lst)
            elif lst[0] > newInterval[-1]:
                after.append(lst)
            else:
                if not merged:
                    merged = [[min(lst[0],newInterval[0]), max(lst[-1],newInterval[-1])]]
                else:
                    merged = [[min(lst[0],merged[0][0]), max(lst[-1],merged[0][-1])]]
        
        if newInterval and not merged:
            final = before + after + [newInterval]
        else:
            final = before + merged + after
        return sorted(final)