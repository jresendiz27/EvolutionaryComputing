__author__ = 'alberto'
from escom.pepo.config import CHROMOSOME_LENGTH, NUMBER_OF_SONS_PER_CROSS, np, random


def one_point_crosses(father, mother):
    offsprings = np.array([])
    for i in range(0, NUMBER_OF_SONS_PER_CROSS):
        cross_point = random.randint(1, CHROMOSOME_LENGTH / 2)
        #
        left_side_father = father[0:cross_point]
        right_side_father = father[cross_point:CHROMOSOME_LENGTH]
        #
        left_side_mother = mother[0:cross_point]
        right_side_mother = mother[cross_point:CHROMOSOME_LENGTH]
        #
        if i % 2 == 0:
            son_one = left_side_father + right_side_mother
            offsprings.append(son_one)
        else:
            son_two = left_side_mother + right_side_father
            offsprings.append(son_two)

    return offsprings