import gzip

print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
print('\n\n')
print('write 3 3 names paths of .gz archives (ex: data1.gz data2.gz data3.gz)')


data = []
best = []
stat = []

for i in range(3):
    data.append(input())
for i in data:
    with gzip.open(f'{i}', 'rt') as f:
        content = f.read().split('\n')
        reads = int(len(content) / 4)
        count_list = []                # Length dnk
        e = ('A', 'G', 'C', 'T', 'N')  # dnk - elements
        dic = {}
        repeats = reads - len(set(content[1:-2:4]))
        kp = 0                         # line counter
        count_n = []
        reads_n = 0
        for i in content[1:-2:4]:
            count_list.append(len(i))
            kp += 1
            if 'N' in i:
                reads_n += 1
                count_n.append(round((i.count('N') / (len(i)))*100, 2))
            for j in e:
                dic.update({kp: {
                    'A': i.count('A'),
                    'C': i.count('C'),
                    'G': i.count('G'),
                    'T': i.count('T'),
                    'N': i.count('N')
                }})
        dic_2 = {k: ((v['G'] + v['C'])/
    (v['A'] + v['T'] + v['G'] + v['C'] + v['N'])) * 100 for k, v in dic.items()}
        gc_avg = sum(dic_2.values()) / reads
        ns = sum(count_n) / reads
        stat.append([reads, round(sum(count_list) /
            reads), repeats, reads_n, round(gc_avg, 2), round(ns, 2)])
        best.extend([(reads_n + ns) / 2])
best_index = best.index(min(best))
reads, avg_length, repeats, reads_n, gc_avg, ns = stat[best_index]
print(f"Reads in the file = {reads}:")
print(f"Reads sequence average length = {avg_length}\n")
print(f"Repeats = {repeats}\nReads with Ns = {reads_n}\n")
print(f"GC content average = {gc_avg}%")
print(f"Ns per read sequence = {ns}%")
