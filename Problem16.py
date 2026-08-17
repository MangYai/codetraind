from typing import List
def insert_at_front(words: List[str]) -> List[str]:
    result = []
    for word in words:
        result.insert(0, word)
    return result

print(insert_at_front(["apple", "banana", "cherry"]))