import prompt
from random import randint


def even_logic():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if (random_number % 2 == 0 and user_answer == 'yes') or (random_number % 2 != 0 and user_answer == 'no'):
            print('Correct!')
            counter = counter + 1
        elif random_number % 2 == 0 and user_answer != 'yes':
            print(f"""'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {user_name}!""")
            break
        elif random_number % 2 != 0 and user_answer != 'no':
            print(f"""'{user_answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {user_name}!""")
            break

    if counter == 3:
        print(f'Congratulations, {user_name}!')
