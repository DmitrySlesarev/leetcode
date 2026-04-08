from multiprocessing import Pool, cpu_count

def square(n):
    return n * n

if __name__ == "__main__":
    # with Pool(processes=4) as pool:
    #     values = [1,2,3,4,5]
    #     results = pool.map(square, values)
    #     print(results)
    with Pool(processes=cpu_count()) as pool:
        values = [1,2,3,4,5]
        results = pool.map(square, values)
        print(results)


