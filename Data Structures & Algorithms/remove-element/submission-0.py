class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for p1 in range(len(nums)):
            if nums[p1] != val:
                nums[k] = nums[p1]
                k += 1
        return k 
