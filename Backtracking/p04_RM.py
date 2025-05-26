n = int(input("Cantidad de reinas: "))

def get_reinas(per):
    if len(per) == n:
        print()
        for i in range(n):
            for j in range(n):
                print('R' if per[i] == j else '.', end="")
            print()
        return
    for i in range(n):
        if i not in per:
            flag = True
            for j in range(len(per)):
                if j - per[j] == len(per) - i:
                    flag = False
                if j + per[j] == len(per) + i:
                    flag = False
            if flag :
                per.append(i)
                get_reinas(per)
                per.pop()

get_reinas([])