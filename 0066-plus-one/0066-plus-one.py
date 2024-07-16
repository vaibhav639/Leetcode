class Solution(object):
    def plusOne(self, digits):
        result = int("".join(map(str,digits))) + 1
        result = str(result)
        new_arr = []
        
        for i in result:
            new_arr.append(int(i))
        return new_arr
        