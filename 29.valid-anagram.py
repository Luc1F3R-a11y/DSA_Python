class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = list(s) 
        new_t = list(t)

        new_s.sort()
        new_t.sort()

        return new_s == new_t