
print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')

#100010 =  34
#1 * 2**5 + 0 * 2**4 + 0 * 2**3 + 0 * 2**2 + 1 * 2**1 + 0 * 2**0

x = input('Enter you Binary number to convert in decimal').split()
total = []
list = []
d2 = []
for i in x:
    for j in i:
        list.append(j)
for k in range(len(list) - 1, -1, -1):
    d2.append(2**k)
for g in list:
    total.append(int(g) * d2[0])
    del d2[0]
total = sum(total)
print(total)
