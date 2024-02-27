def countAndSay(n):
    if n == 1 :
        return '1'
    if n == 2:
        return '11'
    
    return helperTwo(helperOne(countAndSay(n-1)))


def helperOne(tring):
    count_list = []
    count = 0
    for i in range(1,len(tring)):
        


def helperTwo(count_list):
    final_str = ''
    temp = ''
    for val in count_list:
        temp += str(val[1]) + str(val[0])
        final_str += temp
        temp = ''
    return final_str

countAndSay(4)