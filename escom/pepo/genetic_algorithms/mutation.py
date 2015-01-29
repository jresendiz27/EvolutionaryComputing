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