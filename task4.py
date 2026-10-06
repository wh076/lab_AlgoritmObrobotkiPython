import time
import matplotlib.pyplot as plt


def fibonacci(n):
    # базовый случай
    if n == 0:
        return 0
    if n == 1:
        return 1
    # рекурсивный случай
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    # базовый случай
    if n == 0:
        return 2
    if n == 1:
        return 1
    # рекурсивный случай
    return lucas(n - 1) + lucas(n - 2)


def fib_with_lucas(n):
    # базовый случай (для маленьких n формула зациклится, поэтому задаём их сами)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    # рекурсивный случай
    i = n // 2
    j = n - i
    return (fib_with_lucas(i) * lucas_with_fib(j) + fib_with_lucas(j) * lucas_with_fib(i)) // 2


def lucas_with_fib(n):
    # базовый случай
    if n == 0:
        return 2
    if n == 1:
        return 1
    # рекурсивный случай
    return fib_with_lucas(n - 1) + fib_with_lucas(n + 1)


# проверка, что формулы дают те же числа
print("Проверка для n = 0..20:")
all_ok = True
for n in range(21):
    f1 = fibonacci(n)
    f2 = fib_with_lucas(n)
    l1 = lucas(n)
    l2 = lucas_with_fib(n)
    print(n, f1, f2, l1, l2)
    if f1 != f2 or l1 != l2:
        all_ok = False
if all_ok:
    print("Все значения совпали")
else:
    print("Есть ошибки!")

# замер времени
max_n = 35
numbers = []
fib_times = []
lucas_times = []
fib_lucas_times = []

for n in range(1, max_n + 1):
    numbers.append(n)

    start = time.time()
    fibonacci(n)
    fib_times.append(time.time() - start)

    start = time.time()
    lucas(n)
    lucas_times.append(time.time() - start)

    start = time.time()
    fib_with_lucas(n)
    fib_lucas_times.append(time.time() - start)

    print("n =", n, "fibonacci:", round(fib_times[-1], 4), "lucas:", round(lucas_times[-1], 4),
          "fib_with_lucas:", round(fib_lucas_times[-1], 6))

plt.plot(numbers, fib_times, label="fibonacci()")
plt.plot(numbers, fib_lucas_times, label="fib_with_lucas()")
plt.xlabel("n")
plt.ylabel("Время, сек")
plt.title("Сравнение времени вычисления чисел Фибоначчи")
plt.legend()
plt.grid()
plt.savefig("graph_fib.png")
plt.show()
