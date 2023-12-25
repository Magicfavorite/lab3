w = int(input("Введите размер стороны квадрата"))

for i in range(w + 1):
     for j in range(w + 1):
          if i == 0 or i == w:
               print("*", end='')
          elif j == 0 or j == w:
               print("*", end='')
          else :
               print(" ", end='')
     print()