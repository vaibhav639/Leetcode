class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_num = set(nums)
        set_list = list(sorted(set_num))
        reverse_set_list = list(reversed(set_list))
        n = len(reverse_set_list)
        if n >= 3:
            return (reverse_set_list[2])
        else:
            return (max(reverse_set_list))
        





        