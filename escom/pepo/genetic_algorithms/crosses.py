__author__ = 'alberto'
from escom.pepo.config import CHROMOSOME_LENGTH, random, logger

log = logger.getLogger(__file__)

def one_point_crosses(father, mother):
    log.debug("OK")
    cross_point = random.randint(1, CHROMOSOME_LENGTH - 1)
    #
    left_side_father = father[0:cross_point]
    right_side_father = father[cross_point:CHROMOSOME_LENGTH]
    #
    left_side_mother = mother[0:cross_point]
    right_side_mother = mother[cross_point:CHROMOSOME_LENGTH]
    #
    son_one = left_side_father + right_side_mother
    son_two = left_side_mother + right_side_father

    return son_one, son_two

one_point_crosses([0],[0])