from random import randint
from random import choice


TASK = 'What is the result of the expression?'


def get_question_answer():
    random_operator = choice(['+', '-', '*'])
    random_number_1 = randint(1, 10)
    random_number_2 = randint(1, 10)
    question = f'{random_number_1} {random_operator} {random_number_2}'
    if random_operator == '+':
        correct_answer = str(random_number_1 + random_number_2)
    elif random_operator == '-':
        correct_answer = str(random_number_1 - random_number_2)
    else:
        correct_answer = str(random_number_1 * random_number_2)
    return question, correct_answer
