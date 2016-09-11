class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        pathlen = {0:0}
        for line in input.splitlines():# split line eliminate "\n"
            name = line.lstrip('\t') # lstrip eliminate "\t"
            depth = len(line) - len(name)
            if "." in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth+1] = pathlen[depth] + len(name) + 1 # for every dir level, there need a "/" appended
        return maxlen

if __name__ == '__main__':
    """
    dir
      subdir1
      subdir2
        file.ext
    """
    # input = "dir/subdir2/subsubdir2/file2.ext"
    input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    solution = Solution()
    print solution.lengthLongestPath(input)
