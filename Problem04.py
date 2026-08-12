def calculate_sum_and_average() -> None:
    numbers = []
    for i in range(5):
        number = float(input(f'Enter number {i + 1}: '))
        numbers.append(number)
        
    print(f"Sum: ", sum(numbers))
    print(f"Average: ", sum(numbers) / len(numbers))
    
calculate_sum_and_average()