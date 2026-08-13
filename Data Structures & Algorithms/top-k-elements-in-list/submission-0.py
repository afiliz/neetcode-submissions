from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        for i in nums:
            freq_dict[i] += 1

        result = []
        sorted_freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
        for i, num in enumerate(sorted_freq):
            if i >= k:
                break
            result.append(num[0])

        return result
            
