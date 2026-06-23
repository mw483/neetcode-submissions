class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check substring 1 length
        length_s1 = len(s1)
        if length_s1 > len(s2):
            return False

        # create frequency array for s1
        s1_freq, s2_freq = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        # gets the number of matching frequencies
        matches = 0
        for i in range(26):
            matches += (1 if s1_freq[i] == s2_freq[i] else 0)
            
        # use the s1 length as the fixed size sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2_freq[index] += 1
            if s1_freq[index] == s2_freq[index]:
                matches += 1
            elif s1_freq[index] + 1 == s2_freq[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2_freq[index] -= 1
            if s1_freq[index] == s2_freq[index]:
                matches += 1
            elif s1_freq[index] - 1 == s2_freq[index]:
                matches -= 1
            l += 1 

        return matches == 26
        