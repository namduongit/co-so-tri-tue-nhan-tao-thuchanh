#Input: số lượng chi tiết, thời gian của máy A và máy B
#5
#5 3 8 10 7
#2 6 4 7 12
#Output: Thứ tự chi tiết, Thời gian hoàn thành trên máy A và máy B
class Job:
    def __init__(self, id, time_on_a, time_on_b):
        self.id = id
        self.time_on_a = time_on_a
        self.time_on_b = time_on_b
        self.start_time_on_a = None
        self.end_time_on_a = None
        self.start_time_on_b = None
        self.end_time_on_b = None

def calculate_timing(jobs):
    time_on_a = 0
    time_on_b = 0

    for job in jobs:
        job.start_time_on_a = time_on_a
        job.end_time_on_a = time_on_a + job.time_on_a
        job.start_time_on_b = max(job.end_time_on_a, time_on_b)
        job.end_time_on_b = job.start_time_on_b + job.time_on_b

        time_on_a = job.end_time_on_a
        time_on_b = job.end_time_on_b

def apply_johnson_algorithm(jobs):
    group1 = [job for job in jobs if job.time_on_a < job.time_on_b]
    group2 = [job for job in jobs if job.time_on_a >= job.time_on_b]

    group1.sort(key=lambda job: job.time_on_a)
    group2.sort(key=lambda job: job.time_on_b, reverse=True)

    return group1 + group2

def main():
    n = int(input())  # Đọc số lượng công việc

    time_on_a = list(map(int, input().split()))  # Thời gian gia công trên máy A
    time_on_b = list(map(int, input().split()))  # Thời gian gia công trên máy B

    jobs = [Job(i + 1, time_on_a[i], time_on_b[i]) for i in range(n)]

    result = apply_johnson_algorithm(jobs)

    calculate_timing(result)

    print("Thứ tự chi tiết được gia công tuần tự là: ", end='')
    for job in result:
        print(job.id, end=' ')

    last_job = result[-1]
    print("\nThời gian hoàn thành trên máy A: ", last_job.end_time_on_a)
    print("Thời gian hoàn thành trên máy B: ", last_job.end_time_on_b)

if __name__ == "__main__":
    main()