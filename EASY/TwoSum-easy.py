class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rl = []
        previous = {} #val:index
        for i, n1 in enumerate(nums):
            diff = target - n1
            if(diff in previous):
                rl = [i, previous[diff]]
                break
            else:
                previous[n1] = i
        
        return rl