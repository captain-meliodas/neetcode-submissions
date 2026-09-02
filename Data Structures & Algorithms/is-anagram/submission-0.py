class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        res = True
        if len(s) != len(t):
            return False
            
        for c in s:
            hash_map[c] = hash_map.get(c,0)+1
        
        for c in t:
            if hash_map.get(c):
                hash_map[c] = hash_map[c]-1
                if hash_map[c] < 0:
                    res = False
                    break
            else:
                res = False
                break

        return res
        