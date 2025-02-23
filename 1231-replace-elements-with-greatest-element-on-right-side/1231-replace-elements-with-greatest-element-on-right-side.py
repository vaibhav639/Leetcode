class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_val = -1

        for i in range(n-1,-1,-1):
            new_val = max_val
            max_val = max(max_val, arr[i])
            arr[i] = new_val

        return arr        