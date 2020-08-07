import random


def generate_random_ints(start, end, count):
    '''
    returns array with n number of unique random integers
    '''
    return random.sample(range(start, end), count)
