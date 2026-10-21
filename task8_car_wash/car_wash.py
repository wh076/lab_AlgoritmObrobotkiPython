# Задание 8. Симуляция очереди машин на автомойку (вариант 1)
# По примеру симуляции "Задания на печать" из лекции:
# Task -> Car, Printer -> WashPost.
#
# Источник параметров: "Бизнес-план автомойки",
# Рубцовский институт (филиал) АлтГУ, 2015:
# rb.asu.ru/public/uploads/1435726734_Biznes_plan_avtomoyki_2015PR.pdf
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "task4_stack_queue_deque"))
from structures import Queue

# один шаг симуляции = 1 минута
# режим работы с 10:00 до 20:00 (источник) -> 10 часов
WORK_MINUTES = 10 * 60
# мойка кузова длится 10-15 минут (источник), берём равномерно
WASH_MIN = 10
WASH_MAX = 15
# пропускная способность ручной мойки - 5 машин в час (источник)
CARS_PER_HOUR_MAX = 5
# загрузка мойки: 60% в будни и 80% в выходные (источник, таблица доходов)
LOAD_WEEKDAY = 0.6
LOAD_WEEKEND = 0.8
# сколько раз повторяем симуляцию
RUNS = 100
SEED = 1


def arrival_prob(load):
    """Вероятность приезда машины за одну минуту."""
    # машин в час = загрузка * 5, делим на 60 минут
    return load * CARS_PER_HOUR_MAX / 60


class Car:
    def __init__(self, time):
        self.arrival = time

    def wait_time(self, now):
        return now - self.arrival


class WashPost:
    """Один пост мойки."""

    def __init__(self):
        self.current = None
        self.time_left = 0

    def busy(self):
        return self.current is not None

    def tick(self):
        if self.current is not None:
            self.time_left -= 1
            if self.time_left <= 0:
                self.current = None

    def start_next(self, car):
        self.current = car
        self.time_left = random.randint(WASH_MIN, WASH_MAX)


def new_car(prob):
    # приехала ли машина в эту минуту
    return random.random() < prob


def simulation(prob, posts=1, minutes=WORK_MINUTES):
    """Один рабочий день.
    Возвращает (среднее ожидание, осталось в очереди, обслужено)."""
    queue = Queue()
    wash = [WashPost() for _ in range(posts)]
    waits = []
    for minute in range(minutes):
        if new_car(prob):
            queue.enqueue(Car(minute))
        for post in wash:
            if not post.busy() and not queue.isEmpty():
                car = queue.dequeue()
                waits.append(car.wait_time(minute))
                post.start_next(car)
            post.tick()
    avg = sum(waits) / len(waits) if waits else 0
    return avg, queue.size(), len(waits)


def many_runs(prob, posts, runs=RUNS):
    """Средние значения за runs рабочих дней."""
    total_wait = total_left = total_served = 0
    for _ in range(runs):
        w, left, served = simulation(prob, posts)
        total_wait += w
        total_left += left
        total_served += served
    return total_wait / runs, total_left / runs, total_served / runs


if __name__ == "__main__":
    random.seed(SEED)
    print(f"Рабочий день {WORK_MINUTES} мин, мойка {WASH_MIN}-{WASH_MAX} мин, "
          f"{RUNS} запусков")
    print(f"{'день':<9}| {'машин/ч':>7} | {'постов':>6} | "
          f"{'ожидание, мин':>13} | {'осталось':>8} | {'обслужено':>9}")
    for name, load in [("будни", LOAD_WEEKDAY), ("выходные", LOAD_WEEKEND)]:
        prob = arrival_prob(load)
        for posts in (1, 2):
            w, left, served = many_runs(prob, posts)
            print(f"{name:<9}| {prob * 60:>7.1f} | {posts:>6} | {w:>13.1f} | "
                  f"{left:>8.2f} | {served:>9.1f}")
