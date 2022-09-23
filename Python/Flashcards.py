import argparse
import logging
import os.path
import shutil


def init_logger(name):
    logger = logging.getLogger(name)
    FORMAT = '%(levelname)s::%(message)s'
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(filename='flash_logs.txt')
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.DEBUG)
    if not logging.getLogger(name).hasHandlers():
        logger.addHandler(fh)


init_logger('main_log')
logger = logging.getLogger('main_log')

parser = argparse.ArgumentParser(description="FlashCards.")
parser.add_argument("--import_from", help='Incorrect Parameters')
parser.add_argument("--export_to", help='Incorrect Parameters')
args = parser.parse_args()

cards = {}

print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')

if args.import_from is not None:
    with open(args.import_from, 'r') as arg_import:
        f_r = [arg_import.read().split()]
        odd, even = [], []
        for i in f_r:
            for j in i:
                if i.index(j) % 2 == 0:
                    even.append(j)
                else:
                    odd.append(j)
        for i, j in zip(even, odd):
            cards[i] = j
    print(f'{len(cards)} cards have been loaded.\n')
    logger.info(f'{len(cards)} cards have been loaded.\n')


def adder():
    card_name = input('The card:\n')
    logger.info('The card:')
    logger.info(card_name)
    while True:
        if card_name in cards.keys():
            card_name = input(f'The term "{card_name}" already exists. Try again:\n')
            logger.info(f'The term "{card_name}" already exists. Try again:')
            logger.info(card_name)
        else:
            break
    defi = input(f'The definition of the card:\n')
    logger.info('The definition of the card:')
    logger.info(defi)
    while True:
        if defi in cards.values():
            defi = input(f'The definition "{defi}" already exists. Try again:\n')
            logger.info(f'The definition "{defi}" already exists. Try again:')
            logger.info(defi)
        else:
            cards[card_name] = defi
            print(f'The pair ("{card_name}":"{defi}") has been added.\n')
            logger.info(f'The pair ("{card_name}":"{defi}") has been added.\n')
            break
    main()


def exporter(act):
    file_name = input('File name:\n')
    logger.info('File name:')
    logger.info(file_name)
    f = open(file_name, 'w')
    if act == 'export':
        for i in cards:
            f.write(i + ' ' + cards[i] + ' ')
        f.close()
        print(f'{len(cards)} cards have been saved.\n')
        logger.info(f'{len(cards)} cards have been saved.\n')
    else:
        shutil.copy('flash_logs.txt', file_name)
        f.close()
        print('The log has been saved.\n')
        logger.info('The log has been saved.\n')
    main()


def importer():
    file_name = input('File name:\n')
    logger.info('File name:')
    logger.info(file_name)
    check_file = os.path.isfile(file_name)
    if not check_file:
        print('File not found.\n')
        logger.info('File not found.\n')
    else:
        with open(file_name, 'r') as f:
            f_r = [f.read().split()]
            odd, even = [], []
            for i in f_r:
                for j in i:
                    if i.index(j) % 2 == 0:
                        even.append(j)
                    else:
                        odd.append(j)
            for i, j in zip(even, odd):
                cards[i] = j
        print(f'{int(len(f_r[0]) / 2)} cards have been loaded.\n')
        logger.info(f'{int(len(f_r[0]) / 2)} cards have been loaded.\n')
    main()


def remover():
    card_name = input('Which card?\n')
    logger.info('Which card?')
    logger.info(card_name)
    if card_name not in cards.keys():
        print(f"Can't remove \"{card_name}\": there is no such card.\n")
        logger.info(f"Can't remove \"{card_name}\": there is no such card.\n")
    else:
        del cards[card_name]
        print('The card has been removed.\n')
        logger.info('The card has been removed.\n')
    main()


def asker():
    var = ''
    n = int(input('How many times to ask?\n'))
    logger.info('How many times to ask?')
    logger.info(n)
    count = 0
    while True:
        for j in cards:
            if count == n:
                print()
                main()
                logger.warning("Here`s bug with While Loop")  # LOGGER warning
                break
                logger.warning("Here`s bug with While Loop after break")  # LOGGER warning
            answer = input(f'Print the definition of "{j}":\n')
            logger.info(f'Print the definition of {j}')
            logger.info(answer)
            count += 1
            if answer == cards[j]:
                print('Correct!')
                logger.info('Correct')
            else:
                logger.debug("%s", j)  # LOGGER for count words
                if answer in cards.values():
                    for key in cards:
                        if cards[key] == answer:
                            var = key
                    print(f'Wrong. The right answer is "{cards[j]}",'
                          f' but your definition is correct for "{var}".')
                    logger.info(f'Wrong. The right answer is "{cards[j]}",'
                                f' but your definition is correct for "{var}".')
                else:
                    print(f'Wrong. The right answer is "{cards[j]}".')
                    logger.info(f'Wrong. The right answer is "{cards[j]}"')


def hardest_card():
    card_list = []
    stats = {}
    with open('flash_logs.txt', 'r') as file:
        file = file.readlines()
    for line in file:
        if 'DEBUG' in line:
            line = line.rstrip('\n').split('::')
            card_list.append(line[1])
    for i in card_list:
        if i not in stats.keys():
            stats[i] = card_list.count(i)
    if len(stats) == 0:
        print('There are no cards with errors.')
        logger.info('There are no cards with errors.')
    else:
        hardest = []
        var = max(stats.values())
        for key in stats:
            if stats[key] == var:
                hardest.append(key)
        if len(hardest) <= 1:
            print(f'The hardest card is "{hardest[0]}".'
                  f' You have {var} errors answering it.\n')
            logger.info(f'The hardest card is "{hardest[0]}".'
                        f' You have {var} errors answering it.\n')
        else:
            print(f'The hardest cards are "{hardest[0]}", "{hardest[1]}".'
                  f' You have {var} errors answering them.\n')
            logger.info(f'The hardest cards are "{hardest[0]}", "{hardest[1]}".'
                        f' You have {var} errors answering them.\n')
    main()


def main():
    act = input('Input the action (add, remove, import, export,'
                ' ask, exit, log, hardest card, reset stats):\n')
    logger.info('Input the action (add, remove, import, export,'
                ' ask, exit, log, hardest card, reset stats):\n')
    logger.info(act)
    if act == 'exit':
        print('Bye bye!')
        if args.export_to is not None:
            file = open(args.export_to, 'w')
            for i in cards:
                file.write(i + ' ' + cards[i] + ' ')
            file.close()
            print(f'{len(cards)} cards have been saved.\n')
        file = open('flash_logs.txt', 'w')
        file.close()
        exit()
    if act == 'add':
        adder()
    if act == 'remove':
        remover()
    if act == 'ask':
        asker()
    if act in ['export', 'log']:
        exporter(act)
    if act == 'import':
        importer()
    if act == 'hardest card':
        hardest_card()
    if act == 'reset stats':
        file = open('flash_logs.txt', 'w')
        file.close()
        print('Card statistics have been reset.\n')
        logger.info('Card statistics have been reset.\n')
        main()
    else:
        print('Invalid input.\n')
        logger.info('Invalid input.\n')
        main()


main()
