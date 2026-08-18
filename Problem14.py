from typing import List
def collect_unique_words(s) -> List[str]:
    result = []
    
    for word in s:
        if word not in result:
            result.append(word)
            
    return " ".join(result)

print(collect_unique_words(["apple", "banana", "apple", "cherry", "date", "banana", "elderberry"]))
# apple banana cherry date elderberry