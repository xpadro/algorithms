from algorithms.easy.two_sum import Solution

def test_two_sum():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1], "Should be [0, 1]"