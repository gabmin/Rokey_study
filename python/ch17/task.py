path = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
]
#
#
# for i in path:
#     print(i)


# def get_map_list():
#
#     width = int(input("가로의 크기를 입력하세요."))
#     height = int(input("세로의 크기를 입력하세요."))
#
#     new_list = [[0] * width for _ in range(height)]
#
#     for i in range(height):
#         for j in range(width):
#             data = int(input("지도 정보를 입력하세요. (0: 길, 1: 벽)"))
#
#             if data == 0 or data == 1:
#                 new_list[i][j] = data
#             else:
#                 raise ValueError("0 또는 1만 입력해주세요.")
#
#     return new_list
#
#
# print(get_map_list())


def dfs(map_list):
    stack = []
    visited = []

    width = len(map_list[0])
    height = len(map_list)

    stack.append([0, 0])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while stack:
        x, y = stack.pop()

        if [x, y] not in visited:
            print([x, y])

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if 0 <= new_x < width and 0 <= new_y < height:
                    if map_list[new_x][new_y] == 0:
                        stack.append([new_x, new_y])

            visited.append([x, y])


dfs(path)


def bfs(map_list):
    queue = []
    visited = []

    width = len(map_list[0])
    height = len(map_list)

    queue.append([0, 0])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y = queue.pop(0)

        if [x, y] not in visited:
            print([x, y])

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if 0 <= new_x < width and 0 <= new_y < height:
                    if map_list[new_x][new_y] == 0:
                        queue.append([new_x, new_y])

            visited.append([x, y])


bfs(path)
