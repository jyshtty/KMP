


# Brute force way - to check pattern is present in string -
# check text[i+j] == pat[j]


def search(pat, txt):
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while (j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            print("Pattern found at index ", i)


# Driver Code
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)

# In KMP, you create a longest prefix suffix first - LPS
# and  compare charater by character of string with pattern.
#     If it doesnt match you don't break as you do in brute force.
#     instead you make j  = lps[prev_lps - 1]
#
# To create LPS -
# # So the Idea is you start with 2 pointer
# # prev_lps = 0 which is pointer to index of prev LPS
# # i = 0 points to current.

def search_pattern(haystack, needle):
    if not len(needle):
        return
    lps = [0] * len(needle)
    prevLPS = 0
    i = 1

    # Step 1 - Creation of LPS array
    while i < len(needle):
        if needle[i] == needle[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1

        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]

    # Step 2 - Checking index of first occurance of match using LPS
    i = 0 # index of haystack
    j = 0 # index of needle

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

        if j == len(needle): # which means there is a match
            return i-len(needle)
    return -1



haystack  = "mississippi"
needle = "issip"
print(search_pattern(haystack, needle))


