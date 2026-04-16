def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 60:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 55:
        return "C", "Good job! Keep improving! 🙂"
    elif marks >= 40:
        return "D", "You passed! Keep working harder! 💪"
    else:
        return "F", "Don't give up! Try again! 🔄"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except:
            print("❌ Please enter a valid number.")


def main():
    name = input("Enter student name: ")

    marks = get_valid_marks()

    grade, message = get_grade(marks)

    print("\n📊 RESULT FOR", name.upper() + ":")
    print("Marks:", str(marks) + "/100")
    print("Grade:", grade)
    print("Message:", message)


# Run program
main()