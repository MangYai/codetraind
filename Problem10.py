def character_frequency(*args: str) -> dict:
    check = {}
    for s in args:
        for i in s:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
    return check

print(character_frequency(
    "hello",
    "world",
    "test",
    "case",
    "example"
))
#{'h': 1, 'e': 5, 'l': 4, 'o': 2, 'w': 1, 'r': 1, 'd': 1, 't': 2, 's': 2, 'c': 1, 'a': 2, 'x': 1, 'm': 1, 'p': 1}