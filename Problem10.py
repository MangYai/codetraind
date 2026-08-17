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