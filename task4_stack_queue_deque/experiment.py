# Задание 4. Эксперимент: список Python и связный список
# Замеряем пару "вставка + удаление" у начала и у конца
# структуры из n элементов.
import os
import time

import matplotlib.pyplot as plt

from structures import Deque

# размеры структуры
SIZES = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
# сколько пар операций делаем для одного замера
REPEATS = 100
# замер повторяем несколько раз и берём минимум (как в timeit)
TRIES = 5


def make_deque(n):
    d = Deque()
    for i in range(n):
        d.addFront(i)
    return d


def timed(insert, remove):
    """Лучшее время одной пары операций в микросекундах."""
    best = None
    for _ in range(TRIES):
        t = time.perf_counter()
        for _ in range(REPEATS):
            insert(-1)
            remove()
        cur = (time.perf_counter() - t) / REPEATS * 1e6
        if best is None or cur < best:
            best = cur
    return best


def measure(n):
    py = list(range(n))
    d = make_deque(n)
    return {
        "list_front": timed(lambda x: py.insert(0, x), lambda: py.pop(0)),
        "linked_front": timed(d.addFront, d.removeFront),
        "list_rear": timed(py.append, py.pop),
        "linked_rear": timed(d.addRear, d.removeRear),
    }


def draw(results, path):
    blue, orange = "#2a78d6", "#eb6834"
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
    panels = [(axes[0], "front", "Вставка и удаление в начале"),
              (axes[1], "rear", "Вставка и удаление в конце")]
    for ax, side, title in panels:
        ax.plot(SIZES, [r["list_" + side] for r in results], "o-", color=blue,
                lw=2, ms=6, label="список Python")
        ax.plot(SIZES, [r["linked_" + side] for r in results], "s-",
                color=orange, lw=2, ms=6, label="связный список")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_title(title)
        ax.set_xlabel("n, элементов")
        ax.grid(True, which="major", color="#e0e0dc", lw=0.8)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axes[0].set_ylabel("время пары операций, мкс")
    axes[0].legend(frameon=False)
    fig.tight_layout()
    fig.savefig(path, dpi=150)


if __name__ == "__main__":
    results = []
    print(f"{'n':>7} | {'list нач.':>10} | {'связн. нач.':>11} | "
          f"{'list кон.':>10} | {'связн. кон.':>11}")
    for n in SIZES:
        r = measure(n)
        results.append(r)
        print(f"{n:>7} | {r['list_front']:>10.2f} | "
              f"{r['linked_front']:>11.2f} | {r['list_rear']:>10.2f} | "
              f"{r['linked_rear']:>11.2f}")
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, "experiment.png")
    draw(results, path)
    print("График сохранён:", path)
