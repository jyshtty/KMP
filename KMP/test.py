class Solution:
    def strStr(self, haystack, needle):
        if not len(needle):
            return

        LPS = [0] * len(needle)
        i = 1
        prevlps = 0

        while i < len(needle):
            if needle[i] == needle[prevlps]:
                LPS[i] = prevlps + 1
                prevlps += 1
                i += 1

            elif prevlps == 0:
                LPS[i] = 0
                i += 1

            else:
                prevlps = LPS[prevlps - 1]

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = LPS[j - 1]

            if j == len(needle):
                return i - len(needle)
        return -1




if __name__ == "__main__":
    haystack  = "mississippi"
    needle = "issip"
    obj = Solution()
    print(obj.strStr(haystack, needle))