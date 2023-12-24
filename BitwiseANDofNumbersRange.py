def rangeBitwiseAnd(left: int, right: int) -> int:
    result = left
    for element in range(left + 1, right + 1):
        result &= element
    return result

print(rangeBitwiseAnd(0,0))