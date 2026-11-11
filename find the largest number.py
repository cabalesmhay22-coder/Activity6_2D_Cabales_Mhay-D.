def find_largest(numbers):
    
    if len(numbers) == 1:
        return numbers[0]

    find_largest(numbers[1:])

    
    if numbers[0] > largest_rest:
        return numbers[0]
    else:
        return largest_rest