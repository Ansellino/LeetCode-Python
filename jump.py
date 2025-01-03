
#
# Note: The class, method and parameter have been specified. Please do not modify
#
#
# 
# @param nums Integer One-dimensional Array 
# @return Boolean
#
class Solution:
    def canReach(self, nums) :
        # write code here
        counter = 0
        for num in nums:
            if counter < 0:
                return False
            elif num > counter:
                counter = num
            counter -= 1
        return True 