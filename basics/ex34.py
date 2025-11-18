from multiprocessing import Pool, cpu_count

# func is applied to each element
def square(n):
    return n * n

if __name__ == "__main__":
    # create pool of 4 processes
    with Pool(processes=cpu_count()) as pool:
        values = [1,2,3,4,5]
        results = pool.map(square, values)
        print(results)
