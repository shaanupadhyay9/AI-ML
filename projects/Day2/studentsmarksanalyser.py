def get_marks():
    n = int(input("Enter the number of students: "))
    marks = []

    for i in range(n):
        mark = float(input(f"Enter marks of Student {i+1}: "))
        marks.append(mark)

    return marks


def highest_mark(marks):
    return max(marks)


def lowest_mark(marks):
    return min(marks)


def average_mark(marks):
    return sum(marks) / len(marks)


def above_average_students(marks, avg):
    print("\nStudents scoring above average:")
    found = False
    for i, mark in enumerate(marks):
        if mark > avg:
            print(f"Student {i+1}: {mark}")
            found = True

    if not found:
        print("No student scored above average.")


def display_results(marks):
    avg = average_mark(marks)

    print("\n----- Results -----")
    print(f"Highest Marks : {highest_mark(marks)}")
    print(f"Lowest Marks  : {lowest_mark(marks)}")
    print(f"Average Marks : {avg:.2f}")

    above_average_students(marks, avg)


def main():
    marks = get_marks()
    display_results(marks)


if __name__ == "__main__":
    main()