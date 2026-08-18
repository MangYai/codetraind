from typing import List
def is_word_in_list(word_list: List[str], search_term: str) -> bool:
    return search_term in word_list
word_list = ["apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon",]

print(is_word_in_list(word_list, "cherry"))
print(is_word_in_list(word_list, "mango"))
#True
#False