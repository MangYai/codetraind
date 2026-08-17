def calculate_sum_and_average() -> None:
    result = []
    for i in range(5):
        number = int(input('Enter Number: '))
        result.append(number)
        
    Sum = sum(result)
    Average = sum(result) / len(result)
    
    print(Sum)
    print(Average)
calculate_sum_and_average()