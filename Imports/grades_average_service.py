def calculate_homework(homework_assignments_arg):
    avg_of_grades = 0
    for homework in homework_assignments_arg.values():
        avg_of_grades += homework
    final_grades = round(avg_of_grades / len(homework_assignments_arg), 2)
    print(final_grades)

