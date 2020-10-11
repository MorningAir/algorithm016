num = [-1,-3,2,5,4,6]
ans = [-float('inf') for _ in range(len(num))]
ans[0] = num[0]
for i in range(1,len(num)):
    ans[i] = max(ans[i-1], num[i])
print(ans)
ans.sort()