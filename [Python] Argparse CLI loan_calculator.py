
import argparse
import math
parser = argparse.ArgumentParser(description="This program is calculating smth.")
parser.add_argument("--type", choices=['diff', 'annuity'], help='Incorrect parameters')
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()
#  ------  #
calculation = [args.type, args.principal, args.periods, args.payment, args.interest]
error = 'Incorrect parameters'
#  ------  #
calc = []
for val in calculation:
    if val != None:
        calc.append(val)
#  ------  #
if len(calc) < 4 or args.type == None or args.interest == None or args.interest < 0:
    print(error)
#  ------  #
elif args.type == 'diff':
    p = args.principal
    n = args.periods
    i = args.interest
    if p == None or n == None or i == None:
        print(error)
    elif p < 0 or n < 0 or i < 0:
        print(error)
    elif p >= 0 or n >= 0 or i >= 0:
        i = args.interest / (12 * 100)
        m = 0
        d1 = 0
        for m in range(n):
            m += 1
            d = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
            d1 += d
            months = 'Month ' + str(m) + ': payment is ' + str(d)
            print(months)
            if m == n:
                d2 = d1 - p
                overpayment = '\nOverpayment = ' + str(d2)
                print(overpayment)
                break
#  ------  #
elif args.type == 'annuity':
    p = args.principal
    n = args.periods
    i = args.interest
    a = args.payment
    #loan principal -  (annuity)  -   payment/ periods/ float(interest)
    if a != None and n != None and i != None:
        if a >= 0 and n >= 0 and i >= 0:
            i = args.interest / (12 * 100)
            p_ = (i * math.pow((1+i), n)) / (math.pow((1+i), n) - 1)
            p = math.floor( a / p_)
            print('Your loan principal = ' + str(p) + '!')
            d2 = (a * n) - p
            overpayment = 'Overpayment = ' + str(d2)
            print(overpayment)
        else:
            print(error)
    #annuity payment  -   (annuity)  -   principal/ periods/ float(interest)
    elif p != None and n != None and i != None:
        if p >= 0 and n >= 0 and i >= 0:
            i = args.interest / (12 * 100)
            a = math.ceil(p * (i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
            print('Your annuity payment = ' + str(a) + '!')
            d2 = (a * n) - p
            overpayment = 'Overpayment = ' + str(d2)
            print(overpayment)
        else:
            print(error)
    #It will take...   -    (annuity)   -  principal/ payment / float(interest)
    elif p != None and a != None and i != None:
        if p >= 0 and a >= 0 and i >= 0:
            i = args.interest / (12 * 100)
            n = math.ceil(math.log((a / (a - i * p)), 1 + i))
            n_year = math.floor(n / 12)
            n_month = round(n % 12)
            month = ''
            year = ''
            if n_year > 1:
                year = str(n_year) + ' years'
            if n_year == 1:
                year = str(n_year) + ' year'
            if n_year == 0:
                year = ''
            if n_month > 1:
                month = ' and ' + str(n_month) + ' months'
            if n_month == 1:
                month = ' and ' + str(n_month) + ' month'
            if n_month == 0:
                month = ''
            print(f'It will take ' + year + month + ' to repay this loan!')
            d2 = (a * n) - p
            overpayment = 'Overpayment = ' + str(d2)
            print(overpayment)
        else:
            print(error)
#  -------  #
