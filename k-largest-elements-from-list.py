# This is my solution for AlgoDaily problem K Largest Elements From List
# Located at https://algodaily.com/challenges/k-largest-elements-from-list

def k_largest(nums, k):
    # fill in
    nums.sort()
   
    largestNums = nums[-k:]
    print(nums)
    print(largestNums)
    
    return largestNums
   


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert sorted(k_largest([5, 16, 7, 9, -1, 4, 3, 11, 2], 3)) == sorted(
            [9, 11, 16]
        )
        print(
            "PASSED: assert `k_largest([5, 16, 7, 9, -1, 4, 3, 11, 2], 3)` returns `[9, 11, 16]`"
        )

    def test_2(self):
        assert sorted(k_largest([29, 17, 9, -1, -3, 11, 2], 6)) == sorted(
            [29, 17, 11, 9, 2, -1]
        )
        print(
            "PASSED: assert `k_largest([29, 17, 9, -1, -3, 11, 2], 6)` returns `[29, 17, 11, 9, 2, -1]`"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 2/2 tests passed!")
