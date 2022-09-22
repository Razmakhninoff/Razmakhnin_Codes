with open('applicant_list_6.txt', 'r') as f:
    f_cache, cache, n = [[line.rstrip()] for line in f], [], int(input())
for j in f_cache:
    cache.append(j[0].split())

dic_fac = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
ex_ind = {'Biotech': [3, 2, 2], 'Chemistry': 3, 'Engineering': [5, 4, 2], 'Mathematics': 4, 'Physics': [2, 4, 2]}

for status in range(6, 9):  # adder to dic
    accepted = []  # this list need for deleting from cache
    for t in dic_fac:  #  't' - faculty name
        if t not in ['Mathematics', 'Chemistry']:  # sorting here >>>
            cache = sorted(cache, key=lambda x: (- ( float(x[ex_ind[t][0]]) + float(x[ex_ind[t][1]]) )
                                                 / ex_ind[t][2], x[0], x[1] ))
        else:
            cache = sorted(cache, key=lambda x: (-float(x[ex_ind[t]]), x[0], x[1]))

        for i in cache:  # player`s line
            if i[status] == t and len(dic_fac[t]) < n:
                if i[status] not in ['Mathematics', 'Chemistry']:  # slicing here >>>
                    dic_fac[t].append([i[0], i[1], (float(i[ex_ind[t][0]]) + float(i[ex_ind[t][1]])) / 2])
                else:
                    dic_fac[t].append([i[0], i[1], float(i[ex_ind[t]])])
                accepted.append(i)

    for j in accepted:  # cleaner
        cache.remove(j)

for f in dic_fac:  # last sort for each fac here
    dic_fac[f] = sorted(dic_fac[f], key=lambda x: (-float(x[2]), x[0], x[1]))

for k in dic_fac: #  load to file
    with open(f'{k.lower()}.txt', 'w') as fw:
        for j in dic_fac[k]:
            j = j[0] + ' ' + j[1] + ' ' + str(j[2]) + '\n'
            fw.write(j)

for k in dic_fac:  # printer
    print(k)
    for j in dic_fac[k]:
        print(*j[0:3])
    print()
