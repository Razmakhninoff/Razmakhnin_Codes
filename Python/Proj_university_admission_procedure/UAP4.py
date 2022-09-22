with open('applicant_list.txt', 'r') as f:
    f_cache, cache, n = [[line.rstrip()] for line in f], [], int(input())
for j in f_cache:
    cache.append(j[0].split())
cache = sorted(cache, key=lambda x: (-float(x[2]), x[0], x[1]))
dic_fac = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

for status in range(3, 6):  # adder to dic
    accepted = []
    for i in cache:
        for f in dic_fac:
            if i[status] == f and len(dic_fac[f]) < n:
                dic_fac[f].append(i)
                accepted.append(i)
    for j in accepted:
        cache.remove(j)

for f in dic_fac:  # last sort for each fac here
    dic_fac[f] = sorted(dic_fac[f], key=lambda x: (-float(x[2]), x[0], x[1]))

for k in dic_fac:  # printer
    print(k)
    for j in dic_fac[k]:
        print(*j[0:3])
    print()
