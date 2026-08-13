def is_armstrong(number):
    text = str(number)
    digit_count = len(text)
    total = 0
    
    for char in text:
        digit = int(char)
        total += digit ** digit_count
        
    if total == number:
        return True
    else:
        return False


print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))