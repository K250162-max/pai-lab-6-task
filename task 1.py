import numpy as np

# Marks of 10 students in 5 subjects
marks = np.array([
    [65, 72, 58, 80, 75],
    [45, 55, 60, 48, 52],
    [90, 85, 88, 92, 95],
    [40, 35, 50, 45, 42],
    [70, 68, 75, 80, 72],
    [55, 60, 65, 58, 62],
    [82, 78, 85, 80, 88],
    [48, 52, 45, 50, 55],
    [75, 80, 70, 68, 78],
    [60, 65, 55, 62, 58]
])


student_total = np.sum(marks, axis=1)

student_average = np.mean(marks, axis=1)

subject_average = np.mean(marks, axis=0)

highest_student = np.argmax(student_average)

passed_count = np.sum(student_average >= 50)

result = np.where(student_average >= 50, "Pass", "Fail")

print("Marks:")
print(marks)

print("\nStudent Totals:")
print(student_total)

print("\nStudent Averages:")
print(student_average)

print("\nSubject Averages:")
print(subject_average)

print("\nStudent with highest average:")
print("Student", highest_student + 1)

print("\nNumber of students with average >= 50:")
print(passed_count)

print("\nPass/Fail:")
print(result)