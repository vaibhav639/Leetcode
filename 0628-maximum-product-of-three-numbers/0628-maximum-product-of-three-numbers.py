class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)

        fist_small = nums[0]
        second_small = nums[1]

        first_large = nums[-1]
        second_large = nums[-2]
        thirdlarge = nums[-3]

        productSmallLarge = fist_small * second_small * first_large

        productLarge = first_large * second_large * thirdlarge

        result = max(productSmallLarge,productLarge)
        return result
        