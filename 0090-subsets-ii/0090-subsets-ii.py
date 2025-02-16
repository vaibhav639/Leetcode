class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(ip,op):
            if not ip:
                if op not in result:
                    result.append(op)
                return
    
            solve(ip[1:],op)
            solve(ip[1:],op + [ip[0]])
        

        solve(sorted(nums),[])
        return result