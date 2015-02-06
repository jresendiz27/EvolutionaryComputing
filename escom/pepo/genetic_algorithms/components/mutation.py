__author__ = 'alberto'

import random


def single_mutation(single, allele_index=0, modifier=None):
    if modifier:
        single[allele_index] = modifier(single[allele_index])
    else:
        # Considering its a bit!
        if single[allele_index] == 0:
            single[allele_index] = 1
        else:
            single[allele_index] = 0
    return single


def whole_mutation(single, modifier=None):
    for index in range(0, len(single)):
        if modifier:
            single[index] = modifier(single[index])
        else:
            # Considering its a bit!
            if single[index] == 0:
                single[index] = 1
            else:
                single[index] = 0
        return single


def random_mutation(single, chromosome_min_value, chromosome_max_value):
    single_clone = single
    for index in range(0, len(single)):
        single_clone[index] = random.randint(chromosome_min_value, chromosome_max_value)
    return single_clone