import random
import datetime
import os

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
  
  return studentId, fName, lName
  
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

def readFile(questAmount):
  '''
  read test bank, maybe pick 10 random questions
  '''
  testBank = 'TestBank.txt'
  qList = []
  
  try:
    with open(testBank, 'r') as tb:
      questions = tb.readlines()
      for i in range(0, questAmount):
        rq = random.choice(questions)
        
        #if the question is in the list get a new question
        while rq in qList:
          rq = random.choice(questions)

#        print(i+1, qList[i]) #see questions in list
        qList.append([rq.split('#')[0], rq.split('#')[1]])
        
        
  except(FileNotFoundError):
    print(testBank, "was not found")
    
  return qList

def outputFile(sInfo, qaList, totalScore, et):
  '''
  Creating the file to be used for the results. Naming format of id_fn_ln.txt
  '''
#  si, fn, ln = sInfo[0], sInfo[0],sInfo[0]
  resultsFile = str(sInfo[0][0]) + "_" + str(sInfo[0][1]) + "_" + str(sInfo[0][2]) + ".txt"
  
  try:
    # if there is already a file with this name, overwrite it.
      with open(resultsFile, "w") as usrF:
        usrF.write("")
        
  except FileNotFoundError:
    print(resultsFile + " Created")
    with open(resultsFile, "w") as usrF:
      usrF.write("")
      
  try:
    with open(resultsFile, 'a') as usrF:
      usrF.write("Student ID: " + sInfo[0][0] + "\n" + "First Name: " + sInfo[0][1] + "\n" + "Last name: " + sInfo[0][2] + "\n")
      usrF.write("Score: " + str(totalScore) + "/10\n")
      usrF.write("Elapsed time: " + str(et) + "\n")
      
      for i in range(0, len(qaList)):
        usrF.write("\nQ" + str(i + 1) + ". " + qaList[i][0] + "\n" + "Correct answer: " + qaList[i][1] + "\n" + "User answer: " + qaList[i][2] + "\n")
        
  except FileNotFoundError:
    pass
    
def checkInput(questionAnswer, userAnswer):
  '''
  Check if student's input matches one of the following:
  true, TRUE, T, t, false, FALSE, f, F
  for any invalid answers, stay on current question and ask student to re-enter answer
  '''
  if userAnswer == 'T':
    userAnswer = 'TRUE'
  elif userAnswer == 'F':
    userAnswer = 'FALSE'
    
  if userAnswer == questionAnswer:
      return True
  else:
    return False
    
def quizTrack(qList, qTotal):
  score = 0
  qaList = []
  
  if qTotal == 10:
    qPoint = 1
  else:
    qPoint = .5
    
  for i in range(0, len(qList)):
    print(qList[i][0])
    userAnswer = input("True or False?: ").upper()
    print()
    qaList.append([qList[i][0], qList[i][1], userAnswer])
    
    if checkInput(qList[i][1], userAnswer):
      score += qPoint
      
  return qaList, score
  
def main():
  # get dat student info boi
  studentInfo = [getStudentInfo()]
  # 10 or 20 questions?
  qTotal = int(input("How many questions would you like? (10 or 20): "))
  print()
  while qTotal != 10 and qTotal != 20:
    qTotal = int(input("Invalid entry; Please enter 10 or 20: "))
    print()
  
  # get those questions and answers [[q][a]]
  qList = readFile(qTotal)
  # get the question list plus what the user answered [[q][a][ua]] also the total score
  answeredQs, totalScore = quizTrack(qList, qTotal)
  # output the file into the directory with the information needed
  outputFile(studentInfo, answeredQs, totalScore, 10) #this 10 will be elapsed time when i figure this shit out

  



if __name__ == "__main__":
  main()
