# test_haralick.py
import unittest
import numpy as np
from haralick_descriptors import (
    grayscale, binarize, opening_filter, closing_filter,
    matrix_concurrency, haralick_descriptors, root_mean_square_error, normalize_array, euclidean
)

class TestHaralick(unittest.TestCase):
    def test_grayscale_binarize(self):
        img = np.array([[[108, 201, 72], [255, 11, 127]],
                        [[56, 56, 56], [128, 255, 107]]])
        gray = grayscale(img)
        binary = binarize(gray)
        self.assertEqual(binary.shape, gray.shape)

    def test_haralick_simple(self):
        img = np.array([[1, 0], [0, 1]])
        concurrency = matrix_concurrency(img, (0, 1))
        desc = haralick_descriptors(concurrency)
        self.assertEqual(len(desc), 8)


# ================ 5 CHOSEN MUTANTS AND THEIR ADDED TESTS ================

    def test_root_mean_square_error(self):
        # kills mutant that returns None
        result = root_mean_square_error(np.array([1, 2, 3]), np.array([6, 4, 2]))
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 3.1622776601683795, places=6)


    def test_normalize_array_mutant(self):
        arr = np.array([10, 20, 40, 80])
        normalized = normalize_array(arr, cap=10)

        # Hand-derived expected values
        # min = 10, max = 80, diff = 70
        # (x - 10) / 70 * 10
        expected = np.array([0.0, 1.42857143, 4.28571429, 10.0])

        np.testing.assert_allclose(normalized, expected, rtol=1e-6)


    def test_grayscale_ignores_alpha_channel(self):
        # RGBA image: alpha channel must be ignored
        img = np.array([[[255, 0, 0, 255]]], dtype=np.uint8)

        gray = grayscale(img)

        # Only RGB should be used:
        # 0.299 * 255 = 76.245 -> 76
        expected = np.array([[76]], dtype=np.uint8)

        np.testing.assert_array_equal(gray, expected)


    def test_euclidean_mutant(self):
        a = np.array([3, -4, 12])
        b = np.array([-1, 2, 5])

        dist = euclidean(a, b)

        # sqrt((4)^2 + (-6)^2 + (7)^2) = sqrt(16 + 36 + 49) = sqrt(101)
        expected = np.sqrt(101)

        self.assertAlmostEqual(dist, expected, places=6)

    def test_matrix_concurrency_mutant(self):
        img = np.array([
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ], dtype=np.uint8)

        coordinate = (0, 1)
        result = matrix_concurrency(img, coordinate)

        # Hand-derived expected matrix:
        # Only center pixel (1,1) is iterated.
        # base_pixel = 0
        # offset_pixel = img[1,2] = 1
        expected = np.zeros((2, 2))
        expected[0, 1] = 1.0

        np.testing.assert_allclose(result, expected, rtol=1e-6)


if __name__ == "__main__":
    unittest.main()