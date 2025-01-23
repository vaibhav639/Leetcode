class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates easily
        result = []
    
        def backtrack(start, target, current_combination):
            if target == 0 and current_combination[:] not in result:
                result.append(current_combination[:])  # Found a valid combination
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
            # If the current number exceeds the target, break the loop
                if candidates[i] > target:
                    return
            # Include the current number and move forward
                current_combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current_combination)
                current_combination.pop()  # Backtrack and try the next number
    
        backtrack(0, target, [])
        return result