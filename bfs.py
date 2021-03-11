from collections import deque
def bfs(graph, start, visited):
    # 탐색 시작 노드를 큐에 삽입하고 방문 처리
    queue = deque([start])
    visited[start] = True

    # 큐에서 꺼낸 뒤 해당 노드의 인접 노드 중
    # 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
      

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

bfs(graph, 1, visited)
