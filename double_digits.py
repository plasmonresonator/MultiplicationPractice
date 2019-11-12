import random, winsound, os, pygame, time
from datetime import datetime
from pathlib import Path
from os import path
from send_gmail_results import send_email
from credentials import app_password, matt_email, maddie_email, krista_email

print(os.getcwd())

path = Path(os.getcwd())
# path = 'c:\\users\\212330207\\desktop\\'
sound_path = 'c:\\windows\\media\\'
correct_image_path = 'pictures/correct/'
# correct_image_path = 'c:\\users\\212330207\\desktop\\cat pictures\\correct\\'
wrong_image_path = 'pictures/wrong/'
# wrong_image_path = 'c:\\users\\212330207\\desktop\\cat pictures\\wrong\\'
correct_image_list = os.listdir(path / correct_image_path)
# correct_image_list = os.listdir(correct_image_path)
wrong_image_list = os.listdir(path / wrong_image_path)
# wrong_image_list = os.listdir(wrong_image_path) 

greeting_messages = ['Hello, Meatbag!']
right_answer_messages = ['Freaking awesome!  You got it right, I knew you could do it!!!', 
                        'Awesome-sauce!', 'You rock!!!',
                        'You are a multiplication GENIUS!!!',
                        'How did you get so smart?!?!',
                        'Nice job! Keep it up!!!',
                        'Nailed it!!  Here, check out this cat!\n\n\t /\\_/\\\n\t( o.o )\n\t > ^ <\n\n',
                        "Perfect!  Look at this cute little lion:\n\n(\"`-''-/\").___..--''\"`-._\n `6_ 6  )   `-.  (     ).`-.__.`)\n (_Y_.)'  ._   )  `._ `. ``-..-' \n   _..`--'_..-_/  /--'_.'\n  ((((.-''  ((((.'  (((.-' ",
                        ]

wrong_answer_messages = ['Oops! Either you got the wrong answer, or Daddy didn\'t code this right! Let\'s try another one...',
                        'Almost! Maybe try one of your math strategies next time you\'re having trouble?',
                        'Oops! I know you can figure that one out, maybe you typed the wrong number by accident?',
                        'Uh Oh! You missed that one, but I KNOW you can get the next one right!!',
                        'Bummer, you missed that one, now you have to look at dog poop again!!! :-p ',
                        ]

# common_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# test_numbers = []
# practice_selection = []
# all_problems = []
# correct = []
# wrong = []
# wrong2 = []

def play_correct_sound():
    os.chdir(sound_path)
    winsound.PlaySound('Windows Exclamation.wav', winsound.SND_FILENAME)
    os.chdir(path)
    


def play_wrong_sound():
    os.chdir(sound_path)
    winsound.PlaySound('ir_begin.wav', winsound.SND_FILENAME)
    os.chdir(path)
    

def display_image(image_type, question_number):
    def do_it(image_type):
        if image_type == 'correct':
            picture = pygame.image.load(correct_image_path + str(random.choice(correct_image_list)))
            sleep_time = 2.5
        else:
            picture = pygame.image.load(wrong_image_path + str(random.choice(wrong_image_list)))
            sleep_time = 1.75
        pygame.display.set_mode(picture.get_size())
        main_surface = pygame.display.get_surface()
        main_surface.blit(picture,(0,0))
        pygame.display.update()
        time.sleep(sleep_time)
        pygame.quit()
    
    if image_type == 'wrong':
        do_it(image_type)
    elif image_type == 'correct':
        if question_number % 2 == 0:
            do_it('correct')
        else:
            pass
    

def get_problem(problem, question_number, round=1):
    num1 = problem[0]
    num2 = problem[1]
    show = f'{num1} x {num2} ?'
    answer = input(f"What is {show}")
    #NEED TO HANDLE FOR IF AN INTEGER IS NOT ENTERED
    calc = num1*num2
    answer = int(answer)
    if answer == calc:
        # play_correct_sound()
        print(random.choice(right_answer_messages))
        right.append(problem)
        f.write(f"Correct\t{show}{answer}\n")
        # display_image('correct', question_number)
    else:
        if round == 1:
            print(f"Sorry, the correct answer is {calc}.\n\tWe'll revisit that one again later.")
            wrong.append(problem)
            f.write(f"WRONG\t{show}{answer}\n")
            # display_image('wrong', question_number)
        else:
            print(f"Oops!  The correct answer is {calc}.")
            wrong2.append(problem)
            # display_image('wrong', question_number)
            f.write(f"WRONG\t{show}{answer}\n")
    

print('\n\n')
name = input('Hello, thanks for wanting to play Daddy\'s super amazing multiplication game!!!\n\nPlease type your name:\t')
if str.lower(name) == 'maddie':
    pass
else:
    print("\nEither you're trying to trick me, OR you spelled you're name wrong!  I'm going to call you Maddie McStinkerButt for now!",
        "anyway! :-)\n\n")
    name = 'Maddie McStinkerButt'

keep_playing = 'y'
while keep_playing == str.lower('y'):
    common_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    test_numbers = []
    practice_selection = []
    all_problems = []
    right = []
    wrong = []
    wrong2 = []
    total = []
    errors = []
    while True:
        howmany = input('How many numbers do you want to practice today?\t')
        
        try:
            howmany = int(howmany)
            if howmany > 0:
                break
        except:
            print("That's not a number, please try entering a number again.")
    
    for i in range(howmany):
        if i == 0:
            practice_nums = input("Enter the first number you want to practice today:\t")
        else:
            practice_nums = input("Enter the next number you'd like to practice today:\t")
        
        if practice_nums in practice_selection:
            print(f"You already added that number, here are the numbers you are working on so far: {practice_selection}")
            practice_nums = input("Enter the next number you'd like to practice today:\t")
        
        practice_selection.append(practice_nums)
        
    print(f"OK, you will be practicing these numbers today:\n{practice_selection}.\n")  
    for i in practice_selection:
        try:
            int(i)
            test_numbers.append(int(i))
        except:
            print(f"{i} is not a number and will not be added to your practice list.")
    for test in test_numbers:
        for comm in common_numbers:
            all_problems.append([test, comm])
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
        f.write(f"Numbers worked on {test_numbers}\n\n")
        f.write('*********************************')
        f.write('\n\tRound 1\n')
        f.write('*********************************\n\n')
        x=0
        while len(all_problems) >= 1:
            x+=1
            current_problem = all_problems.pop()
            try:
                get_problem(current_problem, x, 1)
            except Exception as e:
                print("Error, it doesn't look like you entered a number, try it again.\n")
                try:
                    get_problem(current_problem, x, 1)
                except:
                    all_problems.append(current_problem)
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
        time_message = f'\nTotal time to answer {total} problems: {duration} seconds.\n'
        accuracy = f'\nYou answered {len(right)} out of {total} questions correctly.\n'
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