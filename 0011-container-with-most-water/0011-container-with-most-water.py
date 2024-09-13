class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        water_unit = 0
        while left < right:
            column = right - left
            if height[left] < height[right]:
                water_unit = max(water_unit, height[left] * column)
                left += 1
            elif height[left] == height[right]:
                water_unit = max(water_unit, height[left] * column)
                left += 1
            else:
                water_unit = max(water_unit, height[right] * column)
                right -= 1

        return water_unit


            



        