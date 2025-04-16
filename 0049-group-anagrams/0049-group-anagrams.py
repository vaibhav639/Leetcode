class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for el in strs:
            sort_el = " ".join(map(str,sorted(el)))
            freq[sort_el] = []

        for el in strs: 
            sort_el = " ".join(map(str,sorted(el)))
            if sort_el in freq:
                freq[sort_el].append(el)

        result = [val for key,val in freq.items()]
        return result

        