class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse = True)
        set_score = {}
        result = []
        if len(score) == 1:
            return ["Gold Medal"]
        if len(score) == 2:
            if score[0] < score[1]:
                return ["Silver Medal","Gold Medal"]
            else:
                return ["Gold Medal","Silver Medal"]

        set_score[sorted_score[0]] = "Gold Medal"
        set_score[sorted_score[1]] = "Silver Medal"
        set_score[sorted_score[2]] = "Bronze Medal"

        for i in range(3,len(sorted_score)):
            set_score[sorted_score[i]] = str(i + 1)

        for score in score:
            result.append(set_score[score])
        return result


        