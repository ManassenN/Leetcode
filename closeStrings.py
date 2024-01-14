def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    if set(word1)!=set(word2):
        return False
    # find string structures
    structure1 = {char: word1.count(char) for char in set(word1)}
    structure2 = {char: word2.count(char) for char in set(word2)}
    
    structure1_sorted = {k: v for k, v in sorted(structure1.items(), key=lambda item: item[1])}
    structure2_sorted = {k: v for k, v in sorted(structure2.items(), key=lambda item: item[1])}

    for val1,val2 in zip(structure1_sorted.values(),structure2_sorted.values()):
        if val1 != val2:
            return False

    return print(True)    


closeStrings("cabbba","abbccc")