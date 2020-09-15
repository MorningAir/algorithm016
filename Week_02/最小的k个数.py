import heapq
class Solution:
    def getLeastNumbers(self, arr, k):
        #建立最小堆，能够找最大的数字，找到最大的数字替换，也就是找前k个小的数字
        if k ==0:
            return []
        heap = [-x for x in arr[:k]]
        heapq.heapify(heap)
        for i in range(k,len(arr)):
            if -arr[i]>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,-arr[i])
        return [-x for x in heap]