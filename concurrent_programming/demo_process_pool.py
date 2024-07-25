from datetime import datetime
from functools import wraps
from multiprocessing import Pool

def debug(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"[Call] function {f.__name__} at {datetime.now()} with args: {args}, {kwargs}")
        result = f(*args, **kwargs)
        print(f"[Result] function {f.__name__} at {datetime.now()}: {result}")
        return result
    return wrapper

def fibo(n):
    """Fibonacci series"""
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fibo(n-2) + fibo(n-1)
        
@debug
def fibo_compute(n):
    return fibo(n)

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:
        data_in = range(38,33,-1)
        results = pool.map(fibo_compute, data_in)
        print(results)