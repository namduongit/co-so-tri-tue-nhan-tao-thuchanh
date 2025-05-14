import random

def generate_hanoi_file(filename=""):
    n = random.randint(3, 16)
    disks = list(range(1, n + 1))
    # Xáo trộn đĩa lên
    random.shuffle(disks)

    towers = [[], [], []]
    for disk in disks:
        tower_index = random.randint(0, 2)
        towers[tower_index].append(disk)

    # Sắp xếp từng cột theo thứ tự giảm dần (đĩa nhỏ hơn nằm trên)
    for tower in towers:
        tower.sort(reverse=True)

    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        for tower in towers:
            if tower:
                f.write(" ".join(map(str, tower)) + "\n")
            else:
                f.write("0\n")

    print(f"Đã tạo file {filename} với n = {n}")


for i in range(0, 3):
    generate_hanoi_file(f'HNtower{i}.txt')
