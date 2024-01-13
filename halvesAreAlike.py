class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        half = int(len(s) / 2 )
        a,b,count = s[:half],s[half: len(s)],0
        number_of_vowels_in_first_half,number_of_vowels_in_second_half = 0,0
        
        for val in a:
            if val in vowels:
                number_of_vowels_in_first_half += 1

        for val in b:
            if val in vowels:
                number_of_vowels_in_second_half += 1

        if number_of_vowels_in_first_half == number_of_vowels_in_second_half:
            return True

        return False    
