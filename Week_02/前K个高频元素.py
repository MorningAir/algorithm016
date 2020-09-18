class Solution:
    def topKFrequent(self, nums,k):
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0) + 1
        array = sorted(dict.items(),key = lambda x:x[1],reverse=True)
        result = []
        for i in range(k):
            result.append(array[i][0])
        return result

