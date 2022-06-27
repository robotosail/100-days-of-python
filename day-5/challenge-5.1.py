# ---------------Average Student height--------------------#
student_heights = input("Input a list of student heights: ").split(", ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# defining variables
total_height = 0
num_students = 0
# using for loop to incrementally add the height together
for height in student_heights:
    total_height += height

for students in student_heights:
    num_students += 1
# getting the average height by dividing the sum of the height and dividing by the total number of students
average = total_height / num_students
# printing the final value of the total height
print(average)
