class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0] * n
        for i in range(n):
            result[i] = prefix_product
            #print("this is prefix_product",prefix_product)
            prefix_product *= nums[i]
            #print("this is nums[i]",nums[i])
            #print("this is prefix_product",prefix_product)
        for i in range(n-1,-1,-1):
            #print(i)
            #print("this is result[i]", result[i])
            result[i] *= postfix_product
            #print("this is postfix[i]",postfix_product)
            #print("this is result after multiply", result[i])
            postfix_product *= nums[i]
            #print("this is nums[i]", nums[i])
        return result