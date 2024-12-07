class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)/2
        set_candy_type = {}

        for candy in candyType:
            if candy in set_candy_type:
                set_candy_type[candy] += 1
            else:
                set_candy_type[candy] = 1

        if n > len(set_candy_type):
            return (int(len(set_candy_type)))
        else:
            return (int(n))
        