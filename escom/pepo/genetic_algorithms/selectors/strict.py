__author__ = 'alberto'
# Returns the index of the most suitable
def strict_selector(fitness, asc=False):
    selected_value = fitness[0]
    index = 0
    if asc:
        selected_value = min(fitness)
    else:
        selected_value = max(fitness)

    for i in range(0, len(fitness)):
        if fitness[i] is selected_value:
            index = i

    return index