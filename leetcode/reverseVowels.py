class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        if not s:
            return ''
        
        res = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and res[left] not in VOWELS:
                left += 1
            
            while left < right and res[right] not in VOWELS:
                right -= 1

            if left < right:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
        
        return ''.join(res)