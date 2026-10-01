class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check length and rule out obvious cases:
        if len(s) != len(t):
            return False

        # build frequency map of s:
        counts_s = {}
        for item in s:
            counts_s[item] = counts_s.get(item, 0) + 1
        
        # iterating thru t:
        for item in t:
            if counts_s.get(item, 0) == 0:
                return False
            counts_s[item] -= 1
        return True


        