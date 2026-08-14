from typing import Tuple
def separate_by_index(s: str) -> Tuple[str, str]:
    even_chars = s[0::2]
    odd_chars = s[1::2]
    return (even_chars, odd_chars)

print(separate_by_index("Hello World"))