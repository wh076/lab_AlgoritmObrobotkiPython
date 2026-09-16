import time
import timeit
import matplotlib.pyplot as plt


# Задание 1
def foo(n):
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1
        if divisors == 0:
            res.append(i)
    return res


print(foo(30))

sizes = list(range(100, 3001, 200))
times = []
for n in sizes:
    start = time.perf_counter()
    foo(n)
    times.append(time.perf_counter() - start)

plt.figure()
plt.plot(sizes, times, marker='o')
plt.xlabel('N')
plt.ylabel('время, с')
plt.title('Задание 1. foo(n)')
plt.grid(True)
plt.show()


# Задание 2
def is_palindrome_loop(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_slice(s):
    return s == s[::-1]


def make_string(n):
    half = 'a' * (n // 2)
    if n % 2 == 0:
        return half + half[::-1]
    return half + 'b' + half[::-1]


print(is_palindrome_loop("topot"), is_palindrome_slice("topot"))
print(is_palindrome_loop("python"), is_palindrome_slice("python"))

sizes = list(range(1000, 200001, 10000))
times_loop = []
times_slice = []
for n in sizes:
    s = make_string(n)

    start = time.perf_counter()
    is_palindrome_loop(s)
    times_loop.append(time.perf_counter() - start)

    start = time.perf_counter()
    is_palindrome_slice(s)
    times_slice.append(time.perf_counter() - start)

plt.figure()
plt.plot(sizes, times_loop, marker='o', label='цикл')
plt.plot(sizes, times_slice, marker='o', label='срез s[::-1]')
plt.xlabel('N (длина строки)')
plt.ylabel('время, с')
plt.title('Задание 2. Проверка палиндрома')
plt.legend()
plt.grid(True)
plt.show()


# Задание 3
a, b, c = 1, -5, -50
d = b ** 2 - 4 * a * c
n1 = (-b + d ** 0.5) / (2 * a)
n2 = (-b - d ** 0.5) / (2 * a)
print("Дискриминант:", d)
print("Корни:", n1, n2)


# Задание 4
sizes = list(range(10000, 200001, 10000))
times_list = []
times_dict = []
for n in sizes:
    lst = list(range(n))
    start = time.perf_counter()
    for i in range(100):
        del lst[0]
    times_list.append(time.perf_counter() - start)

    dct = {i: i for i in range(n)}
    start = time.perf_counter()
    for i in range(100):
        del dct[i]
    times_dict.append(time.perf_counter() - start)

plt.figure()
plt.plot(sizes, times_list, marker='o', label='список')
plt.plot(sizes, times_dict, marker='o', label='словарь')
plt.xlabel('N')
plt.ylabel('время 100 удалений, с')
plt.title('Задание 4. del: список и словарь')
plt.legend()
plt.grid(True)
plt.show()


# Задание 5
sizes = list(range(10000, 200001, 10000))
times_list = []
times_set = []
for n in sizes:
    lst = list(range(n))
    st = set(lst)
    t1 = timeit.timeit(lambda: -1 in lst, number=100)
    t2 = timeit.timeit(lambda: -1 in st, number=100)
    times_list.append(t1)
    times_set.append(t2)

plt.figure()
plt.plot(sizes, times_list, marker='o', label='список')
plt.plot(sizes, times_set, marker='o', label='множество')
plt.xlabel('N')
plt.ylabel('время 100 проверок, с')
plt.title('Задание 5. in: список и множество')
plt.legend()
plt.grid(True)
plt.show()
