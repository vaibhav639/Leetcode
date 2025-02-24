class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for substr in emails:
            ls = list(substr)
            temp = []
            index1 = None
            index2 = None
            flag = True
            for char in ls[:]:
                if char == "." and flag==True:
                    continue
                elif char == "+":
                    temp.append(char)
                    index1 = temp.index(char)
                elif char == "@":
                    flag = False
                    temp.append(char)
                    index2 = temp.index(char)
                else:
                    temp.append(char)
            new_ls = []
            if index1 and index2:
                new_ls = temp[:index1] + temp[index2:] + [".", "c", "o", "m"]
                s = "".join(new_ls)
                seen.add(s)
            else:
                new_ls = temp[:] + [".", "c", "o", "m"]
                s = "".join(new_ls)
                seen.add(s)

        return len(seen)