ice_list = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(arr):
    n = len(arr)
    m = len(arr[0])
    answer = 0

    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and not visited[i][j]:
                stack = [[i, j]]

                while stack:
                    x, y = stack.pop()

                    if not visited[x][y]:
                        for k in range(4):
                            new_x = x + dx[k]
                            new_y = y + dy[k]

                            if (
                                0 <= new_x < n
                                and 0 <= new_y < m
                                and arr[new_x][new_y] == 0
                            ):
                                stack.append([new_x, new_y])
                                visited[x][y] = True

                answer += 1

    return answer


print(solution(ice_list))
