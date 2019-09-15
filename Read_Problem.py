
'''in this function I read the txt file and save it in a list without z, end, and spaces'''
def read_file():

    file_name = input('Give the file name')

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            ch_list1 = []
            i = 0
            counter_n = 0
            for line in f:
                for ch in line:
                    i += 1
                    if ch == ' ':
                        continue
                    elif ch == 'd' or ch == 'D' or ch == 'e' or ch == 'E' or ch == 'z' or ch == 'Z':
                        continue
                    elif (ch == 'n' or ch == 'N') and i > 4:
                        continue
                    ch_list1.append(ch)
            return ch_list1
    except EOFError:
        print("ERROR")


'''find if the input file is in the right format and return one boolean_ flag and if my problem is min or max'''
def error_finder(list_ch):

    min_max = 0  # if it's -1 the problem is min otherwise if it's 1 the problem is max
    flag1 = True
    flag_f = True
    counter1 = 0
    counter2 = 0
    x_counter = 0
    sign_counter = 0
    line_counter = 0
    symbol_counter = 0

    for ch in range(len(list_ch)):

        # in the next line I check if max or min exists in my problem
        if flag1:
            if (list_ch[0] == 'm' or list_ch[0] == 'M') and \
                    (list_ch[1] == 'a' or list_ch[1] == 'A') and (list_ch[2] == 'x' or list_ch[2] == 'X'):
                min_max = 1
                flag1 = False
            elif (list_ch[0] == 'm' or list_ch[0] == 'M') and \
                    (list_ch[1] == 'i' or list_ch[1] == 'I') and (list_ch[2] == 'N' or list_ch[2] == 'n'):
                min_max = -1
                flag1 = False

            else:
                print('Error! max or min does not exist in the problem.')
                flag_f = False
                break

        # in the next lines I check if "st" exist in my problem
        if counter1 == 1:
            counter2 += 1
            if not ((list_ch[ch] == 's' and list_ch[ch + 1] == 't') or (list_ch[ch] == 's.' and list_ch[ch + 1] == 't.') \
                    or (list_ch[ch] == 'S' and list_ch[ch + 1] == 'T') or (
                            list_ch[ch] == 'S.' and list_ch[ch + 1] == 'T.')) \
                    and counter2 < 2:
                print("Error! st do not exist in the problem!")
                flag_f = False
                break
        if list_ch[ch] == '\n' and counter2 < 3:
            counter1 += 1

        # in the next lines I check if all my factors have a sign in Z
        if list_ch[ch] == 'x':
            x_counter += 1

        if list_ch[ch] == '+' or list_ch[ch] == '-':
            sign_counter += 1

        if list_ch[ch] == '\n':
            line_counter += 1

        if list_ch[ch] == '=':
            symbol_counter += 1

    if min_max == 1:
        if x_counter - 1 != sign_counter:
            print("Error! Signs missings")
            flag_f = False
    elif min_max == -1:
        if x_counter != sign_counter:
            print("Error! Signs missings")
            flag_f = False
    if line_counter - 2 != symbol_counter:
        print("Error! Symbols missing")
        flag_f = False

        if list_ch[ch] == '=':
            if list_ch[ch + 1] not in ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('Error! The right part of the equation does not exist')
                flag_f = False

    return min_max, flag_f


'''In this function I find the tables A, b, c, equin'''
def find_tables(list):

    '''find the equin table and b'''
    equin = []
    b = []
    for ch in range(len(list)):
        if list[ch] == '<' and list[ch + 1] == '=':
            equin.append('-1')
        elif list[ch] == '>' and list[ch + 1] == '=':
            equin.append('1')
        elif (list[ch] == '=' and list[ch - 1] != '>') and (
                list[ch] == '=' and list[ch - 1] != '<'):
            equin.append('0')
        if list[ch] == '=':
            temp_b = []

            while list[ch + 1] is not '\n':
                temp_b.append(list[ch + 1])
                ch += 1
            for value in temp_b:
                b.append(value)
            # i use the '/' to separate the numbers of each line
            b.append('/')

    '''find the c table and the indexes from them'''
    sym = 1
    flag_cof = True
    c = []
    c_index = []
    i = 3
    pos_n = 0
    while i < len(list):
        if list[i] == '\n':
            pos_n = i
            break

        if list[i] == '+':
            sym = 1
            i += 1
        elif list[i] == '-':
            sym = -1
            i += 1

        if 48 <= ord(list[i]) <= 57:
            temp_digits = []
            sum = 0

            while 48 <= ord(list[i]) <= 57:
                temp_digits.append(int(list[i]))
                i += 1
            for value in temp_digits:
                sum += value * pow(10, len(temp_digits) - 1)
            if flag_cof:
                flag_cof = False
                if list[i] == 'x' or list[i] == 'X':
                    sum = sum * sym
                    sym = 1
                    c.append(sum)
                i += 1
            else:
                flag_cof = True
                c_index.append(sum)

        elif list[i] == 'x' or list[i] == 'X':
            if flag_cof:
                flag_cof = False
                c.append(sym)
                sym = 1
            i += 1

    '''I have keep one variable pos_n, which refer to the position that the first\n
    found to start for the A table from there'''
    A = []  # the pos_n + 3 to start from the first number or sign
    A_index = []
    index = pos_n + 3

    for line in range(len(equin)):
        flag_coef = True
        coef_a = []
        index_a = []
        sym = 1

        while index < len(list):
            if list[index] == '<' or list[index] == '>':
                index += 1

                while list[index] is not '\n':
                    index += 1
                break

            if list[index] == '+':
                sym = 1
                index += 1
            elif list[index] == '-':
                sym = -1
                index += 1

            if 48 <= ord(list[index]) <= 57:
                temp_digits = []
                sum = 0

                while 48 <= ord(list[index]) <= 57:
                    temp_digits.append(int(list[index]))
                    index += 1
                for value in temp_digits:
                    sum += value * pow(10, len(temp_digits) - 1)
                if flag_coef:
                    flag_coef = False
                    if list[index] == 'x' or list[index] == 'X':
                        sum = sum * sym
                        sym = 1
                        coef_a.append(sum)
                    index += 1
                else:
                    flag_coef = True
                    index_a.append(sum)

            elif list[index] == 'x' or list[index] == 'X':
                if flag_coef:
                    flag_coef = False
                    coef_a.append(sym)
                index += 1
        temp = []
        count_appen = 0

        for i in range(1, len(c) + 1):
            if i in index_a:
                temp.append(coef_a[count_appen])
                count_appen += 1
            else:
                temp.append(0)
        index += 1
        A.append(temp)

    return A, b, c, equin


'''write the results in a txt file  '''
def write(A, b, c, equin, min_max):
    file_name = 'result.txt'
    with open(file_name, 'w') as f:
        if min_max == -1:
            f.write('min\n')
        else:
            f.write('max\n')
        f.write('c=[\t')

        for item in c:
            f.write('%s\t' % item)
        f.write(']\n')
        f.write('A=[\t')
        for index, item in enumerate(A):
            if index == len(A) - 1:
                f.writelines('%s]\n' % item)
            else:
                f.writelines('%s\n\t' % item)
        f.write('\nequin=[\t')
        for item in equin:
            f.write('%s\t' % item)
        f.write(']\n')

        f.write('\nb=[\t')
        for item in b:
            if item is not '/':
                f.write('%s' % item)
            else:
                f.write('\t')
        f.write(']\n')


if __name__ == '__main__':
    ch_list = read_file()
    min_max, flag = error_finder(ch_list)
    if flag:
        A, b, c, equin = find_tables(ch_list)
        write(A, b, c, equin, min_max)
        print("Finished check the results txt file")
    else:
        print('WROOONG!!!!!!')