"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code". 
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # DP solution
        # d = [False] * len(s)    
        # for i in range(len(s)):
        #     for w in wordDict:
        #         if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
        #             d[i] = True
        # return d[-1]
        
        # BFS solution
        if s in wordDict:
            return True
        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)
        while queue:
            curIdx = queue.popleft()
            for i in xrange(curIdx+1, len(s)+1):
                if i in visited:
                    continue
                if s[curIdx:i] in wordDict:
                    if i == len(s):
                        return True
                    queue.append(i)
                    visited.add(i)
        return False
        
"""
public boolean wordBreak(String s, Set<String> dict) {
    if (dict.contains(s)) return true;
    Queue<Integer> queue = new LinkedList<Integer>();
    queue.offer(0);
    // use a set to record checked index to avoid repeated work.
    // This is the key to reduce the running time to O(N^2).
    Set<Integer> visited = new HashSet<Integer>();
    visited.add(0);
    while (!queue.isEmpty()) {
        int curIdx = queue.poll();
        for (int i = curIdx+1; i <= s.length(); i++) {
            if (visited.contains(i)) continue;
            if (dict.contains(s.substring(curIdx, i))) {
                if (i == s.length()) return true;
                queue.offer(i);
                visited.add(i);
            }
        }
    }
    return false;
}
"""