def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    numbers.sort()
    n = len(numbers)
    return numbers[n // 2] if n % 2 == 1 else (numbers[n // 2 - 1] + numbers[n // 2]) / 2

def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuition = [uni[2] for uni in universities]
    return sum(enrollments), sum(tuition), enrollments, tuition

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

total_students, total_tuition, student_list, tuition_list = enrollment_stats(universities)

print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean(student_list):,.2f}")
print(f"Student median: {median(student_list):,.0f}\n")
print(f"Tuition mean: $ {mean(tuition_list):,.2f}")
print(f"Tuition median: $ {median(tuition_list):,.0f}")