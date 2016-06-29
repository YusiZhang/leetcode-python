"""
 Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # return bin(int(a,2) + int(b,2))[2:]
        a = a[::-1]
        b = b[::-1]
        sum = ""
        carry = 0
        n = max(len(a), len(b))
        for i in xrange(n):
            if i < len(a):
                carry += int(a[i])
            if i < len(b):
                carry += int(b[i])
            sum += str(carry%2)  #!!!!!
            carry /= 2           #!!!!!! 
        if carry > 0:
            sum += "1"
        return sum[::-1]
"""
class Solution {
public:
    string addBinary(string a, string b) {
        reverse(a.begin(),a.end());
        reverse(b.begin(),b.end());
        string sum;
        int carry = 0;
        int n = max(a.size(),b.size());
        for(int i=0; i<n; i++) {
            if(i<a.size()) carry+=(a[i]-'0');
            if(i<b.size()) carry+=(b[i]-'0');
            sum.push_back(carry%2+'0');
            carry/=2; 
        }
        if(carry) sum.push_back('1');
        reverse(sum.begin(),sum.end());
        return sum;
    }
};
"""