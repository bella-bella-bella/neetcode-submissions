class Solution:         
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # each key in char_freqs will be an array of length 26
        # representing the frequencies of each character in the word
        char_freqs = dict()

        for word in strs:
            char_counts = [0] * 26 # initialise all char counts as 0
            for c in word:
                char_counts[ord(c) - ord('a')] += 1
            key = tuple(char_counts) # list isn't hashable
            
            if key not in char_freqs:
                char_freqs[key] = []

            char_freqs[key].append(word)
        
        return list(char_freqs.values())



                 
        

    
