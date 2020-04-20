'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output: 321

Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the 
reversed integer overflows.
'''
class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        string_num = str(x)

        if string_num[0] == "-":
            string_num = string_num.replace("-", "")
            negative = True
        
        reversed_list = list(reversed(list(string_num)))

        if negative:
            reversed_list.insert(0, "-")
                    
        result = int(''.join(map(str, reversed_list)))
        
        if result.bit_length() <= 31:
            return result
        else:
            return 0