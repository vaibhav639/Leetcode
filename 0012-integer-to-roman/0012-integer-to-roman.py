class Solution:
    def intToRoman(self, num: int) -> str:
        roman_values = [(1000, 'M'),(900, 'CM'),(500, 'D'),(400, 'CD'),(100, 'C'),(90, 'XC'),
        (50, 'L'),(40, 'XL'),(10, 'X'),(9, 'IX'),(5, 'V'),(4, 'IV'),(1, 'I')]

        Roman_char = ""

        for value,symbol in roman_values:
            while num >= value:
                Roman_char += symbol
                num-=value

        return Roman_char

        
    
        

        