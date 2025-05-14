import heapq
import copy

def get_data(file_data=''):
    disk = -1
    column_a = []
    column_b = []
    column_c = []
    with open(file=file_data) as file:
        disk = int(file.readline())
        column_a = [int(x) for x in file.readline().strip().split() if int(x) != 0]
        column_b = [int(x) for x in file.readline().strip().split() if int(x) != 0]
        column_c = [int(x) for x in file.readline().strip().split() if int(x) != 0]
        
    return disk, column_a, column_b, column_c



class TowerState:
    def __init__(self, columns, g, total_disks):
        self.columns = columns  # [A, B, C]
        self.g = g
        self.h = self.heuristic(total_disks)
        self.f = self.g + self.h

    def heuristic(self, total_disks):
        return total_disks - len(self.columns[2])

    def is_goal(self, total_disks):
        return len(self.columns[2]) == total_disks and \
               self.columns[2] == list(range(total_disks, 0, -1))

    def get_successors(self, total_disks):
        successors = []
        for from_col in range(3):
            if not self.columns[from_col]:
                continue
            disk = self.columns[from_col][-1]
            for to_col in range(3):
                if from_col == to_col:
                    continue
                if not self.columns[to_col] or self.columns[to_col][-1] > disk:
                    new_columns = copy.deepcopy(self.columns)
                    new_columns[from_col].pop()
                    new_columns[to_col].append(disk)
                    successors.append(TowerState(new_columns, self.g + 1, total_disks))
        return successors

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.columns == other.columns

    def __hash__(self):
        return hash(tuple(tuple(col) for col in self.columns))

    def print_state(self):
        print(f"g = {self.g}, h = {self.h}, f = {self.f}")
        print("A:", self.columns[0])
        print("B:", self.columns[1])
        print("C:", self.columns[2])
        print()

        
        


def solve_tower(disk, col_a, col_b, col_c):
    start_state = TowerState([col_a, col_b, col_c], 0, disk)
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, start_state)

    while open_set:
        current = heapq.heappop(open_set)
        current.print_state()

        if current.is_goal(disk):
            print("Đã tìm thấy lời giải!")
            return

        state_key = tuple(tuple(col) for col in current.columns)
        if state_key in closed_set:
            continue
        closed_set.add(state_key)

        for neighbor in current.get_successors(disk):
            neighbor_key = tuple(tuple(col) for col in neighbor.columns)
            if neighbor_key not in closed_set:
                heapq.heappush(open_set, neighbor)

    print("Không tìm thấy lời giải.")


if __name__ == '__main__':
    disk, column_a, column_b, column_c = get_data('HNtower.txt')
    solve_tower(disk, column_a, column_b, column_c)