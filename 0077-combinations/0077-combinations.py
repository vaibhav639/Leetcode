class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        lst = list(range(1,n+1))

        def solve(ip,op):
            if len(op) == k:
                result.append(op[:])
                return
            if not ip:
                return
    
            notpick = op
            pick = op + [ip[0]]
            ip = ip[1:]
    
            solve(ip,notpick)
            solve(ip,pick)
    
        solve(lst,[])
        return result
        