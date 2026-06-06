def calculate_average(marks):
    """Calculates the average from a list of marks."""
    if not marks:
        return 0
    return sum(marks) / len(marks)

def get_grade(average):
    """Determines the letter grade based on the average score."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

def main():
    # Dictionary to store student names as keys and their marks (list) as values
    student_results = {}

    print("--- Student Result Analyzer ---")
    
    # Loop to take input for multiple students
    while True:
        name = input("\nEnter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        # Input marks as a comma-separated string and convert to a list of floats
        try:
            marks_input = input(f"Enter marks for {name} separated by commas (e.g., 85, 90, 78): ")
            # Instead of list comprehension, we use a basic loop to build the list
            marks_list = []
            parts = marks_input.split(",")
            for p in parts:
                marks_list.append(float(p.strip()))
            student_results[name] = marks_list
        except ValueError:
            print("Invalid input! Please enter numeric values separated by commas.")

    if not student_results:
        print("No student data entered.")
        return

    # Processing and Displaying Results
    print("\n" + "="*30)
    print("Student | Average | Grade")
    print("-" * 30)
    
    # Dictionary to store averages for topper calculation
    averages = {}
    
    for name, marks in student_results.items():
        avg = calculate_average(marks)
        averages[name] = avg
        grade = get_grade(avg)
        # Using simple print arguments instead of complex alignment
        print(name, "|", avg, "|", grade)

    # Finding the topper using a basic loop (replaces the lambda/max function)
    topper_name = ""
    highest_avg = -1
    for student in averages:
        if averages[student] > highest_avg:
            highest_avg = averages[student]
            topper_name = student
            
    class_avg = sum(averages.values()) / len(averages)

    print("-" * 30)
    print("Class Average:", class_avg)
    print("Topper:", topper_name, "with average:", highest_avg)
    print("="*30)

if __name__ == "__main__":
    main()
