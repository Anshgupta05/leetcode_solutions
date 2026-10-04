class Solution:
    def isValid(self, s: str) -> bool:
        while "()"in s or "{}" in s or "[]" in s:
            s=s.replace("()","").replace("{}","").replace("[]","")
        return s==""    
        # if s=="()":
        #     return True
        # elif s=="()[]{}":
        #     return True
        # elif s=="(]":
        #     return False
        # elif s=="([])":
        #     return True
        # elif s=="([)]":
        #     return False               
        