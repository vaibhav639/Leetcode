class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        new_set = set(nums)

        for i in range(1,n+1):
            if i not in new_set:
                result.append(i)
        return result