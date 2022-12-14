res = {"water": 400, "milk": 540,
       "beans": 120, "cups": 9, "money": 550}


def bank():
    print("The coffee machine has:")
    print(f"{res['water']} ml of water")
    print(f"{res['milk']} ml of milk")
    print(f"{res['beans']} g of coffee beans")
    print(f"{res['cups']} disposable cups")
    print(f"${res['money']} of money\n")


def checker():
    n1 = {'water': 250, 'beans': 16,
          'cups': 1}
    n2 = {'water': 350, 'milk': 75,
          'beans': 20, 'cups': 1}
    n3 = {'water': 200, 'milk': 100,
          'beans': 16, 'cups': 1}

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    num = input()
    if num == "back":
        print()
        main()

    num = int(num)
    if num == 1:
        if res['water'] - n1['water'] < 0:
            print("Sorry, not enough water!\n")
        elif res['beans'] - n1['beans'] < 0:
            print("Sorry, not enough coffee beans!\n")
        elif res['cups'] - n1['cups'] < 0:
            print("Sorry, not enough disposable cups!\n")
        else:
            print("I have enough resources, making you a coffee!")
            buy(num)
    elif num == 2:
        if res['water'] - n2['water'] < 0:
            print("Sorry, not enough water!\n")
        elif res['milk'] - n2['milk'] < 0:
            print("Sorry, not enough milk!\n")
        elif res['beans'] - n2['beans'] < 0:
            print("Sorry, not enough coffee beans!\n")
        elif res['cups'] - n2['cups'] < 0:
            print("Sorry, not enough disposable cups!\n")
        else:
            print("I have enough resources, making you a coffee!")
            buy(num)
    elif num == 3:
        if res['water'] - n3['water'] < 0:
            print("Sorry, not enough water!\n")
        elif res['milk'] - n3['milk'] < 0:
            print("Sorry, not enough milk!\n")
        elif res['beans'] - n3['beans'] < 0:
            print("Sorry, not enough coffee beans!\n")
        elif res['cups'] - n3['cups'] < 0:
            print("Sorry, not enough disposable cups!\n")
        else:
            print("I have enough resources, making you a coffee!")
            buy(num)


def buy(num):
    if num == 1:  # espresso
        res.update([('water', (res['water']) - 250)])
        res.update([('beans', (res['beans']) - 16)])
        res.update([('money', (res['money']) + 4)])
        res.update([('cups', (res['cups']) - 1)])
        print()
    elif num == 2:  # latte
        res.update([('water', (res['water']) - 350)])
        res.update([('milk', (res['milk']) - 75)])
        res.update([('beans', (res['beans']) - 20)])
        res.update([('money', (res['money']) + 7)])
        res.update([('cups', (res['cups']) - 1)])
        print()
    elif num == 3:  # cappuccino 
        res.update([('water', (res['water']) - 200)])
        res.update([('milk', (res['milk']) - 100)])
        res.update([('beans', (res['beans']) - 12)])
        res.update([('money', (res['money']) + 6)])
        res.update([('cups', (res['cups']) - 1)])
        print()


def fill():
    print("Write how many ml of water you want to add:")
    num = int(input())
    res.update([('water', (res['water']) + num)])
    print("Write how many ml of milk you want to add:")
    num = int(input())
    res.update([('milk', (res['milk']) + num)])
    print("Write how many grams of coffee beans you want to add:")
    num = int(input())
    res.update([('beans', (res['beans']) + num)])
    print("Write how many disposable cups you want to add:")
    num = int(input())
    res.update([('cups', (res['cups']) + num)])
    print()


def take():
    print(f"I gave you ${res['money']}\n")
    res.update([('money', (res['money']) - (res['money']))])


def remaining():
    bank()


def main():
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        num = input()
        print()
        if num == "exit":
            exit()
        if num == "buy":
            checker()
        if num == "fill":
            fill()
        if num == "take":
            take()
        if num == "remaining":
            remaining()

print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
main()