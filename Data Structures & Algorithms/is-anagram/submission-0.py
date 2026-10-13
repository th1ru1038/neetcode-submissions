from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the lengths are equal (min condition for anagram)
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            # .get()
            # returns the value of key char, or else it will be initialized as 0
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t
        