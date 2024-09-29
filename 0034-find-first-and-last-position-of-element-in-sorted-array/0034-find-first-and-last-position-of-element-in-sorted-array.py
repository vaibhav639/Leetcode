class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)

        position = []
        new_position = []
        for i in range(l):
            if nums[i] == target:
                position.append(i)

        if len(position) == 2:
            return position

        elif len(position) > 2:
            new_position.append(position[0])
            new_position.append(position[-1])
            return new_position

        elif len(position) == 1:
            position.append(position[0])
            return position

        else:
            return [-1,-1]

        