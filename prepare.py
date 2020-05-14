"""Solves a map with removable walls."""


def solution(map):
    """Find the shortest path in map."""
    maxRow, maxCol = len(map), len(map[0])

    maps = []
    for y in range(maxRow):
        for x in range(maxCol):
            if map[y][x]:
                maps.append([])
                maps[-1] = [row[:] for row in map]
                maps[-1][y][x] = 0

    rowNum = [1, -1, 0, 0]
    colNum = [0, 0, 1, -1]

    mapDists = []
    for map in maps:
        mapDists.append(BFS(map, maxRow, maxCol, rowNum, colNum))

    return min([n for n in mapDists if n > 0])


class Node:
    """Used for BFS algorithm."""

    def __init__(self, pt, dist):
        """Initialise the node class."""
        self.pt = pt
        self.dist = dist


def valid(row: int, col: int, maxRow: int, maxCol: int):
    """Check if point is valid in 2D array."""
    return (row >= 0) and (row < maxRow) and (col >= 0) and (col < maxCol)


def BFS(map, maxRow, maxCol, rowNum, colNum):
    """Maze solving algorithm."""
    dest = (maxRow - 1, maxCol - 1)

    visited = [[False for i in range(maxCol)] for j in range(maxRow)]
    visited[0][0] = True

    src = Node((0, 0), 1)
    queue = [src]

    while len(queue) > 0:
        curr = queue.pop(0)

        if curr.pt == dest:
            return curr.dist

        for i in range(4):
            row = curr.pt[0] + rowNum[i]
            col = curr.pt[1] + colNum[i]

            if valid(row, col, maxRow, maxCol) and \
                    not map[row][col] and \
                    not visited[row][col]:
                visited[row][col] = True
                adj = Node((row, col), curr.dist + 1)
                queue.append(adj)

    return -1


print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [
      0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
