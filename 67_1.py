def find_single_occurrence_numbers(numbers: list) -> list:
    result = {}
    for i in numbers:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
            
    final = []
    for a,b in result.items():
        if b == 1:
            final.append(a)
    return final
        


print(find_single_occurrence_numbers([4, 5, 6, 4, 7, 5, 8]))
print(find_single_occurrence_numbers([1, 2, 2, 3, 3, 4, 4]))
print(find_single_occurrence_numbers([1, 2, 3, 4, 5, 6]))
print(find_single_occurrence_numbers([1, 1, 1, 1, 1]))