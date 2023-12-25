l = int(input("Введите размер длины прямоуголника"))
w = int(input("Введите размер ширины прямоуголника"))


for i in range(l):
    for j in range(w):
        if i == 0 or i == l - 1:
            print("*", end=" ")
        elif j == 0 or j == w - 1:
               print("*", end=" ")
        else:
            print(" ", end=" ")

    print()












