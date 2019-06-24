def lengthOfLongestSubstring(s):
        max_sub=0
        cur = 0
        i=0
        while i < len(s)-max_sub:
            j = i
            d = {}
            cur = 0
            while s[j] not in d.keys() and j < len(s):
                d[s[j]] = 1
                cur += 1
                if cur > max_sub:
                    max_sub = cur
                j+=1
            i += 1
        return max_sub
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))