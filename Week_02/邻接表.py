# edges表示邻接矩阵
edges = [[0, 1, 12, 0, 0, 0],
         [0, 0, 9, 3, 0, 0],
         [0, 0, 0, 0, 5, 0],
         [0, 0, 4, 0, 13, 15],
         [0, 0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0, 0]]



dis = [float('inf')] * len(edges)#起点到每一个点的最短距离
visited = []
dis[0] = 0



for _ in range(len(dis)):
    min_dis = float('inf')
    for i in range(len(edges)):  # 找到dis中距离起始点距离最小的点
        if dis[i] < min_dis and i not in visited:
            min_dis = dis[i]
            min_index = i
    visited.append(min_index)

    for j in range(len(edges)):  # 遍历最小点的邻接点，更新距离
        if edges[min_index][j] > 0:  # 找到邻接点
            dis[j] = min(min_dis + edges[min_index][j], dis[j])


print(dis)
# 由于python中列表的索引是从0开始的，而我们的点是1-6，因此min_dis_point在邻接矩阵中的位置需要减一，
# 这里容易犯错，若是将点改为从0开始无论是写还是可读性都会好很多
