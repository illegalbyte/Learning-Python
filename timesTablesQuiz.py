import pyinputplus as pyip
import random, time

numberOfQuestions = pyip.inputInt('How many questions would you like to answer? \n')
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        prompt = f'\nQ{questionNumber}: {num1} X {num2}: '
        try:
                pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                        blockRegexes=[('.*', 'Incorrect!')],
                        timeout=8, limit=3)
        except pyip.TimeoutException:
                print('Out of time!')
        except pyip.RetryLimitException:
                print('Out of tries!')
        else:
                # This block runs if no exceptions were raised in the try block.
                print('Correct!')
                correctAnswers += 1
        time.sleep(2)
        print(f'Score: {correctAnswers} / {numberOfQuestions}. \
                {round(correctAnswers*100/numberOfQuestions, 2)}% Correct')
