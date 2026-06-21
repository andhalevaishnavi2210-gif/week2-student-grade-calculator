# ==========================================
# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
#
# Author: Narendra Ankush Surase
# ==========================================

def calculate_grade(average):
    """Calculate grade and comment based on average marks"""

    if average >= 90:
        return "A", "Excellent! Keep up the great work! 🌟"

    elif average >= 80:
        return "B", "Very Good! You're doing well. 👍"

    elif average >= 70:
        return "C", "Good. Room for improvement. 😊"

    elif average >= 60:
        return "D", "Needs Improvement. Please study more. 📚"

    else:
        return "F", "Failed. Please seek help from teacher. 💪"


def get_valid_marks(subject):
    """Validate marks between 0 and 100"""

    while True:
        try:
            marks = float(input(f"{subject}: "))

            if 0 <= marks <= 100:
                return marks

            else:
                print("❌ Marks must be between 0 and 100.")

        except ValueError:
            print("❌ Invalid Input! Enter numbers only.")


def search_student(student_names, student_results):
    """Search student by name"""

    search_name = input("\nEnter student name to search: ")

    found = False

    for i in range(len(student_names)):

        if student_names[i].lower() == search_name.lower():

            print("\nStudent Found")
            print("-" * 40)

            print("Name :", student_names[i])
            print("Average :", round(student_results[i]["average"], 2))
            print("Grade :", student_results[i]["grade"])
            print("Comment :", student_results[i]["comment"])

            found = True
            break

    if not found:
        print("Student not found.")


def save_results(student_names, student_results):
    """Save results into file"""

    with open("results_sample.txt", "w") as file:

        file.write("RESULT SUMMARY\n")
        file.write("=" * 50 + "\n")

        for i in range(len(student_names)):
            file.write(
                f"{student_names[i]} | "
                f"{student_results[i]['average']:.1f} | "
                f"{student_results[i]['grade']} | "
                f"{student_results[i]['comment']}\n"
            )

    print("\n✅ Results saved successfully in results_sample.txt")


def main():

    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # Number of Students

    while True:

        try:
            num_students = int(input("\nEnter Number of Students: "))

            if num_students > 0:
                break

            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input! Enter whole number.")

    # Lists

    student_names = []
    student_marks = []
    student_results = []

    # Collect Data

    for i in range(num_students):

        print(f"\n========== STUDENT {i+1} ==========")

        name = input("Student Name: ")

        while name.strip() == "":
            print("Name cannot be empty.")
            name = input("Student Name: ")

        student_names.append(name)

        print("\nEnter Marks (0-100)")

        math = get_valid_marks("Math")
        science = get_valid_marks("Science")
        english = get_valid_marks("English")

        student_marks.append([math, science, english])

        average = (math + science + english) / 3

        grade, comment = calculate_grade(average)

        student_results.append({
            "average": average,
            "grade": grade,
            "comment": comment
        })

    # Display Results

    print("\n")
    print("=" * 80)
    print("                           RESULTS SUMMARY")
    print("=" * 80)

    print(f"{'Name':<20} {'Average':<10} {'Grade':<10} Comment")
    print("-" * 80)

    for i in range(num_students):

        print(
            f"{student_names[i]:<20} "
            f"{student_results[i]['average']:<10.1f} "
            f"{student_results[i]['grade']:<10} "
            f"{student_results[i]['comment']}"
        )

    # Statistics

    averages = [result["average"] for result in student_results]

    class_average = sum(averages) / len(averages)

    highest = max(averages)
    lowest = min(averages)

    highest_student = student_names[averages.index(highest)]
    lowest_student = student_names[averages.index(lowest)]

    print("\n")
    print("=" * 50)
    print("          CLASS STATISTICS")
    print("=" * 50)

    print("Total Students :", num_students)
    print("Class Average  :", round(class_average, 2))
    print("Highest Score  :", highest, "-", highest_student)
    print("Lowest Score   :", lowest, "-", lowest_student)

    # Search Feature

    choice = input("\nDo you want to search a student? (yes/no): ")

    if choice.lower() == "yes":
        search_student(student_names, student_results)

    # Save Results

    choice = input("\nSave results to file? (yes/no): ")

    if choice.lower() == "yes":
        save_results(student_names, student_results)

    print("\nThank You For Using Student Grade Calculator!")
    print("=" * 50)


# Program Starts Here

if __name__ == "__main__":
    main()