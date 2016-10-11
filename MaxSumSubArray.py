class Kadane(object):
    def getMaxSumSubArray(self, nums, k = None):
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            # get max sum of all
            if not k:
                if cur_sum > max_sum:
                    max_sum = cur_sum
            # get max sum that smaller or equal than k
            else:
                if cur_sum > max_sum and cur_sum <= k:
                    max_sum = cur_sum

        return max_sum

if __name__ == '__main__':
    kadane = Kadane()
    print kadane.getMaxSumSubArray([-1,3,0,-10,4,5])

    print kadane.getMaxSumSubArray([-1,3,0,-10,4,5], k=5)


