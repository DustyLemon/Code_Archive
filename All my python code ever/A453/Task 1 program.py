from random import *                                                #this imports the random module into the script
QUESTION_NUMBER = 1                                                 #this assigns integer 1 to variable QUESTION_NUMBER
TOTAL_SCORE = 0                                                     #this assigns integer 0 to variable TOTAL_SCORE
print('Hello, welcome to the math quiz')                            #this outputs the string 'Hello, welcome to the math quiz' onto the console 
STUDENT_NAME = input('What is your name?\n')                        #this assigns the input from prompt 'What is your name?\n' to STUDENT_NAME
while QUESTION_NUMBER < 11:                                         #this iterates this indented piece of code while the condition is true (in this case while QUESTION_NUMBER is less than 11)
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
