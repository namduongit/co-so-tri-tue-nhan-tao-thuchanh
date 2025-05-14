class Job:
    def __init__(self, pi, di):
        self.pi = pi  # Thời gian cần thiết để hoàn thành công việc
        self.di = di  # Thời hạn hoàn thành công việc

def main():
    # Khởi tạo các công việc
    jobs = [
        Job(7, 35),
        Job(9, 53),
        Job(3, 10),
        Job(8, 41),
        Job(2, 8),
        Job(3, 4),
        Job(1, 1),
        Job(5, 9),
        Job(4, 15),
        Job(2, 7),
        Job(6, 27),
        Job(10, 24)
    ]

    # Sắp xếp công việc theo thời gian cần thiết để hoàn thành
    jobs.sort(key=lambda job: job.pi)

    # Tính toán và in ra kết quả
    current_time = 0
    on_time_count = 0
    late_count = 0
    for job in jobs:
        current_time += job.pi
        if current_time <= job.di:
            on_time_count += 1
            status = "Đúng hạn"
        else:
            late_count += 1
            status = "Trễ hạn"
        print(f"Công việc (pi={job.pi}, di={job.di}): {status}")

    print(f"Số công việc hoàn thành đúng hạn: {on_time_count}")
    print(f"Số công việc hoàn thành trễ hạn: {late_count}")

if __name__ == "__main__":
    main()