def tribonacci(n):
    # базовый случай
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    # рекурсивный случай
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


# печатаем числа от k до n без циклов
def print_tribonacci(k, n):
    # базовый случай
    if k > n:
        return
    # рекурсивный случай
    print("T(" + str(k) + ") =", tribonacci(k))
    print_tribonacci(k + 1, n)


print_tribonacci(0, 14)
