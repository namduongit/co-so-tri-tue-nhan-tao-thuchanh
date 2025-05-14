def find_tour(n, u, c):
    visited = [False] * n
    u_c = u - 1  
    v = u_c
    tour = [v + 1]
    visited[v] = True
    cost = 0

    for _ in range(n - 1):
        w = -1
        min_cost = float('inf')

        for j in range(n):
            if c[v][j] < min_cost and not visited[j]:
                min_cost = c[v][j]
                w = j

        tour.append(w + 1)
        cost += min_cost
        visited[w] = True
        v = w

    cost += c[v][u_c]
    tour.append(u)
    return tour, cost

# Cost matrix
c = [
    [0, 20, 42, 31, 6, 24],
    [10, 0, 17, 6, 35, 18],
    [25, 5, 0, 27, 14, 9],
    [12, 9, 24, 0, 30, 12],
    [14, 7, 21, 15, 0, 38],
    [40, 15, 16, 5, 20, 0]
]

u = int(input("Enter starting city u = "))
tour, cost = find_tour(6, u, c)
print(f"Tour: {tour}")
print(f"Cost: {cost}")