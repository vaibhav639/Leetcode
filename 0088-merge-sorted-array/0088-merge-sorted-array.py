
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = [0] * (m+n)
        result[:m] = nums1[:m]
        result[m:] = nums2[:]
        nums1[:] = sorted(result)
        

        