class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        
        for num in nums:
            count[num] += 1
        index = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[index] = color
                index += 1