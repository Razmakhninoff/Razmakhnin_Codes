
def crypt(status, cesar=''):
    word = input(f'Type a word to {status[0]}:\n')
    for i in word:
        cesar += chr(ord(i) + status[2])
    print(f'Word "{word} was {status[1]} into "{cesar}"\n')
    main()


def main():
    while True:
        choice = input("Your choice -> Code/Decode by Cesar's pass\n")
        if choice in ["Code", "code", "c"]:
            status = ['code', 'coded', + 1]
            crypt(status)
        if choice in ["Decode", "decode", "d"]:
            status = ['decode', 'decoded', - 1]
            crypt(status)
        if choice == "!exit":
            print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
            exit()
        else:
            print('Invalid input. Try Again. (exit = !exit)')


main()