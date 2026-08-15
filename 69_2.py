def find_duplicate_chars_count(s: str) -> dict:
    check = {}
    result = {}
    for i in s:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1
            
    for a,b in check.items():
        if b > 1:
            result[a] = b
    return result

print(find_duplicate_chars_count("programming"))
print(find_duplicate_chars_count("mississippi"))
print(find_duplicate_chars_count("abcdefg"))
print(find_duplicate_chars_count("abacabad"))