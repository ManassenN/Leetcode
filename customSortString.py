def customSortString(order,s):
    output = ''

    i = 0 
    while True:
        if i == len(order):
            break
        else: 
            if order[i] in s:
                output += order[i]
                i = i + 1
            else:
                i = i + 1    

    i = 0
    while True:
        if i == len(s):
            return output
        else:
            if s[i] in output:
                i = i + 1
                continue
            else:
                output += s[i]
                i = i + 1
order = 'bcafg'
s = 'abcd'
customSortString(order,s)