from typing import List
from typing import Dict
def count_word_occurrences(words: List[str]) -> Dict[str, int]:
    result = {}
    for word in words:
        if word.lower() in result:
            result[word.lower()] += 1
        else:
            result[word.lower()] = 1
    return result
    
    
print(count_word_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]))
#{'apple': 3, 'banana': 2, 'orange': 1}