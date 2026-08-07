import numpy as np
marks = np.array([
    [78, 85, 90],
    [67, 74, 80],
    [92, 88, 95],
    [56, 60, 58],
    [81, 79, 84]
])

subjects = ["Math", "Science", "English"]

print("Student Marks Analyzer\n")

for i in range(len(marks)):
    total = np.sum(marks[i])
    average = np.mean(marks[i])
    highest = np.max(marks[i])
    lowest = np.min(marks[i])

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    print(f"Student {i+1}")
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Grade:", grade)
    print("-" * 30)

print("\nSubject-wise Statistics")

for i in range(len(subjects)):
    print(subjects[i])
    print("Average:", round(np.mean(marks[:, i]), 2))
    print("Highest:", np.max(marks[:, i]))
    print("Lowest:", np.min(marks[:, i]))
    print()