print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')


def fibo_loop(n):
    result = [0, 1]
    while len(result) < n:
        result.append(result[-1] + result[-2])
    return result


def fibo_yield(n):
    seq_one, seq_two = 0, 1
    for _ in range(n):
        yield seq_one
        prev_sum = seq_one + seq_two
        seq_one = seq_two
        seq_two = prev_sum


def main():
    print('- - Generating Fibonacci- --')
    n = int(input('Enter Fibonacci length:\n'))
    choice = input('Yield or Simple Loop?\n')
    if choice == 'Yield':
        for _ in fibo_yield(n):
            print(_)
    if choice == 'Simple Loop':
        print(fibo_loop(n))


main()
