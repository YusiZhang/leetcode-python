class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False
        left, right = 1, num
        
        while left <= right:
            mid = left + (right-left)/2
            t = mid * mid
            if t > num:
                right = mid-1
            elif t < num:
                left = mid+1
            else:
                return True
        return False
        
"""
public boolean isPerfectSquare(int num) {
  if (num < 1) return false;
  for (int i = 1; num > 0; i += 2)
    num -= i;
  return num == 0;
}

public boolean isPerfectSquare(int num) {
  if (num < 1) return false;
  long left = 1, right = num;// long type to avoid 2147483647 case

  while (left <= right) {
    long mid = left + (right - left) / 2;
    long t = mid * mid;
    if (t > num) {
      right = mid - 1;
    } else if (t < num) {
      left = mid + 1;
    } else {
      return true;
    }
  }

  return false;
}

boolean isPerfectSquare(int num) {
  if (num < 1) return false;
  long t = num / 2;
  while (t * t > num) {
    t = (t + num / t) / 2;
  }
  return t * t == num;
}
"""