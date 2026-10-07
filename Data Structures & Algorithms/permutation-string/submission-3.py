class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freqs = [0] * 26
        s2_freqs = [0] * 26
        for i in range(len(s1)):
            s1_freqs[ord(s1[i]) - ord('a')] += 1
            s2_freqs[ord(s2[i]) - ord('a')] += 1

        if s1_freqs == s2_freqs:
            return True

        for end in range(len(s1), len(s2)):
            s2_freqs[ord(s2[end]) - ord('a')] += 1
            s2_freqs[ord(s2[end - len(s1)]) - ord('a')] -= 1
            if s1_freqs == s2_freqs:
                return True

        return False
        