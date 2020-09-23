class Solution:
    def heapsort(self, nums):
        n = len(nums)
        for i in range((n - 1) // 2, -1, -1):#建堆的过程，从子堆开始，逐步往上建
            self.heapify(nums, n, i)
        for i in range(n - 1, 0, -1):#取最大，与最后一个位置交换
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)

    def heapify(self, nums, length, cur):
        largest = cur
        left = 2 * cur + 1
        right = 2 * cur + 2
        if left < length and nums[left] > nums[largest]:
            largest = left
        if right < length and nums[right] > nums[largest]:
            largest = right
        if cur != largest:
            nums[largest], nums[cur] = nums[cur], nums[largest]
            self.heapify(nums, length, largest)


s = Solution()
nums = [12, 11, 13, 5, 6, 7]
s.heapsort(nums)
print(nums)
