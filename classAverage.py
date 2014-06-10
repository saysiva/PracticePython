siva = {
    "name": "Siva",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
raj = {
    "name": "Raj",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
stephen = {
    "name": "Stephen",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Individual functions are created for average calculation

def average(numbers):
    total = sum(numbers)
    total = float(total)
    average = total / len(numbers)
    return average
    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.10*homework + 0.30*quizzes + 0.60*tests

def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"
        
def get_class_average(students):
    results = []
    for student in students:
        
        results.append(get_average(student))
    return average(results)        
    
    
students = [siva,raj,stephen]  
aaa = get_class_average(students)
print aaa
print get_letter_grade(aaa)
