#Write a PYTHON program to print Fibonacci series up to n!
n = int(input("Enter the value of n: "))
a, b = 0, 1

for value in range(n): #range untuk menentukan jumlah perulangan
    print(a, end=" ") #end untuk memberi spasi agar tidak pindah baris
    a, b = b, a + b
