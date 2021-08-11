#! python3

# randomQuizGenerator.py - Creates quizzes with questions 
# and answers in random order.

import random, os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate Quiz Files

for quizNumber in range(10):
    # Create Quiz and answer key files
    quizFile = open(f'capitalsQuiz{quizNumber+1}.txt', 'w')
    answerKeyFile = open(f'capitalsQuiz_answers{quizNumber+1}.txt', 'w')
    # Write Header for Quiz: 
    quizFile.write('Name: \n\nDate: \n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNumber + 1})')
    quizFile.write('\n\n')
    #Shuffle States:
    states = list(capitals.keys())
    random.shuffle(states)

    # Generate the correct answer and three incorrect answers as a list
    for questionNumber in range(50):
        correctAnswer = capitals[states[questionNumber]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the choices to the test: 
        quizFile.write(f'{questionNumber+1}. What is the capital of {states[questionNumber]}?\n')
        for i, answerOption in enumerate(answerOptions):
            quizFile.write(f"  {'ABCD'[i]}. {answerOption}\n")
        quizFile.write('\n')

        # Write the answer key to a file:
        answerKeyFile.write(
            f"{questionNumber+1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()


