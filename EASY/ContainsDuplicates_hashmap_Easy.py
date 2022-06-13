class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        freq = {} #num, frquency
        bDistinct = 0
        
        for num in nums:
            print(num)
            if freq.get(num, 0) > 0:
                freq[num] += 1
                if freq[num] > 1:
                    bDistinct = 1
                    break
            else:
                freq[num] = 1
        
        return bDistinct