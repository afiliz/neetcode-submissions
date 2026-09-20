class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                self.moveToEnd(nums, i)
        
    def moveToEnd(self, nums: List[int], i: int) -> None:
        index = i
        while index + 1 < len(nums) and nums[index + 1] != 0:
            temp = nums[index + 1]
            nums[index + 1] = nums[index]
            nums[index] = temp
            index += 1