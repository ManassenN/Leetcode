def frequencySort(s: str) -> str: 
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Sort the characters based on their frequency in decreasing order
        sorted_chars = sorted(char_count, key=lambda x: char_count[x], reverse=True)

        # Construct the sorted string
        sorted_string = ''.join([char * char_count[char] for char in sorted_chars])

        return sorted_string

frequencySort('tree')