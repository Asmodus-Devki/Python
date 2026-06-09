students = {}
num_students = int(input("Enter the number of students : "))
for i in range(num_students):
    name = input("Enter the name of students : ")
    attended_classes = int(input("Enter the number of classes attended : "))
    total_classes = int(input("Enter the total number of classes : "))

    students[name] = {'attended_classes': attended_classes, 
                      'total_classes': total_classes}
    
print(f'\n{students}')

def calculate_percentage(attended, total):
    if attended < 0 or total < 0:
        return "no negative inputs please"
    elif total == 0:
        return 0
    else:
        return (attended / total) * 100

for name in students:
    attended = students[name]['attended_classes']
    total = students[name]['total_classes']
    attendance_percentages = []
    percentage = calculate_percentage(attended, total)
    attendance_percentages.append(percentage)

    print(f"\n{name} has attended {percentage:.2f}% of classes.")

    if percentage < 75:
        status = "Defaulter"
    else:
        status = "Eligible"

    print(f"{name} | {percentage:.2f}% | {status}")    

    defaulters = set()
    if percentage < 75:
        defaulters.add(name)   
        print("\nStudents below 75% Attendance are Defaulters and their names are as follows:\n\n")

    for name in defaulters:
        print(
        f"{name} attended {students[name]['attended_classes']} classes so the total attendence percentage for {name} is {calculate_percentage(students[name]['attended_classes'], students[name]['total_classes']):.2f}%")

    eligible_students = 0
    if students[name]['attended_classes'] >= 75:
        eligible_students += 1

    total_students = len(students)
    defaulters_count = len(defaulters)
    average_attendance = sum(attendance_percentages) / len(attendance_percentages)

print(f'\n{'='*40}\nATTENDANCE REPORT\n{'='*40}')
print(f'Total Students: {total_students}')
print(f'Eligible Students: {eligible_students}')
print(f'Average Attendance: {average_attendance:.2f}%')
print(f'\n{'='*40}\nDEFAULTERS LIST\n{'='*40}')
print(f'Defaulters: {defaulters_count}')
