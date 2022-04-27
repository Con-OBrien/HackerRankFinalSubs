# This is my solution for AlgoDaily problem Zeros to the End
# Located at https://algodaily.com/challenges/zeros-to-the-end

def zeros_to_the_end(nums):
    nonZeros = []
    for item in nums[::-1]:
      if item not in nonZeros:
        if item != 0:
          nonZeros.append(item)
          nums.insert(0, nums.pop(nums.index(item)))
    return nums


print(zeros_to_the_end([1, 0, 2, 0, 4, 0]))


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert zeros_to_the_end([1, 0, 2, 0, 4, 0]) == [1, 2, 4, 0, 0, 0]
        print(
            "PASSED: zeros_to_the_end([1, 0, 2, 0, 4, 0]) should get us [1, 2, 4, 0, 0, 0]"
        )

    def test_2(self):
        assert zeros_to_the_end([4, 13, 0, 2, 0, 0, 15, 0]) == [4, 13, 2, 15, 0, 0, 0, 0]
        
        print(
            "PASSED: zeros_to_the_end([4, 13, 0, 2, 0, 0, 15, 0]) should get us [4, 13, 2, 15, 0, 0, 0, 0]"
        )

    def test_3(self):
        assert zeros_to_the_end([0]) == [0]
        print("PASSED: zeros_to_the_end([0]) should get us [0]")

    def test_4(self):
        assert zeros_to_the_end([]) == []
        print("PASSED: zeros_to_the_end([]) should get us []")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
