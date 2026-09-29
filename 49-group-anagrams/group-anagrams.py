class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_map={}
        for s in strs:
            sorted_key=tuple(sorted(s))
            if sorted_key not in anagrams_map:
                anagrams_map[sorted_key]=[]
            anagrams_map[sorted_key].append(s)
        return list(anagrams_map.values())
                


        