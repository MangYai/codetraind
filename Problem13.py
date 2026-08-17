def reverse_string(s: str) -> str:
    char = list(s)
    char.reverse()
    return "".join(char)

print(reverse_string("Hello World"))
