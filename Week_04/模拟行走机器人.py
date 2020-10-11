class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        oo = set(map(tuple, obstacles))
        start = 0
        ans = 0
        i = 0
        j = 0
        x = 0
        y = 1
        for cur in commands:
            if cur == -2:
                start = (start + 3) % 4
            elif cur == -1:
                start = (start + 1) % 4
            else:
                x, y = direction[start]
                while cur > 0 and (i + x, j + y) not in oo:
                    i += x
                    j += y
                    cur -= 1
                ans = max(ans, i ** 2 + j ** 2)
        return ans

