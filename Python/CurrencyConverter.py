import requests
import json

print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
print('--- --\nExample: \n>eur\n>usd\n>30\n>> You received 30.26 USD.\n--- --')
print('>>> Enter 1-st any currency >>>')
x = input()
r = requests.get(f'http://www.floatrates.com/daily/{x}.json')
cache = {}
while True:
    print(f'({x}) >>> Enter 2-nd any currency >>>')
    y = input()
    if y == "":
            break
    if y == 'usd':
        req = requests.get(f'http://www.floatrates.com/daily/{x}.json')
        j1 = req.json()
        j1 = j1['usd']
        j1 = j1['rate']
        cache1 = {y: j1, }
        cache.update(cache1)
    if y == 'eur':
        req = requests.get(f'http://www.floatrates.com/daily/{x}.json')
        j1 = req.json()
        j1 = j1['eur']
        j1 = j1['rate']
        cache1 = {y: j1,}
        cache.update(cache1)
    print(f'({x}->{y}) >>> Enter amount >>>')
    z = float(input())
    print('Checking the cache...')
    if y in cache:
        print('Oh! It is in the cache!')
        f2 = round((z * cache[y]), 2)
        print(f'You received {f2} {y.upper()}.')
    elif y not in cache:
        print('Sorry, but it is not in the cache!')
        r1 = r.json()[y]
        r2 = r1['rate']
        r3 = round(z * r2, 2)
        cache1 = {y: r2,}
        cache.update(cache1)
        print(f'You received {r3} {y.upper()}.')