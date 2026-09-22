#Write a PYTHON program to produce following design
#1
#2 2
#3 3 3.
#4 4 4 4 
#5 5 5 5 5
#If user enters n value as 5
n = int (input("Enter the value of n: "))

print("The design is: ")
for i in range(1, n + 1):
    print((str(i) + " ") * i) #str(i) untuk mengubah integer menjadi string, agar bisa dikalikan
    