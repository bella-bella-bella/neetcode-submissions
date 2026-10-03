class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        s_chars = dict()
        t_chars = dict()

        for c1 in s:
            s_chars.update({c1: s_chars.get(c1, 0) + 1})
        for c2 in t:
            t_chars.update({c2: t_chars.get(c2, 0) + 1})
        
        if s_chars == t_chars:
            return True
        
        return False
        