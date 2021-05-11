class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sliding window technique
        # time complexity: o(n) since "in" and "index()" operation is o(n) on average
        # space complexity: o(1) in place
        if len(needle) == 0:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
