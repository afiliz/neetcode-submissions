class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        print(s_dict)
        print(t_dict)

        for key in s_dict.keys():
            if key in s_dict and key in t_dict:
                if s_dict[key] != t_dict[key]: return False
            else:
                return False

        return True