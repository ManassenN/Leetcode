def sequential_digits(low, high):
    result = []

    for length in range(len(str(low)), len(str(high)) + 1):
        for start in range(1, 10 - length + 1):
            num = int("".join(str(digit) for digit in range(start, start + length)))
            if low <= num <= high:
                result.append(num)

    return sorted(result)

# Example usage:
low = 100
high = 300
result_list = sequential_digits(low, high)
print(result_list)
