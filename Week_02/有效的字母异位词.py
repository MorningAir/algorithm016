import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0 for _ in range(26)]
        for i in s:
            a[ord(i)-ord('a')] +=1
        for i in t:
            a[ord(i)-ord('a')] -=1
        return a==[0 for _ in range(26)]
s = Solution()
print(s.isAnagram('anagram','nagaram'))
