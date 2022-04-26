# This is my solution for AlgoDaily problem Find Missing Number in Array
# Located at https://algodaily.com/challenges/find-missing-number-in-array

def missing_numbers(num_arr):
    missing = []
    allV =[]
    i = 0
    finalVal = num_arr[-1]
    firstVal = num_arr[0]
    
    while firstVal <= finalVal:
      allV.append(firstVal)
      firstVal += 1
      i += 1
    missing = list(sorted(set(allV) - set(num_arr)))

    return missing

import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert missing_numbers([0, 1, 3]) == [2]
        print("PASSED: missing_numbers([0, 1, 3]) should equal [2]")

    def test_2(self):
        assert missing_numbers([10, 11, 14, 17]) == [12, 13, 15, 16]
        print(
            "PASSED: missing_numbers([10, 11, 14, 17]) should equal [ 12, 13, 15, 16 ]"
        )

    def test_3(self):
        assert missing_numbers([3, 7, 9, 19]) == [
            4,
            5,
            6,
            8,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
        ]
        print(
            "PASSED: missing_numbers([3, 7, 9, 19]) should equal [ 4, 5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18 ]"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
