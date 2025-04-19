class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
        total = 0
        prev = None
        for char in s[::-1]:
            if not total:
                val = roman_map[char]
                total+=val
                prev = val
            elif prev <= roman_map[char]:
                total+= roman_map[char]
                prev = roman_map[char]
            else:
                total-= roman_map[char]
                prev = roman_map[char]

        return total