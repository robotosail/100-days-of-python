student_scores = {"Harry": 81, "Ron": 78,
                  "Hermione": 99, "Draco": 74, "Neville": 62}
student_Grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_Grades[student] = "Outsanding"
    elif score > 80:
        student_Grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_Grades[student] = "Acceptable"
    else:
        student_Grades[student] = "Fail"

print(student_Grades)