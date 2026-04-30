from collections.abc import Callable
from typing import Any, Generator, Sequence, TypeVar


class Animal:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Animal(name={self.name})"


T = TypeVar("T")


def my_map(func: Callable[[T], T], item_list: Sequence[T]) -> Generator[T, None, None]:
    print("Inside my_map")
    for idx in range(len(item_list)):
        yield func(item_list[idx])


def square(x: int) -> int:
    print("About to square x=", x)
    return x**2


def capitalize(s: str) -> str:
    print("About to capitalize s=", s)
    return s.capitalize()


if __name__ == "__main__":
    item_ls = [1, 2, 3, 4, 5]
    print("Before calling my_map")
    map_ret = my_map(square, item_ls)
    print("After calling my_map")

    for i in map_ret:
        print(i)

    str_ls = ["hello", "world", "python"]
    print("Before calling my_map for capitalize")
    map_ret_str = my_map(capitalize, str_ls)
    print("After calling my_map for capitalize")
    for s in map_ret_str:
        print(s)

    animal_ls = [Animal("cat"), Animal("dog"), Animal("rabbit")]

    y = my_map(lambda a: Animal(f"New {a.name}"), animal_ls)
    for name in y:
        print(name)
