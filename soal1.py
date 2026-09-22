#Write a PYTHON program to evaluate the student performance
performance = int (input("Enter the student's percentage: "))

if performance >= 90 :
    print("Excellent performance")
elif performance >= 80 :
    print("Very good performance")
elif performance >= 70 :
    print("Good performance")
elif performance >= 60 :
    print("Average performance")
else :
    print("Poor performance")