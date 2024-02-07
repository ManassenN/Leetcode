def frequencySort(s: str) -> str: 
    char_count = {char: s.count(char) for char in s}

    sorted_dict_values = sorted(char_count.items(), key=lambda x: -x[1])
    t = ''.join([char[0]*char[1] for char in sorted_dict_values])

    return t

print(frequencySort('Aabb'))