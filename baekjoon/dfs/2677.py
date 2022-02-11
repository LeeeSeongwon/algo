count = 0


def main(graph):
    num = []
    result = 0

    for i in range(n):
        for j in range(n):
            if dfs(graph, i, j) == True:
                global count
                num.append(count)
                result += 1
                count = 0

    num.sort()
    print(result)
    for i in range(len(num)):
        print(num[i])


def dfs(graph, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph, nx, ny)
        return True
    return False


if __name__ == "__main__":
    n = int(input())
    graph = []

    for i in range(n):
        graph.append(list(map(int, input())))

    main(graph)
