class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            tmpMax = curMax
            curMax = max(n, n*curMax, n*curMin)
            curMin = min(n, n*tmpMax, n*curMin)
            res = max(res, curMax)
            
        return res