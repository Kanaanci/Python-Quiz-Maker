import random
import time
import os
import sys

def header_info():
  print('Quiz Maker')
  print("During the quiz, enter 'S' to restart or 'Q' to exit")
  print()

def getStudentInfo():
  '''
  gets the name and ID of the student taking the quiz
  Validates that the number of attempts to enter information is not greater than 3, else exits the program
  Throws the ID to checkId() to validate 
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
    #if the first character is 'A', the length after the first is 5 and every character after the first is a digit
    return True
  else:
    return False

def readFile(questAmount):
  '''
  read test bank, pick 10 or 20 random questions
  '''
  testBank = 'TestBank.txt'
  qList = [] #list of questions
  
  try:
    with open(testBank, 'r') as tb: #reading the file
      questions = tb.readlines()    #...
      for i in range(0, questAmount): #looping over the number of questions
        random_question = random.choice(questions) #and choosing a random one
        
        #if the question is in the list get a new question
        while random_question in qList:
          random_question = random.choice(questions)

        qList.append([random_question.split('#')[0], random_question.split('#')[1]])
        #append the random question to the list of questions, splitting the question and answer into separate indexes
        
  except(FileNotFoundError):
    print(testBank, "was not found...")
    
  return qList

def outputFile(sInfo, qaList, totalScore, et):
  '''
  Creating the file to be used for the results. Naming format of id_fn_ln.txt
  Appending the user info and questions/answers to the file along with score and time
  '''
  unit_of_time = " minutes" #if the elapsed time is more than one minute

  resultsFile = str(sInfo[0][0]) + "_" + str(sInfo[0][1]) + "_" + str(sInfo[0][2]) + ".txt"
  #creating file name

  # this is just creating the file to append to later
  open(resultsFile, 'w').close()
        
  try:
    with open(resultsFile, 'a') as user_file:
      #appending the name, score and elapsed time to the header of the file
      user_file.write("Student ID: " + sInfo[0][0] + "\n" + "First Name: " + sInfo[0][1] + "\n" + "Last name: " + sInfo[0][2] + "\n")
      user_file.write("Score: " + str(totalScore) + "/10\n")
      
      if et < 1:
        unit_of_time = " seconds"
        et = round(et * 60)
      
      user_file.write("Elapsed time: " + str(et) + unit_of_time + "\n")
      
      for i in range(0, len(qaList)):
        #looping over questions answered, printing them out along with user's answer/correct answer
        user_file.write("\nQ" + str(i + 1) + ". " + qaList[i][0] + "\n" + "Correct answer: " + qaList[i][1] + "\n" + "User answer: " + qaList[i][2] + "\n")
        
  except FileNotFoundError:
    print("Error creating results file")
    
  print(resultsFile + " was created")
  
  sys.exit()

def exitProgram(user_input):
  if user_input == 'S':
    print("\n"*100) #this is just for IDEs 
    os.system('cls' if os.name == 'nt' else 'clear') #this will clear on TERMINALS
    main()
  else:
    sys.exit()
    


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
    
def quizTrack(qList, number_of_questions):
  score = 0 #score out of 10
  i = 0 #increment
  qaList = [] #list of questions asked
  PERIOD_OF_TIME = 600 #10 min
  startTime = time.time() #current time
  currentTime = 0 #time after each question
  endTime = time.time() + PERIOD_OF_TIME #10 minutes
  
  if number_of_questions == 10:
    qPoint = 1
  else:
    qPoint = .5
  
  for question in qList:
    while currentTime < endTime: #while the time is less than 10 mins
      currentTime = time.time()
      print(qList[i][0]) #print a random questions
      userAnswer = input("True or False?: ").upper()
      
      if userAnswer.upper() == 'Q' or userAnswer.upper() == 'S':
        exitProgram(userAnswer)
        
      print()
      qaList.append([qList[i][0], qList[i][1], userAnswer]) #append the answer to the answer list
      
      if checkInput(qList[i][1], userAnswer): #if the answer is a proper input
        score += qPoint #if the answer is correct, add a point
      i += 1 #increment the while loop
      if i == len(qList): #ensure i is only going up to 10
        break
    break
  
  elapsedTime = round((currentTime - startTime) / 60, 2) #checks elapsed time
  if elapsedTime < 0: #if it has been over 10 minutes
    elapsedTime = 10.00 #set the time to 10 minutes


    
  return qaList, score, elapsedTime
    
def main():
  header_info()
  # get student info
  studentInfo = [getStudentInfo()] #list of a tuple
  # 10 or 20 questions
  number_of_questions = int(input("How many questions would you like? (10 or 20): ")) #number of questions user wants to answer
  print()
  while number_of_questions != 10 and number_of_questions != 20: #if the input is not 10 or 20
    number_of_questions = int(input("Invalid entry; Please enter 10 or 20: "))
    print()
  
  # get those questions and answers [[q][a]]
  qList = readFile(number_of_questions)

  # get the question list plus what the user answered [[q][a][ua]] also the total score
  answeredQs, totalScore, elapsedTime = quizTrack(qList, number_of_questions)
  # output the file into the directory with the information needed
  outputFile(studentInfo, answeredQs, totalScore, elapsedTime)


  print("Bye!")
if __name__ == "__main__":
  main()

