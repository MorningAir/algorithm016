class Solution:
    def combine(self, n, k):
        ans = []

        def solve(start, cur):
            # print(cur)
            if len(cur) == k:
                ans.append(cur[:])
                return
            if n - start + 1 == k - len(cur):#如果剩余数字和剩余需要的长度一样，则直接全部打印
                for i in range(start, n + 1):
                    cur += [i]
                ans.append(cur[:])
                return
            for i in range(start, n + 1 - k + len(cur)+1):#加速过程，如果剩余数字不够剩余需要的长度，就不需要递归了
                solve(i + 1, cur + [i])

        solve(1, [])
        return ans



s = Solution()
print(s.combine(4, 2))
