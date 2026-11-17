def countVowelSubstrings(word: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    last_seen = {'a': -1, 'e': -1, 'i': -1, 'o': -1, 'u': -1}
    last_consonant = -1
    count = 0
    
    for i, char in enumerate(word):
        if char in vowels:
            last_seen[char] = i
            earliest_all_vowels = min(last_seen.values())
            
            if earliest_all_vowels > last_consonant:
                count += earliest_all_vowels - last_consonant
        else:
            last_consonant = i
            
    return count
