# Uses of Imports
import Imports.grades_average_service as import_services

homeworks_assignment_grades = {
    'homework_1': 85,
    'homework_2': 95,
    'homework_3': 70
}

import_services.calculate_homework(homeworks_assignment_grades)
