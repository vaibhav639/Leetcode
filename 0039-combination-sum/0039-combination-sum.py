class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def solve(target,combination,start):
            if target == 0:
                result.append(list(combination))
            elif target < 0:
                return
    
            for i in range(start,len(candidates)):
        
                combination.append(candidates[i])
        
                solve(target-candidates[i], combination, i)
                combination.pop()
        
        solve(target,[],0)
        return result