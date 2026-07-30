class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_tracker = set()

        for i in nums:
            if i in dup_tracker:
                return True
            dup_tracker.add(i)
        return False
                