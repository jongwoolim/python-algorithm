def dfs(graph, start, visited):
    # 탐색 시작 노드를 스택에 삽입하고 방문 처리
    visited[start] = True

    print(start, end=" ")
    
    # 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면
    # 그 노드를 스택에 넣고 방문 처리
    # 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

if __name__ == '__main__':
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
    visited = [False]*9

dfs(graph, 1, visited)