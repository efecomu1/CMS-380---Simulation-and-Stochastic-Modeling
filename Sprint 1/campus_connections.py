"""
Campus Connections - Efe Comu
"""

# Standard matplotlib import
import matplotlib

matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv


def calc_mean(values):
  sum = 0
  for course_id in values:
    n = len(values[course_id])
    sum += n

  average = sum / len(values)

  print("Mean: %.2f" % average)


def calc_median(values):
  x = []
  for course_id in values:
    x.append(len(values[course_id]))

  x.sort()
  if len(x) % 2 == 1:
    mid1 = int((len(x) / 2))
    median = x[mid1]
  else:
    mid1 = int(len(x) / 2 - 1)
    mid2 = int(len(x) / 2)
    median = (x[mid1] + x[mid2]) / 2

  print("Median: ", median)


def makehist(values):
  plt.figure()
  list = []
  for course_id in values:
    list.append(len(values[course_id]))

  plt.hist(list, bins=20)
  plt.title("Class Size Histogram")
  plt.ylabel("Count")
  plt.xlabel("Class Size")
  plt.savefig("campus_hist.png", bbox_inches='tight')


def makeboxplot(values):
  plt.figure()
  list = []
  for course_id in values:
    list.append(len(values[course_id]))
  plt.boxplot(list)
  plt.title("Class Size Boxplot")
  plt.savefig("campus_boxplot.png", bbox_inches='tight')


def PrintStudents(students_per_course):

  # Here's an example of how to iterate through the keys in a dictionary
  # Print the students in each course
  for course_id in students_per_course:
    student_list = students_per_course[course_id]
    print(course_id + ': ' + str(student_list))


# Create an empty dictionary to record which students are in each course

students_per_course = {}
courses_per_student = {}
unique_interactions = {}

# Open the file and create a csv reader
f = open('enrollments.csv', 'r')
reader = csv.reader(f)

# Reader automatically iterates through the lines in the file
for line in reader:

  # csv reader automatically turns the line into a list of fields
  student_id = line[0]
  course_id = line[1]

  if course_id not in students_per_course:
    students_per_course[course_id] = []
  if student_id not in courses_per_student:
    courses_per_student[student_id] = []

  students_per_course[course_id].append(student_id)
  courses_per_student[student_id].append(course_id)

## interactions

for student_id in courses_per_student:
  class_list = courses_per_student[student_id]

  if student_id not in unique_interactions:
    unique_interactions[student_id] = []

  for course_id in class_list:
    for s in students_per_course[course_id]:
      if s not in unique_interactions[student_id]:
        unique_interactions[student_id].append(s)

## interactions average
total_int = 0
total_students = 0
for student_id in courses_per_student:
  total_students += 1

for student_id in unique_interactions:
  total_int += len(unique_interactions[student_id])
average = total_int / total_students

## print statements
calc_mean(students_per_course)
calc_median(students_per_course)
makehist(students_per_course)
makeboxplot(students_per_course)
print("Average interactions per student: %.2f" % average)
