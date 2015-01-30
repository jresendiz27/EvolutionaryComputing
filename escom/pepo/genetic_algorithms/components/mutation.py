__author__ = 'alberto'


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