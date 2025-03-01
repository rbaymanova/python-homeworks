import csv
from collections import defaultdict

def read_grades(file_name):
    grades = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade']) 
            grades.append(row)
    return grades

def calculate_average(grades):
    subject_totals = defaultdict(list)
    for entry in grades:
        subject_totals[entry['Subject']].append(entry['Grade'])
    
    subject_averages = {subject: sum(grades) / len(grades) for subject, grades in subject_totals.items()}
    return subject_averages

def write_averages(file_name, averages):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

grade_file = r"C:\Users\user\Desktop\python-homeworks\lesson-9\homework\grades.csv"
average_file = "average_grades.csv"

grades_data = read_grades(grade_file)
average_grades = calculate_average(grades_data)
write_averages(average_file, average_grades)

print(f"Averages written to {average_file}")


