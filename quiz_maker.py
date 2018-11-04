import random
import datetime

def check_name(fname, lname, student_id):
  '''
  check the student's first name, last name, and ID matches this format:
  a number of 6 digits, starts with letter 'A' then 5 numbers, 
  each number could be any val between 1 AND 9
  After 3 failed attempts, exit
  Valid ID's: A12345, A92154
  Invalid: a12345, 123456, A02456
  '''
  print("Name: " + fname + " " + lname)
  print("ID: " + student_id)

def read_file():
  '''
  read test bank, maybe pick 10 random questions
  '''
  pass

def output_file():
  '''
  student's returned answer bank, name is ID_Fname_Lname
  write in the following data:
  ID, Fname, Lname
  Score,
  Elapsed time
  Questions answered, with correct answer and student's answer
  '''
  pass

def timer():
  '''
  user has 10 minutes to answer questions
  '''
  pass

def check_input():
  '''
  Check if student's input matches one of the following:
  true, TRUE, T, t, false, FALSE, f, F
  for any invalid answers, stay on current question and ask student to re-enter answer
  '''
  pass

def main():
  fname = input("First Name: ")
  lname = input("Last Name: ")
  student_id = input("Student ID (Ex: A12345): ")
  fname = fname.title()
  lname = lname.title()
  student_id = student_id.title()

  check_name(fname, lname, student_id)  

if __name__ == "__main__":
  main()
