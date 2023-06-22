from random import randint
from random import choice


TASK = 'What is the result of the expression?'


def game_logic():
    random_operator = choice(['+', '-', '*'])
    random_number_1 = randint(1, 10)
    random_number_2 = randint(1, 10)
    question = f'{random_number_1} {random_operator} {random_number_2}'
    correct_answer = str(eval(question))
    return question, correct_answer
