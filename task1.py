import random
import time
import sys
import matplotlib.pyplot as plt

# на отсортированном списке быстрая сортировка уходит глубоко в рекурсию
sys.setrecursionlimit(10000)


def selection_sort(arr):
    arr = arr[:]  # копия, чтобы не портить исходный список
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def quick_sort(arr):
    # базовый случай
    if len(arr) < 2:
        return arr
    # рекурсивный случай
    pivot = arr[0]
    less = []
    greater = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            less.append(arr[i])
        else:
            greater.append(arr[i])
    return quick_sort(less) + [pivot] + quick_sort(greater)


def measure(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return end - start


def make_list(size, case):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, 10000))
    if case == "sorted":
        arr.sort()
    if case == "reversed":
        arr.sort()
        arr.reverse()
    return arr


def draw_graph(sizes, sel_times, quick_times, title, file_name):
    plt.figure()
    plt.plot(sizes, sel_times, label="Сортировка выбором")
    plt.plot(sizes, quick_times, label="Быстрая сортировка")
    plt.xlabel("Размер списка")
    plt.ylabel("Время, сек")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.savefig(file_name)


sizes = []
for size in range(100, 2001, 100):
    sizes.append(size)

cases = ["random", "sorted", "reversed"]
titles = ["Случайный список", "Отсортированный список", "Список в обратном порядке"]

for k in range(len(cases)):
    case = cases[k]
    sel_times = []
    quick_times = []
    print("Случай:", titles[k])
    for size in sizes:
        arr = make_list(size, case)
        t1 = measure(selection_sort, arr)
        t2 = measure(quick_sort, arr)
        sel_times.append(t1)
        quick_times.append(t2)
        print("размер", size, "выбором:", round(t1, 4), "быстрая:", round(t2, 4))
    draw_graph(sizes, sel_times, quick_times, titles[k], "graph_" + case + ".png")

plt.show()
