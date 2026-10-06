def recursive_reverse(some_list):
    # базовый случай: пустой список или один элемент переворачивать не нужно
    if len(some_list) <= 1:
        return some_list
    # рекурсивный случай: переворачиваем хвост и ставим первый элемент в конец
    return recursive_reverse(some_list[1:]) + [some_list[0]]


print(recursive_reverse([1, 2, 3, 4, 5]))
print(recursive_reverse(["a", "b", "c"]))
print(recursive_reverse([7]))
print(recursive_reverse([]))
