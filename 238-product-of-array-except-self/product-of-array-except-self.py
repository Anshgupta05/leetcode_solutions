class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
         n = len(nums)
         answer = [1] * n
        
        # Step 1: Calculate prefix products (left side)
         prefix = 1
         for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate suffix products (right side) and multiply
         suffix = 1
         for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
         return answer

    
    

   
         
        