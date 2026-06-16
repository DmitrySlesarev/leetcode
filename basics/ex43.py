def get_numbers():
    return [1, 2, 3, 4, 5]


numbers = get_numbers()
for num in numbers:
    print(num)

print("***")

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)

print("****")

def simple_generator():
    print("Starting...")
    yield 1
    print("Resuming after first yield...")
    yield 2
    print("Resuming after second yield...")
    yield 3
    print("Done!")

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))