from functools import wraps
import time
from threading import Thread
import multiprocessing


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def count(max_number: int, tp: str) -> int:
    print(f"""Starting {tp}""")
    n = 0
    while n < max_number:
        n = n + 1
    return 1


if __name__ == '__main__':
    mt = Thread(target=count, args=(1000_000_000, "Multi Thread"))
    mt.run()
    mp = multiprocessing.Process(target=count, args=(1000_000_000, "MultiProcess"))
    mp.start()
    mp.join()
    print("done")
