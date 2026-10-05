class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Keep only lowercase letters and numbers
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]

        