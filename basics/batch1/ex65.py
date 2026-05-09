import time

N = 6
# a = [0] * N
#
# for i in range(N):
#     a[i] = i ** 2

def check_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Elapsed time {end-start:.9f}")
        return res
    return wrapper

# a = lambda n: [x ** 2 for x in range(n)]
@check_time
def via_list_comprehension(n):
    return [x ** 2 for x in range(n)]

@check_time
def step_by_step(n):
    a = [0] * n
    for i in range(n):
        a[i] = i ** 2
    return a

print(via_list_comprehension(6))
print(step_by_step(6))
a = 0.000004300
b = 0.000002700
print(f"{b/a:.6f}")

# print(a(6))