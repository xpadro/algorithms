from algorithms.easy.reverse_integer import Solution

def test_reverse_integer_positive():
    solution = Solution()
    assert solution.reverse(123) == 321, "Should be 321"

def test_reverse_integer_negative():
    solution = Solution()
    assert solution.reverse(-123) == -321, "Should be -321"

def test_reverse_integer_trailing_zero():
    solution = Solution()
    assert solution.reverse(120) == 21, "Should be 21"

def test_reverse_integer_overflow1():
    solution = Solution()
    assert solution.reverse(1534236469) == 0, "Should be 0"

def test_reverse_integer_overflow2():
    solution = Solution()
    assert solution.reverse(1563847412) == 0, "Should be 0"