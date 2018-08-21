#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in # random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.

    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w+')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w+')
    
    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')   
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))    
    quizFile.write('\n\n')
    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    
    # TODO: Loop through all 50 states, making a question for each
    i=0
    for question in states:
        #question is each individual key/state/string
        i=i+1
        quizFile.write("%d. What is the capital of %s?\n" % (i,question ))
        answers = [capitals.get(question)]
        for ans in range(0,4):
            #get 3 other random capitals, and the real one. shuffle them then print?
            checkState = random.choice(states)  #this variable is for comparing to the current state so it doesn't appear twice
            while checkState == question:   #if the randomly chosen state matches the current state, it will randomly choose another one again
                checkState = random.choice(states)
            answers = answers + [capitals.get(checkState)]
        random.shuffle(answers)     #after all states have been confirmed to be unique and capitals have been added to the list, shuffle them
        ABCD = ['A','B','C','D']        #letters are required for forms, not numbers
        letterAns = 0                   #for saving the index of the correct answer/capital for printing on the answer sheet
        for y in range(0,4):        #writes the 4 capitals
            if answers[y] == capitals.get(question):
                letterAns = y
            quizFile.write("    %s. %s\n" % (ABCD[y],answers[y]))

        answerKeyFile.write("%d. %s,%s\n" % (i,ABCD[letterAns],capitals.get(question))) #writes the answer to the answer txt
