class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freqList1 = {}

        min_index = float('inf')
        result = []

        for i in range(len(list1)):
            freqList1[list1[i]] = i
    

        for j in range(len(list2)):
            if list2[j] in freqList1:
                index_sum = freqList1[list2[j]] + j
                if index_sum <  min_index:
                    min_index = index_sum
                    result = [list2[j]]
                elif index_sum == min_index:
                    result.append(list2[j])
        return result
    
        