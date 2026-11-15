class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for l in range(1, n // 2 + 1):
            if n % l == 0:
                ok = True
                for i in range(l, n):
                    if s[i] != s[i - l]:
                        ok = False
                        break
                if ok:
                    return True
        return False