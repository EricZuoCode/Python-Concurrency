import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        results = pool.map(square, range(10))
    print(results)
