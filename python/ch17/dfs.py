from graph import my_graph


def my_dfs(graph, start_node):
    stack = list()
    visited = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            stack.extend(reversed(graph[node]))
            visited.append(node)

    return visited


print(my_dfs(my_graph, "A"))
