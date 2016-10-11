"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0 or not s:
            return []
        
        self.result = []
        self.dfs(0,s, "")
        
        return self.result
    #0. result ip address should have 4 ip parts.
    #1. each ip part should be less than 255
    #2. each ip part cannot be starting with 0, except only 0. For example, no "01.123.123.123"
    #3. each ip part cannot longer than 3 digits.
    def dfs(self, depth, source_string_leftover, current_ip_part):
        #0. result ip address should have 4 ip parts.
        if depth == 4:
            if source_string_leftover == "":
                self.result.append(current_ip_part[1:]) # remove the first "."
            return
        #3. each ip part cannot longer than 3 digits.
        for i in range(1, 4):
            # if i > len(s), s[:i] will make false!!!!
            if i <= len(source_string_leftover):                   
                #1. each ip part should be less than 255
                if int(source_string_leftover[:i]) <= 255:
                    # this will make the result like ".111.244.55.123", so you have to remove the first "." when add the ip to result set.
                    self.dfs(depth+1, source_string_leftover[i:], current_ip_part + "." + source_string_leftover[:i])
                #2. each ip part cannot be starting with 0, except only 0. For example, no "01.123.123.123"
                if source_string_leftover[0] == "0":
                    return
    
                
        