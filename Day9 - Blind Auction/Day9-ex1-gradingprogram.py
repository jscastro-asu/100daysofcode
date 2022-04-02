student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades = {}


for x in student_scores:
  score = student_scores[x]


  if score >= 91:
    student_grades[x] = "Outstanding"
  elif score >= 81:
    student_grades[x] = "Exceeds Expectations"
  elif score >= 71:
    student_grades[x] = "Acceptable"
  elif score <= 70:
    student_grades[x] = "Fail"


print(student_grades)

 