import math

from escom.pepo.config import NUMBER_OF_VARIABLES


__author__ = 'azu'

n = NUMBER_OF_VARIABLES


def fitness1(single):
    result = 0
    for i in range(n):
        result += abs(single[i] * math.sin(single[i]) + 0.1 * single[i])
    return result


def fitness2(single):
    result = 0
    for i in range(n):
        result += (single[i] ** 2 - 10 * math.cos(2 * math.pi * single[i]))
    return result * 10 * n


def fitness3(single):
    result = 0
    for i in range(n):
        result += single[i] ** 4 - 16 * single[i] ** 2 + 5 * single[i]
    return result * 1 / 2


def fitness4(single):
    result = 0
    for i in range(n):
        result += single[i]
    return result


function = {1: fitness1, 2: fitness2, 3: fitness3, 4: fitness4}

