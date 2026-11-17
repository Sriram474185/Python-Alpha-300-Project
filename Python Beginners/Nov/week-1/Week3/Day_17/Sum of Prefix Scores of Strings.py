from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def sumPrefixScores(words: List[str]) -> List[int]:
    root = TrieNode()
    
    for word in words:
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1
            
    ans = []
    for word in words:
        curr = root
        score = 0
        for char in word:
            curr = curr.children[char]
            score += curr.count
        ans.append(score)
        
    return ans
