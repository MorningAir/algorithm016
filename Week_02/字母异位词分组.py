class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for i in strs:
            a = [0 for _ in range(26)]
            for j in i:
                a[ord(j) - ord('a')] += 1
            a = tuple(a)
            if a not in dic:
                dic[a] = [i]
            else:

                dic[a].append(i)

        return(list(dic.values()))
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
