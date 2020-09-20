class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for index in range(len(pushed)):
            stack.append(pushed[index])  # 每次入栈一个
            while stack and stack[-1] == popped[i] and i < len(popped):
                stack.pop()
                i += 1
        return len(stack) == 0

