#####################################################################
#                           TASK 1    
                                                
from random import *                                                #this imports the random module into the script
QUESTION_NUMBER = 1                                                 #this assigns integer 1 to variable QUESTION_NUMBER
TOTAL_SCORE = 0                                                     #this assigns integer 0 to variable TOTAL_SCORE
print('Hello, welcome to the math quiz')                            #this outputs the string 'Hello, welcome to the math quiz' onto the console 
STUDENT_NAME = input('What is your name?\n')                        #this assigns the input from prompt 'What is your name?\n' to STUDENT_NAME
while QUESTION_NUMBER < 3:                                          #this iterates this indented piece of code while the condition is true (in this case while QUESTION_NUMBER is less than 11)
    QUESTION_NUMBER = QUESTION_NUMBER + 1                           #this increments QUESTION_NUMBER by + 1 every iteration
    NUMBER_1 = randint(1,10)                                        #this assigns a random integer between 1 and 10 to varibale NUMBER_1
    NUMBER_2 = randint(1,10)                                        #this assigns a random integer between 1 and 10 to varibale NUMBER_2
    OPERATOR = choice(['+','-','*'])                                #this assigns a random symbol from the array ['+','-','*'] to variable OPERATOR
    if OPERATOR == '+':                                             #this conditional runs the indented code if the condition OPERATOR equals '+' is met
        ACTUAL_ANSWER = NUMBER_1 + NUMBER_2                         #this assigns NUMBER_1 + NUMBER_2 to variable ACTUAL_ANSWER if the above conditional is met
    elif OPERATOR == '-':                                           #this conditional runs the indented code if the condition OPERATOR equals '-' is met
        ACTUAL_ANSWER = NUMBER_1 - NUMBER_2                         #this assigns NUMBER_1 - NUMBER_2 to variable ACTUAL_ANSWER if the above conditional is met
    else:                                                           #this conditional runs the indented code if all the previous conditions have not been met
        ACTUAL_ANSWER = NUMBER_1 * NUMBER_2                         #this assigns NUMBER_1 * NUMBER_2 to variable ACTUAL_ANSWER if the above conditional is met
    print(NUMBER_1, OPERATOR, NUMBER_2)                             #this outputs the variables NUMBER_1 OPERATOR NUMBER_2 to the console
    while True:                                                     #this iterates this indented piece of code while the condition is true
        try:                                                        #this executes the clause between try and except. If an exception occurs at this time, then the rest of this clause is skipped    
            THEIR_ANSWER = int(input())                             #this assigns the integer from the input to the variable their answer
            break                                                   #this control flow break means that the iteration is broken out of
        except ValueError:                                          #this allows the computer to accept the value error and respond if this occurs with the code below
            print('Type in a number please!')                       #this outputs the string 'Type in a number please!' onto the console
    if THEIR_ANSWER == ACTUAL_ANSWER:                               #this conditional runs the indented code if the condition THEIR_ANSWER equals ACTUAL_ANSWER is met
        TOTAL_SCORE = TOTAL_SCORE +1                                #this increments TOTAL_SCORE by +1 every iteration and if the conditional is met 
        print('Right answer!')                                      #this outputs the string 'Right answer!' to the console
    else:                                                           #this conditional runs the indented code if all the previous conditions have not been met
        print('Wrong answer. The answer was' ,ACTUAL_ANSWER)        #this outputs the string 'Wrong answer. The answer was' plus the variable to the console 
print( STUDENT_NAME, 'your total score was', TOTAL_SCORE)           #this outputs the variable STUDENT_NAME plus the string 'your total score was' plus the variable TOTAL_SCORE to the console


#####################################################################################################
#                           TASK 2

STUDENT_CLASS = input('Please input your class\n')                                                  #this assigns the input from prompt 'Please input your class' to STUDENT_CLASS
while STUDENT_CLASS != 'Class_1' and STUDENT_CLASS != 'Class_2' and STUDENT_CLASS != 'Class_3':     #this iterates this indented piece of code while the conditions are true (the condtions being that STUDENT_NAME is not Class 1,2 or 3)
    STUDENT_CLASS = input('Please input a valid class - Class_1 or Class_2 or Class_3\n')           #this assigns the input from prompt 'Please input a valid class - Class_1 or Class_2 or Class_3\n' to STUDENT_CLASS
if STUDENT_CLASS == 'Class_1':                                                                      #this conditional runs the indented code if STUDENT_CLASS is the same as 'Class_1'
    Class_1_file = open('Class_1', 'a')                                                             #this assigns the file object open('Class_1','a') to variable Class_1_file
    Class_1_file.write(STUDENT_NAME + ' ' + str(TOTAL_SCORE)+'\n')                                  #this writes the values (STUDENT_NAME + ' ' + str(TOTAL_SCORE)+'\n') to Class_1_file
    Class_1_file.close()                                                                            #this closes Class_1_file
elif STUDENT_CLASS == 'Class_2':                                                                    #this conditional runs the indented code if STUDENT_CLASS is the same as 'Class_2'
    Class_2_file = open('Class_2','a')                                                              #this assigns the file object open('Class_2','a') to variable Class_2_file
    Class_2_file.write(STUDENT_NAME + ' ' + str(TOTAL_SCORE)+'\n')                                  #this writes the values (STUDENT_NAME + ' ' + str(TOTAL_SCORE)+'\n') to Class_2_file
    Class_2_file.close()                                                                            #this closes Class_2_file
else:                                                                                               #this conditional runs the indented code if the above two conditionals have not been met
    Class_3_file = open('Class_3','a')                                                              #this assigns the file object open('Class_3','a') to variable Class_3_file
    Class_3_file.write(STUDENT_NAME + ' ' + str(TOTAL_SCORE)+'\n')                                  #this writes the values (STUDENT_NAME + ' ' + str(TOTAL_SCORE)+'\n') to Class_3_file
    Class_3_file.close()                                                                            #this closes Class_3_file
