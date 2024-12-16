class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []

        for i in dirs:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)

        return '/' + '/'.join(stack)
