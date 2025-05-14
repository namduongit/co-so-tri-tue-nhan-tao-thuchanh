import heapq
import copy

def get_data(file_data = ''):
    row = -1
    start = []
    end = []
    with open(file=file_data) as file:
        row = int(file.readline())
        for _ in range(row):
            line = file.readline().strip()
            numbers = list(map(int, line.split()))
            start.append(numbers)
        
        for _ in range(row):
            line = file.readline().strip()
            numbers = list(map(int, line.split()))
            end.append(numbers)
    
    return row, start, end



def calculate_hamming(state, goal_state):
    hamming = 0
    for i in range(N):
        for j in range(N):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                hamming += 1
    return hamming

def calculate_manhattan(state, goal_state):
    pos = {}
    for i in range(N):
        for j in range(N):
            pos[goal_state[i][j]] = (i, j)
    
    dist = 0
    for i in range(N):
        for j in range(N):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = pos[val]
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist

def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    path.reverse()
    return path

class PuzzleState:
    def __init__(self, state, g, goal_state, parent=None):
        self.state = state
        self.g = g
        self.h = calculate_manhattan(state, goal_state)
        self.f = self.g + self.h
        self.goal_state = goal_state
        self.parent = parent 

    def is_goal(self):
        return self.state == self.goal_state

    def get_successors(self):
        successors = []
        row, col = -1, -1
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    row, col = i, j
                    break
            if row != -1:
                break

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < len(self.state) and 0 <= new_col < len(self.state):
                new_state = copy.deepcopy(self.state)
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                successors.append(PuzzleState(new_state, self.g + 1, self.goal_state, self))  # gán parent
        return successors

    def print_state(self):
        print(f"g = {self.g}, h = {self.h}, f = {self.f}")
        for row in self.state:
            print(" ".join(str(val) for val in row))
        print()

    def __lt__(self, other):
        return self.f < other.f


def solvePuzzle(start_state, goal_state):
    open_set = []
    closed_set = set()

    start_node = PuzzleState(start_state, 0, goal_state)
    heapq.heappush(open_set, start_node)

    while open_set:
        current = heapq.heappop(open_set)

        # Nếu đạt trạng thái đích
        if current.is_goal():
            print("Đã tìm thấy lời giải:")
            path = reconstruct_path(current)
            for step in path:
                step.print_state()
            print(f"Số bước: {len(path)-1}")
            return


        # Biến state thành tuple để lưu trong tập closed (vì list không hashable)
        state_key = tuple(tuple(row) for row in current.state)
        if state_key in closed_set:
            continue
        closed_set.add(state_key)

        for neighbor in current.get_successors():
            neighbor_key = tuple(tuple(row) for row in neighbor.state)
            if neighbor_key not in closed_set:
                heapq.heappush(open_set, neighbor)

    print("Không tìm thấy lời giải.")


if __name__ == '__main__':
    row, start, end = get_data('data/taci1.txt')
    N = row
    solvePuzzle(start, end)
