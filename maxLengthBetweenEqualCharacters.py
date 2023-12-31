def maxLengthBetweenEqualCharacters(s):
    char_positions = {}  # Dictionary to store the positions of characters
    max_length = -1

    for i, char in enumerate(s):
        if char in char_positions:
            # Update the maximum length if a duplicate character is found
            max_length = max(max_length, i - char_positions[char] - 1)
        else:
            # Store the position of the character
            char_positions[char] = i

    return max_length

# Example usage:
s = "cabbac"
result = maxLengthBetweenEqualCharacters(s)
print(result)
