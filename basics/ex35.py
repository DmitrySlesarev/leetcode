import threading

def square(n):
    return n * n

if __name__ == "__main__":
    values = list(range(1,6))
    results = []
    lock = threading.Lock()

    def worker(value):
        result = square(value)
        with lock:
            results.append(result)

    threads = []
    for value in values:
        thread = threading.Thread(target=worker, args=(value,))
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()

print(results)