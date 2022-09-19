
choice_dic = {'1': '[Binary->Decimal]', '2': '[Binary->hex]', '3': '[Decimal->Binary]',
              '4': '[Decimal->Hex]', '5': '[Hex->Binary]', '6': '[Hex->Decimal]'}

bi_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
          '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
          '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

hex_bi = {'0': '0000', '1': '0001','2': '0010', '3': '0011', '4': '0100', '5': '0101',
          '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
          'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


def binary_to_decimal(number):
    bina_num = number.split()
    total = []
    list_r = []
    d2 = []
    for i in bina_num:
        for j in i:
            list_r.append(j)
    for k in range(len(list_r) - 1, -1, -1):
        d2.append(2**k)
    for g in list_r:
        total.append(int(g) * d2[0])
        del d2[0]
    total = sum(total)
    return total


def decimal_to_binary(number):
    dec = int(number)
    dec_list = []
    while True:
        if dec > 0:
            dec_1 = dec % 2
            dec = dec // 2
            dec_list.insert(0, dec_1)
        elif dec <= 0:
            break
    dec_list2 = []
    for i in dec_list:
        dec_list2.append(str(i))
    dec_list = ''
    for i in dec_list2:
        dec_list += i
    return dec_list


def binary_to_hex(number):  # MAX 16 digits
    bina_he = number
    hex_list = []
    bina_he_2 = []
    zero_need = 16 - len(bina_he)
    if len(bina_he) < 16:
        bina_he = str(zero_need * '0') + bina_he
    for i in bina_he:
        bina_he_2.append(i)
    for i in bina_he_2:
        hex_list.append(bina_he_2[0] + bina_he_2[1] + bina_he_2[2] + bina_he_2[3])
        del bina_he_2[0:4]
    hexadecimal = []
    for i in hex_list:
        hexadecimal.append(bi_hex[i])
    total_hexadecimal = ''
    for i in hexadecimal:
        total_hexadecimal += i
    total_hexadecimal = total_hexadecimal.lstrip('0')
    return total_hexadecimal


def hex_to_binary(number):
    he_bi = ''
    for i in number:
        he_bi += hex_bi[i]
    return he_bi


def main():
    print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
    print('-- Options - -\n ___choose(0-6)')
    while True:
        print('''---   ---------  ---
    1. Binary to Decimal
    2. Binary to Hex
    3. Decimal to Binary
    4. Decimal to Hex
    5. Hex to Binary
    6. Hex to Decimal
-------- ------   --''')
        choice = input('Make your choice:\n')
        if choice not in choice_dic:
            print('Invalid input. try again!')
        else:
            print(f'{choice_dic[choice]} Enter your number:\n')
            number = input()
            if choice == '1':
                print(f'Decimal: {binary_to_decimal(number)}')
            if choice == '2':
                print(f'Hex: {binary_to_hex(number)}')
            if choice == '3':
                print(f'Binary: {decimal_to_binary(number)}')
            if choice == '4':
                print(f'Hex: {binary_to_hex(decimal_to_binary(number))}')
            if choice == '5':
                print(f'Binary: {hex_to_binary(number)}')
            if choice == '6':
                print(f'Decimal: {binary_to_decimal(hex_to_binary(number))}')


main()
