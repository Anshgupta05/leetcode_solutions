class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
             return False
        original_num=x
        result=0

        while x>0:
            last_digit=x%10
            result=(result*10)+last_digit
            x=x//10

        return result== original_num        
        