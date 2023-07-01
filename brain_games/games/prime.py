from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    if number != 2 and number % 2 == 0:
        return False
    dividers = []
    for divider in range(1, number + 1):
        if number % divider == 0:
            dividers.append(divider)
    if len(dividers) > 2:
        return False
    else:
        return True


def get_question_answer():
    question = randint(1, 100)
    if is_prime_number(question) is False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer
