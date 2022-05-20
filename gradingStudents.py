import os


def gradingStudents(grades):
    # Rounding process:
    # If less than 40, no rounding keep as is,
    # If grade % 5 < 3, grade += (5 - (grade % 5))
    dummyGrade = [0] * len(grades)
    for i, grade in enumerate(grades):
        if grade >= 40:
            if ((grade % 5) > 2):
                grade += (5 - (grade % 5))
                dummyGrade[i] = grade
            else:
                dummyGrade[i] = grade
        else:
            if grade >= 38:
                grade += (5 - (grade % 5))
                dummyGrade[i] = grade
            else:
                dummyGrade[i] = grade
    return dummyGrade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
