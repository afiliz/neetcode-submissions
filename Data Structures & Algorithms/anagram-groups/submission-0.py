class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        alphabetical_strs = strs.copy()
        for i, word in enumerate(strs):
            word = ''.join(sorted(word))
            if word not in str_dict:
                str_dict[word] = [i]
            else:
                str_dict[word].append(i)

        result = []
        for word in str_dict.keys():
            anagram_group = []
            for i in str_dict[word]:
                anagram_group.append(strs[i])
            result.append(anagram_group)
        
        return result
        