class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        unique_nums = list(set(nums))
        result = []
        def solve(ip,op):
            if len(ip) == 0:
                result.append(op[:])
                return
    
            notpick = op
            pick = op + [ip[0]]
            ip = ip[1:]
    
            solve(ip,notpick)
            solve(ip,pick)
    
        solve(unique_nums,[])
        return result
    