from file_loader.file_loader import load_lists_from_file
from algorithm1.algorithm1 import enumeration
import unittest


class Algorithm1Test(unittest.TestCase):

    def test_algorithm1_providedInput_shouldReturnMatchProvidedOutput(self):
        test_lists = load_lists_from_file('Problems/MSS_TestProblems-1.txt')
        expected = [(3, 14, 34), (0, 5, 30), (6, 12, 50), (2, 7, 187), (0, 4, 7), (0, 3, 210), (3, 7, 6)]
        actual = []
        for test_list in test_lists:
            actual.append(enumeration(test_list))
        message = "For the instructor provided input, should return the max sum of the provided output \n%s, but was \n%s" % (expected, actual)

        self.assertEqual(expected, actual, message)
