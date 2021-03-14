# 연결 요소 찾기 dfs & bfs
# 음려수 얼려 먹기

# DFS로 특정 노드를 방문하고 연결된 모든 노드들 방문
def dfs(x, y):

    #주어진 범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 공백 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 대해 음료수 채우기
result = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)






