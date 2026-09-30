class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums.sort()
        count_digit={}
        for num in nums:
            if num in count_digit:
                count_digit[num]+=1
            else:
                count_digit[num]=1
        sorted_by_frequency = sorted(count_digit.items(), key=lambda item: item[1], reverse=True)
        result=[]
        for i in range (k):
            result.append(sorted_by_frequency[i][0])
        return result
