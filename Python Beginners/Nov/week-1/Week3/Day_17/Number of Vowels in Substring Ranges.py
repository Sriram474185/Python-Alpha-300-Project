from typing import List

def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(words)
    prefix = [0] * (n + 1)
    for i in range(n):
        is_valid = 1 if (words[i][0] in vowels and words[i][-1] in vowels) else 0
        prefix[i + 1] = prefix[i] + is_valid
        
    ans = []
    for left, right in queries:
        ans.append(prefix[right + 1] - prefix[left])
        
    return ans
