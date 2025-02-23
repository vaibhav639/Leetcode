import heapq
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        max_heaps = []

        for row in grid:
            heap = [-num for num in row]
            heapq.heapify(heap)
            max_heaps.append(heap)

        total_sum = 0
        cols =  len(grid[0])

        for _ in range(cols):
            max_val = 0
            for heap in max_heaps:
                if heap:
                    max_val = max(max_val, -heapq.heappop(heap))
            total_sum += max_val

        return total_sum
        