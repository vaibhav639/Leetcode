class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []

        for char in operations:
            try:
                value = int(char)
                arr.append(value)
                
            except:
                if char == "C":
                    del arr[-1]
                elif char == "D":
                    arr.append(2 * arr[-1])
                elif char == "+":
                    arr.append(arr[-1]+arr[-2])

        return sum(arr)