class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        capital = [chr(i) for i in range(ord('A'), ord('Z')+1)]

        while columnNumber > 0:
            result.append(capital[(columnNumber-1)%26])
            columnNumber =  (columnNumber-1)//26

        result.reverse()
        return ''.join(result)