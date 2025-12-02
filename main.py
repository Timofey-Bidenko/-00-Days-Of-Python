cube = {
    "size": 3,
    "position": (0, 0, 0),
    "color": "green",
}

print(cube["size"]) # get
cube["color"] = "blue" # set
cube.pop("position") # delete entry

for key in cube:
    value = cube[key]
    print(f'kv pair: ["{key}"] = {value}')

for key, value in cube.items():
    print(f'kv pair: ["{key}"] = {value}')

students_scores = {
    "Alice": 75,
    "Bob": 63,
    "Chris": 92,
    "Diana": 48,
}

students_grades = {}

for name, score in students_scores.items():
    if score >= 90:
        students_grades[name] = "Outstanding"
    elif score >= 80:
        students_grades[name] = "Exceeds Expectations"
    elif score >= 70:
        students_grades[name] = "Acceptable"
    else:
        students_grades[name] = "Fail"

print(students_grades)