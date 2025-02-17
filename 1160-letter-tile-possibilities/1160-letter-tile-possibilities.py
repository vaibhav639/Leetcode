from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result_set = set()

        for i in range(1,len(tiles)+1):
            for perm in permutations(tiles,i):
                result_set.add("".join(perm))

        return len(result_set)

        