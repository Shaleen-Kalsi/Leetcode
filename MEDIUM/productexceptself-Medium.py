class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = []
        
        #prefix pass
        answer =[1]*len(nums)
        i = 1
        while i < len(nums):
            answer[i] = nums[i-1] * answer[i-1]
            i+=1
            
        #postfix pass
        j = len(nums) - 2
        postfix = 1
        while j >= 0:
            answer[j] = answer[j] * nums[j+1] * postfix
            postfix *= nums[j+1]
            j-=1
            
        return answer