class Solution(object):
    # def reverse(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     if x<0:
    #         x=self.rev(x)
    #         if x>2147483648:
    #             return 0
    #         return int("-"+str(x))
    #     else:
    #         x=self.rev(x)
    #         if x>2147483647:
    #             return 0
    #         return x
    
    # def rev(self, x):
    #     x=str(abs(x))
    #     x=x[::-1]
    #     return int(x)
    def reverse(self, x):
        ret = 0
    
        if x==0:
            return 0
    
        remains = abs(x)
        sign = -1 if x < 0 else 1
    
        while(True):
            # remains is not zero
            digit = remains % 10
            remains = remains / 10
            ret = ret * 10 + digit
            if remains == 0:
                break
    
        ret *= sign
        if abs(ret) > 0x7FFFFFFF:
            return 0
        else:
            return ret