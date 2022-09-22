with open('applicant_list_5.txt', 'r') as f:
    f_cache, cache, n = [[line.rstrip()] for line in f], [], int(input())
for j in f_cache:
    cache.append(j[0].split())

dic_fac = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
exam_ind = {'Biotech': 3, 'Chemistry': 3, 'Engineering': 5, 'Mathematics': 4, 'Physics': 2}

for status in range(6, 9):  # adder to dic 
    accepted = []  # this list need for deleting from cache
    for t in dic_fac:  #  't' - faculty name
        cache = sorted(cache, key=lambda x: (-float(x[exam_ind[t]]), x[0], x[1]))  # sort every loop
        for i in cache:  # player`s line
            if i[status] == t and len(dic_fac[t]) < n:
                dic_fac[t].append([i[0], i[1], float(i[exam_ind[t]])])  # slicing here
                accepted.append(i)
    for j in accepted:  # cleaner
        cache.remove(j)

for f in dic_fac:  # last sort for each fac here
    dic_fac[f] = sorted(dic_fac[f], key=lambda x: (-float(x[2]), x[0], x[1]))
for k in dic_fac:  # printer  
    print(k)
    for j in dic_fac[k]:
        print(*j[0:3])
    print()
