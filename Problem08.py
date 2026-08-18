from typing import List
def average_length_of_strings(strings: List[str]) -> float:
    total_length = 0
    for s in strings:
        total_length += len(s)
    average_length = total_length / len(strings)
    return average_length
        
word = ["apple", "banana", "cherry", "date", "elderberry"]    
print(average_length_of_strings(word))
# output 6.2