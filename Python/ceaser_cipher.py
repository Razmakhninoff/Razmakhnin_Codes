def code():
    cesar = ''
    word = input("Type a word to code:\n")
    for i in word:
        cesar += chr(ord(i) + 1)
    print(f'Word "{word}" was coded into "{cesar}"')
    print()
    main()


def decode():
    cesar = ''
    word = input("Type a word to decode:\n")
    for i in word:
        cesar += chr(ord(i) - 1)
    print(f'Word "{word}" was decoded into "{cesar}"')
    print()
    main()


def main():
    while True:
        choice = input("Your choice -> Code/Decode by Cesar's pass\n")
        if choice in ["Code", "code", "c"]:
            code()
        if choice in ["Decode", "decode", "d"]:
            decode()
        if choice == "!exit":
            print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
            exit()
        else:
            print('Invalid input. Try Again. (exit = !exit)')

            
main()
