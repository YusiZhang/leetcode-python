60.Permutation Sequence
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

1."123"

2."132"

3."213"

4."231"

5."312"

6."321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

HOW?
If n=6 and k=400, and the Kth number is represented as A=a1a2a3a4a5a6. ax represents the index of array [1,2,3...n]. 
Need to understand why a1=k/(n-1)!!!!
The number of possible ways to generate a number A starting with a1, is 5! which is (n-1)!. In this case, k=400, and (n-1)!=5!=120. so a1=400/120=3. 
You can understand "3" as whatever a1 is, it should at lease hold 3 times of 5!. So the a1 is 4. Because if a1 is 4, then the first/minimum number is 412356.
And this number is at least larger than all numbers starting with 1/2/3. For example, the largest number staring with 3 is 365421, which is less than 412356.
So the amount of numbers that are smaller than 412356 is 3*5!. And that is why the 400th number should be starting with "4".

If we put numbers 1~n into an array [1,2,3,4,5...n], then the a1=k/(n-1)!=400/5!=3 is actually the index of value 4 in the array. 
In the code, we start k from k-1. So that it is easier to represent the index. It makes no difference if k=400 and n-1=5. But if k=120, then the a1=120/5=1.
However, we should not choose array[1]=2 to be the leading number. Instead, we should choose array[0]=1. So the number should be 123456.
Another example would be k=121, so first we do k=k-1=120. so the a1_index=120/120=1. Then the leading number should be "2"

Here are codes:

```
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        k = k-1
        factor = 1
        for i in range(1,n):
            factor *= i #this will give you (n-1)!
        nums = [1,2,3,4,5,6,7,8,9]
        for i in reversed(range(n)):
            current_number = num[k/factor]
            result += str(current_number)
            num.remove(current_number)
            if i != 0:
                k %= factor
                factor /= i
        return result
```
