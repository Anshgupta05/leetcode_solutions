class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            # If the character is already in the map and within the current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Move the left pointer past the previous occurrence of the duplicate
                left = char_map[s[right]] + 1
            
            # Update or insert the character's latest index
            char_map[s[right]] = right
            
            # Calculate the current window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length
        