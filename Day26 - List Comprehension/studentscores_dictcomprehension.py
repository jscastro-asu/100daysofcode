names = ["Albert", "Tom", "Brook", "Pink", "Blue", "Carol", "Tisha"]
import random
student_score = {student:random.randint(70,100) for student in names}
print(student_score)

#will be using the student score dictionary
passed_students =  {student:score for (student, score) in student_score.items() if score >=75}
print(f"The following passed: {passed_students}")