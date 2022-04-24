def gradingStudents(grades):
    myList = len(grades)
    for i in range(myList):
        if grades[i] >= 38 and grades[i] % 5 >= 3:
            grades[i] = (grades[i]+5 - (grades[i] % 5))


def main():
    value = int(input())
    grades = []
    for i in range(value):
        data = int(input())
        grades.append(data)
    gradingStudents(grades)
    for i in range(value):
        print(grades[i])


main()
