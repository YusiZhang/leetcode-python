# leetcode log

### nine chapter review
风格：缩进 空格 变量名
coding习惯：异常检查，边界处理
沟通
测试
1. strstr:
https://leetcode.com/problems/implement-strstr/

## DFS 模板 
2. subsets:
https://leetcode.com/problems/subsets
递归： 看答案有多少个解。时间复杂度O(2^n)因为结果有2^n个

3. Permutations
https://leetcode.com/problems/permutations/

模板：什么时候输出，什么时候跳过

https://leetcode.com/problems/combinations/
https://leetcode.com/problems/combination-sum
https://leetcode.com/problems/combination-sum-ii
https://leetcode.com/problems/combination-sum-iii
https://leetcode.com/problems/combination-sum-iv (not really dfs)

https://leetcode.com/problems/subsets
https://leetcode.com/problems/subsets-ii

https://leetcode.com/problems/permutations
https://leetcode.com/problems/permutations-ii

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
https://leetcode.com/problems/restore-ip-addresses/

### Binary search
要找的数字可能在，也可能不存在数组当中

https://leetcode.com/problems/search-for-a-range
https://leetcode.com/problems/search-insert-position/
https://leetcode.com/problems/search-in-rotated-sorted-array/
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
https://leetcode.com/problems/search-a-2d-matrix/
https://leetcode.com/problems/search-a-2d-matrix-ii/ (not BS)
https://leetcode.com/problems/first-bad-version/
https://leetcode.com/problems/find-peak-element/

### sorted array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
https://leetcode.com/problems/merge-sorted-array/


### find kth
https://leetcode.com/problems/median-of-two-sorted-arrays/

### 3 step rotate
http://www.lintcode.com/en/problem/recover-rotated-sorted-array/
https://leetcode.com/problems/rotate-array/
https://leetcode.com/problems/reverse-words-in-a-string-ii/

### Linked list
dummy node: when head is not determined

https://leetcode.com/problems/remove-duplicates-from-sorted-list/
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

https://leetcode.com/problems/merge-two-sorted-lists/
https://leetcode.com/problems/partition-list/
https://leetcode.com/problems/reverse-linked-list/
https://leetcode.com/problems/reverse-linked-list-ii/
https://leetcode.com/problems/insertion-sort-list/

###DP
Triangle
https://leetcode.com/problems/triangle/
State: f[x][y] dist from 0,0 to x,y
function f[x][y] = f[x-1][y], f[x-1][y-1]
init: f[0][0] = a[0][0]
answer f[n-1][0...n-1]

matrix dp
https://leetcode.com/problems/unique-paths/
https://leetcode.com/problems/unique-paths-ii/
	unique path 统计方案个数，初始化(0,0), (i,0), (0,i)
	minimum path sum, 
sequence dp
	state: f[i]前i个位置、数字、字母
	climbing stairs
	jump game
	palindrome partitioning II
	word break
	LIS
two sequence dp
	state: f[i][j] 表示第一个seq的前i个字符，匹配上了第二个的前j个
	LCS: longest common subsequence
	longest common substring
	edit distance
	backpack
	k sum


特征
1. 
find max/min result
yes or no
count all possibile solution

2. cannot sort, cannot swap

unique path


###########
Graph
###########
clone graph

######linked list with random pointer/number

topological sorting

https://leetcode.com/problems/reconstruct-itinerary/
word ladder

search:
depth first search

######
stack
########

min-stack: two stack,
implement queue using stack
largest rectangle in histogram
construct maxtree






















