msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg = ""
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_integer_num(v1):
    if isinstance(v1, int):
        return True
    if isinstance(v1, float):
        return v1.is_integer()
    return False


def is_ten(res):
    if 10 > res > - 10:
        return True
    else:
        return False


memory = 0

print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
print('Example (5 + 5)')
print('Operators: +, -, *, /')
print('stored result = M, example (5 + M)\n')
while True:
    print(msg_0)

    try:
        x, oper, y = input().split(" ")
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if oper == '+':
        result = x + y
        msg = ""
        if is_integer_num(x) and is_integer_num(y):
            msg = msg + msg_6
        if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
            msg = msg + msg_8
        if msg != "":
            msg = msg_9 + msg
        print(msg)
        print(result)
        print(msg_4)
        answer1 = input()
        if answer1 == "y" and is_ten(result) == True and is_integer_num(result) == True:
            print(msg_10)
            answer3 = input()
            if answer3 == "n":
                print(msg_5)
                answer2 = input()
                continue  # continue
            if answer3 == "y":
                print(msg_11)
                answer4 = input()
            if answer4 == "n":
                print(msg_5)
                answer2 = input()
                continue  # continue
            if answer4 == "y":
                print(msg_12)
                answer5 = input()
            if answer5 == "n":
                print(msg_5)
                answer2 = input()
                continue
            if answer5 == "y":
                memory = result
                print(msg_5)
                answer2 = input()
            if answer2 == "y":
                continue
            if answer2 == "n":
                break
            if answer3 == "n":
                continue
        if answer1 == "y":
            memory = result
            print(msg_5)
            answer2 = input()
        if answer1 == "n":
            print(msg_5)
            answer2 = input()
        if answer2 == "y":
            continue
        if answer2 == "n":
            break

    if oper == '-':
        result = x - y
        print(result)
        msg = ""
        print(msg_4)
        answer1 = input()
        if answer1 == "y" and is_integer_num(result) == True:
            print(msg_10)
            answer3 = input()
            if answer3 == "n":
                continue
            if answer3 == "y":
                print(msg_11)
                answer4 = input()
            if answer4 == "n":
                continue
            if answer4 == "y":
                print(msg_12)
                answer5 = input()
            if answer5 == "n":
                continue
            if answer5 == "y":
                memory = result
                print(msg_5)
                answer2 = input()
            if answer2 == "y":
                continue
            if answer2 == "n":
                break
            if answer3 == "n":
                continue
        if answer1 == "y" and is_integer_num(result) == False:
            memory = result
            print(msg_5)
            answer2 = input()
        if answer1 == "n":
            print(msg_5)
            answer2 = input()
        if answer2 == "y":
            continue
        if answer2 == "n":
            break

    if oper == '*':
        result = x * y
        msg = ""
        if (x < 10 and x > -10) and (y < 10 and y > -10) and is_integer_num(x) and is_integer_num(y) and (
                x > 0 and y >= 0):
            msg = msg + msg_6
        if (x == 1 or y == 1) and oper == "*":
            msg = msg + msg_7
        if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
            msg = msg + msg_8
        if msg != "":
            msg = msg_9 + msg
            print(msg)
        print(result)
        print(msg_4)
        answer1 = input()
        if answer1 == "y" and is_ten(result) == True and is_integer_num(result) == True:
            print(msg_10)
            answer3 = input()
            if answer3 == "n":
                print(msg_5)
                answer2 = input()
                continue  # continue
            if answer3 == "y":
                print(msg_11)
                answer4 = input()
            if answer4 == "n":
                print(msg_5)
                answer2 = input()
                continue  # continue
            if answer4 == "y":
                print(msg_12)
                answer5 = input()
            if answer5 == "n":
                print(msg_5)
                answer2 = input()
                continue
            if answer5 == "y":
                memory = result
                print(msg_5)
                answer2 = input()
            if answer2 == "y":
                continue
            if answer2 == "n":
                break
            if answer3 == "n":
                continue
        if answer1 == "y":
            memory = result
            print(msg_5)
            answer2 = input()
        if answer1 == "n":
            print(msg_5)
            answer2 = input()
        if answer2 == "y":
            continue
        if answer2 == "n":
            break

    if oper == '/' and y == 0:
        msg = ""
        msg = msg_9 + msg_6
        print(msg)
        print(msg_3)
        continue
    if oper == '/' and y != 0:
        result = x / y
        msg = ""
        if (x < 10 and x > -10) and (y < 10 and y > -10) and is_integer_num(x) and is_integer_num(y):
            msg = msg + msg_6
        if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
            msg = msg + msg_8
        if msg != "":
            msg = msg_9 + msg
            print(msg)
        print(result)
        print(msg_4)
        answer1 = input()
        check(y, n)
    else:
        print(msg_2)