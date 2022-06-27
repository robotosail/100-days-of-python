#------------------------Calculating the Highest score-----------------------#
student_scores = input("Input a list of student scores: ").split(", ")

# turning all the scores into integers
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# variable initialization
highest_score = 0

# for each score in the students score
for score in student_scores:
    # if the score is greater than 0 set the highest score that score then you repeat this time the higest score is a different value
    if(score > highest_score):
        highest_score = score

print(
    f"The highest score in the class is the student with a score of {highest_score}")
