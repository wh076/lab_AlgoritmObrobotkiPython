# Запуск тестов всех заданий
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    suite = unittest.TestSuite()
    for folder in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, folder)
        if folder.startswith("task") and os.path.isdir(path):
            sys.path.insert(0, path)
            suite.addTests(unittest.defaultTestLoader.discover(path, top_level_dir=path))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
