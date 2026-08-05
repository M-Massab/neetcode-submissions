class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        
        for word in strs:
            # Sort characters to create a canonical key (e.g., "eat" -> "aet")
            key = "".join(sorted(word))
            
            # If the key is already in our dictionary, append to its list
            if key in anagram_map:
                anagram_map[key].append(word)
            # Otherwise, initialize a new list with this word
            else:
                anagram_map[key] = [word]
                
        # Return all the grouped lists as a list of lists
        return list(anagram_map.values())