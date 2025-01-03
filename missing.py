
#
# Note: The class, method and parameter have been specified. Please do not modify
#
#
# This function will take an array of integers as argument and return the missing number from the range of the array as an integer
# @param nums Integer One-dimensional Array 
# @return Integer
#
class Solution:
    def findMissingNumber(self, nums) :
        # write code here
        nums.sort() 
        missing = 0
        for num in nums:
            if num == missing:
                missing += 1
        return missing
            

