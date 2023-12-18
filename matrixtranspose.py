def transpose(matrix):
    trans_matrix = []
    length = len(matrix[0])

    temp = []
    for i in range(length):
        for mlist in matrix:
            temp.append(mlist[i])

        trans_matrix.append(temp)
        temp = []
    return trans_matrix