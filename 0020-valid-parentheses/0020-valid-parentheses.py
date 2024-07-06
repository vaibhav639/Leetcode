class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }

        for i in s:
            if i in pairs:
                stack.append(i)
            elif (len(stack) == 0 or i!=pairs[stack.pop()]):
                return False

        if (len(stack) == 0):
            return True
        else:
            return False

        
        