from collections import OrderedDict                                     #this imports the datatype OrderedDict from the collections module into the script
from operator import itemgetter                                         #this imports the function itemgetter from the operator module into the script

names_and_scores = []                                                   #assigns an empty list to identifier names_and_scores
no_repeats = {}                                                         #assigns an empty dictionary to identifier no_repeats
no_repeats = OrderedDict(no_repeats)                                    #changes the dictionary no_repeats into an ordered dictionary
dict_of_their_scores = {}                                               #assigns an empty dictionary to identifier dict_of_their_scores
highest_to_lowest =  {}                                                 #assigns an empty dictionary to identifier highest_to_lowest

SELECTED_CLASS = input('Please select a class: Class_1, Class_2 or Class_3\n')                          #this assigns the input of the prompted string to identifier SELECTED_CLASS 
while SELECTED_CLASS != 'Class_1' and SELECTED_CLASS != 'Class_2' and SELECTED_CLASS != 'Class_3':      #this iterates the indented piece of code below it while the condition is true (in this case while SELECTED_CLASS doesn't equal Class_1,2 or 3)
    SELECTED_CLASS = input('Please select a valid class: Class_1, Class_2 or Class_3\n')                #this assigns the input of the prompted string to identifier SELECTED_CLASS

Class_file = open('{0}.txt'.format(SELECTED_CLASS), 'r',)   #this assigns file object open('{0}.txt'.format(SELECTED_CLASS), 'r',) to Class_file. Format() means that the {0} is replaced by the string assigned earlier to SELECTED_CLASS

for line in Class_file:                                     #this iterates for every line in Class_file and executes the indented code for each line
    student_data = line.split(' ')                          #this assigns the identifier student_data to the tuple of splitting line at the space ' '.                                                           
    names_and_scores.insert(0,student_data)                 #this inserts student_data into the list names_and_scores, importantly at the beginning fo the list through the first parameter 0

Class_file.close()                                          #this closes the file in use

for pair in names_and_scores:                               #this iterates for every pair (which is our student data) in names_and_scores and executes the indented code below for each line
    if pair[0] not in no_repeats:                           #this conditional executes the indented code below if the conditions are met (in this case if pair[0] not in no_repeats)
        no_repeats[pair[0]] = 1                             #this creates the key pair[0] in dctionary no_repeats and assigns it value 1
        vars()[pair[0]] = []                                    #this creates an empty list where the variable name is pair[0] 
        vars()[pair[0]].append(int(pair[1]))                    #this appends the integer of pair[1] into the list with variable name pair[0]
        dict_of_their_scores[pair[0]] = vars()[pair[0]]         #this creates the key pair[0] in dictionary dict_of_their_scores and assigns it to the list vars()[pair[0]] 
    elif no_repeats[pair[0]] == 3:                              #this conditional executes the indented code below if the previous conditional is not met and its conditions are
        pass                                                    #this does nothing, because we don't want anything to be appended if no_repeats is already 3
    else:                                                       #this conditional executes the indented code below if all previous conditionals are not met
        no_repeats[pair[0]] = no_repeats[pair[0]] + 1           #this increments no_repeats[pair[0]] by one, effectively counting how many times the student has done the quiz
        vars()[pair[0]].append(int(pair[1]))                    #this appends the integer of pair[1] into the list with variable name pair[0]                                             


print('Alphabetical order:')                                    #this outputs the string 'Alphabetical order:'
for key in sorted(dict_of_their_scores, key=str.lower):         #this iterates for every key in sorted(dict_of_their_scores)
    print('    ' ,key, dict_of_their_scores[key])               #this outputs the string '    ' ,key, dict_of_their_scores[key] so the student name is linked to their score

print(' Highest to lowest score:')                              #this outputs the string ' Highest to lowest score:'
for key in dict_of_their_scores:                                #this iterates for every key in dict_of_their_scores
    highest_to_lowest[key] = max(dict_of_their_scores[key])     #this creates the key from the iterated key into dictionary highest_to_lowest and assigns it the highest dict_of_their_scores[key] 
highest_to_lowest = sorted(highest_to_lowest.items(), key = itemgetter(1))  #this sorts the dictionary highest_to_lowest to a sorted dictionary by key[1] (the highest score of each student)
for key in reversed(highest_to_lowest):                                     #this iterates for every key in dictionary highest_to_lowest
    print('    ' + key[0], dict_of_their_scores[key[0]])                    #this outputs the string '    ' ,key[0], dict_of_their_scores[key[0]] so the student name is linked to their score

highest_to_lowest =  {}                                         #this wipes this variable name to an empty dictionary, making it ready for reuse in average highet to lowest
print(' Highest average score:')                                #this outputs the string ' Highest average score:'
for key in dict_of_their_scores:                                #this iterates for every key in dict_of_their_scores
    highest_to_lowest[key] = sum(dict_of_their_scores[key])/len(dict_of_their_scores[key])  #this creates the key from the iterated key into dicrionary highest_to_lowest and assigns it the average of dict_of_their_scores[key]
highest_to_lowest = sorted(highest_to_lowest.items(), key = itemgetter(1))                  #this sorts the dictionary highest_to_lowest to a sorted dictionary by key[1] (the average score of each student)
for key in reversed(highest_to_lowest):                                                     #this iterates for every key in dictionary highest_to_lowest
    print('    ' + key[0], dict_of_their_scores[key[0]])                                    #this outputs the string '    ' ,key[0], dict_of_their_scores[key[0]] so the student name is linked to their score
