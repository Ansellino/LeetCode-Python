class Solution:
    def canJump(self, nums: List[int]) -> bool:
        energy = nums[0]
        for num in nums:
            if energy < 0:
                return False
            elif energy < num:
                energy = num
            energy -= 1
        return True