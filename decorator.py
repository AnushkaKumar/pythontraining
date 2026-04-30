import time
from typing import Any, Callable


def time_it(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        print(f"Executing {func.__name__} with arguments: {args}, {kwargs}")
        res = func(*args, **kwargs)
        print(f"Result of {func.__name__}: {res}")
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return 0

    return wrapper


@time_it
def sum(*args: Any) -> int:
    print("Inside sum function")
    sum_val = 0
    for arg in args:
        sum_val += arg
    return sum_val


# def sum(*args: Any) -> int:
#     start_time = time.time()
#     print(f"Executing {func.__name__} with arguments: {args}, {kwargs
#     print("Inside sum function")
#     sum_val = 0
#     for arg in args:
#         sum_val += arg
#     res = sum_val
#     print(f"Result of {func.__name__}: {res}")
#     end_time = time.time()
#     print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
#     return 0


if __name__ == "__main__":
    print("Before calling sum")
    result = sum(1, 2, 3, 4, 5)
    print("After calling sum")
    print(f"Result: {result}")
