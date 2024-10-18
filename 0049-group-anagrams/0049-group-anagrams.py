class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroup = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagramGroup[sorted_word].append(word)

        return list(anagramGroup.values())

        