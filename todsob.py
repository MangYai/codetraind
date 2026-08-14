def calculate_stats(numbers):
    return sum(numbers), sum(numbers)/len(numbers), max(numbers), min(numbers)

total, avg, max_num, min_num = calculate_stats([5,10,15,20,25])

print(calculate_stats([5,10,15,20,25]))