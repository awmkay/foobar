def solution(src, dest):
    if src == dest:
        return 0

    width = 8
    graph = {}
    for cell in range(64):
        graph[cell] = set()

    for vertex in graph:
        posList = []
        mod = vertex % 8

        if mod != 7:
            posList.append(vertex + (2 * width + 1))
            posList.append(vertex - (2 * width - 1))
        if mod != 0:
            posList.append(vertex + (2 * width - 1))
            posList.append(vertex - (2 * width + 1))
        if mod != 7 and mod != 6:
            posList.append(vertex + (width + 2))
            posList.append(vertex - (width - 2))
        if mod != 1 and mod != 0:
            posList.append(vertex + (width - 2))
            posList.append(vertex - (width + 2))

        for neighbour in graph:
            if neighbour in posList:
                graph[vertex].add(neighbour)

    print(graph)

    return len(shortest_path(graph, src, dest)) - 1


def BFS(graph, src, dest):
    queue = [(src, [src])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == dest:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, src, dest):
    try:
        return next(BFS(graph, src, dest))
    except StopIteration:
        return None
