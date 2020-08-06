import random


def generate_random_ints(n):
    '''
    returns array with n number of unique random integers
    '''
    return [random.randrange(100000, 999999) for _ in range(n)]
