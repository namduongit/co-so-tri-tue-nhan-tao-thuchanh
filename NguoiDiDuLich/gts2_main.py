class TourResult:
    def __init__(self, tour, cost):
        self.tour = tour  # Danh sách các điểm đến trong tour
        self.cost = cost  # Tổng chi phí của tour

def find_tour(n, u, c):
    visited = [False] * n  # Đánh dấu các thành phố đã thăm
    u_c = u - 1  # Điều chỉnh chỉ số thành phố xuất phát về chỉ mục dựa trên 0
    v = u_c
    tour = [v + 1]
    visited[v] = True
    cost = 0

    for _ in range(n - 1):
        w = -1
        min_cost = float('inf')

        for j in range(n):
            if not visited[j] and c[v][j] < min_cost:
                min_cost = c[v][j]
                w = j

        tour.append(w + 1)
        cost += min_cost
        visited[w] = True
        v = w

    cost += c[v][u_c]
    tour.append(u)
    return TourResult(tour, cost)

def find_best_tour(n, c, p, start_points):
    best_tour = TourResult([], float('inf'))

    for start_city in start_points:
        for _ in range(p):
            current_tour = find_tour(n, start_city, c)

            if current_tour.cost < best_tour.cost:
                best_tour = current_tour

    return best_tour

# Ví dụ sử dụng
if __name__ == "__main__":
    # Ma trận chi phí
    c = [
        [0, 20, 42, 31, 6, 24],
        [10, 0, 17, 6, 35, 18],
        [25, 5, 0, 27, 14, 9],
        [12, 9, 24, 0, 30, 12],
        [14, 7, 21, 15, 0, 38],
        [40, 15, 16, 5, 20, 0]
    ]

    # Nhập liệu
    p = int(input("Nhập số lần chạy GTS1: "))
    start_points = []
    print("Nhập các điểm xuất phát: ")
    for _ in range(p):
        v = int(input())
        start_points.append(v)

    best_result = find_best_tour(6, c, p, start_points)

    print("Best Tour:", best_result.tour)
    print("Best Cost:", best_result.cost)