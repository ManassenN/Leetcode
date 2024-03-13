def sum_numbers_in_range(a, b):
    total = 0
    for i in range(a, b + 1):
        total += i
    return total


def pivotInteger(n):
        i = 1
        while i < n:
            if sum_numbers_in_range(1,i) == sum_numbers_in_range(i,n):
                return i

            else:
                i = i + 1
                continue
pivotInteger(8)