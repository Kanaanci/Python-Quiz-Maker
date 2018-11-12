import random
import datetime

def getStudentInfo():
  '''
  gets the name and ID of the student taking the quiz
  '''
  idCheckCounter = 1
  fName = input("First Name: ").title()
  lName = input("Last Name: ").title()
  studentId = input("Student ID (Ex: A12345): ").title()
  
  while True:
    if checkId(studentId):
      break
    elif idCheckCounter == 3:
      print("Too many failed attempts; Exiting program")
      exit()
    else:
      idCheckCounter += 1
      print("Invalid ID; Please try again\n")
      studentId = input("Student ID (Ex: A12345): ").title()
  
  return fName, lName, studentId
  
def checkId(id):
  '''
  check the student's ID matches this format:
  a number of 6 digits, starts with letter 'A' then 5 numbers, 
  each number could be any val between 1 AND 9
  After 3 failed attempts, exit
  Valid ID's: A12345, A92154
  Invalid: a12345, 123456, A02456
  '''
  idLen = len(id[1:])
    
  if id[:1] == 'A' and idLen == 5 and id[1:].isdigit():
    return True
  else:
    return False

def readFile():
  '''
  read test bank, maybe pick 10 random questions
  '''
  testBank = 'TestBank.txt'
  
  try:
    with open(testBank, 'r') as tb:
      pass
  except(FileNotFoundError):
    print(testBank, "was not found")

def outputFile():
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

def checkInput():
  '''
  Check if student's input matches one of the following:
  true, TRUE, T, t, false, FALSE, f, F
  for any invalid answers, stay on current question and ask student to re-enter answer
  '''
  pass

def main():
  readFile()
  getStudentInfo()

if __name__ == "__main__":
  main()
