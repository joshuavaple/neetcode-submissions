class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        for item in s:
            counts_s[item] = counts_s.get(item, 0) + 1
        counts_t = {}
        for item in t:
            if counts_s.get(item, 0) == 0: # if t has a new char
                return False
            counts_t[item] = counts_t.get(item, 0) + 1
        return counts_s == counts_t