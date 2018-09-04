# Find sequence of 1, 2, 3, 6, 11, 20, 37, .. , ..

n = int(input("Enter the length of the sequence: ")) # Do not change this line

last_num = 0
last_num2 = 0
num = 1

for x in range(n):
    summa = 0
    summa = last_num2 + last_num + num
    if summa >= 3:
        last_num2 = last_num
    last_num = num
    num = summa
    print(summa)
