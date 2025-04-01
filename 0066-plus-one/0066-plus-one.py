class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = str(int("".join(map(str,digits))) + 1)
        re = []

        for char in num_str:
            re.append(int(char))
        return re
        
