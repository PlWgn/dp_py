def backpack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]
    
weights = [1, 2, 3]
values = [50, 120, 300]
print(backpack(weights, values, 5))

def lcs(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

x = "LDSAVFES"
y = "FKKAS"
print(lcs(x, y))

def partition(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for number in range(1, n + 1):
        for total in range(number, n + 1):
            dp[total] += dp[total - number]

    return dp[n]

print(partition(4))
print(partition(5))
print(partition(9))

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = float('inf')

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist

graph = [
    [0, 2, 0, 1],
    [2, 0, 3, 2],
    [0, 3, 0, 4],
    [1, 2, 4, 0]
]

for row in floyd_warshall(graph):
    print(row)
    