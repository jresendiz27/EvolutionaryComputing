__author__ = 'alberto'
from escom.pepo.config import CHROMOSOME_LENGTH, NUMBER_OF_SONS_PER_CROSS, random


def one_point_crosses(father, mother):
    offsprings = []
    for i in range(0, NUMBER_OF_SONS_PER_CROSS):
        cross_point = random.randint(1, CHROMOSOME_LENGTH-1)
        #
        left_side_father = father[0:cross_point]
        right_side_father = father[cross_point:CHROMOSOME_LENGTH]
        #
        left_side_mother = mother[0:cross_point]
        right_side_mother = mother[cross_point:CHROMOSOME_LENGTH]
        #
        if i % 2 == 0:
            son = left_side_father + right_side_mother
            offsprings.append(son)
        else:
            son = left_side_mother + right_side_father
            offsprings.append(son)

    return offsprings