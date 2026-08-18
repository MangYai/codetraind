def contains_vowel(s: str) -> bool:
    vowel = ['a','e','i','o','u']
    
    for ch in s.lower():
        if ch in vowel:
            return True
    return False

print(contains_vowel("Hello World"))
#True