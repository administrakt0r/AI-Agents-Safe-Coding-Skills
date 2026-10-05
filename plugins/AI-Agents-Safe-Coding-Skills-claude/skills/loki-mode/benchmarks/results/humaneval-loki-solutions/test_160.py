import unittest
import importlib.util
import os

# Dynamically import 160.py
file_path = os.path.join(os.path.dirname(__file__), "160.py")
spec = importlib.util.spec_from_file_location("solution_160", file_path)
solution_160 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_160)
do_algebra = solution_160.do_algebra


class TestDoAlgebra(unittest.TestCase):
    def test_example(self):
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
        self.assertEqual(do_algebra(operator, operand), 9)

    def test_floor_division_and_pow(self):
        operator = ['//', '**']
        operand = [100, 2, 3]
        # 100 // 2 ** 3 = 100 // 8 = 12
        self.assertEqual(do_algebra(operator, operand), 12)

    def test_addition_subtraction(self):
        operator = ['+', '-']
        operand = [10, 20, 5]
        # 10 + 20 - 5 = 25
        self.assertEqual(do_algebra(operator, operand), 25)

    def test_injection_attempt(self):
        operator = ['+', '__import__("os").system("echo hacked") +']
        operand = [1, 2, 3]
        with self.assertRaises(Exception):
            do_algebra(operator, operand)


if __name__ == "__main__":
    unittest.main()
