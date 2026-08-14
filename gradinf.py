score = int(input("Enter your score: "))
score_midterm = int(input("Enter your midterm: "))
score_Final = int(input("Enter your Final: "))

your_grading = score + score_midterm + score_Final
if your_grading >= 80 :
    print("A")
elif your_grading >= 75:
    print("B+")
elif your_grading >= 70:
    print("B")
elif your_grading >= 65:
    print("C+")
elif your_grading >= 60:
    print("C")
elif your_grading >= 55:
    print("D+")
elif your_grading >= 50:
    print("D")
else:
    print("F")