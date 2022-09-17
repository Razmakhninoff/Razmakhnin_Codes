import hashlib
import os
import argparse

#python DuplicateFileHandler.py module
print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
def save_files(inp_path):
    size_dict = {}
    sort_dict = {}
    inp_form = input("Enter file format:\n")
    print("Size sorting options:\n1. Descending\n2. Ascending\n")
    while True:
        inp_sort = input("Enter a sorting option:\n")
        if inp_sort in "12":
            ascending = bool(int(inp_sort) - 1)
            break
        else:
            print("Wrong option")
    for root, dirs, files in os.walk(inp_path, topdown=True):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            size_dict.setdefault(size, []).append(path)
    for key in sorted(size_dict.keys(), reverse=(not ascending)):
        print(f"{key} bytes")
        for path in size_dict[key]:
            if path.endswith(inp_form):
                print(path)
                sort_dict.setdefault(key, []).append(path)
    return sort_dict

def check_duplicate(file_dict):
    dic_1 = {}  # 1:module
    dic_2 = {}  # 1:bytes
    total = 0   # total bytes
    while True:
        inp_dup = input("Check for duplicates?\n")
        if inp_dup == "yes":
            break
        elif inp_dup == "no":
            exit()
        else:
            print("Wrong option")
    hash_dict = {}
    for key in file_dict.keys():
        hash_temp = {}
        for path in file_dict[key]:
            with open(path, "rb") as file:
                f_hash = hashlib.md5()
                f_hash.update(file.read())
                hash_temp.setdefault(f_hash.hexdigest(), []).append(path)
        hash_dict[key] = hash_temp
    count = 0
    for key in hash_dict.keys():
        hash_temp = hash_dict[key]
        if max([len(hash_temp[k]) for k in hash_temp.keys()]) > 1:
            print()
            print(f"{key} bytes")
            for hvalue in hash_temp.keys():
                if len(hash_temp[hvalue]) > 1:
                    print(f"Hash: {hvalue}")
                    for path in hash_temp[hvalue]:
                        count += 1
                        print(f"{count}. {path}")
                        dic_1[count] = path
                        dic_2[count] = key

    while True:
        usdel = input("Delete files?\n")
        if usdel == "yes":
            break
        elif usdel == "no":
            exit()
        else:
            print("Wrong option")

    validate_count = []
    for i in range(1, count + 1):
        validate_count.append(str(i))

    while True:
        usdeco = 0
        usdelnum = input('Enter file numbers to delete:\n').split()
        if usdelnum == [] or usdelnum == '':
            usdeco += 1
        for i in usdelnum:
            if i not in validate_count:
                usdeco += 1
        if usdeco > 0:
            print("\nWrong format\n")
        else:
            break

    for i in usdelnum:
        total = dic_2[int(i)] + total
        os.remove(dic_1[int(i)])
    print(f'Total freed up space: {total} bytes')

parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=None)
args = parser.parse_args()

if args.path:
    f_dict = save_files(args.path)
    check_duplicate(f_dict)
else:
    print("Directory is not specified")
