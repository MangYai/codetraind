def find_repeated_substrings(s: str) -> list:
    check = []
    result = {}
    for i in range(len(s)+1):
        for a in range(2+i, len(s)+1):
            check.append(s[i:a])
            
    for a in check:
        if a in result:
            result[a] += 1
        else:
            result[a] = 1
    return [a for a,b in result.items() if b > 1]     


print(find_repeated_substrings("banana"))
print(find_repeated_substrings("abcdefg"))
print(find_repeated_substrings("abcabcabc"))
print(find_repeated_substrings("aaaa"))