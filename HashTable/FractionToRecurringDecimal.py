class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
        	return "0"
        fraction = []
        # if either one is negative (not both)
        # if numerator < 0 ^ denominator < 0:
        # 	fraction.append("-")
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            fraction.append("-")
        # convert to long or else abs(-2147483648) overflows
        dividend = long(abs(numerator))
        divisor = long(abs(denominator))
        fraction.append(str(dividend/divisor))

        reminder = dividend % divisor
        if reminder == 0:
        	return "".join(fraction)
        fraction.append(".")
        reminder_position = {}
        while reminder != 0:
        	if reminder in reminder_position:
        		fraction.insert(reminder_position[reminder], "(")
        		fraction.append(")")
        		break
        	reminder_position[reminder] = len(fraction)
        	reminder *= 10
        	fraction.append(str(reminder/divisor))
        	reminder %= divisor

        return ''.join(fraction)
        