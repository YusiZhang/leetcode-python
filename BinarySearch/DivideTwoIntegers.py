# coding=utf-8
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        
        sum = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
        
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            """
            e.g. 36/4 --> sum一直加到32，之后无法再内层while循环一次。所以要在被除数里面抛去已经得到的结果，把剩下的36-32=4再进行一次除法
            """
            res += count

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        
        # return res
        return min(max(-2147483648, res), 2147483647)


    #similar solution, using bit manipulation
    def divide2(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

if __name__ == '__main__':
    solution = Solution()
    solution.divide2(36, 4)