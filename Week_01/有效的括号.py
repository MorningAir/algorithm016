from collections import deque
class Solution:
    def isValid(self, s):
        dic = {')': '(', '}': '{', ']': '[','?':'?'}
        d = deque('?')
        for cur in s:
            if cur not in dic: d.append(cur)#遇到前括号 入栈
            elif dic[cur]!=d.pop(): return False #遇到后括号，出栈匹配，若不匹配直接判断失败，倘若出栈的是‘？’，也说明没有匹配上
        return len(d)==1


s = Solution()
print(s.isValid("()"))
