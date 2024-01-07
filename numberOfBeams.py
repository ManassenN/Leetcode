def numberOfBeams(bank):
    length_col = len(bank)

    number_of_beams,i = 0,0
    j = i + 1
    number_of_ones_first_leg,number_of_ones_second_leg = 0,0
    
    while (j < length_col):
        if count_ones(bank[j]) == 0:
            j = j + 1
            continue
        else:
            number_of_ones_first_leg = count_ones(bank[i])
            number_of_ones_second_leg = count_ones(bank[j])
            number_of_beams += number_of_ones_first_leg * number_of_ones_second_leg
            i = j
            j+=1

    return  number_of_beams



def count_ones(string):
    count = 0
    for char in string:
        if char == '1':
            count += 1
    return count


bank = ["011001","000000","010100","001000"]
numberOfBeams(bank)