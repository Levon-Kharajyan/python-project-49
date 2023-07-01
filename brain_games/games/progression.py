from random import randint


TASK = 'What number is missing in the progression?'


def get_question_answer():
    progression = []
    zero_element = randint(1, 100)
    progression_difference = randint(1, 10)
    progression.append(zero_element)
    progression_length = randint(5, 10)
    for i in range(0, progression_length):
        progression.append(progression[i] + progression_difference)
    hidden_element_index = randint(0, progression_length)
    correct_answer = str(progression[hidden_element_index])
    progression[hidden_element_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
