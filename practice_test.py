import random, winsound, os, pygame, time
from datetime import datetime
from pathlib import Path
from os import path
from send_gmail_results import send_email
from credentials import app_password, matt_email, maddie_email, krista_email

print(os.getcwd())

path = Path(os.getcwd())

greeting_messages = ['Hello, Meatbag!']

# common_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# test_numbers = []
# practice_selection = []
# all_problems = []
# correct = []
# wrong = []
# wrong2 = []

   

def get_problem(problem, question_number, round=1):
    random.shuffle(problem)
    num1 = problem[0]
    num2 = problem[1]
    show = f'{num1} x {num2}'
    answer = input(f"\nWhat is {show} ?\t")
    #NEED TO HANDLE FOR IF AN INTEGER IS NOT ENTERED
    calc = num1*num2
    answer = int(answer)
    if answer == calc:
        right.append(problem)
        f.write(f"Correct\t{show}\t{answer}\n")
    else:
        if round == 1:
            wrong.append(problem)
            f.write(f"WRONG\t{show}\t{answer}\n")
        else:
            wrong2.append(problem)
            f.write(f"WRONG\t{show}\t{answer}\n")
    

print('\n\n')
name = input('Hello, thanks for wanting to play Daddy\'s super amazing multiplication game!!!\n\nPlease type your name:\t')
if str.lower(name) == 'maddie':
    pass
else:
    print("\nEither you're trying to trick me, OR you spelled you're name wrong!  I'm going to call you Maddie McStinkerButt for now!",
        "anyway! :-)\n\n")
    name = 'Maddie McStinkerButt'
length = int(input('How many minutes do you want to practice today?\t'))
keep_playing = 'y'
while keep_playing.lower() == 'y':
    common_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    all_problems = []
    right = []
    wrong = []
    wrong2 = []
    total = []
    
    for first in common_numbers:
        for second in test_numbers:
            if [second, first] in all_problems:
                pass
            else:
                all_problems.append([first, second])
    total = len(all_problems)
    print(f"You have {total} problems in this set...let's get started!")

    random.shuffle(all_problems)

    start = datetime.now()
    starttime = start.strftime('%Y-%m-%d_%H_%M_%S')
    if not os.path.exists('mathresultfiles'):
        os.mkdir('mathresultfiles')
    indiv_path = path / 'mathresultfiles' #c:\\users\\212330207\\desktop\\mathresultfiles\\'
    indiv_filename = os.path.join(indiv_path, starttime + '.txt')

    with open(indiv_filename, 'a+') as f:
        f.write(f"Start Time: {start}\n")
        f.write(f"Length of practice test was {length} minutes\n\n")
        f.write('*********************************')
        f.write('\n\tRound 1\n')
        f.write('*********************************\n\n')
        x=0

        time_end = time.time() + 60*length
        current_time = time.time()
        while len(all_problems) >= 1:
            x+=1
            current_time = time.time()
            if current_time >= time_end:
                break
            current_problem = all_problems.pop()
            try:
                get_problem(current_problem, x, 1)
            except Exception as e:
                print("Error, it doesn't look like you entered a number, try it again.\n")
                # try:
                get_problem(current_problem, x, 1)
                # except:
                    # all_problems.append(current_problem)
                    # f.write(f"\n****ERROR IN CODE****")
                    # f.write(f"\t{e}\n")
                    # f.write(f"problem added to wrong list by default")
        
        if len(wrong) >=1:
            f.write('*********************************')
            f.write('\n\tRound 2 (revisiting missed problems)\n')
            f.write('*********************************\n\n')
            random.shuffle(wrong)
            while len(wrong) >= 1:
                x+=1
                current_time = time.time()
                if current_time >= time_end:
                    break
                current_problem = wrong.pop()
                try:
                    get_problem(current_problem, x, 2)
                except Exception as e:
                    wrong.append(current_problem)
                    # f.write(f"\n****ERROR IN CODE****")
                    # f.write(f"\t{e}\n")
                    # f.write(f"problem added to error list by default")


        end = datetime.now()
        duration = end - start
        problems_seen = len(right) + len(wrong) + len(wrong2)
        time_message = f'\nYou went through {problems_seen} problems: {length} minutes.\n'
        accuracy = f'\nYou answered {len(right)} out of {problems_seen} questions correctly.\n'
        linebreak = '\n ################################################ \n\n'

        print(time_message)
        print(accuracy)
        print(linebreak)
        f.write(time_message)
        f.write(accuracy)
        f.write(linebreak)


    with open(indiv_filename, 'r') as f:
        email_report = f.read()
    print('Mom and Dad should have a copy of your awesome work in their email soon!')
    try:
        send_email(recipient=krista_email, msg=email_report)
        send_email(msg=email_report)
    except Exception as e:
        print(f"Your results didn't sent for some reason.\n\n{e}\n\n\tYou can go to the folder: {os.getcwd()} and find your results file named {filename} if you want to.")





    keep_playing = input('Do you want to play again? (Type y or n and then press enter)\n')

print('Thanks for playing!!!  Goodbye!')

'''

    with open(indiv_filename, 'a+') as ff:
        with open('Maddie multiplaction results.txt', 'a+') as f:
            print('OK, ' + str.title(name) + ', let\'s do it!!!\n\n')
            f.write(f'Level {level} start time: {starttime}\n')
            ff.write(f'Level {level} start time: {starttime}\n')
            
            for i in range(problems):
                num1 = int(random.choice(values))
                num2 = int(random.choice(common))
                answer = num1 * num2
                problem = 'What is ' + str(num1) + ' x ' + str(num2) + ' ?\t '
                while True:
                    x = input(problem)
                    try:
                        int(x)
                        break
                    except ValueError:
                        print("\nThat's not a number silly!!! Try typing your answer again!!! :-)")

                if int(x) == int(answer):
                    print(str(random.choice(right_answer_messages)) + '\n')
                    display_image('correct', i)
                    right.append(i)
                    f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT\n')
                    ff.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT\n')
                elif int(x) != int(answer):
                    print('\nOops, you missed it that time.  Let\'s try it one more time!')
                    x = input(problem)
                    if int(x) == int(answer):
                        print(str(random.choice(right_answer_messages)) + '\n')
                        right.append(i)
                        f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT (2nd try)\n')
                        ff.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT (2nd try)\n')
                    else:
                        print(str(random.choice(wrong_answer_messages)) + '\n')
                        print(f'The correct answer was {num1} x {num2} = {answer}')
                        display_image('wrong', i)
                        wrong.append(i)
                        f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  WRONG\n')
                        ff.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  WRONG\n')

                total.append(i)
            end = datetime.now()
            duration = end - start
            time_message = '\nTotal time to answer 10 problems: ' + str(duration) + ' seconds.\n'
            accuracy = 'You answered ' + str(len(right)) + ' out of 10 questions correctly.\n'
            linebreak = '\n ################################################ \n\n'

            print(time_message)
            print(accuracy)
            print(linebreak)
            f.write(time_message)
            f.write(accuracy)
            f.write(linebreak)
            ff.write(time_message)
            ff.write(accuracy)
            ff.write(linebreak)
    # except Exception as e:
    #   print(f'An error occurred with the message: \n\t{e}\nPlease let Daddy know!')

'''