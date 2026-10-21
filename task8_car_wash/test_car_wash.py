import random
import unittest

import car_wash
from car_wash import Car, WashPost, arrival_prob, simulation


class TestCarWash(unittest.TestCase):
    def test_arrival_prob(self):
        # 0.6 * 5 = 3 машины в час -> 3 / 60 = 0.05
        self.assertAlmostEqual(arrival_prob(0.6), 0.05)
        self.assertAlmostEqual(arrival_prob(0.8), 4 / 60)

    def test_car_wait(self):
        self.assertEqual(Car(10).wait_time(25), 15)

    def test_post(self):
        post = WashPost()
        self.assertFalse(post.busy())
        post.start_next(Car(0))
        self.assertGreaterEqual(post.time_left, car_wash.WASH_MIN)
        self.assertLessEqual(post.time_left, car_wash.WASH_MAX)
        for _ in range(car_wash.WASH_MAX):
            post.tick()
        self.assertFalse(post.busy())

    def test_no_cars(self):
        self.assertEqual(simulation(0), (0, 0, 0))

    def test_car_every_minute(self):
        # машины приезжают каждую минуту - очередь растёт
        random.seed(0)
        avg, left, served = simulation(1.0, minutes=60)
        self.assertGreater(left, 40)
        self.assertGreater(avg, 0)
        self.assertEqual(left + served, 60)

    def test_two_posts_better(self):
        random.seed(5)
        w1, left1, _ = car_wash.many_runs(arrival_prob(0.8), 1, runs=30)
        random.seed(5)
        w2, left2, _ = car_wash.many_runs(arrival_prob(0.8), 2, runs=30)
        self.assertLess(w2, w1)
        self.assertLessEqual(left2, left1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
