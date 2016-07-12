class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        return ''.join('%d:' % len(s) + s for s in strs)



    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(strs))

if __name__ == '__main__':
    codec = Codec()
    inputs = ["str31", "strww2", "str3"]
    encoded = codec.encode(inputs)
    print encoded
    # 5:str316:strww24:str3

    decoded = codec.decode(encoded)
    print decoded
    # ['str31', 'strww2', 'str3']
