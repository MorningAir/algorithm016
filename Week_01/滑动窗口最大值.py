class Solution:
    def maxSlidingWindow(self, nums, k):
        res,q = [],[]
        for i in range(len(nums)):
            if not q:
                q.append(i)
            else:
                if q[0]+k == i:
                    q.pop(0)
                while q and nums[q[-1]]<nums[i]:
                    q.pop()
                q.append(i)
            res.append(nums[q[0]])
        return res[k-1:]