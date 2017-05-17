#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ints(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_reverse(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)
    def test_same(self):
        self.assertEqual(max_integer([11, 11]), 11)
    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def test_int_bool(self):
        self.assertEqual(max_integer([True, 98, False, 402]), 402)
    def test_big(self):
        self.assertEqual(max_integer([-4579, -1, 84594, 98989898989899889898989898998889898989]), 98989898989899889898989898998889898989)
    def test_float(self):
        self.assertEqual(max_integer([0.9, 1.2, 1.3]), 1.3)
    def test_int_float(self):
        self.assertEqual(max_integer([0.9, 1.2, 2]), 2)
    def test_bool(self):
        self.assertEqual(max_integer([True, False]), True)
    def test_char(self):
        self.assertEqual(max_integer('c'), 'c')
    def test_chars(self):
        self.assertEqual(max_integer(['a', 'b', 'c']),'c')
    def test_string(self):
        self.assertEqual(max_integer("string"), 't')
    def test_strings(self):
        self.assertEqual(max_integer(["bye", "hi"]),'hi')
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    def test_none_list(self):
        with self.assertRaises(TypeError):
            max_integer([None, 2])
    def test_mix_list(self):
        with self.assertRaises(TypeError):
            max_integer(['z', 1.2, 2])
    def test_str_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([-27, 23, "hi"])

if __name__ == '__main__':
    unittest.main()
