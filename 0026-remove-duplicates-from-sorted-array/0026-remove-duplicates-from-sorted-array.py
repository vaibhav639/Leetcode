class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))  # Extract unique elements & sort (optional)
    
        nums[:len(unique_nums)] = unique_nums  # Overwrite first k elements
        return len(unique_nums) 
        