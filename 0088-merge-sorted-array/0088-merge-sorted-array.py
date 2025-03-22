
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        result = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i+=1
            elif nums2[j] < nums1[i]:
                result.append(nums2[j])
                j+=1

        while i < m:
            result.append(nums1[i])
            i += 1
        while j < n:
            result.append(nums2[j])
            j += 1

        nums1[:] = result
        

        